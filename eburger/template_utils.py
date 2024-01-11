# Extract highlighted code given a solidity src_location and a contract path
from click import Path
from eburger import settings


def parse_code_highlight(node: dict, src_file_list: list) -> (str, str, str):
    src_location = node.get("src", "")
    file_index = int(src_location.split(":")[2])
    file_name = (
        src_file_list[file_index] if file_index < len(src_file_list) else "Unknown file"
    )
    file_path = str(settings.project_root / file_name)
    start_offset, length, _ = map(int, src_location.split(":"))

    with open(file_path, "r") as file:
        file_content = file.read()
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
                    file_path,
                    f"Line {line_number} Columns {start_char + 1}-{end_char + 1}",
                    vulnerable_code,
                )
            current_offset = end_offset + 1  # +1 for the newline character
            line_number += 1

        return "Location not found in file", None, None
