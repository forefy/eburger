import json
import os
import shutil
import sys
from pathlib import Path

from eburger import settings
from eburger.serializer import reduce_json
from eburger.utils.cli_args import args
from eburger.utils.filesystem import (
    create_or_empty_directory,
    find_and_read_sol_file,
    get_foundry_ast_json,
    get_hardhat_ast_json,
    get_solidity_version_from_file,
)
from eburger.utils.helpers import (
    construct_solc_cmdline,
    get_filename_from_path,
    is_valid_json,
    run_command,
)
from eburger.utils.installers import (
    construct_sourceable_nvm_string,
    set_solc_compiler_version,
)
from eburger.utils.logger import log


def compile_solc(path_type: str) -> tuple[Path, dict, str, list, dict]:
    try:
        run_command("solc --version")
        run_command("solc-select versions")
    except FileNotFoundError:
        log(
            "info",
            "Please ensure solc and solc-select are installed and availble globally, and run again.",
        )
        sys.exit(0)

    sample_file_path = args.solidity_file_or_folder
    compilation_source_path = args.solidity_file_or_folder

    if path_type == "folder":
        sample_file_path = find_and_read_sol_file(args.solidity_file_or_folder)

    filename, output_filename = get_filename_from_path(sample_file_path)

    if args.solc_compiler_version:
        solc_required_version = args.solc_compiler_version
    else:
        solc_required_version = get_solidity_version_from_file(sample_file_path)
    set_solc_compiler_version(solc_required_version)
    solc_cmdline = construct_solc_cmdline(path_type, compilation_source_path)
    if solc_cmdline is None:
        log("error", "Error constructing solc command line", sorry=True)

    solc_compile_res, _ = run_command(solc_cmdline, live_output=args.debug)

    # We continue as long as solc compiled something
    if not is_valid_json(solc_compile_res):
        error_string = "Locally installed solc errored out trying to compile the contract. Please review comiler warnings above"
        if not args.solc_remappings:
            error_string += (
                "or see if library remappings (using the -r option) are needed"
            )
        if not args.solc_compiler_version:
            error_string += (
                ", or try specifing the solidity compiler version (using the -s option)"
            )
        error_string += "."
        log(
            "error",
            error_string,
        )
    solc_compile_res_parsed = json.loads("".join(solc_compile_res))
    ast_json, src_paths = reduce_json(solc_compile_res_parsed)

    return output_filename, ast_json, filename, src_paths, solc_compile_res_parsed


def compile_foundry(forge_full_path_binary_found: bool) -> tuple[Path, dict, str, list]:
    # Call foundry's full path if necessary, otherwise use the bins available through PATH
    forge_clean_command = "forge clean"
    if forge_full_path_binary_found:
        forge_clean_command = (
            f"{os.environ.get('HOME')}/.foundry/bin/{forge_clean_command}"
        )

    run_command(forge_clean_command, directory=args.solidity_file_or_folder)
    forge_out_dir = settings.outputs_dir / "forge-output"
    create_or_empty_directory(forge_out_dir)

    foundry_excluded_dirs = " ".join(
        [item for item in settings.excluded_dirs if item != "lib"]
    )
    # Call foundry's full path if necessary, otherwise use the bins available through PATH
    forge_build_command = f"forge build --force --skip {foundry_excluded_dirs} --build-info --build-info-path {forge_out_dir}"
    if forge_full_path_binary_found:
        forge_build_command = (
            f"{os.environ.get('HOME')}/.foundry/bin/{forge_build_command}"
        )

    run_command(
        forge_build_command,
        directory=args.solidity_file_or_folder,
        live_output=args.debug,
    )
    sample_file_path = find_and_read_sol_file(args.solidity_file_or_folder)
    filename, output_filename = get_filename_from_path(sample_file_path)
    ast_json = get_foundry_ast_json(forge_out_dir)

    ast_json, src_paths = reduce_json(ast_json)

    return output_filename, ast_json, filename, src_paths


def compile_hardhat() -> tuple[Path, dict, str, list]:
    # try runing npx normally, as a fallback try the construct_sourceable_nvm_string method
    # if a user hadn't got npx installed / or it's not on path (meaning it was installed in same run as the analysis)
    # it still needs the fallback option
    try:
        run_command(f"npx hardhat clean", directory=settings.project_root)
        run_command(
            f"npx hardhat compile --force",
            directory=settings.project_root,
            live_output=args.debug,
        )
    except FileNotFoundError:
        run_command(
            construct_sourceable_nvm_string("npx hardhat clean"),
            directory=settings.project_root,
        )
        run_command(
            construct_sourceable_nvm_string("npx hardhat compile --force"),
            directory=settings.project_root,
            live_output=args.debug,
        )

    # Copy compilation results to .eburger
    expected_hardhat_outfiles = os.path.join(
        args.solidity_file_or_folder, "artifacts", "build-info"
    )
    if not os.path.isdir(expected_hardhat_outfiles):
        log(
            "error",
            f"Hardhat's compilation files were not found in expected location {expected_hardhat_outfiles}",
        )
    hardhat_out_dir = settings.outputs_dir / "hardhat-output"
    if os.path.exists(hardhat_out_dir):
        shutil.rmtree(hardhat_out_dir)
    shutil.copytree(expected_hardhat_outfiles, hardhat_out_dir)

    sample_file_path = find_and_read_sol_file(args.solidity_file_or_folder)
    filename, output_filename = get_filename_from_path(sample_file_path)

    ast_json = get_hardhat_ast_json(hardhat_out_dir)

    ast_json, src_paths = reduce_json(ast_json)

    return output_filename, ast_json, filename, src_paths
