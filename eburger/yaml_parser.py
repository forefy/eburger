import inspect
from pathlib import Path
import traceback
import yaml
import concurrent.futures
import io
import ast
from eburger.logger import color, log
import eburger.models as models
from eburger.template_utils import *


def load_ast_data(file_path):
    with open(file_path, "r") as file:
        ast_data_content = file.read()
    ast_data = ast.literal_eval(ast_data_content)
    return ast_data


def execute_python_code(python_code, ast_data):
    local_vars = {"ast_data": ast_data}
    for attr in dir(models):
        attr_value = getattr(models, attr)
        if inspect.isclass(attr_value):
            local_vars[attr] = attr_value

    output = io.StringIO()
    try:
        compiled_code = compile(python_code, "<string>", "exec")
        exec(compiled_code, globals(), local_vars)
    except Exception as e:
        line = f"[Error] Error occurred during execution: {str(e)}"
        try:
            line += f" at line {traceback.extract_tb(e.__traceback__)[-1][1]}"
        except:
            pass
        return line
    return output.getvalue()


def prettify_output(results):
    prettified_results = []

    for line in results:
        # Check if the line is not empty
        if line != "[]":
            # Remove the outermost square brackets and single quotes
            cleaned_line = line[2:-2]
            # Add the cleaned line to the results
            prettified_results.append(cleaned_line)

    return prettified_results


# Function to process a single YAML file
def process_yaml(file_path, ast_data):
    with open(file_path, "r") as file:
        yaml_data = yaml.safe_load(file)

    results = execute_python_code(yaml_data["python"], ast_data)
    results = results.splitlines()
    results = prettify_output(results)
    return {
        "name": yaml_data.get("name"),
        "description": yaml_data.get("description"),
        "severity": yaml_data.get("severity"),
        "results": results,
    }


def process_files_concurrently(directory_path, ast_data):
    yaml_files = list(Path(directory_path).glob("*.yaml"))
    log(
        "info",
        f"Loaded {color.Success}{len(yaml_files)}{color.Default} templates for execution.",
    )
    insights = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(process_yaml, str(file_path), ast_data)
            for file_path in yaml_files
        ]
        for future in concurrent.futures.as_completed(futures):
            try:
                results = future.result(timeout=30)  # 30 seconds timeout
                if results.get("results"):
                    insights.append(results)
            except concurrent.futures.TimeoutError:
                print("A task has timed out.")
            except Exception as e:
                print(f"An error occurred: {e}")
    return insights
