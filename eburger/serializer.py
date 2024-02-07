from eburger import settings
from eburger.utils.logger import log


def parse_solidity_ast(ast_json: dict) -> list:
    """
    Parses the Solidity AST from the JSON representation.
    """
    root_nodes = []
    for key, node in ast_json.get("sources", {}).items():
        ast_node = node.get("AST", node.get("ast", {}))
        if ast_node:
            root_nodes.append(ast_node)
    return root_nodes


def reduce_json(ast_json: dict) -> tuple:
    # Maintain original file list array
    def extract_file_list_from_ast(ast_data):
        if "sources" in ast_data:
            return list(ast_data["sources"].keys())
        return []

    original_file_list = extract_file_list_from_ast(ast_json)

    # Function to remove keys in-place from a dictionary
    def remove_keys_in_place(dictionary):
        removal_list = [
            key
            for key in dictionary
            if any(substring in key for substring in settings.excluded_contracts)
        ]
        for key in removal_list:
            log("debug", f"Excluding {key}")
            del dictionary[key]

    for section in ["sources", "contracts"]:
        if section in ast_json:
            remove_keys_in_place(ast_json[section])

    return ast_json, original_file_list
