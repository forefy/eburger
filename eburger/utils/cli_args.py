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
    dest="template_paths",
    type=str,
    nargs="+",
    help="Path to eburger yaml templates folder",
)
parser.add_argument(
    "-d",
    "--debug",
    dest="debug",
    action="store_true",
    help="Print debug output",
)
parser.add_argument(
    "-ns",
    "--nsloc",
    dest="nsloc",
    action="store_true",
    help="Only print summary of NSLOC (Normalized Source Code)",
)
parser.add_argument(
    "-o",
    "--output",
    dest="output",
    type=str,
    help="Results output format: json (default) / sarif",
)
parser.add_argument(
    "-as",
    "--auto-selection",
    dest="auto_selection",
    type=int,
    help="If multiple projects are present within the eburger working directory, choose the N'th option without prompting.",
)

parser.add_argument(
    "-si",
    "--skip-installations",
    dest="skip_installations",
    action="store_true",
    help="Don't install missing dependencies automatically.",
)

parser.add_argument(
    "-rp",
    "--relative_paths",
    dest="relative_file_paths",
    action="store_true",
    help="Don't install missing dependencies automatically.",
)

# Only here to allow "." as an argument, ignored in the rest of the code.
parser.add_argument(
    "default_solidity_file_or_folder",
    type=str,
    nargs="?",
    default=".",
    help=argparse.SUPPRESS,
)
args = parser.parse_args()
