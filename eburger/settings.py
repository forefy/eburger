import os
from pathlib import Path


project_root = Path.cwd()
outputs_dir = Path.cwd() / ".eburger"
excluded_dirs = ["test", "script"]
excluded_contracts = [
    "@openzeppelin",
    "@uniswap",
    "solmate",
    "solady",
    "forge-std",
    "ds-test",
]

templates_directory = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "templates"
)
if __package__ is None or __package__ == "":
    templates_directory = Path.cwd() / "eburger" / "templates"
