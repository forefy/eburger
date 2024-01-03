import inspect
from pathlib import Path
import traceback
import yaml
import concurrent.futures
from contextlib import redirect_stdout
import io
import ast
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
        with redirect_stdout(output):
            exec(compiled_code, globals(), local_vars)
    except Exception as e:
        line = f"Error occurred during execution: {str(e)}"
        try:
            line += f" at line {traceback.extract_tb(e.__traceback__)[-1][1]}"
        except:
            pass
        return line
    return output.getvalue()


# Function to process a single YAML file
def process_yaml(file_path, ast_data):
    with open(file_path, "r") as file:
        yaml_data = yaml.safe_load(file)
    results = execute_python_code(yaml_data["python"], ast_data)
    print(results.splitlines())
    return {
        "name": yaml_data.get("name"),
        "description": yaml_data.get("description"),
        "severity": yaml_data.get("severity"),
        "results": results.splitlines(),
    }


def process_files_concurrently(directory_path, ast_data):
    yaml_files = list(Path(directory_path).glob("*.yaml"))
    insights = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(process_yaml, str(file_path), ast_data)
            for file_path in yaml_files
        ]
        for future in concurrent.futures.as_completed(futures):
            insights.append(future.result())
    return insights
