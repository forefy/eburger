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

from eburger.serializer import parse_solidity_ast
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
                solidity_files.append(os.path.join(folder_path, file))
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
                return sol_file_path


def get_solidity_version_from_file(solidity_file_or_folder: str) -> str:
    with open(solidity_file_or_folder, "r") as f:
        for line in f:
            if line.startswith("pragma solidity"):
                solc_required_version = (
                    line.replace("pragma solidity ", "")
                    .replace("^", "")
                    .replace(";", "")
                )
                break
    if not solc_required_version:
        log("error", "Couldn't extract solidity version from file")
        exit(0)
    return solc_required_version


def main():
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    if args.solidity_file_or_folder:
        path_type = None
        if os.path.isfile(args.solidity_file_or_folder):
            path_type = "file"
        elif os.path.isdir(args.solidity_file_or_folder):
            path_type = "folder"
        else:
            log(
                "error",
                f"{args.solidity_file_or_folder} is neither a file nor a directory.",
            )
            sys.exit(0)

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

        # get contract version
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
        log("info", "Successfully switched solc version")
        log("info", "Trying to compile contract")

        outputs_dir = Path.cwd() / "contract_outputs"
        create_directory_if_not_exists(outputs_dir)

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
        log("info", f"[Info] {solc_cmdline}")
        solc_compile_res = run_command(solc_cmdline)
        solc_compile_res_parsed = json.loads("".join(solc_compile_res))
        save_as_json(output_filename, solc_compile_res_parsed)
        with open(output_filename, "r") as f:
            ast_json = json.load(f)

    elif args.ast_json_file:
        filename = args.ast_json_file
        with open(args.ast_json_file, "r") as f:
            ast_json = json.load(f)

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

    insights = process_files_concurrently(templates_directory_path, ast_json)

    # Convert the insights to JSON and print
    if insights:
        # insights_json_printable = json.dumps(insights, indent=4)
        report_file_name = outputs_dir / f"{filename}_insights.json"
        save_as_json(report_file_name, insights)

    log("success", f"Results saved to {outputs_dir}/{filename}.*")


if __name__ == "__main__":
    main()
