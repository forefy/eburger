import os
import re
import shutil
from eburger.utils.logger import log


def find_and_read_sol_file(folder_path):
    # Search for .sol files recursively in the given folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".sol") and not file.endswith(".t.sol"):
                sol_file_path = os.path.join(root, file)
                with open(sol_file_path, "r") as input_file:
                    head = [line for line, _ in zip(input_file, range(10))]
                    if any("pragma" in line for line in head):
                        return sol_file_path


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


def get_all_solidity_files(folder_path):
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


def create_directory_if_not_exists(directory_path):
    # Check if the directory already exists
    if not os.path.exists(directory_path):
        # Create the directory
        os.makedirs(directory_path)
        log("info", f"Created directory: {directory_path}")


def create_or_empty_directory(directory_path):
    # Check if the directory already exists
    if os.path.exists(directory_path):
        # Empty the directory by removing all its contents
        shutil.rmtree(directory_path)
        os.makedirs(directory_path)
        log("info", f"Emptied and re-created directory: {directory_path}")
    else:
        # Create the directory if it does not exist
        os.makedirs(directory_path)
        log("info", f"Created directory: {directory_path}")
