# Silence tool prints
import copy
from datetime import datetime
import json
import os
from pathlib import Path
import sys
from prettytable import PrettyTable, MARKDOWN
from pygount import ProjectSummary, SourceAnalysis

from eburger import settings
from eburger.utils.cli_args import args
from eburger.utils.logger import log


def save_as_json(file_path: Path, json_data: dict):
    with open(file_path, "w") as outfile:
        json.dump(json_data, outfile, indent=4)


def save_as_markdown(output_file_path: Path, json_data: dict):
    md_report_root_dir = Path(output_file_path).resolve().parent

    markdown_content = "# eBurger Static Analysis Report\n\n"
    markdown_content += f"This report was generated by the [eBurger](https://github.com/forefy/eburger) static analyzer on {datetime.now().strftime('%d.%m.%Y at %H:%M')}.\n\nThe results are not intended to substitute for comprehensive audits or professional assessments, and should be used only as a tool to help identify possible security vulnerabilities or insights and not for any other purpose.\n\n"

    markdown_content += "## Insights Summary\n\n"
    markdown_content += "| Issue | Severity | Occurrences |\n"
    markdown_content += "|-------|----------|-------------|\n"

    details_md = ""

    for issue in json_data["insights"]:
        name = f"[{issue['severity']}] {issue['name']}"
        severity = issue["severity"]
        occurrences = len(issue["results"])
        anchor_name = (
            name.replace(" ", "-")
            .replace(",", "")
            .replace(".", "")
            .replace("[", "")
            .replace("]", "")
            .lower()
        )

        # Add issue to the table with a hyperlink to its detailed description
        markdown_content += (
            f"| [{name}](#{anchor_name}) | {severity} | {occurrences} |\n"
        )

        # Generate detailed description for each issue
        details_md += f"\n### {name}\n{issue['description']}\n\n"
        details_md += "#### Vulnerable Locations\n"
        for result in issue["results"]:
            try:
                # Convert the file path to be absolute and normalize it
                full_path = Path(result["file"]).resolve()
                # Calculate the relative path safely
                relative_path = full_path.relative_to(md_report_root_dir)

                line_info, column_info = (
                    result["lines"]
                    .replace("Line ", "")
                    .replace("Columns ", "")
                    .split(" ")
                )
                start_line = line_info
                start_column, end_column = column_info.split("-")
                location_format = (
                    f"{relative_path}:{start_line}:{start_column}-{end_column}"
                )
                details_md += f"- {location_format}\n"

                # Include the vulnerable code snippet
                if "code" in result:
                    code_snippet = result["code"].replace(
                        "\n", "\n\t"
                    )  # Indent for better readability
                    details_md += f"\t```\n\t{code_snippet}\n\t```\n"
            except ValueError as e:
                log("error", f"Error processing path {result['file']}: {e}")

        details_md += "\n"

        if "action-items" in issue:
            details_md += (
                "#### Action Items\n"
                + "\n".join(f"- {item}" for item in issue["action-items"])
                + "\n\n"
            )
        if "references" in issue:
            details_md += (
                "#### References\n"
                + "\n".join(f"- [{ref}]({ref})" for ref in issue["references"])
                + "\n\n"
            )
        details_md += "---\n"

    markdown_content += "\n" + details_md

    markdown_content += '<p align=center>Generated by <a href=https://github.com/forefy/eburger title="eBurger">eBurger</a> </p>\n'

    with open(output_file_path, "w") as md_file:
        md_file.write(markdown_content)


def convert_severity_to_sarif_level(severity: str) -> str:
    mapping = {"High": "error", "Medium": "warning", "Low": "note"}
    mapped_severity = mapping.get(severity, None)
    if mapped_severity is None:
        log(
            "error",
            "Failed converting a template's severity to the respective SARIF level",
        )
    return mapped_severity


def convert_severity_to_sarif_security_severity(severity: str) -> str:
    mapping = mapping = {"High": 8.0, "Medium": 5.0, "Low": 3.0}
    mapped_severity = mapping.get(severity, None)
    if mapped_severity is None:
        log(
            "error",
            "Failed converting a template's severity to the respective SARIF/GitHub Code Scanning security severity",
        )
    return mapped_severity


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

    # precision - very-high, high, medium, or low
    # security-severity - 9.0 is critical, 7.0 to 8.9 is high, 4.0 to 6.9 is medium and 3.9 or less is low
    # simplified: 9.0, 8.0, 5.0, 3.0
    sarif_rule_template = {
        "id": "",
        "name": "",
        "shortDescription": {"text": ""},
        "fullDescription": {"text": ""},
        "helpUri": "",
        "help": {
            "text": "",
            "markdown": "",
        },
        "properties": {"precision": "", "problem": {"security-severity": ""}},
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

    new_run = copy.deepcopy(sarif_run_template)

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
            new_rule = copy.deepcopy(sarif_rule_template)
            new_rule["id"] = rule_id
            new_rule["name"] = insight["name"]
            new_rule["shortDescription"]["text"] = insight["name"]
            new_rule["fullDescription"]["text"] = insight["description"]
            new_rule["helpUri"] = insight["references"][0]
            new_rule["help"]["text"] = insight["action-items"][0]
            new_rule["help"][
                "markdown"
            ] = f"[{insight['action-items'][0]}]({insight['references'][0]})"
            new_rule["properties"]["precision"] = insight["precision"].casefold()
            new_rule["properties"]["problem"]["security-severity"] = (
                convert_severity_to_sarif_security_severity(insight["severity"])
            )

            new_run["tool"]["driver"]["rules"].append(new_rule)
            rule_index = len(new_run["tool"]["driver"]["rules"]) - 1

        for result in insight["results"]:
            new_result = {
                "ruleId": rule_id,
                "ruleIndex": rule_index,
                "level": convert_severity_to_sarif_level(insight["severity"]),
                "message": {
                    "text": insight["name"]
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


def calculate_nsloc() -> tuple[list, list]:
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
