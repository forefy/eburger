# Extract the filenames from the 'sources' key, which usually contains file paths
def extract_file_list_from_ast(ast_data):
    if "sources" in ast_data:
        return list(ast_data["sources"].keys())
    return []


# Extract highlighted code given a solidity src_location and a contract path
def parse_code_highlight(src_location, file_path):
    start_offset, length, _ = map(int, src_location.split(":"))

    with open(file_path, "r") as file:
        file_content = file.read()
        if start_offset + length > len(file_content):
            return "The start offset and length exceed the file content."

        vulnerable_code = file_content[start_offset : start_offset + length]

        # Find the line number and character positions
        current_offset = 0
        line_number = 1
        for line in file_content.split("\n"):
            end_offset = current_offset + len(line)
            if current_offset <= start_offset < end_offset:
                start_char = start_offset - current_offset
                end_char = min(start_char + length, len(line))
                return f"Line {line_number} Columns {start_char}-{end_char}: {vulnerable_code}"
            current_offset = end_offset + 1  # +1 for the newline character
            line_number += 1

        return "Location not found in file"
