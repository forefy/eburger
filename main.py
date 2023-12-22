import json
import re
import shlex
import subprocess
from eburger.serializer import parse_solidity_ast
import networkx as nx
from pyvis.network import Network
import argparse

parser = argparse.ArgumentParser(description="help")
parser.add_argument("-sf", dest="solidity_file", type=str, help="path to Solidty file")
parser.add_argument(
    "-sr",
    dest="solc_remappings",
    type=str,
    nargs="+",
    help="Solidity compiler remappings",
)
parser.add_argument(
    "-jf", dest="json_file", type=str, help="path to Solidty AST JSON file"
)
args = parser.parse_args()


def draw_graph(ast_json):
    G = nx.MultiDiGraph()
    ast_roots, G = parse_solidity_ast(ast_json, G)

    nt = Network("800px", "1800px", select_menu=True, directed=True)
    nt.from_nx(G)

    nt.show_buttons(filter_=[])
    nt.show("output.html", notebook=False)


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


def construct_solc_cmdline():
    solc_cmdline = "solc"
    if args.solc_remappings:
        solc_cmdline += " "
        solc_cmdline += " ".join(args.solc_remappings)
    solc_cmdline += f" --combined-json abi,ast,bin,bin-runtime,srcmap,srcmap-runtime,userdoc,devdoc,hashes {args.solidity_file}"
    return solc_cmdline


if args.solidity_file:
    # get contract version
    with open(args.solidity_file, "r") as f:
        solc_required_version = None
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
        print(f"Trying to switch solc to version {solc_required_version}")
        solc_use_res = run_command(f"solc-select use {solc_required_version}")
        print("------")
        if not solc_use_res:
            print("Error switching solc version, trying to install")
            solc_install_res = run_command(
                f"solc-select install {solc_required_version}"
            )
            solc_use_res = run_command(f"solc-select use {solc_required_version}")
            if not solc_use_res:
                print("Failed to install required solc version")
                exit(0)
        solc_versions_res = run_command(f"solc-select versions")
        print(f"Successfully switched solc version")
        print("Trying to compile contract")
        from pathlib import Path

        ast_workspace = Path.cwd() / "contract_asts"
        filename_match = re.search(r"/([^/]+)\.sol$", args.solidity_file)
        filename = filename_match.group(1) if filename_match else None
        output_filename = ast_workspace / f"{filename}.json"
        solc_remappings = " ".join(args.solc_remappings)
        solc_cmdline = construct_solc_cmdline()
        print(solc_cmdline)
        solc_compile_res = run_command(solc_cmdline)
        solc_compile_res_parsed = json.loads("".join(solc_compile_res))
        with open(output_filename, "w") as outfile:
            json.dump(solc_compile_res_parsed, outfile, indent=4)
        with open(output_filename, "r") as f:
            ast_json = json.load(f)
            draw_graph(ast_json)

elif args.json_file:
    with open(args.json_file, "r") as f:
        ast_json = json.load(f)
        draw_graph(ast_json)
