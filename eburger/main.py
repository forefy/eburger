from datetime import datetime
import io
import json
import os
from pathlib import Path
import re
import shlex
import shutil
import subprocess
import sys
import networkx as nx
from pyvis.network import Network
import argparse
from eburger.logger import log

from eburger.serializer import parse_solidity_ast, reduce_json
from eburger.yaml_parser import process_files_concurrently


parser = argparse.ArgumentParser(description="help")
parser.add_argument(
    "-f",
    dest="solidity_file_or_folder",
    type=str,
    help="Path to Solidty file or folder",
)
parser.add_argument(
    "-r",
    dest="solc_remappings",
    type=str,
    nargs="+",
    help="Solidity compiler remappings",
)
parser.add_argument(
    "-s",
    dest="solc_compiler_version",
    type=str,
    help="Solidity compiler version",
)
parser.add_argument(
    "-ast", dest="ast_json_file", type=str, help="Path to Solidty AST JSON file"
)
parser.add_argument(
    "-n",
    dest="project_name",
    type=str,
    help="Name of the project, if not supplied - name is automatically picked",
)
args = parser.parse_args()


# Silence tool prints
class Silent(io.StringIO):
    def write(self, txt):
        pass


def create_directory_if_not_exists(directory_path):
    # Check if the directory already exists
    if not os.path.exists(directory_path):
        # Create the directory
        os.makedirs(directory_path)
        log("info", f"Created directory: {directory_path}")


def is_valid_json(json_string):
    if not json_string:
        return False
    try:
        json.loads("".join(json_string))
        return True
    except ValueError:
        return False


def draw_graph(outputs_dir, file_name, G):
    nt = Network("800px", "1800px", select_menu=True, directed=True)
    nt.from_nx(G)
    nt.show_buttons(filter_=[])

    original_stdout = sys.stdout
    sys.stdout = Silent()
    file_path = outputs_dir / f"{file_name}.html"
    nt.show(str(file_path), notebook=False)
    sys.stdout = original_stdout

    graph_vis_lib_path = outputs_dir / "lib"
    if os.path.exists(graph_vis_lib_path):
        shutil.rmtree(graph_vis_lib_path)
    shutil.move("lib", graph_vis_lib_path)


def save_python_ast(outputs_dir, file_name, data):
    orig_name = file_name
    file_path = outputs_dir / f"{file_name}.py"
    with open(file_path, "w") as file:
        data_str = repr(data)
        file.write(f"{orig_name} = {data_str}\n")


def save_as_json(file_path, json_data):
    with open(file_path, "w") as outfile:
        json.dump(json_data, outfile, indent=4)


def run_command(command):
    log("info", f"{command}")
    results = []
    process = subprocess.Popen(
        shlex.split(command), stdout=subprocess.PIPE, encoding="utf-8", shell=False
    )
    while True:
        output = process.stdout.readline()
        if output == "" and process.poll() is not None:
            break
        if output:
            results.append(output.strip())
    return results


def get_all_solidity_files(folder_path):
    solidity_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".sol"):
                # only include files with a pragma statement
                file_path = os.path.join(root, file)
                with open(file_path, "r") as input_file:
                    head = [line for line, _ in zip(input_file, range(10))]
                    if any("pragma" in line for line in head):
                        solidity_files.append(file_path)

    return solidity_files


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


def find_and_read_sol_file(folder_path):
    # Search for .sol files recursively in the given folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".sol"):
                sol_file_path = os.path.join(root, file)
                with open(sol_file_path, "r") as input_file:
                    head = [line for line, _ in zip(input_file, range(10))]
                    if any("pragma" in line for line in head):
                        return sol_file_path


def get_solidity_version_from_file(solidity_file_or_folder: str) -> str:
    solc_required_version = None
    version_pattern = r"pragma\s+solidity\s+([^;]+);"
    version_number_pattern = r"\d+\.\d+\.\d+|\d+\.\d+"
    with open(solidity_file_or_folder, "r") as f:
        content = f.read()

        match = re.search(version_pattern, content)
        if match:
            version_match = match.group(1)

            # Extract all version numbers
            version_numbers = re.findall(version_number_pattern, version_match)

            if version_numbers:
                # If there is an upper limit, choose the version just below the upper limit
                if "<" in version_match and len(version_numbers) > 1:
                    upper_version = version_numbers[-1]
                    lower_version = (
                        version_numbers[0] if len(version_numbers) > 1 else None
                    )

                    major, minor, *patch = map(int, upper_version.split("."))
                    lower_major, lower_minor, *lower_patch = (
                        map(int, lower_version.split(".")) if lower_version else (0, 0)
                    )

                    if minor > 0 and (
                        major > lower_major
                        or (major == lower_major and minor - 1 >= lower_minor)
                    ):
                        # Choose the highest minor version below the upper limit
                        solc_required_version = f"{major}.{minor - 1}.0"
                    else:
                        # If the upper limit is too close to the lower limit, return the lower limit
                        solc_required_version = lower_version
                else:
                    # Return the highest version number found
                    solc_required_version = version_numbers[-1]
    if solc_required_version is None:
        log("warning", "Couldn't extract solidity version from file, trying 0.8.20")
        solc_required_version = "0.8.20"
    return solc_required_version


def main():
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    outputs_dir = Path.cwd() / ".eburger"
    create_directory_if_not_exists(outputs_dir)

    if args.solidity_file_or_folder:
        path_type = None
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
    if path_type == "foundry":
        log("info", "Foundry project detected, compiling using forge")
        run_command(f"forge clean")
        forge_out_dir = outputs_dir / "forge-output"
        create_directory_if_not_exists(forge_out_dir)
        build_output_lines = run_command(
            f"forge build --force --skip test script --build-info --build-info-path {forge_out_dir}"
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
        output_filename = outputs_dir / f"{filename}.json"

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
            solc_install_res = run_command(
                f"solc-select install {solc_required_version}"
            )
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
        output_filename = outputs_dir / f"{filename}.json"
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

    elif args.ast_json_file:
        filename = args.ast_json_file
        with open(args.ast_json_file, "r") as f:
            ast_json = json.load(f)
            ast_json, src_file_list = reduce_json(ast_json)
        save_as_json(output_filename, ast_json)

    # Parse AST
    G = nx.MultiDiGraph()
    ast_roots, G = parse_solidity_ast(ast_json, G)

    # Draw graph
    draw_graph(outputs_dir, filename, G)
    save_python_ast(outputs_dir, filename, ast_roots)

    # Parse YAML templates
    if __package__ is None or __package__ == "":
        templates_directory_path = Path.cwd() / "eburger" / "templates"
    else:
        templates_directory_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "templates"
        )
    log("info", f"Templates path: {templates_directory_path}")

    insights = process_files_concurrently(
        templates_directory_path, ast_json, src_file_list
    )

    # Convert the insights to JSON and print
    if insights:
        report_file_name = outputs_dir / f"{filename}_insights.json"
        save_as_json(report_file_name, insights)

        # If path is a folder, also put a json insights file at the folder root.
        if path_type == "folder":
            project_report_file_name = Path.cwd() / "eburger-output.json"
            save_as_json(project_report_file_name, insights)

    log("success", f"Results saved to {outputs_dir}/{filename}.*")


if __name__ == "__main__":
    main()
