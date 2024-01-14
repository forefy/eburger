from datetime import datetime
import json
import os
from pathlib import Path
import re
import shutil
import sys
import networkx as nx
from eburger.utils.cli_args import args
from eburger.utils.filesystem import (
    create_directory_if_not_exists,
    create_or_empty_directory,
    find_and_read_sol_file,
    get_foundry_ast_json,
    get_hardhat_ast_json,
    get_solidity_version_from_file,
)
from eburger.utils.helpers import (
    construct_solc_cmdline,
    get_filename_from_path,
    is_valid_json,
    run_command,
)
from eburger.utils.installers import (
    install_foundry_if_not_found,
    install_hardhat_if_not_found,
    set_solc_compiler_version,
)
from eburger.utils.logger import log
import eburger.settings as settings
from eburger.serializer import parse_solidity_ast, reduce_json
from eburger.utils.outputs import draw_graph, save_as_json, save_python_ast
from eburger.yaml_parser import process_files_concurrently


def main():
    if not args.solidity_file_or_folder and not args.ast_json_file:
        args.solidity_file_or_folder = "."

    create_directory_if_not_exists(settings.outputs_dir)
    path_type = None

    if args.solidity_file_or_folder:
        if os.path.isfile(args.solidity_file_or_folder):
            path_type = "file"
        elif os.path.isdir(args.solidity_file_or_folder):
            path_type = "folder"
            settings.project_root = settings.project_root / args.solidity_file_or_folder

            # Check if foundry project, in which case it is better just using forge
            if os.path.isfile(
                os.path.join(args.solidity_file_or_folder, "foundry.toml")
            ):
                path_type = "foundry"

            # Check if hardhat project
            if os.path.isfile(
                os.path.join(args.solidity_file_or_folder, "hardhat.config.js")
            ) or os.path.isfile(
                os.path.join(args.solidity_file_or_folder, "hardhat.config.ts")
            ):
                path_type = "hardhat"
        else:
            log(
                "error",
                f"{args.solidity_file_or_folder} is neither a file nor a directory.",
            )
    elif args.ast_json_file:
        filename = args.ast_json_file
        filename = filename.replace(".json", "")  # Clean possible file extension
        with open(args.ast_json_file, "r") as f:
            ast_json = json.load(f)
            ast_json, src_file_list = reduce_json(ast_json)
        output_path = settings.outputs_dir / f"{filename}.json"
        save_as_json(output_path, ast_json)

    if path_type is not None:
        # Foundry compilation flow
        if path_type == "foundry":
            log("info", "Foundry project detected, compiling using forge.")
            install_foundry_if_not_found()

            if args.solc_remappings:
                log("warning", "Ignoring the -r option in foundry based projects.")

            run_command(f"forge clean", args.solidity_file_or_folder)
            forge_out_dir = settings.outputs_dir / "forge-output"
            create_or_empty_directory(forge_out_dir)

            build_output_lines, _ = run_command(
                f"forge build --force --skip {' '.join(settings.excluded_dirs)} --build-info --build-info-path {forge_out_dir}",
                args.solidity_file_or_folder,
            )
            for line in build_output_lines:
                log("info", line)

            sample_file_path = find_and_read_sol_file(args.solidity_file_or_folder)
            filename, output_filename = get_filename_from_path(sample_file_path)

            ast_json = get_foundry_ast_json(forge_out_dir)
            ast_json, src_file_list = reduce_json(ast_json)
            save_as_json(output_filename, ast_json)

        # Hardhat compilation flow
        if path_type == "hardhat":
            log("info", "Hardhat project detected, compiling using hardhat.")
            install_hardhat_if_not_found()

            if args.solc_remappings:
                log("warning", "Ignoring the -r option in hardhat based projects.")

            run_command(f"npx hardhat clean", directory=settings.project_root)

            build_output_lines, _ = run_command(
                f"npx hardhat compile --force",
                directory=settings.project_root,
            )
            for line in build_output_lines:
                log("info", line)

            # Copy compilation results to .eburger
            expected_hardhat_outfiles = os.path.join(
                args.solidity_file_or_folder, "artifacts", "build-info"
            )
            if not os.path.isdir(expected_hardhat_outfiles):
                log(
                    "error",
                    f"Hardhat's compilation files were not found in expected location {expected_hardhat_outfiles}",
                )
            hardhat_out_dir = settings.outputs_dir / "hardhat-output"
            if os.path.exists(hardhat_out_dir):
                shutil.rmtree(hardhat_out_dir)
            shutil.copytree(expected_hardhat_outfiles, hardhat_out_dir)

            sample_file_path = find_and_read_sol_file(args.solidity_file_or_folder)
            filename, output_filename = get_filename_from_path(sample_file_path)

            ast_json = get_hardhat_ast_json(hardhat_out_dir)
            ast_json, src_file_list = reduce_json(ast_json)
            save_as_json(output_filename, ast_json)

        # solc compilation flow
        elif path_type in ["file", "folder"]:
            sample_file_path = args.solidity_file_or_folder
            compilation_source_path = args.solidity_file_or_folder

            if path_type == "folder":
                sample_file_path = find_and_read_sol_file(args.solidity_file_or_folder)

            filename, output_filename = get_filename_from_path(sample_file_path)

            if args.solc_compiler_version:
                solc_required_version = args.solc_compiler_version
            else:
                solc_required_version = get_solidity_version_from_file(sample_file_path)
            set_solc_compiler_version(solc_required_version)
            solc_cmdline = construct_solc_cmdline(path_type, compilation_source_path)
            if solc_cmdline is None:
                log("error", "Error constructing solc command line")
            solc_compile_res, _ = run_command(solc_cmdline)
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
            solc_compile_res_parsed = json.loads("".join(solc_compile_res))
            ast_json, src_file_list = reduce_json(solc_compile_res_parsed)
            save_as_json(output_filename, solc_compile_res_parsed)

    # Parse AST
    G = nx.MultiDiGraph()
    ast_roots, G = parse_solidity_ast(ast_json, G)

    # Draw graph
    settings.outputs_dir / filename
    draw_graph(settings.outputs_dir / filename, G)
    save_python_ast(filename, ast_roots)

    # Parse YAML templates
    if args.templates_path:
        settings.templates_directory = Path(args.templates_path)
    log("info", f"Templates path: {settings.templates_directory}")

    insights = process_files_concurrently(ast_json, src_file_list)

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
