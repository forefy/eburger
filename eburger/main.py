import json
import os
from pathlib import Path
import shutil
import sys
from eburger.utils.cli_args import args
from eburger.utils.filesystem import (
    create_directory_if_not_exists,
    create_or_empty_directory,
    find_and_read_sol_file,
    find_recursive_files_by_patterns,
    get_foundry_ast_json,
    get_hardhat_ast_json,
    get_solidity_version_from_file,
    roughly_check_valid_file_path_name,
    select_project,
)
from eburger.utils.helpers import (
    construct_solc_cmdline,
    get_filename_from_path,
    is_valid_json,
    run_command,
)
from eburger.utils.installers import (
    construct_sourceable_nvm_string,
    install_foundry_if_not_found,
    install_hardhat_if_not_found,
    set_solc_compiler_version,
)
from eburger.utils.logger import log
import eburger.settings as settings
from eburger.serializer import parse_solidity_ast, reduce_json
from eburger.utils.outputs import (
    calculate_nsloc,
    draw_nsloc_table,
    save_as_json,
    save_as_markdown,
    save_as_sarif,
)
from eburger.yaml_parser import process_files_concurrently


def main():
    if not args.solidity_file_or_folder and not args.ast_json_file:
        args.solidity_file_or_folder = "."

    log("debug", f"Project path: {args.solidity_file_or_folder}")

    create_directory_if_not_exists(settings.outputs_dir)
    path_type = None

    if args.solidity_file_or_folder:
        if os.path.isfile(args.solidity_file_or_folder):
            log("debug", f"Path type: file")
            path_type = "file"
        elif os.path.isdir(args.solidity_file_or_folder):
            log("debug", f"Path type: folder")
            path_type = "folder"

            project_paths = find_recursive_files_by_patterns(
                args.solidity_file_or_folder,
                ["foundry.toml", "hardhat.config.*"],
            )

            selected_path_file_name = None
            if len(project_paths) < 1:
                log(
                    "info",
                    "No contract projects here, specifiy a path/single files via `-f` or run `eburger` in the smart contract project root.",
                )
                sys.exit(0)
            elif len(project_paths) > 1:
                if args.auto_selection:
                    selected_project_path = Path(project_paths[args.auto_selection - 1])
                else:
                    selected_project_path = select_project(project_paths)

                selected_path_file_name = selected_project_path.name
                args.solidity_file_or_folder = selected_project_path.parent
                log(
                    "info",
                    f"Project path set to: {args.solidity_file_or_folder} ({selected_path_file_name})",
                )
            else:
                args.solidity_file_or_folder = project_paths[0].parent

            # Update project root to the user arg
            settings.project_root = settings.project_root / args.solidity_file_or_folder

            # Check if foundry project, in which case it is better just using forge
            if (settings.project_root / "foundry.toml").exists() and (
                selected_path_file_name in ["foundry.toml", None]
            ):
                path_type = "foundry"

            # Check if hardhat project
            elif any(settings.project_root.glob("hardhat.config.*")) and (
                selected_path_file_name
                in ["hardhat.config.js", "hardhat.config.ts", None]
            ):
                path_type = "hardhat"
        else:
            log(
                "info",
                f"{args.solidity_file_or_folder} is neither a file nor a directory, please select a valid path.",
            )
            sys.exit(0)

    elif args.ast_json_file:
        filename = args.ast_json_file
        filename = filename.replace(".json", "")  # Clean possible file extension
        filename = filename.replace(
            ".eburger/", ""
        )  # Protection against analysis of files inside the output path
        with open(args.ast_json_file, "r") as f:
            ast_json = json.load(f)
            ast_json, src_file_list = reduce_json(ast_json)
        output_path = settings.outputs_dir / f"{filename}.json"

        save_as_json(output_path, ast_json)

    # NSLOC only mode
    if args.nsloc:
        draw_nsloc_table()

    if path_type is not None:
        # Foundry compilation flow
        if path_type == "foundry":
            log("info", "Foundry project detected, compiling using forge.")
            install_foundry_if_not_found()

            if args.solc_remappings:
                log("warning", "Ignoring the -r option in foundry based projects.")

            run_command(f"forge clean", args.solidity_file_or_folder)
            forge_out_dir = settings.outputs_dir / "forge-output"
            create_or_empty_directory(forge_out_dir)

            run_command(
                f"forge build --force --skip {' '.join(settings.excluded_dirs)} --build-info --build-info-path {forge_out_dir}",
                args.solidity_file_or_folder,
                live_output=args.debug,
            )

            sample_file_path = find_and_read_sol_file(args.solidity_file_or_folder)
            filename, output_filename = get_filename_from_path(sample_file_path)

            ast_json = get_foundry_ast_json(forge_out_dir)
            ast_json, src_file_list = reduce_json(ast_json)
            save_as_json(output_filename, ast_json)

        # Hardhat compilation flow
        if path_type == "hardhat":
            log("info", "Hardhat project detected, compiling using hardhat.")
            install_hardhat_if_not_found()

            if args.solc_remappings:
                log("warning", "Ignoring the -r option in hardhat based projects.")

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
            ast_json, src_file_list = reduce_json(ast_json)
            save_as_json(output_filename, ast_json)

        # solc compilation flow
        elif path_type in ["file", "folder"]:
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
                log("error", "Error constructing solc command line")

            solc_compile_res, _ = run_command(solc_cmdline, live_output=True)

            # We continue as long as solc compiled something
            if not is_valid_json(solc_compile_res):
                error_string = "Locally installed solc errored out trying to compile the contract. Please review comiler warnings above"
                if not args.solc_remappings:
                    error_string += (
                        "or see if library remappings (using the -r option) are needed"
                    )
                if not args.solc_compiler_version:
                    error_string += ", or try specifing the solidity compiler version (using the -s option)"
                error_string += "."
                log(
                    "error",
                    error_string,
                )
            solc_compile_res_parsed = json.loads("".join(solc_compile_res))
            ast_json, src_file_list = reduce_json(solc_compile_res_parsed)
            save_as_json(output_filename, solc_compile_res_parsed)

    # Parse AST
    ast_roots = parse_solidity_ast(ast_json)

    # Parse YAML templates
    if args.template_paths:
        settings.templates_directories = []
        for template_path in args.template_paths:
            settings.templates_directories.append(Path(template_path))
            log("info", f"Templates path: {Path(template_path)}")

    insights = process_files_concurrently(ast_roots, src_file_list)

    if insights:
        analysis_output = {}
        analysis_output["insights"] = insights

        _, summary = calculate_nsloc()
        analysis_output["nsloc"] = summary

        insights_json_path = settings.outputs_dir / f"eburger_output_{filename}.json"
        save_as_json(insights_json_path, analysis_output)

        if roughly_check_valid_file_path_name(args.output):
            custom_output_path = Path(args.output)
            file_extension = custom_output_path.suffix[1:]
            if file_extension not in ["json", "sarif", "md"]:
                log(
                    "error",
                    f"Unrecognized output file extension provided. ({file_extension})",
                )

            results_path = Path.cwd() / custom_output_path
            if file_extension == "sarif":
                save_as_sarif(results_path, insights)
            elif file_extension == "md":
                save_as_markdown(results_path, analysis_output)
            elif file_extension == "json":
                save_as_json(results_path, analysis_output)
        elif args.output == "sarif":
            results_path = settings.project_root / f"eburger-output.sarif"
            save_as_sarif(results_path, insights)
        elif args.output in ["markdown", "md"]:
            results_path = settings.project_root / f"eburger-output.md"
            save_as_markdown(results_path, analysis_output)
        else:
            results_path = settings.project_root / "eburger-output.json"
            save_as_json(results_path, analysis_output)

        log(
            "success",
            f"Results saved to {str(Path(results_path).resolve())}",
        )
    else:
        log("success", f"No insights found. Results saved to {settings.outputs_dir}")


if __name__ == "__main__":
    main()
