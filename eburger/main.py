import json
import os
import sys
from pathlib import Path

import eburger.settings as settings
from eburger.serializer import parse_solidity_ast, reduce_json
from eburger.utils.cli_args import args
from eburger.utils.compilers import compile_foundry, compile_hardhat, compile_solc
from eburger.utils.filesystem import (
    create_directory_if_not_exists,
    find_recursive_files_by_patterns,
    roughly_check_valid_file_path_name,
    select_project,
)
from eburger.utils.helpers import get_eburger_version
from eburger.utils.installers import (
    install_foundry_if_not_found,
    install_hardhat_if_not_found,
)
from eburger.utils.logger import log
from eburger.utils.outputs import (
    calculate_nsloc,
    draw_nsloc_table,
    save_as_json,
    save_as_markdown,
    save_as_sarif,
)
from eburger.yaml_parser import process_files_concurrently


def main():
    if args.version:
        print(get_eburger_version())
        sys.exit(0)

    if not args.solidity_file_or_folder:
        args.solidity_file_or_folder = "."

    if args.ast_json_file and args.solidity_file_or_folder:
        settings.outputs_dir = (
            settings.project_root / args.solidity_file_or_folder
        ).resolve() / ".eburger"

    create_directory_if_not_exists(settings.outputs_dir)

    log("debug", f"Project path: {args.solidity_file_or_folder}")

    path_type = None

    if args.ast_json_file:
        filename = Path(args.ast_json_file).name

        with open(args.ast_json_file, "r") as f:
            ast_json = json.load(f)
            ast_json, src_paths = reduce_json(ast_json)

        ast_suffix = "_ast"
        if filename.endswith("_ast"):
            ast_suffix = ""

        output_path = (settings.outputs_dir / f"{filename}{ast_suffix}.json").resolve()

        save_as_json(output_path, ast_json)

    elif args.solidity_file_or_folder:
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

    # NSLOC only mode
    if args.nsloc:
        draw_nsloc_table()

    # Compilation
    if path_type is not None:
        if path_type == "foundry":
            log("info", "Foundry project detected, compiling using forge.")
            _, forge_full_path_binary_found = install_foundry_if_not_found()

            if args.solc_remappings:
                log("warning", "Ignoring the -r option in foundry based projects.")

            output_filename, ast_json, filename, src_paths = compile_foundry(
                forge_full_path_binary_found
            )
            save_as_json(output_filename, ast_json)

        elif path_type == "hardhat":
            log("info", "Hardhat project detected, compiling using hardhat.")
            install_hardhat_if_not_found()

            if args.solc_remappings:
                log("warning", "Ignoring the -r option in hardhat based projects.")

            output_filename, ast_json, filename, src_paths = compile_hardhat()
            save_as_json(output_filename, ast_json)

        # solc compilation flow
        elif path_type in ["file", "folder"]:
            output_filename, ast_json, filename, src_paths, solc_compile_res_parsed = (
                compile_solc(path_type)
            )

            save_as_json(output_filename, solc_compile_res_parsed)

    # Parse AST
    ast_roots = parse_solidity_ast(ast_json)

    # Parse YAML templates
    if args.template_paths:
        settings.templates_directories = []
        for template_path in args.template_paths:
            settings.templates_directories.append(Path(template_path))
            log("info", f"Templates path: {Path(template_path)}")

    insights = process_files_concurrently(ast_roots, src_paths)

    if insights:
        analysis_output = {}
        analysis_output["insights"] = insights
        _, summary = calculate_nsloc()
        analysis_output["nsloc"] = summary

        insights_json_path = settings.outputs_dir / f"{filename}_eburger_output.json"
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
