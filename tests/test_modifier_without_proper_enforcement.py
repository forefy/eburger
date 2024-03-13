import json
import pytest
from eburger.serializer import reduce_json
from eburger.yaml_parser import process_yaml


@pytest.fixture
def vulnerable_ast() -> tuple[dict, list]:
    ast_json = """{
    "sources": {
        "vulnerable_contracts/modifier_without_proper_enforcement.sol": {
            "AST": {
                "absolutePath": "vulnerable_contracts/modifier_without_proper_enforcement.sol",
                "exportedSymbols": {
                    "BuggieContract": [
                        34
                    ]
                },
                "id": 35,
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
                        "canonicalName": "BuggieContract",
                        "contractDependencies": [],
                        "contractKind": "contract",
                        "fullyImplemented": true,
                        "id": 34,
                        "linearizedBaseContracts": [
                            34
                        ],
                        "name": "BuggieContract",
                        "nameLocation": "33:14:0",
                        "nodeType": "ContractDefinition",
                        "nodes": [
                            {
                                "constant": false,
                                "functionSelector": "8da5cb5b",
                                "id": 3,
                                "mutability": "mutable",
                                "name": "owner",
                                "nameLocation": "69:5:0",
                                "nodeType": "VariableDeclaration",
                                "scope": 34,
                                "src": "54:20:0",
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
                                    "id": 11,
                                    "nodeType": "Block",
                                    "src": "94:35:0",
                                    "statements": [
                                        {
                                            "expression": {
                                                "id": 9,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "lValueRequested": false,
                                                "leftHandSide": {
                                                    "id": 6,
                                                    "name": "owner",
                                                    "nodeType": "Identifier",
                                                    "overloadedDeclarations": [],
                                                    "referencedDeclaration": 3,
                                                    "src": "104:5:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_address",
                                                        "typeString": "address"
                                                    }
                                                },
                                                "nodeType": "Assignment",
                                                "operator": "=",
                                                "rightHandSide": {
                                                    "expression": {
                                                        "id": 7,
                                                        "name": "msg",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": -15,
                                                        "src": "112:3:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_magic_message",
                                                            "typeString": "msg"
                                                        }
                                                    },
                                                    "id": 8,
                                                    "isConstant": false,
                                                    "isLValue": false,
                                                    "isPure": false,
                                                    "lValueRequested": false,
                                                    "memberLocation": "116:6:0",
                                                    "memberName": "sender",
                                                    "nodeType": "MemberAccess",
                                                    "src": "112:10:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_address",
                                                        "typeString": "address"
                                                    }
                                                },
                                                "src": "104:18:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_address",
                                                    "typeString": "address"
                                                }
                                            },
                                            "id": 10,
                                            "nodeType": "ExpressionStatement",
                                            "src": "104:18:0"
                                        }
                                    ]
                                },
                                "id": 12,
                                "implemented": true,
                                "kind": "constructor",
                                "modifiers": [],
                                "name": "",
                                "nameLocation": "-1:-1:-1",
                                "nodeType": "FunctionDefinition",
                                "parameters": {
                                    "id": 4,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "91:2:0"
                                },
                                "returnParameters": {
                                    "id": 5,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "94:0:0"
                                },
                                "scope": 34,
                                "src": "80:49:0",
                                "stateMutability": "nonpayable",
                                "virtual": false,
                                "visibility": "public"
                            },
                            {
                                "body": {
                                    "id": 20,
                                    "nodeType": "Block",
                                    "src": "156:118:0",
                                    "statements": [
                                        {
                                            "expression": {
                                                "commonType": {
                                                    "typeIdentifier": "t_address",
                                                    "typeString": "address"
                                                },
                                                "id": 17,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "lValueRequested": false,
                                                "leftExpression": {
                                                    "id": 14,
                                                    "name": "owner",
                                                    "nodeType": "Identifier",
                                                    "overloadedDeclarations": [],
                                                    "referencedDeclaration": 3,
                                                    "src": "237:5:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_address",
                                                        "typeString": "address"
                                                    }
                                                },
                                                "nodeType": "BinaryOperation",
                                                "operator": "==",
                                                "rightExpression": {
                                                    "expression": {
                                                        "id": 15,
                                                        "name": "msg",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": -15,
                                                        "src": "246:3:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_magic_message",
                                                            "typeString": "msg"
                                                        }
                                                    },
                                                    "id": 16,
                                                    "isConstant": false,
                                                    "isLValue": false,
                                                    "isPure": false,
                                                    "lValueRequested": false,
                                                    "memberLocation": "250:6:0",
                                                    "memberName": "sender",
                                                    "nodeType": "MemberAccess",
                                                    "src": "246:10:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_address",
                                                        "typeString": "address"
                                                    }
                                                },
                                                "src": "237:19:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_bool",
                                                    "typeString": "bool"
                                                }
                                            },
                                            "id": 18,
                                            "nodeType": "ExpressionStatement",
                                            "src": "237:19:0"
                                        },
                                        {
                                            "id": 19,
                                            "nodeType": "PlaceholderStatement",
                                            "src": "266:1:0"
                                        }
                                    ]
                                },
                                "id": 21,
                                "name": "onlyOwner",
                                "nameLocation": "144:9:0",
                                "nodeType": "ModifierDefinition",
                                "parameters": {
                                    "id": 13,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "153:2:0"
                                },
                                "src": "135:139:0",
                                "virtual": false,
                                "visibility": "internal"
                            },
                            {
                                "body": {
                                    "id": 32,
                                    "nodeType": "Block",
                                    "src": "337:192:0",
                                    "statements": [
                                        {
                                            "expression": {
                                                "id": 30,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "lValueRequested": false,
                                                "leftHandSide": {
                                                    "id": 28,
                                                    "name": "owner",
                                                    "nodeType": "Identifier",
                                                    "overloadedDeclarations": [],
                                                    "referencedDeclaration": 3,
                                                    "src": "505:5:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_address",
                                                        "typeString": "address"
                                                    }
                                                },
                                                "nodeType": "Assignment",
                                                "operator": "=",
                                                "rightHandSide": {
                                                    "id": 29,
                                                    "name": "_newOwner",
                                                    "nodeType": "Identifier",
                                                    "overloadedDeclarations": [],
                                                    "referencedDeclaration": 23,
                                                    "src": "513:9:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_address",
                                                        "typeString": "address"
                                                    }
                                                },
                                                "src": "505:17:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_address",
                                                    "typeString": "address"
                                                }
                                            },
                                            "id": 31,
                                            "nodeType": "ExpressionStatement",
                                            "src": "505:17:0"
                                        }
                                    ]
                                },
                                "functionSelector": "a6f9dae1",
                                "id": 33,
                                "implemented": true,
                                "kind": "function",
                                "modifiers": [
                                    {
                                        "id": 26,
                                        "kind": "modifierInvocation",
                                        "modifierName": {
                                            "id": 25,
                                            "name": "onlyOwner",
                                            "nameLocations": [
                                                "327:9:0"
                                            ],
                                            "nodeType": "IdentifierPath",
                                            "referencedDeclaration": 21,
                                            "src": "327:9:0"
                                        },
                                        "nodeType": "ModifierInvocation",
                                        "src": "327:9:0"
                                    }
                                ],
                                "name": "changeOwner",
                                "nameLocation": "289:11:0",
                                "nodeType": "FunctionDefinition",
                                "parameters": {
                                    "id": 24,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 23,
                                            "mutability": "mutable",
                                            "name": "_newOwner",
                                            "nameLocation": "309:9:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 33,
                                            "src": "301:17:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_address",
                                                "typeString": "address"
                                            },
                                            "typeName": {
                                                "id": 22,
                                                "name": "address",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "301:7:0",
                                                "stateMutability": "nonpayable",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_address",
                                                    "typeString": "address"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "300:19:0"
                                },
                                "returnParameters": {
                                    "id": 27,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "337:0:0"
                                },
                                "scope": 34,
                                "src": "280:249:0",
                                "stateMutability": "nonpayable",
                                "virtual": false,
                                "visibility": "public"
                            }
                        ],
                        "scope": 35,
                        "src": "24:507:0",
                        "usedErrors": [],
                        "usedEvents": []
                    }
                ],
                "src": "0:532:0"
            },
            "id": 0
        }
    }
}"""
    return json.loads(ast_json)


def test_modifier_without_proper_enforcement(vulnerable_ast):
    ast_json, src_paths = reduce_json(vulnerable_ast)
    results = process_yaml(
        "eburger/templates/modifier_without_proper_enforcement.yaml",
        ast_json,
        src_paths,
    )
    assert "Line 6 Columns 8-28" in results["results"][0]["lines"]
