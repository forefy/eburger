# Silence tool prints
import json
import os
from pathlib import Path
import sys
from prettytable import PrettyTable
from pygount import ProjectSummary, SourceAnalysis

from eburger import settings
from eburger.utils.cli_args import args
from eburger.utils.logger import log


def save_as_json(file_path: Path, json_data: dict):
    with open(file_path, "w") as outfile:
        json.dump(json_data, outfile, indent=4)


def convert_severity_to_sarif_level(severity: str) -> str:
    match severity:
        case "High":
            sarif_level = "error"
        case "Medium":
            sarif_level = "warning"
        case "Low":
            sarif_level = "note"
        case _:
            sarif_level = "note"
    return sarif_level


def save_as_sarif(output_file_path: Path, insights: dict):
    sarif_run_template = {
        "tool": {
            "driver": {
                "name": "eburger",
                "informationUri": "https://github.com/forefy/eburger",
                "rules": [],
            }
        },
        "artifacts": [],
        "results": [],
    }

    sarif_rule_template = {
        "id": "",
        "name": "",
        "shortDescription": {"text": ""},
        "helpUri": "",
        "help": {
            "text": "",
            "markdown": "",
        },
    }

    if os.path.exists(output_file_path):
        with open(output_file_path, "r") as infile:
            try:
                sarif_json = json.load(infile)
            except json.JSONDecodeError:
                log("warninng", "")
                sarif_json = {
                    "$schema": "https://schemastore.azurewebsites.net/schemas/json/sarif-2.1.0-rtm.5.json",
                    "version": "2.1.0",
                    "runs": [],
                }
    else:
        sarif_json = {
            "$schema": "https://schemastore.azurewebsites.net/schemas/json/sarif-2.1.0-rtm.5.json",
            "version": "2.1.0",
            "runs": [],
        }

    new_run = sarif_run_template.copy()

    # insight is like a result object
    for insight in insights:
        rule_id = insight["name"].replace(" ", "_")

        rule_exists = False
        for index, rule in enumerate(new_run["tool"]["driver"]["rules"]):
            if rule["id"] == rule_id:
                rule_exists = True
                rule_index = index  # Capture the index of the existing rule
                break

        if not rule_exists:
            new_rule = sarif_rule_template.copy()
            new_rule["id"] = rule_id
            new_rule["name"] = insight["name"]
            new_rule["shortDescription"]["text"] = insight["description"]
            new_rule["helpUri"] = insight["references"][0]
            new_rule["help"]["text"] = insight["action-items"][0]
            new_rule["help"][
                "markdown"
            ] = f"[{insight['action-items'][0]}]({insight['references'][0]})"
            new_run["tool"]["driver"]["rules"].append(new_rule)
            rule_index = len(new_run["tool"]["driver"]["rules"]) - 1

        for result in insight["results"]:
            new_result = {
                "ruleId": rule_id,
                "ruleIndex": rule_index,
                "level": convert_severity_to_sarif_level(insight["severity"]),
                "message": {
                    "text": new_rule["name"]
                },  # TODO: display an instruction instead of the finding name
                "locations": [],
            }

            artifact_uri = f'file://{result["file"]}'

            artifact_index = 0
            artifact_exists = False

            # create an artifcat location for the file, if it doesn't exist
            # location should occur once per finding mostly
            for existing_artifact_index, artifact in enumerate(new_run["artifacts"]):
                if artifact["location"]["uri"] == artifact_uri:
                    artifact_index = existing_artifact_index
                    artifact_exists = True
                    break

            # If the artifact doesn't exist, add it
            if not artifact_exists:
                new_artifact = {"location": {"uri": artifact_uri}}
                new_run["artifacts"].append(new_artifact)
                artifact_index = len(new_run["artifacts"]) - 1

            # Extract line and column info and create a new location for each result
            line_info, column_info = (
                result["lines"].replace("Line ", "").replace("Columns ", "").split(" ")
            )
            start_line = int(line_info)
            start_column, end_column = map(int, column_info.split("-"))

            new_result_location = {
                "physicalLocation": {
                    "artifactLocation": {
                        "uri": result["file"],
                        "index": artifact_index,
                    },
                    "region": {
                        "startLine": start_line,
                        "startColumn": start_column,
                        "endColumn": end_column,
                    },
                }
            }
            new_result["locations"].append(new_result_location)

            new_run["results"].append(new_result)

    sarif_json["runs"].append(new_run)

    with open(output_file_path, "w") as outfile:
        json.dump(sarif_json, outfile, indent=4)


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
