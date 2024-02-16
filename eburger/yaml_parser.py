import traceback
import yaml
import concurrent.futures
from eburger import settings

from eburger.template_utils import *
from eburger.utils.logger import color, log
from eburger.utils.cli_args import args


def execute_python_code(
    template_name: str, python_code: str, ast_data: dict, src_file_list: list
) -> list:
    local_vars = {
        "ast_data": ast_data,
        "src_file_list": src_file_list,
        "project_root": settings.project_root,
    }

    try:
        compiled_code = compile(python_code, "<string>", "exec")
        exec(compiled_code, globals(), local_vars)
        return local_vars["results"]
    except Exception as e:
        line = f"Error occurred during execution: {str(e)}"
        try:
            line += f" at line {traceback.extract_tb(e.__traceback__)[-1][1]}"
        except Exception as e:
            line = f"failed extracting traceback - {line}"
        log("error", f"Failed parsing template {template_name} -> {line}")


# Function to process a single YAML file
def process_yaml(file_path, ast_data, src_file_list):
    with open(file_path, "r") as file:
        yaml_data = yaml.safe_load(file)

    results = execute_python_code(
        yaml_data["name"], yaml_data["python"], ast_data, src_file_list
    )
    return {
        "name": yaml_data.get("name"),
        "severity": yaml_data.get("severity"),
        "precision": yaml_data.get("precision"),
        "description": yaml_data.get("description"),
        "results": results,
        "action-items": yaml_data.get("action-items"),
        "references": yaml_data.get("references"),
        "reports": yaml_data.get("reports"),
    }


def process_files_concurrently(ast_data: dict, src_file_list: list) -> list:
    yaml_files = []
    for templates_directory in settings.templates_directories:
        if templates_directory.is_dir():
            yaml_files = list(
                set(yaml_files + list(templates_directory.glob("*.yaml")))
            )
        elif templates_directory.is_file() and templates_directory.suffix == ".yaml":
            if templates_directory not in yaml_files:
                yaml_files.append(templates_directory)
        else:
            log("error", "Invalid templates directory or file.")

    log(
        "info",
        f"Loaded {color.Success}{len(yaml_files)}{color.Default} templates for execution.",
    )
    insights = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(process_yaml, str(file_path), ast_data, src_file_list)
            for file_path in yaml_files
        ]
        for future in concurrent.futures.as_completed(futures):
            try:
                results = future.result(timeout=30)  # 30 seconds timeout
                if results.get("results"):
                    if args.no:
                        if results.get("severity").casefold() in args.no:
                            continue
                    insights.append(results)
            except concurrent.futures.TimeoutError:
                log("error", "A task has timed out.")
            except Exception as e:
                log("error", f"Unhandled error: {e}")
    log(
        "info",
        f"{color.Error}{len(insights)}{color.Default} insight{'s were' if (len(insights) > 1 or len(insights) == 0) else ' was'} found by eBurger.",
    )
    if insights:
        log("insights", insights)
    return insights
