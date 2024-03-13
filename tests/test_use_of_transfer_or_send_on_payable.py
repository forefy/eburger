import json
import pytest
from eburger.serializer import reduce_json
from eburger.yaml_parser import process_yaml


@pytest.fixture
def vulnerable_ast() -> tuple[dict, list]:
    ast_json = """{
    "sources": {
        "vulnerable_contracts/use_of_transfer_or_send_on_payable.sol": {
            "AST": {
                "absolutePath": "vulnerable_contracts/use_of_transfer_or_send_on_payable.sol",
                "exportedSymbols": {
                    "UngoodContract": [
                        36
                    ]
                },
                "id": 37,
                "license": "MIT",
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
                        "src": "32:23:0"
                    },
                    {
                        "abstract": false,
                        "baseContracts": [],
                        "canonicalName": "UngoodContract",
                        "contractDependencies": [],
                        "contractKind": "contract",
                        "fullyImplemented": true,
                        "id": 36,
                        "linearizedBaseContracts": [
                            36
                        ],
                        "name": "UngoodContract",
                        "nameLocation": "66:14:0",
                        "nodeType": "ContractDefinition",
                        "nodes": [
                            {
                                "body": {
                                    "id": 14,
                                    "nodeType": "Block",
                                    "src": "160:102:0",
                                    "statements": [
                                        {
                                            "expression": {
                                                "arguments": [
                                                    {
                                                        "id": 11,
                                                        "name": "amount",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 5,
                                                        "src": "248:6:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_uint256",
                                                            "typeString": "uint256"
                                                        }
                                                    }
                                                ],
                                                "expression": {
                                                    "argumentTypes": [
                                                        {
                                                            "typeIdentifier": "t_uint256",
                                                            "typeString": "uint256"
                                                        }
                                                    ],
                                                    "expression": {
                                                        "id": 8,
                                                        "name": "recipient",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 3,
                                                        "src": "229:9:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_address_payable",
                                                            "typeString": "address payable"
                                                        }
                                                    },
                                                    "id": 10,
                                                    "isConstant": false,
                                                    "isLValue": false,
                                                    "isPure": false,
                                                    "lValueRequested": false,
                                                    "memberLocation": "239:8:0",
                                                    "memberName": "transfer",
                                                    "nodeType": "MemberAccess",
                                                    "src": "229:18:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_function_transfer_nonpayable$_t_uint256_$returns$__$",
                                                        "typeString": "function (uint256)"
                                                    }
                                                },
                                                "id": 12,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "kind": "functionCall",
                                                "lValueRequested": false,
                                                "nameLocations": [],
                                                "names": [],
                                                "nodeType": "FunctionCall",
                                                "src": "229:26:0",
                                                "tryCall": false,
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_tuple$__$",
                                                    "typeString": "tuple()"
                                                }
                                            },
                                            "id": 13,
                                            "nodeType": "ExpressionStatement",
                                            "src": "229:26:0"
                                        }
                                    ]
                                },
                                "functionSelector": "05b1137b",
                                "id": 15,
                                "implemented": true,
                                "kind": "function",
                                "modifiers": [],
                                "name": "transferEther",
                                "nameLocation": "96:13:0",
                                "nodeType": "FunctionDefinition",
                                "parameters": {
                                    "id": 6,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 3,
                                            "mutability": "mutable",
                                            "name": "recipient",
                                            "nameLocation": "126:9:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 15,
                                            "src": "110:25:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_address_payable",
                                                "typeString": "address payable"
                                            },
                                            "typeName": {
                                                "id": 2,
                                                "name": "address",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "110:15:0",
                                                "stateMutability": "payable",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_address_payable",
                                                    "typeString": "address payable"
                                                }
                                            },
                                            "visibility": "internal"
                                        },
                                        {
                                            "constant": false,
                                            "id": 5,
                                            "mutability": "mutable",
                                            "name": "amount",
                                            "nameLocation": "145:6:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 15,
                                            "src": "137:14:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_uint256",
                                                "typeString": "uint256"
                                            },
                                            "typeName": {
                                                "id": 4,
                                                "name": "uint256",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "137:7:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint256",
                                                    "typeString": "uint256"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "109:43:0"
                                },
                                "returnParameters": {
                                    "id": 7,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "160:0:0"
                                },
                                "scope": 36,
                                "src": "87:175:0",
                                "stateMutability": "nonpayable",
                                "virtual": false,
                                "visibility": "public"
                            },
                            {
                                "body": {
                                    "id": 34,
                                    "nodeType": "Block",
                                    "src": "337:153:0",
                                    "statements": [
                                        {
                                            "assignments": [
                                                23
                                            ],
                                            "declarations": [
                                                {
                                                    "constant": false,
                                                    "id": 23,
                                                    "mutability": "mutable",
                                                    "name": "sent",
                                                    "nameLocation": "407:4:0",
                                                    "nodeType": "VariableDeclaration",
                                                    "scope": 34,
                                                    "src": "402:9:0",
                                                    "stateVariable": false,
                                                    "storageLocation": "default",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_bool",
                                                        "typeString": "bool"
                                                    },
                                                    "typeName": {
                                                        "id": 22,
                                                        "name": "bool",
                                                        "nodeType": "ElementaryTypeName",
                                                        "src": "402:4:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_bool",
                                                            "typeString": "bool"
                                                        }
                                                    },
                                                    "visibility": "internal"
                                                }
                                            ],
                                            "id": 28,
                                            "initialValue": {
                                                "arguments": [
                                                    {
                                                        "id": 26,
                                                        "name": "amount",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 19,
                                                        "src": "429:6:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_uint256",
                                                            "typeString": "uint256"
                                                        }
                                                    }
                                                ],
                                                "expression": {
                                                    "argumentTypes": [
                                                        {
                                                            "typeIdentifier": "t_uint256",
                                                            "typeString": "uint256"
                                                        }
                                                    ],
                                                    "expression": {
                                                        "id": 24,
                                                        "name": "recipient",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 17,
                                                        "src": "414:9:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_address_payable",
                                                            "typeString": "address payable"
                                                        }
                                                    },
                                                    "id": 25,
                                                    "isConstant": false,
                                                    "isLValue": false,
                                                    "isPure": false,
                                                    "lValueRequested": false,
                                                    "memberLocation": "424:4:0",
                                                    "memberName": "send",
                                                    "nodeType": "MemberAccess",
                                                    "src": "414:14:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_function_send_nonpayable$_t_uint256_$returns$_t_bool_$",
                                                        "typeString": "function (uint256) returns (bool)"
                                                    }
                                                },
                                                "id": 27,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "kind": "functionCall",
                                                "lValueRequested": false,
                                                "nameLocations": [],
                                                "names": [],
                                                "nodeType": "FunctionCall",
                                                "src": "414:22:0",
                                                "tryCall": false,
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_bool",
                                                    "typeString": "bool"
                                                }
                                            },
                                            "nodeType": "VariableDeclarationStatement",
                                            "src": "402:34:0"
                                        },
                                        {
                                            "expression": {
                                                "arguments": [
                                                    {
                                                        "id": 30,
                                                        "name": "sent",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 23,
                                                        "src": "454:4:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_bool",
                                                            "typeString": "bool"
                                                        }
                                                    },
                                                    {
                                                        "hexValue": "4661696c656420746f2073656e64204574686572",
                                                        "id": 31,
                                                        "isConstant": false,
                                                        "isLValue": false,
                                                        "isPure": true,
                                                        "kind": "string",
                                                        "lValueRequested": false,
                                                        "nodeType": "Literal",
                                                        "src": "460:22:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_stringliteral_445140255c9d889994129d349e64078d6f76b4b37ec896948f7e858f9b8a0dcb",
                                                            "typeString": "literal_string Failed to send Ether"
                                                        },
                                                        "value": "Failed to send Ether"
                                                    }
                                                ],
                                                "expression": {
                                                    "argumentTypes": [
                                                        {
                                                            "typeIdentifier": "t_bool",
                                                            "typeString": "bool"
                                                        },
                                                        {
                                                            "typeIdentifier": "t_stringliteral_445140255c9d889994129d349e64078d6f76b4b37ec896948f7e858f9b8a0dcb",
                                                            "typeString": "literal_string Failed to send Ether"
                                                        }
                                                    ],
                                                    "id": 29,
                                                    "name": "require",
                                                    "nodeType": "Identifier",
                                                    "overloadedDeclarations": [
                                                        -18,
                                                        -18
                                                    ],
                                                    "referencedDeclaration": -18,
                                                    "src": "446:7:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_function_require_pure$_t_bool_$_t_string_memory_ptr_$returns$__$",
                                                        "typeString": "function (bool,string memory) pure"
                                                    }
                                                },
                                                "id": 32,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "kind": "functionCall",
                                                "lValueRequested": false,
                                                "nameLocations": [],
                                                "names": [],
                                                "nodeType": "FunctionCall",
                                                "src": "446:37:0",
                                                "tryCall": false,
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_tuple$__$",
                                                    "typeString": "tuple()"
                                                }
                                            },
                                            "id": 33,
                                            "nodeType": "ExpressionStatement",
                                            "src": "446:37:0"
                                        }
                                    ]
                                },
                                "functionSelector": "c1756a2c",
                                "id": 35,
                                "implemented": true,
                                "kind": "function",
                                "modifiers": [],
                                "name": "sendEther",
                                "nameLocation": "277:9:0",
                                "nodeType": "FunctionDefinition",
                                "parameters": {
                                    "id": 20,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 17,
                                            "mutability": "mutable",
                                            "name": "recipient",
                                            "nameLocation": "303:9:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 35,
                                            "src": "287:25:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_address_payable",
                                                "typeString": "address payable"
                                            },
                                            "typeName": {
                                                "id": 16,
                                                "name": "address",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "287:15:0",
                                                "stateMutability": "payable",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_address_payable",
                                                    "typeString": "address payable"
                                                }
                                            },
                                            "visibility": "internal"
                                        },
                                        {
                                            "constant": false,
                                            "id": 19,
                                            "mutability": "mutable",
                                            "name": "amount",
                                            "nameLocation": "322:6:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 35,
                                            "src": "314:14:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_uint256",
                                                "typeString": "uint256"
                                            },
                                            "typeName": {
                                                "id": 18,
                                                "name": "uint256",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "314:7:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint256",
                                                    "typeString": "uint256"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "286:43:0"
                                },
                                "returnParameters": {
                                    "id": 21,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "337:0:0"
                                },
                                "scope": 36,
                                "src": "268:222:0",
                                "stateMutability": "nonpayable",
                                "virtual": false,
                                "visibility": "public"
                            }
                        ],
                        "scope": 37,
                        "src": "57:435:0",
                        "usedErrors": [],
                        "usedEvents": []
                    }
                ],
                "src": "32:460:0"
            },
            "id": 0
        }
    }
}"""
    return json.loads(ast_json)


def test_use_of_transfer_or_send_on_payable(vulnerable_ast):
    ast_json, src_paths = reduce_json(vulnerable_ast)
    results = process_yaml(
        "eburger/templates/use_of_transfer_or_send_on_payable.yaml",
        ast_json,
        src_paths,
    )
    assert "Line 7 Columns 9-35" in results["results"][0]["lines"]
