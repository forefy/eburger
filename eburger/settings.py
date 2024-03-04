import os
from pathlib import Path


project_root = Path.cwd()
outputs_dir = Path.cwd() / ".eburger"
excluded_dirs = ["test", "script", "mocks", "MockContracts" "lib", "node_modules"]
excluded_contracts = [
    "@openzeppelin",
    "openzeppelin-contracts",
    "@uniswap",
    "@gnosis.pm",
    "pendle",
    "solmate",
    "solady",
    "forge-std",
    "ds-test",
    "mocks",
    "MockContracts",
]

templates_directories = [Path(os.path.dirname(os.path.abspath(__file__)), "templates")]
if __package__ is None or __package__ == "":
    templates_directories = [Path.cwd() / "eburger" / "templates"]
