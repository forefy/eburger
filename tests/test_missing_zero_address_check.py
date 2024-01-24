import json
import pytest
from eburger.serializer import reduce_json
from eburger.yaml_parser import process_yaml


@pytest.fixture
def vulnerable_ast() -> (dict, list):
    ast_json = """{
    "sources": {
        "vulnerable_contracts/missing_zero_address_check.sol": {
            "AST": {
                "absolutePath": "vulnerable_contracts/missing_zero_address_check.sol",
                "exportedSymbols": {
                    "WrongContract": [
                        14
                    ]
                },
                "id": 15,
                "nodeType": "SourceUnit",
                "nodes": [
                    {
                        "id": 1,
                        "literals": [
                            "solidity",
                            "0.8",
                            ".20"
                        ],
                        "nodeType": "PragmaDirective",
                        "src": "0:23:0"
                    },
                    {
                        "abstract": false,
                        "baseContracts": [],
                        "canonicalName": "WrongContract",
                        "contractDependencies": [],
                        "contractKind": "contract",
                        "fullyImplemented": true,
                        "id": 14,
                        "linearizedBaseContracts": [
                            14
                        ],
                        "name": "WrongContract",
                        "nameLocation": "34:13:0",
                        "nodeType": "ContractDefinition",
                        "nodes": [
                            {
                                "constant": false,
                                "functionSelector": "66d003ac",
                                "id": 3,
                                "mutability": "mutable",
                                "name": "recipient",
                                "nameLocation": "69:9:0",
                                "nodeType": "VariableDeclaration",
                                "scope": 14,
                                "src": "54:24:0",
                                "stateVariable": true,
                                "storageLocation": "default",
                                "typeDescriptions": {
                                    "typeIdentifier": "t_address",
                                    "typeString": "address"
                                },
                                "typeName": {
                                    "id": 2,
                                    "name": "address",
                                    "nodeType": "ElementaryTypeName",
                                    "src": "54:7:0",
                                    "stateMutability": "nonpayable",
                                    "typeDescriptions": {
                                        "typeIdentifier": "t_address",
                                        "typeString": "address"
                                    }
                                },
                                "visibility": "public"
                            },
                            {
                                "body": {
                                    "id": 12,
                                    "nodeType": "Block",
                                    "src": "134:109:0",
                                    "statements": [
                                        {
                                            "expression": {
                                                "id": 10,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "lValueRequested": false,
                                                "leftHandSide": {
                                                    "id": 8,
                                                    "name": "recipient",
                                                    "nodeType": "Identifier",
                                                    "overloadedDeclarations": [],
                                                    "referencedDeclaration": 3,
                                                    "src": "214:9:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_address",
                                                        "typeString": "address"
                                                    }
                                                },
                                                "nodeType": "Assignment",
                                                "operator": "=",
                                                "rightHandSide": {
                                                    "id": 9,
                                                    "name": "_recipient",
                                                    "nodeType": "Identifier",
                                                    "overloadedDeclarations": [],
                                                    "referencedDeclaration": 5,
                                                    "src": "226:10:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_address",
                                                        "typeString": "address"
                                                    }
                                                },
                                                "src": "214:22:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_address",
                                                    "typeString": "address"
                                                }
                                            },
                                            "id": 11,
                                            "nodeType": "ExpressionStatement",
                                            "src": "214:22:0"
                                        }
                                    ]
                                },
                                "functionSelector": "3bbed4a0",
                                "id": 13,
                                "implemented": true,
                                "kind": "function",
                                "modifiers": [],
                                "name": "setRecipient",
                                "nameLocation": "94:12:0",
                                "nodeType": "FunctionDefinition",
                                "parameters": {
                                    "id": 6,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 5,
                                            "mutability": "mutable",
                                            "name": "_recipient",
                                            "nameLocation": "115:10:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 13,
                                            "src": "107:18:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_address",
                                                "typeString": "address"
                                            },
                                            "typeName": {
                                                "id": 4,
                                                "name": "address",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "107:7:0",
                                                "stateMutability": "nonpayable",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_address",
                                                    "typeString": "address"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "106:20:0"
                                },
                                "returnParameters": {
                                    "id": 7,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "134:0:0"
                                },
                                "scope": 14,
                                "src": "85:158:0",
                                "stateMutability": "nonpayable",
                                "virtual": false,
                                "visibility": "public"
                            }
                        ],
                        "scope": 15,
                        "src": "25:220:0",
                        "usedErrors": [],
                        "usedEvents": []
                    }
                ],
                "src": "0:245:0"
            },
            "id": 0
        }
    }
}"""
    return json.loads(ast_json)


def test_missing_zero_address_check(vulnerable_ast):
    ast_json, src_file_list = reduce_json(vulnerable_ast)
    results = process_yaml(
        "eburger/templates/missing_zero_address_check.yaml",
        ast_json,
        src_file_list,
    )
    assert "Line 6 Columns 27-45" in results["results"][0]["lines"]
