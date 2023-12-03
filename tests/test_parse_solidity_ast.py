import pytest
from eburger.serializer import (
    parse_solidity_ast,
)
from eburger.models import ContractDefinition, FunctionDefinition

# Sample AST JSON data for testing
sample_ast_json = {
    "sources": {
        "test.sol": {
            "AST": {
                "nodeType": "SourceUnit",
                "id": 1,
                "nodes": [
                    {
                        "nodeType": "ContractDefinition",
                        "id": 2,
                        "attributes": {"name": "TestContract"},
                        "nodes": [
                            {
                                "nodeType": "FunctionDefinition",
                                "id": 3,
                                "attributes": {"name": "testFunction"},
                            }
                        ],
                    }
                ],
            }
        }
    }
}


def test_parse_solidity_ast_basic_structure():
    ast_roots = parse_solidity_ast(sample_ast_json)

    assert len(ast_roots) == 1
    root = ast_roots[0]
    assert root.node_type == "SourceUnit"
    assert root.node_id == 1

    assert len(root.children) == 1
    contract = root.children[0]

    # Check if the contract node is of type ContractDefinition
    assert isinstance(contract, ContractDefinition)
    assert contract.node_type == "ContractDefinition"
    assert contract.node_id == 2
    assert contract.name == "TestContract"

    assert len(contract.children) == 1
    function = contract.children[0]

    # Check if the function node is of type FunctionDefinition
    assert isinstance(function, FunctionDefinition)
    assert function.node_type == "FunctionDefinition"
    assert function.node_id == 3
    assert function.name == "testFunction"
