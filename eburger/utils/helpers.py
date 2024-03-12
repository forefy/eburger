import json
import os
import re
import shlex
import subprocess
from datetime import datetime
from importlib.metadata import version
from pathlib import Path

from eburger import settings
from eburger.utils.cli_args import args
from eburger.utils.filesystem import get_all_solidity_files
from eburger.utils.logger import log
from packaging.version import parse as parse_version


def is_valid_json(json_string: str) -> bool:
    if not json_string:
        return False
    try:
        json.loads("".join(json_string))
        return True
    except ValueError:
        return False


def run_command(
    command: str,
    directory: Path = None,
    shell: bool = False,
    live_output: bool = False,
) -> tuple[list, list]:
    log("info", f"{command}")

    results = []
    errors = []

    process = subprocess.Popen(
        command if shell else shlex.split(command),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        shell=shell,
        cwd=directory,
    )
    while True:
        output = process.stdout.readline()
        error = process.stderr.readline()

        if output == "" and error == "" and process.poll() is not None:
            break
        if output:
            output_stripped = output.strip()
            if live_output:
                if args.debug:
                    log("debug", output_stripped)
                else:
                    log("info", output_stripped)
            results.append(output_stripped)

        if error:
            error_stripped = error.strip()
            if live_output:
                if args.debug:
                    log("debug", error_stripped)
                else:
                    log("warning", error_stripped)
            errors.append(error_stripped)

    return results, errors


def construct_solc_cmdline(path_type: str, compilation_source_path: str) -> str:
    solc_cmdline = "solc"
    if args.solc_remappings:
        solc_cmdline += " "
        solc_cmdline += " ".join(args.solc_remappings)
    if path_type == "folder":
        solidity_files = get_all_solidity_files(args.solidity_file_or_folder)
        compilation_source_path = " ".join(solidity_files)
    solc_cmdline += f" --allow-paths . --combined-json abi,ast,bin,bin-runtime,srcmap,srcmap-runtime,userdoc,devdoc,hashes {compilation_source_path}"
    return solc_cmdline


def get_filename_from_path(file_path: str) -> tuple:
    if args.project_name:
        filename = args.project_name
    else:
        filename_match = re.search(r"/([^/]+)\.sol$", file_path)
        filename = filename_match.group(1) if filename_match else None
    filename = f"{filename}_{datetime.now().strftime('%m%y')}"

    ast_suffix = "_ast"
    if filename.endswith("_ast"):
        ast_suffix = ""
    output_filename = Path(settings.outputs_dir) / f"{filename}{ast_suffix}.json"

    return filename, output_filename


# Emulated "source" command to allow subprocesses to reload terminal state without forcing the user to reload the terminal
def python_shell_source(execute_source: bool = True) -> tuple[str, str]:
    shell = os.environ.get("SHELL", "")
    home = os.environ.get("HOME", "")
    source_command = ""

    if "zsh" in shell:
        zdotdir = os.environ.get("ZDOTDIR", home)
        profile = os.path.join(zdotdir, ".zshenv")
        source_command = f"{profile}"
        source_syntax = "source"
        and_sign = "&&"
    elif "bash" in shell:
        profile = os.path.join(home, ".bashrc")
        source_command = f"{profile}"
        source_syntax = "source"
        and_sign = "&&"
    elif "fish" in shell:
        profile = os.path.join(home, ".config/fish/config.fish")
        source_command = f"{profile}"
        source_syntax = "source"
        and_sign = "; and"
    elif "ash" in shell:
        profile = os.path.join(home, ".profile")
        source_command = f"{profile}"
        source_syntax = "."
        and_sign = "&&"
    else:
        log(
            "warning",
            f"Couldn't guess shell environment from '{shell}', setting the profile file to .bashrc and trying to continue.",
        )
        profile = os.path.join(home, ".bashrc")
        source_command = f"{profile}"
        source_syntax = "source"
        and_sign = "&&"

    if execute_source:
        # e.g. 'source .zshenv && printenv'
        constructed_source_command = (
            f"{source_syntax} {source_command} {and_sign} printenv"
        )
        log("info", f"/bin/bash -c {constructed_source_command}")
        pipe = subprocess.Popen(
            ["/bin/bash", "-c", f"{constructed_source_command}"],
            stdout=subprocess.PIPE,
            text=True,
        )
        env_lines = pipe.stdout.readlines()
        env_dict = {
            line.split("=", 1)[0]: line.split("=", 1)[1].strip()
            for line in env_lines
            if "=" in line
        }
        os.environ.update(env_dict)

    return source_syntax, and_sign


def get_eburger_version() -> str:
    return parse_version(version("eburger"))


def parse_code_highlight(node: dict, src_paths: list) -> tuple[str, str, str]:
    """
    Extracts and highlights a specific code snippet from a source file based on a given AST node.

    Parameters:
    - node (dict): The AST node containing the 'src' attribute with location details.
    - src_paths (list): A list of source files associated with the AST.

    Returns:
    - Tuple (str, str, str): A tuple containing:
      1. The file path of the source file where the code snippet is located.
      2. A string representation of the line and column range in the file for the code snippet.
      3. The extracted code snippet itself.

    The 'src' attribute in the node is expected to be in the format 'start_offset:length:file_index'.
    The function calculates the exact location of the code in the file and extracts it along with its
    line and column position. If the location exceeds the content of the file or is not found, appropriate
    messages and null values are returned.
    """

    src_location = node.get("src", "")
    file_index = int(src_location.split(":")[2])

    if file_index < len(src_paths):
        project_relative_file_name = src_paths[file_index]
    else:
        log("warning", "Unrecognized AST src node, using default source file.")
        project_relative_file_name = src_paths[0]

    if args.solidity_file_or_folder and args.ast_json_file:
        file_path = str(
            Path(
                settings.project_root
                / Path(args.solidity_file_or_folder)
                / project_relative_file_name
            ).resolve()
        )
    else:
        file_path = str(
            Path(settings.project_root / project_relative_file_name).resolve()
        )

    if args.relative_file_paths:
        result_file_path_uri = project_relative_file_name
    else:
        result_file_path_uri = file_path

    start_offset, length, _ = map(int, src_location.split(":"))

    file_content = None
    try:
        with open(file_path, "r") as file:
            file_content = file.read()
    except FileNotFoundError:
        log(
            "error",
            f"Non-existent file path extracted from AST: {file_path}. Try to use `-f` to specify a path to the project's original folder to get full results.",
        )
    if file_content is None:
        log("warning", f"File {file_path} unreadable during code lines extraction.")
        return "File unreadable.", None, None

    if start_offset + length > len(file_content):
        log(
            "error",
            f"The start offset and length exceed the file content for file: {file_path}",
        )

    vulnerable_code = file_content[start_offset : start_offset + length]
    # Find the line number and character positions
    current_offset = 0
    line_number = 1
    for line in file_content.split("\n"):
        end_offset = current_offset + len(line)
        if current_offset <= start_offset < end_offset:
            start_char = start_offset - current_offset
            end_char = min(start_char + length, len(line))
            return (
                result_file_path_uri,
                f"Line {line_number} Columns {start_char + 1}-{end_char + 1}",
                vulnerable_code,
            )
        current_offset = end_offset + 1  # +1 for the newline character
        line_number += 1
    return "Location not found in file.", None, None
