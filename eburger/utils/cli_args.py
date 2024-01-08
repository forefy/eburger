import argparse
import sys

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
    help="Force the Solidity compiler version",
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
