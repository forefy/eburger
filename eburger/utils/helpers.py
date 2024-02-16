from datetime import datetime
import json
import os
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
