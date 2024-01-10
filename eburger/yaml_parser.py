import inspect
from pathlib import Path
import sys
import traceback
import yaml
import concurrent.futures
import ast
from eburger import settings

import eburger.models as models
from eburger.template_utils import *
from eburger.utils.logger import color, log


def load_ast_data(file_path):
    with open(file_path, "r") as file:
        ast_data_content = file.read()
    ast_data = ast.literal_eval(ast_data_content)
    return ast_data


def execute_python_code(template_name, python_code, ast_data, src_file_list):
    local_vars = {
        "ast_data": ast_data,
        "src_file_list": src_file_list,
        "project_root": settings.project_root,
    }
    for attr in dir(models):
        attr_value = getattr(models, attr)
        if inspect.isclass(attr_value):
            local_vars[attr] = attr_value

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
        "description": yaml_data.get("description"),
        "results": results,
        "action-items": yaml_data.get("action-items"),
        "references": yaml_data.get("references"),
        "reports": yaml_data.get("reports"),
    }


def process_files_concurrently(
    directory_path: str, ast_data: dict, src_file_list: list
):
    yaml_files = list(Path(directory_path).glob("*.yaml"))
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
