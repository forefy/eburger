import argparse

parser = argparse.ArgumentParser(description="help")

parser.add_argument(
    "-f",
    "--file",
    dest="solidity_file_or_folder",
    type=str,
    help="Path to Solidty file or folder",
)
parser.add_argument(
    "-r",
    "--remappings",
    dest="solc_remappings",
    type=str,
    nargs="+",
    help="Solidity compiler remappings",
)
parser.add_argument(
    "-s",
    "--solc-version",
    dest="solc_compiler_version",
    type=str,
    help="Force the Solidity compiler version",
)
parser.add_argument(
    "-a",
    "--ast",
    dest="ast_json_file",
    type=str,
    help="Path to Solidty AST JSON file",
)
parser.add_argument(
    "-pn",
    "--project-name",
    dest="project_name",
    type=str,
    help="Name of the project, if not supplied - name is automatically picked",
)
parser.add_argument(
    "-n",
    "--no",
    dest="no",
    type=str,
    nargs="+",
    default=[],
    help="Exclude logging output types (e.g. info warning success insights)",
)
parser.add_argument(
    "-t",
    "--templates",
    dest="templates_path",
    type=str,
    help="Path to eburger yaml templates folder.",
)
args = parser.parse_args()
