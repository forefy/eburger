import json
import pytest
from eburger.serializer import (
    parse_solidity_ast,
)


# Sample AST JSON data for testing
@pytest.fixture
def ast_data():
    sample_ast_json = """{
    "sources": {
            "test.sol": {
                "AST": {
                    "nodeType": "SourceUnit",
                    "id": 1,
                    "nodes": [
                        {
                            "nodeType": "ContractDefinition",
                            "id": 2,
                            "attributes": {
                                "name": "TestContract"
                            },
                            "nodes": [
                                {
                                    "nodeType": "FunctionDefinition",
                                    "id": 3,
                                    "attributes": {
                                        "name": "testFunction"
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        }
    }"""
    return json.loads(sample_ast_json)


def test_parse_solidity_ast_basic_structure(ast_data):
    ast_roots = parse_solidity_ast(ast_data)

    assert len(ast_roots) == 1
    root = ast_roots[0]
    assert root.get("nodeType") == "SourceUnit"
    assert root.get("id") == 1

    assert len(root.get("nodes")) == 1
    contract = root.get("nodes")[0]

    # Check if the contract node is of type ContractDefinition
    assert contract.get("nodeType") == "ContractDefinition"
    assert contract.get("id") == 2

    assert len(contract.get("nodes")) == 1
    function = contract.get("nodes")[0]

    # Check if the function node is of type FunctionDefinition
    assert function.get("nodeType") == "FunctionDefinition"
    assert function.get("id") == 3
