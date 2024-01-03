from datetime import datetime
import json
import os
from pathlib import Path
import re
import shlex
import shutil
import subprocess
import sys
import uuid
from eburger.serializer import parse_solidity_ast
import networkx as nx
from pyvis.network import Network
import argparse

from eburger.yaml_parser import process_files_concurrently

parser = argparse.ArgumentParser(description="help")
parser.add_argument(
    "-file", dest="solidity_file", type=str, help="path to Solidty file"
)
parser.add_argument(
    "-folder", dest="solidity_folder", type=str, help="path to Solidty folder"
)
parser.add_argument(
    "-r",
    dest="solc_remappings",
    type=str,
    nargs="+",
    help="Solidity compiler remappings",
)
parser.add_argument(
    "-ast", dest="ast_json_file", type=str, help="path to Solidty AST JSON file"
)
parser.add_argument(
    "-n",
    dest="project_name",
    type=str,
    help="name of the project, if not supplied, name is automatically picked",
)
args = parser.parse_args()


def draw_graph(file_name):
    nt = Network("800px", "1800px", select_menu=True, directed=True)
    nt.from_nx(G)
    nt.show_buttons(filter_=[])
    nt.show(f"contract_outputs/{file_name}.html", notebook=False)
    graph_vis_lib_path = Path("contract_outputs", "lib")
    if os.path.exists(graph_vis_lib_path):
        shutil.rmtree(graph_vis_lib_path)
    shutil.move("lib", graph_vis_lib_path)


def save_python_ast(file_name, data):
    orig_name = file_name
    file_name = f"contract_outputs/{file_name}.py"
    with open(file_name, "w") as file:
        data_str = repr(data)
        file.write(f"{orig_name} = {data_str}\n")


def save_as_json(file_name, json_data):
    with open(file_name, "w") as outfile:
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
            # print(output.strip())
            results.append(output.strip())

    return results


def get_all_solidity_files(folder_path):
    solidity_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".sol"):
                solidity_files.append(os.path.join(folder_path, file))
    return solidity_files


def construct_solc_cmdline(compilation_source_path: str) -> str:
    solc_cmdline = "solc"
    if args.solc_remappings:
        solc_cmdline += " "
        solc_cmdline += " ".join(args.solc_remappings)
    if args.solidity_folder:
        solidity_files = get_all_solidity_files(args.solidity_folder)
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


def get_solidity_version_from_file(solidity_file: str) -> str:
    with open(solidity_file, "r") as f:
        for line in f:
            if line.startswith("pragma solidity"):
                solc_required_version = (
                    line.replace("pragma solidity ", "")
                    .replace("^", "")
                    .replace(";", "")
                )
                break
    if not solc_required_version:
        print("Couldn't extract solidity version from file")
        exit(0)
    return solc_required_version


if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

if args.solidity_file or args.solidity_folder:
    sample_file_path = None
    compilation_source_path = None
    if args.solidity_file:
        sample_file_path = args.solidity_file
        compilation_source_path = args.solidity_file
    elif args.solidity_folder:
        compilation_source_path = args.solidity_folder
        extracted_sample_file_path = find_and_read_sol_file(args.solidity_folder)
        if extracted_sample_file_path is not None:
            sample_file_path = extracted_sample_file_path

    # get contract version
    solc_required_version = get_solidity_version_from_file(sample_file_path)
    print(f"Trying to switch solc to version {solc_required_version}")
    solc_use_res = run_command(f"solc-select use {solc_required_version}")
    print("------")
    if not solc_use_res:
        print("Error switching solc version, trying to install")
        solc_install_res = run_command(f"solc-select install {solc_required_version}")
        solc_use_res = run_command(f"solc-select use {solc_required_version}")
        if not solc_use_res:
            print("Failed to install required solc version")
            exit(0)
    solc_versions_res = run_command(f"solc-select versions")
    print(f"Successfully switched solc version")
    print("Trying to compile contract")

    outputs_dir = Path.cwd() / "contract_outputs"
    if args.project_name:
        filename = args.project_name
    else:
        filename_match = re.search(r"/([^/]+)\.sol$", sample_file_path)
        filename = filename_match.group(1) if filename_match else None
    filename = f"{filename}_{datetime.now().strftime('%m%y')}"
    output_filename = outputs_dir / f"{filename}.json"
    solc_cmdline = construct_solc_cmdline(compilation_source_path)
    if solc_cmdline is None:
        print("Error constructing solc command line")
        exit(0)
    print(solc_cmdline)
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
draw_graph(filename)
save_python_ast(filename, ast_roots)

# Parse YAML templates
templates_path = Path(os.getcwd()) / "templates"
insights = process_files_concurrently(templates_path, ast_json)

# Convert the insights to JSON and print
# insights_json = json.dumps(insights, indent=4)
report_file_name = outputs_dir / f"{filename}_insights.json"
save_as_json(report_file_name, insights)
