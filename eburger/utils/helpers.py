import json
import shlex
import subprocess

from eburger.utils.cli_args import args
from eburger.utils.filesystem import get_all_solidity_files
from eburger.utils.logger import log


def is_valid_json(json_string):
    if not json_string:
        return False
    try:
        json.loads("".join(json_string))
        return True
    except ValueError:
        return False


def run_command(command, directory=None, stdout=subprocess.PIPE, shell=False):
    log("info", f"{command}")
    results = []
    process = subprocess.Popen(
        command if shell else shlex.split(command),
        stdout=subprocess.PIPE,
        encoding="utf-8",
        shell=shell,
        cwd=directory,
    )
    while True:
        output = process.stdout.readline()
        if output == "" and process.poll() is not None:
            break
        if output:
            results.append(output.strip())
    return results


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
