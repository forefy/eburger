from datetime import datetime
import json
from pathlib import Path
import re
import shlex
import subprocess
from eburger import settings

from eburger.utils.cli_args import args
from eburger.utils.filesystem import get_all_solidity_files
from eburger.utils.logger import log


def is_valid_json(json_string: str) -> bool:
    if not json_string:
        return False
    try:
        json.loads("".join(json_string))
        return True
    except ValueError:
        return False


def run_command(
    command: str, directory: Path = None, shell: bool = False, live_output: bool = False
):
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
                log("info", output_stripped)
            results.append(output_stripped)

        if error:
            error_stripped = error.strip()
            if live_output:
                log("info", error_stripped)
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
    output_filename = settings.outputs_dir / f"{filename}.json"

    return filename, output_filename
