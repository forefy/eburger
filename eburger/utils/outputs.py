# Silence tool prints
import json
from pathlib import Path
import sys
from prettytable import PrettyTable
from pygount import ProjectSummary, SourceAnalysis

from eburger import settings
from eburger.utils.cli_args import args
from eburger.utils.logger import log


def save_as_json(file_path, json_data):
    with open(file_path, "w") as outfile:
        json.dump(json_data, outfile, indent=4)


def calculate_nsloc() -> (list, list):
    project_summary = ProjectSummary()
    project_sources = []
    solidity_file_or_folder = Path(args.solidity_file_or_folder)
    if solidity_file_or_folder.is_dir():
        source_paths = solidity_file_or_folder.glob("**/*.sol")
    elif solidity_file_or_folder.is_file() and solidity_file_or_folder.suffix == ".sol":
        source_paths = [solidity_file_or_folder]
    else:
        log("error", "Invalid solidity file or folder.")

    for source_path in source_paths:
        # Exclude non-files
        if not source_path.is_file():
            continue

        # Exclude contracts
        source_path_str = str(source_path)
        if any(
            substring in source_path_str for substring in settings.excluded_contracts
        ):
            continue

        # Exclude dirs
        source_path_str = str(source_path)
        if any(
            substring in source_path_str.casefold()
            for substring in settings.excluded_dirs + ["mocks", "lib", "node_modules"]
        ):
            continue

        source_analysis = SourceAnalysis.from_file(source_path, "nsloc")
        project_summary.add(source_analysis)
        project_sources.append(source_analysis)

    found_solidity = False
    project_solidity_summary = {}
    for language_summary in project_summary.language_to_language_summary_map.values():
        if language_summary.language == "Solidity" and not found_solidity:
            project_solidity_summary["file_count"] = language_summary.file_count
            project_solidity_summary["code_count"] = language_summary.code_count
            project_solidity_summary["documentation_count"] = (
                language_summary.documentation_count
            )
            project_solidity_summary["empty_count"] = language_summary.empty_count
            project_solidity_summary["string_count"] = language_summary.string_count
            found_solidity = True
            break

    return project_sources, project_solidity_summary


def draw_nsloc_table():
    project_sources, summary = calculate_nsloc()
    table = PrettyTable()
    table.field_names = [
        "Source files",
        "Code",
        "Docs",
        "Empty",
        "Strings",
    ]

    for source in project_sources:
        table.add_row(
            [
                str(Path(settings.project_root / source.path).resolve()),
                source.code_count,
                source.documentation_count,
                source.empty_count,
                source.string_count,
            ]
        )

    table.add_row(["", "", "", "", ""])

    table.add_row(
        [
            f"Total {summary.get('file_count')} file{'s' if summary.get('file_count') != 1 else ''}",
            summary.get("code_count"),
            summary.get("documentation_count"),
            summary.get("empty_count"),
            summary.get("string_count"),
        ]
    )

    print(table)
    sys.exit(0)
