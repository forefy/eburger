from datetime import datetime
import json
import os
from pathlib import Path
import re
import shlex
import subprocess
import sys
import networkx as nx
from eburger.utils.cli_args import args
from eburger.utils.filesystem import (
    create_directory_if_not_exists,
    create_or_empty_directory,
    find_and_read_sol_file,
    get_solidity_version_from_file,
)
from eburger.utils.logger import log
import eburger.settings as settings
from eburger.serializer import parse_solidity_ast, reduce_json
from eburger.utils.outputs import draw_graph, save_as_json, save_python_ast
from eburger.yaml_parser import process_files_concurrently


def is_valid_json(json_string):
    if not json_string:
        return False
    try:
        json.loads("".join(json_string))
        return True
    except ValueError:
        return False


def run_command(command, directory=None):
    log("info", f"{command}")
    results = []
    process = subprocess.Popen(
        shlex.split(command),
        stdout=subprocess.PIPE,
        encoding="utf-8",
        shell=False,
        cwd=directory,
    )
    while True:
        output = process.stdout.readline()
        if output == "" and process.poll() is not None:
            break
        if output:
            results.append(output.strip())
    return results


def construct_solc_cmdline(path_type: str, compilation_source_path: str) -> str:
    solc_cmdline = "solc"
    if args.solc_remappings:
        solc_cmdline += " "
        solc_cmdline += " ".join(args.solc_remappings)
    if path_type == "folder":
        solidity_files = get_all_solidity_files(args.solidity_file_or_folder)
        compilation_source_path = " ".join(solidity_files)
    solc_cmdline += f" --combined-json abi,ast,bin,bin-runtime,srcmap,srcmap-runtime,userdoc,devdoc,hashes {compilation_source_path}"
    return solc_cmdline


def main():
    if len(sys.argv) == 1:
        args.solidity_file_or_folder = "."

    create_directory_if_not_exists(settings.outputs_dir)
    path_type = None

    if args.solidity_file_or_folder:
        settings.project_root = Path(args.solidity_file_or_folder)
        if os.path.isfile(args.solidity_file_or_folder):
            path_type = "file"
        elif os.path.isdir(args.solidity_file_or_folder):
            path_type = "folder"

            # Check if foundry project, in which case it is better just using forge
            if os.path.isfile(
                os.path.join(args.solidity_file_or_folder, "foundry.toml")
            ):
                path_type = "foundry"
        else:
            log(
                "error",
                f"{args.solidity_file_or_folder} is neither a file nor a directory.",
            )
            sys.exit(0)
    elif args.ast_json_file:
        filename = args.ast_json_file
        filename = filename.replace(".json", "")  # Clean possible file extension
        with open(args.ast_json_file, "r") as f:
            ast_json = json.load(f)
            ast_json, src_file_list = reduce_json(ast_json)
        output_path = settings.outputs_dir / f"{filename}.json"
        save_as_json(output_path, ast_json)

    if path_type is not None:
        if path_type == "foundry":
            log("info", "Foundry project detected, compiling using forge")
            if args.solc_remappings:
                log("warning", "Ignoring the -r option in foundry based projects.")
            run_command(f"forge clean", args.solidity_file_or_folder)
            forge_out_dir = settings.outputs_dir / "forge-output"
            create_or_empty_directory(forge_out_dir)
            build_output_lines = run_command(
                f"forge build --force --skip test script --build-info --build-info-path {forge_out_dir}",
                args.solidity_file_or_folder,
            )
            for line in build_output_lines:
                log("info", line)
            json_files = [f for f in os.listdir(forge_out_dir) if f.endswith(".json")]
            if not json_files:
                log("error", "forge build generated no output.")
                sys.exit(0)
            if len(json_files) > 1:
                log(
                    "warning",
                    "Multiple forge-output files found, choosing the latest.",
                )
            latest_file = max(
                json_files,
                key=lambda x: os.path.getctime(os.path.join(forge_out_dir, x)),
            )
            latest_file_path = os.path.join(forge_out_dir, latest_file)

            # get sample filename
            extracted_sample_file_path = find_and_read_sol_file(
                args.solidity_file_or_folder
            )
            if extracted_sample_file_path:
                sample_file_path = extracted_sample_file_path
            if sample_file_path is None:
                log("error", "Can't parse path given in argument.")
                sys.exit(0)
            if args.project_name:
                filename = args.project_name
            else:
                filename_match = re.search(r"/([^/]+)\.sol$", sample_file_path)
                filename = filename_match.group(1) if filename_match else None
            filename = f"{filename}_{datetime.now().strftime('%m%y')}"
            output_filename = settings.outputs_dir / f"{filename}.json"

            with open(latest_file_path, "r") as f:
                ast_json = json.load(f)
                ast_json = ast_json["output"]
                ast_json, src_file_list = reduce_json(ast_json)
            save_as_json(output_filename, ast_json)
        elif path_type in ["file", "folder"]:
            sample_file_path = None
            compilation_source_path = None
            if path_type == "file":
                sample_file_path = args.solidity_file_or_folder
                compilation_source_path = args.solidity_file_or_folder
            elif path_type == "folder":
                compilation_source_path = args.solidity_file_or_folder
                extracted_sample_file_path = find_and_read_sol_file(
                    args.solidity_file_or_folder
                )
                if extracted_sample_file_path:
                    sample_file_path = extracted_sample_file_path
            if sample_file_path is None:
                log("error", "Can't parse path given in argument.")
                sys.exit(0)
            # get contract version
            if args.solc_compiler_version:
                solc_required_version = args.solc_compiler_version
            else:
                solc_required_version = get_solidity_version_from_file(sample_file_path)
            log("info", f"Trying to switch solc to version {solc_required_version}")
            solc_use_res = run_command(f"solc-select use {solc_required_version}")
            if not solc_use_res:
                log("error", "Error switching solc version, trying to install")
                run_command(f"solc-select install {solc_required_version}")
                solc_use_res = run_command(f"solc-select use {solc_required_version}")
                if not solc_use_res:
                    log("error", "Failed to install required solc version")
                    exit(0)
            solc_versions_res = run_command(f"solc-select versions")
            log("info", solc_versions_res)
            log("info", "Successfully switched solc version")
            log("info", "Trying to compile contract")
            if args.project_name:
                filename = args.project_name
            else:
                filename_match = re.search(r"/([^/]+)\.sol$", sample_file_path)
                filename = filename_match.group(1) if filename_match else None
            filename = f"{filename}_{datetime.now().strftime('%m%y')}"
            output_filename = settings.outputs_dir / f"{filename}.json"
            solc_cmdline = construct_solc_cmdline(path_type, compilation_source_path)
            if solc_cmdline is None:
                log("error", "Error constructing solc command line")
                exit(0)
            solc_compile_res = run_command(solc_cmdline)
            if not is_valid_json(solc_compile_res):
                error_string = "Locally installed solc errored out trying to compile the contract. Please review comiler warnings above"
                if not args.solc_remappings:
                    error_string += (
                        "or see if library remappings (using the -r option) are needed"
                    )
                if not args.solc_compiler_version:
                    error_string += ", or try specifing the solidity compiler version (using the -s option)"
                error_string += "."
                log(
                    "error",
                    error_string,
                )
                sys.exit(0)
            solc_compile_res_parsed = json.loads("".join(solc_compile_res))
            ast_json, src_file_list = reduce_json(solc_compile_res_parsed)
            save_as_json(output_filename, solc_compile_res_parsed)

    # Parse AST
    G = nx.MultiDiGraph()
    ast_roots, G = parse_solidity_ast(ast_json, G)

    # Draw graph
    settings.outputs_dir / filename
    draw_graph(settings.outputs_dir / filename, G)
    save_python_ast(settings.outputs_dir / filename, ast_roots)

    # Parse YAML templates
    log("info", f"Templates path: {settings.templates_directory}")

    insights = process_files_concurrently(
        settings.templates_directory, ast_json, src_file_list
    )

    if insights:
        # Same data saved twice - once for historic reference and one for clarity
        insights_json_path = settings.outputs_dir / f"eburger_output_{filename}.json"
        results_path = settings.project_root / "eburger-output.json"
        save_as_json(insights_json_path, insights)
        save_as_json(results_path, insights)
        log(
            "success",
            f"Results saved to {results_path}.",
        )
    else:
        log("success", f"No insights found. Results saved to {settings.outputs_dir}")


if __name__ == "__main__":
    main()
