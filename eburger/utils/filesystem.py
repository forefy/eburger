import fnmatch
import json
import os
from pathlib import Path
import re
import shutil
from eburger import settings
from eburger.utils.logger import log
from eburger.utils.cli_args import args


def find_and_read_sol_file(folder_path: str) -> str:
    # Search for .sol files recursively in the given folder
    excluded_folders = settings.excluded_dirs + ["mocks", "lib"]
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            sol_file_path = os.path.join(root, file)
            if any(
                fnmatch.fnmatch(sol_file_path, f"*/{pattern}/*")
                for pattern in excluded_folders
            ):
                continue
            if (
                file.endswith(".sol")
                and not file.endswith(".t.sol")
                and not file.endswith(".s.sol")
            ):
                with open(sol_file_path, "r") as input_file:
                    head = [line for line, _ in zip(input_file, range(10))]
                    if any("pragma" in line for line in head):
                        return sol_file_path

    log("error", "Can't parse path given in argument.")


def get_solidity_version_from_file(solidity_file_or_folder: str) -> str:
    solc_required_version = None
    version_pattern = r"pragma\s+solidity\s+([^;]+);"
    version_number_pattern = r"\d+\.\d+\.\d+|\d+\.\d+"
    with open(solidity_file_or_folder, "r") as f:
        content = f.read()

        match = re.search(version_pattern, content)
        if match:
            version_match = match.group(1)

            # Extract all version numbers
            version_numbers = re.findall(version_number_pattern, version_match)

            if version_numbers:
                # If there is an upper limit, choose the version just below the upper limit
                if "<" in version_match and len(version_numbers) > 1:
                    upper_version = version_numbers[-1]
                    lower_version = (
                        version_numbers[0] if len(version_numbers) > 1 else None
                    )

                    major, minor, *patch = map(int, upper_version.split("."))
                    lower_major, lower_minor, *lower_patch = (
                        map(int, lower_version.split(".")) if lower_version else (0, 0)
                    )

                    if minor > 0 and (
                        major > lower_major
                        or (major == lower_major and minor - 1 >= lower_minor)
                    ):
                        # Choose the highest minor version below the upper limit
                        solc_required_version = f"{major}.{minor - 1}.0"
                    else:
                        # If the upper limit is too close to the lower limit, return the lower limit
                        solc_required_version = lower_version
                else:
                    # Return the highest version number found
                    solc_required_version = version_numbers[-1]
    if solc_required_version is None:
        log("warning", "Couldn't extract solidity version from file, trying 0.8.20")
        solc_required_version = "0.8.20"
    return solc_required_version


def get_all_solidity_files(folder_path: str):
    solidity_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".sol") and not file.endswith(".t.sol"):
                # only include files with a pragma statement
                file_path = os.path.join(root, file)
                with open(file_path, "r") as input_file:
                    head = [line for line, _ in zip(input_file, range(10))]
                    if any("pragma" in line for line in head):
                        solidity_files.append(file_path)

    return solidity_files


def create_directory_if_not_exists(directory_path: Path):
    # Check if the directory already exists
    if not os.path.exists(directory_path):
        # Create the directory
        try:
            os.makedirs(directory_path)
            log("debug", f"Created directory: {directory_path}")
        except Exception as e:
            log("error", f"Could not create direction {directory_path}. {e}")


def create_or_empty_directory(directory_path: Path):
    # Check if the directory already exists
    if os.path.exists(directory_path):
        # Empty the directory by removing all its contents
        shutil.rmtree(directory_path)

        try:
            os.makedirs(directory_path)
            log("debug", f"Emptied and re-created directory: {directory_path}")
        except Exception as e:
            log("error", f"Could not create direction {directory_path}. {e}")
    else:
        # Create the directory if it does not exist
        try:
            os.makedirs(directory_path)
            log("debug", f"Created directory: {directory_path}")
        except Exception as e:
            log("error", f"Could not create direction {directory_path}. {e}")


# TODO: Add better handling for multiple build info files
def get_foundry_ast_json(forge_out_dir) -> dict:
    try:
        json_files = [f for f in os.listdir(forge_out_dir) if f.endswith(".json")]
    except FileNotFoundError:
        err_line = "forge build failed to compile contract."
        if not args.debug:
            err_line += " try running with `--debug`."
        log("error", err_line)

    if not json_files:
        log("error", "forge build generated no output.")
    if len(json_files) > 1:
        log(
            "warning",
            "Multiple forge-output files found, choosing the latest.",
        )
    latest_file = max(
        json_files,
        key=lambda x: os.path.getctime(os.path.join(forge_out_dir, x)),
    )
    latest_file_path = os.path.join(forge_out_dir, latest_file)
    with open(latest_file_path, "r") as f:
        ast_json = json.load(f)
    return ast_json["output"]


# TODO: Add better handling for multiple build info files
def get_hardhat_ast_json(hardhat_out_dir) -> dict:
    json_files = [f for f in os.listdir(hardhat_out_dir) if f.endswith(".json")]
    if not json_files:
        log("error", "npx hardhat compile generated no output.")
    if len(json_files) > 1:
        log(
            "warning",
            "Multiple hardhat output files found, choosing the latest.",
        )
    latest_file = max(
        json_files,
        key=lambda x: os.path.getctime(os.path.join(hardhat_out_dir, x)),
    )
    latest_file_path = os.path.join(hardhat_out_dir, latest_file)
    with open(latest_file_path, "r") as f:
        ast_json = json.load(f)
    return ast_json["output"]


def move_multiple_dirs(source_dir, directories_to_move, destination_dir):
    for dir_name in directories_to_move:
        if "*" in dir_name:
            # For wildcard entries, find matching directories
            for item in os.listdir(source_dir):
                if fnmatch.fnmatch(item, dir_name):
                    src_path = os.path.join(source_dir, item)
                    dest_path = os.path.join(destination_dir, item)
                    create_directory_if_not_exists(dest_path)
                    if os.path.isdir(src_path):
                        shutil.move(src_path, dest_path)
        else:
            # For exact names, move directly
            src_path = os.path.join(source_dir, dir_name)
            dest_path = os.path.join(destination_dir, dir_name)
            create_directory_if_not_exists(dest_path)
            if os.path.exists(src_path) and os.path.isdir(src_path):
                shutil.move(src_path, dest_path)


def find_recursive_files_by_patterns(source_path, patterns: list) -> list:
    file_paths = []
    for pattern in patterns:
        paths = Path(source_path).rglob(pattern)

        filtered_paths = []
        for path in paths:
            if any(part in {"mocks", "lib", "node_modules"} for part in path.parts):
                continue
            filtered_paths.append(path)
        file_paths.extend(filtered_paths)

    unique_file_paths = list(set(file_paths))
    sorted_unique_file_paths = sorted(
        unique_file_paths, key=lambda path: (len(str(path)), str(path))
    )
    return sorted_unique_file_paths


def select_project(project_paths: list) -> Path:
    while True:
        print("Multiple project configurations found:")
        for i, path in enumerate(project_paths, start=1):
            print(f"{i}) {path}")
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= len(project_paths):
                project_path = Path(project_paths[choice - 1])
                return project_path
            else:
                print(
                    f"Invalid choice. Please enter a number between 1 and {len(project_paths) - 1}"
                )
        except ValueError:
            print("Invalid input. Please enter a number.")
        else:
            print("Only one project available.")
            return Path(project_paths[0])


def roughly_check_valid_file_path_name(path_str: str) -> bool:
    if not path_str or path_str.isspace() or "." not in path_str:
        return False

    if os.name == "nt":
        invalid_chars = r'<>:"|?*\n\r\t'
    else:
        invalid_chars = "\0"

    if any(char in path_str for char in invalid_chars):
        return False

    return True
