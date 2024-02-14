from pathlib import Path
from typing import Union
from eburger import settings
from eburger.utils.cli_args import args


def parse_code_highlight(node: dict, src_file_list: list) -> tuple[str, str, str]:
    """
    Extracts and highlights a specific code snippet from a source file based on a given AST node.

    Parameters:
    - node (dict): The AST node containing the 'src' attribute with location details.
    - src_file_list (list): A list of source files associated with the AST.

    Returns:
    - Tuple (str, str, str): A tuple containing:
      1. The file path of the source file where the code snippet is located.
      2. A string representation of the line and column range in the file for the code snippet.
      3. The extracted code snippet itself.

    The 'src' attribute in the node is expected to be in the format 'start_offset:length:file_index'.
    The function calculates the exact location of the code in the file and extracts it along with its
    line and column position. If the location exceeds the content of the file or is not found, appropriate
    messages and null values are returned.
    """

    src_location = node.get("src", "")
    file_index = int(src_location.split(":")[2])
    project_relative_file_name = (
        src_file_list[file_index] if file_index < len(src_file_list) else "Unknown file"
    )
    file_path = str(Path(settings.project_root / project_relative_file_name).resolve())

    if args.relative_file_paths:
        result_file_path_uri = project_relative_file_name
    else:
        result_file_path_uri = file_path

    start_offset, length, _ = map(int, src_location.split(":"))

    file_content = None
    with open(file_path, "r") as file:
        file_content = file.read()

    if file_content is None:
        return "File unreadable.", None, None

    if start_offset + length > len(file_content):
        return "The start offset and length exceed the file content.", None, None

    vulnerable_code = file_content[start_offset : start_offset + length]
    # Find the line number and character positions
    current_offset = 0
    line_number = 1
    for line in file_content.split("\n"):
        end_offset = current_offset + len(line)
        if current_offset <= start_offset < end_offset:
            start_char = start_offset - current_offset
            end_char = min(start_char + length, len(line))
            return (
                result_file_path_uri,
                f"Line {line_number} Columns {start_char + 1}-{end_char + 1}",
                vulnerable_code,
            )
        current_offset = end_offset + 1  # +1 for the newline character
        line_number += 1
    return "Location not found in file", None, None


def join_lists_unique(list1: list, list2: list) -> list:
    """
    Join two lists of dictionaries without duplicates, based on the 'id' key of the dictionaries.

    :param list1: First list of dictionaries.
    :param list2: Second list of dictionaries.
    :return: A list of dictionaries without duplicates.
    """
    # Create a set to track unique ids
    seen_ids = set()
    combined_list = []

    # Function to add dictionaries to the combined list if their id is not seen
    def add_unique_dicts_from_list(lst):
        for d in lst:
            # Check if the dictionary has an 'id' key and it's not seen before
            if "id" in d and d["id"] not in seen_ids:
                combined_list.append(d)
                seen_ids.add(d["id"])

    # Add unique dictionaries from both lists
    add_unique_dicts_from_list(list1)
    add_unique_dicts_from_list(list2)

    return combined_list


def is_entry_unique(results: list, file_path: str, lines: str) -> bool:
    """
    Checks if an entry with the specified file_path and lines already exists in the results.

    :param results: List of dictionaries containing the current results.
    :param file_path: The file path to be checked.
    :param lines: The lines to be checked.
    :return: True if no entry with the same file_path and lines exists, False otherwise.
    """
    return not any(
        result["file"] == file_path and result["lines"] == lines for result in results
    )


def get_nodes_by_types(
    node: dict,
    node_types: Union[str, list],
    filter_key: str = None,
    filter_value: str = None,
) -> list:
    """
    Finds nodes of specific types within the given node or AST.

    :param node: The node or AST to search.
    :param node_types: The type(s) of nodes to find.
    :return: A list of nodes of the specified types.
    """

    if isinstance(node_types, str):
        node_types = [node_types]

    def search_nodes(current_node, result):
        if isinstance(current_node, dict):
            if current_node.get("nodeType") in node_types:
                # Apply filter if filter_key and filter_value are provided
                if filter_key is None or current_node.get(filter_key) == filter_value:
                    result.append(current_node)
            for value in current_node.values():
                if isinstance(value, (dict, list)):
                    search_nodes(value, result)
        elif isinstance(current_node, list):
            for item in current_node:
                search_nodes(item, result)

    results = []
    search_nodes(node, results)
    return results


def get_nodes_by_signature(node, type_string):
    """
    Searches for nodes with a specific typeString within the given node or AST.

    :param node: The node or AST to search.
    :param type_string: The typeString to search for.
    :return: A list of nodes that have the specified typeString.
    """
    matching_nodes = []

    def search_nodes(current_node):
        if isinstance(current_node, dict):
            # Check if the current node matches the typeString
            if (
                current_node.get("typeDescriptions", {}).get("typeString")
                == type_string
            ):
                matching_nodes.append(current_node)
            # Recursively search in child nodes
            for value in current_node.values():
                if isinstance(value, (dict, list)):
                    search_nodes(value)
        elif isinstance(current_node, list):
            for item in current_node:
                search_nodes(item)

    search_nodes(node)
    return matching_nodes


def find_node_ids_first_parent_of_type(
    ast: dict, node_id: int, parent_type: dict
) -> Union[dict, None]:
    """
    Finds the first parent of a specified type for a given node ID in the AST.

    :param ast: The AST to search.
    :param node_id: The ID of the node whose parent is to be found.
    :param parent_type: The nodeType of the parent node to find.
    :return: The first parent node of the specified type, or None if not found.
    """

    def search_node(current_node, target_id, parent_node=None):
        if isinstance(current_node, dict):
            # Check if the current node is the target
            if current_node.get("id") == target_id:
                return parent_node
            # Iterate over child nodes
            for key, value in current_node.items():
                if isinstance(value, (list, dict)):
                    result = search_node(
                        value,
                        target_id,
                        (
                            current_node
                            if current_node.get("nodeType") == parent_type
                            else parent_node
                        ),
                    )
                    if result:
                        return result
        elif isinstance(current_node, list):
            for item in current_node:
                if isinstance(item, (list, dict)):
                    result = search_node(item, target_id, parent_node)
                    if result:
                        return result
        return None

    return search_node(ast, node_id)
