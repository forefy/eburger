import json
import pytest
from eburger.serializer import reduce_json
from eburger.yaml_parser import process_yaml


@pytest.fixture
def vulnerable_ast() -> tuple[dict, list]:
    ast_json = """{
    "sources": {
        "vulnerable_contracts/unspecific_pragma_detector.sol": {
            "AST": {
                "absolutePath": "vulnerable_contracts/unspecific_pragma_detector.sol",
                "exportedSymbols": {
                    "OutOfControlContract": [
                        2
                    ]
                },
                "id": 3,
                "license": "MIT",
                "nodeType": "SourceUnit",
                "nodes": [
                    {
                        "id": 1,
                        "literals": [
                            "solidity",
                            "^",
                            "0.8",
                            ".0"
                        ],
                        "nodeType": "PragmaDirective",
                        "src": "32:23:0"
                    },
                    {
                        "abstract": false,
                        "baseContracts": [],
                        "contractDependencies": [],
                        "contractKind": "contract",
                        "fullyImplemented": true,
                        "id": 2,
                        "linearizedBaseContracts": [
                            2
                        ],
                        "name": "OutOfControlContract",
                        "nodeType": "ContractDefinition",
                        "nodes": [],
                        "scope": 3,
                        "src": "57:32:0"
                    }
                ],
                "src": "32:58:0"
            }
        }
    }
}"""
    return json.loads(ast_json)


def test_unspecific_pragma_detector(vulnerable_ast):
    ast_json, src_paths = reduce_json(vulnerable_ast)
    results = process_yaml(
        "eburger/templates/unspecific_pragma_detector.yaml",
        ast_json,
        src_paths,
    )
    assert "Line 2 Columns 1-24" in results["results"][0]["lines"]
