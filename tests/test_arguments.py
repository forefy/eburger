from pathlib import Path

import pytest
from eburger.utils.cli_args import args
from eburger.main import main
from eburger import settings


def test_arguments():
    original_project_root = settings.project_root
    original_outputs_dir = settings.outputs_dir

    args.solc_compiler_version = "0.8.20"
    args.no = ["info", "warning", "insights", "success"]

    # Single file
    single_contract_path = str(Path("vulnerable_contracts", "unbounded_loop.sol"))
    args.solidity_file_or_folder = single_contract_path
    main()

    # SARIF, Markdown
    args.output = "sarif"
    main()

    args.output = "markdown"
    main()

    # Single traversed file
    traversed_dir_contract = "../eburger/vulnerable_contracts/unbounded_loop.sol"
    args.solidity_file_or_folder = traversed_dir_contract
    main()

    # Folder and project name
    args.project_name = "pytest_project"
    foundry_contract_path = str(
        Path("vulnerable_contracts", "missing_reentrancy_guard/")
    )
    args.solidity_file_or_folder = foundry_contract_path
    main()
    args.project_name = None

    # Reset possibly changed state that can affect other tests
    args.no = []
    args.solidity_file_or_folder = None
    settings.project_root = original_project_root
    settings.original_outputs_dir = original_outputs_dir
