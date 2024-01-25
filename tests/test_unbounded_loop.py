import json
import pytest
from eburger.serializer import reduce_json
from eburger.yaml_parser import process_yaml


@pytest.fixture
def vulnerable_ast() -> (dict, list):
    ast_json = """{
    "sources": {
        "vulnerable_contracts/unbounded_loop.sol": {
            "AST": {
                "absolutePath": "vulnerable_contracts/unbounded_loop.sol",
                "exportedSymbols": {
                    "FaultyContract": [
                        46
                    ]
                },
                "id": 47,
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
                        "canonicalName": "FaultyContract",
                        "contractDependencies": [],
                        "contractKind": "contract",
                        "fullyImplemented": true,
                        "id": 46,
                        "linearizedBaseContracts": [
                            46
                        ],
                        "name": "FaultyContract",
                        "nameLocation": "66:14:0",
                        "nodeType": "ContractDefinition",
                        "nodes": [
                            {
                                "constant": false,
                                "functionSelector": "d42a1aa6",
                                "id": 4,
                                "mutability": "mutable",
                                "name": "largeArray",
                                "nameLocation": "104:10:0",
                                "nodeType": "VariableDeclaration",
                                "scope": 46,
                                "src": "87:27:0",
                                "stateVariable": true,
                                "storageLocation": "default",
                                "typeDescriptions": {
                                    "typeIdentifier": "t_array$_t_uint256_$dyn_storage",
                                    "typeString": "uint256[]"
                                },
                                "typeName": {
                                    "baseType": {
                                        "id": 2,
                                        "name": "uint256",
                                        "nodeType": "ElementaryTypeName",
                                        "src": "87:7:0",
                                        "typeDescriptions": {
                                            "typeIdentifier": "t_uint256",
                                            "typeString": "uint256"
                                        }
                                    },
                                    "id": 3,
                                    "nodeType": "ArrayTypeName",
                                    "src": "87:9:0",
                                    "typeDescriptions": {
                                        "typeIdentifier": "t_array$_t_uint256_$dyn_storage_ptr",
                                        "typeString": "uint256[]"
                                    }
                                },
                                "visibility": "public"
                            },
                            {
                                "constant": false,
                                "functionSelector": "000d02cd",
                                "id": 6,
                                "mutability": "mutable",
                                "name": "lastSum",
                                "nameLocation": "135:7:0",
                                "nodeType": "VariableDeclaration",
                                "scope": 46,
                                "src": "120:22:0",
                                "stateVariable": true,
                                "storageLocation": "default",
                                "typeDescriptions": {
                                    "typeIdentifier": "t_uint256",
                                    "typeString": "uint256"
                                },
                                "typeName": {
                                    "id": 5,
                                    "name": "uint256",
                                    "nodeType": "ElementaryTypeName",
                                    "src": "120:7:0",
                                    "typeDescriptions": {
                                        "typeIdentifier": "t_uint256",
                                        "typeString": "uint256"
                                    }
                                },
                                "visibility": "public"
                            },
                            {
                                "body": {
                                    "id": 17,
                                    "nodeType": "Block",
                                    "src": "250:41:0",
                                    "statements": [
                                        {
                                            "expression": {
                                                "arguments": [
                                                    {
                                                        "id": 14,
                                                        "name": "element",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 8,
                                                        "src": "276:7:0",
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
                                                        "id": 11,
                                                        "name": "largeArray",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 4,
                                                        "src": "260:10:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_array$_t_uint256_$dyn_storage",
                                                            "typeString": "uint256[] storage ref"
                                                        }
                                                    },
                                                    "id": 13,
                                                    "isConstant": false,
                                                    "isLValue": false,
                                                    "isPure": false,
                                                    "lValueRequested": false,
                                                    "memberLocation": "271:4:0",
                                                    "memberName": "push",
                                                    "nodeType": "MemberAccess",
                                                    "src": "260:15:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_function_arraypush_nonpayable$_t_array$_t_uint256_$dyn_storage_ptr_$_t_uint256_$returns$__$attached_to$_t_array$_t_uint256_$dyn_storage_ptr_$",
                                                        "typeString": "function (uint256[] storage pointer,uint256)"
                                                    }
                                                },
                                                "id": 15,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "kind": "functionCall",
                                                "lValueRequested": false,
                                                "nameLocations": [],
                                                "names": [],
                                                "nodeType": "FunctionCall",
                                                "src": "260:24:0",
                                                "tryCall": false,
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_tuple$__$",
                                                    "typeString": "tuple()"
                                                }
                                            },
                                            "id": 16,
                                            "nodeType": "ExpressionStatement",
                                            "src": "260:24:0"
                                        }
                                    ]
                                },
                                "functionSelector": "1c3638db",
                                "id": 18,
                                "implemented": true,
                                "kind": "function",
                                "modifiers": [],
                                "name": "addToLargeArray",
                                "nameLocation": "210:15:0",
                                "nodeType": "FunctionDefinition",
                                "parameters": {
                                    "id": 9,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 8,
                                            "mutability": "mutable",
                                            "name": "element",
                                            "nameLocation": "234:7:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 18,
                                            "src": "226:15:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_uint256",
                                                "typeString": "uint256"
                                            },
                                            "typeName": {
                                                "id": 7,
                                                "name": "uint256",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "226:7:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint256",
                                                    "typeString": "uint256"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "225:17:0"
                                },
                                "returnParameters": {
                                    "id": 10,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "250:0:0"
                                },
                                "scope": 46,
                                "src": "201:90:0",
                                "stateMutability": "nonpayable",
                                "virtual": false,
                                "visibility": "public"
                            },
                            {
                                "body": {
                                    "id": 44,
                                    "nodeType": "Block",
                                    "src": "376:134:0",
                                    "statements": [
                                        {
                                            "assignments": [
                                                22
                                            ],
                                            "declarations": [
                                                {
                                                    "constant": false,
                                                    "id": 22,
                                                    "mutability": "mutable",
                                                    "name": "sum",
                                                    "nameLocation": "394:3:0",
                                                    "nodeType": "VariableDeclaration",
                                                    "scope": 44,
                                                    "src": "386:11:0",
                                                    "stateVariable": false,
                                                    "storageLocation": "default",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_uint256",
                                                        "typeString": "uint256"
                                                    },
                                                    "typeName": {
                                                        "id": 21,
                                                        "name": "uint256",
                                                        "nodeType": "ElementaryTypeName",
                                                        "src": "386:7:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_uint256",
                                                            "typeString": "uint256"
                                                        }
                                                    },
                                                    "visibility": "internal"
                                                }
                                            ],
                                            "id": 24,
                                            "initialValue": {
                                                "hexValue": "30",
                                                "id": 23,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": true,
                                                "kind": "number",
                                                "lValueRequested": false,
                                                "nodeType": "Literal",
                                                "src": "400:1:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_rational_0_by_1",
                                                    "typeString": "int_const 0"
                                                },
                                                "value": "0"
                                            },
                                            "nodeType": "VariableDeclarationStatement",
                                            "src": "386:15:0"
                                        },
                                        {
                                            "body": {
                                                "id": 42,
                                                "nodeType": "Block",
                                                "src": "459:45:0",
                                                "statements": [
                                                    {
                                                        "expression": {
                                                            "id": 40,
                                                            "isConstant": false,
                                                            "isLValue": false,
                                                            "isPure": false,
                                                            "lValueRequested": false,
                                                            "leftHandSide": {
                                                                "id": 36,
                                                                "name": "sum",
                                                                "nodeType": "Identifier",
                                                                "overloadedDeclarations": [],
                                                                "referencedDeclaration": 22,
                                                                "src": "473:3:0",
                                                                "typeDescriptions": {
                                                                    "typeIdentifier": "t_uint256",
                                                                    "typeString": "uint256"
                                                                }
                                                            },
                                                            "nodeType": "Assignment",
                                                            "operator": "+=",
                                                            "rightHandSide": {
                                                                "baseExpression": {
                                                                    "id": 37,
                                                                    "name": "largeArray",
                                                                    "nodeType": "Identifier",
                                                                    "overloadedDeclarations": [],
                                                                    "referencedDeclaration": 4,
                                                                    "src": "480:10:0",
                                                                    "typeDescriptions": {
                                                                        "typeIdentifier": "t_array$_t_uint256_$dyn_storage",
                                                                        "typeString": "uint256[] storage ref"
                                                                    }
                                                                },
                                                                "id": 39,
                                                                "indexExpression": {
                                                                    "id": 38,
                                                                    "name": "i",
                                                                    "nodeType": "Identifier",
                                                                    "overloadedDeclarations": [],
                                                                    "referencedDeclaration": 26,
                                                                    "src": "491:1:0",
                                                                    "typeDescriptions": {
                                                                        "typeIdentifier": "t_uint256",
                                                                        "typeString": "uint256"
                                                                    }
                                                                },
                                                                "isConstant": false,
                                                                "isLValue": true,
                                                                "isPure": false,
                                                                "lValueRequested": false,
                                                                "nodeType": "IndexAccess",
                                                                "src": "480:13:0",
                                                                "typeDescriptions": {
                                                                    "typeIdentifier": "t_uint256",
                                                                    "typeString": "uint256"
                                                                }
                                                            },
                                                            "src": "473:20:0",
                                                            "typeDescriptions": {
                                                                "typeIdentifier": "t_uint256",
                                                                "typeString": "uint256"
                                                            }
                                                        },
                                                        "id": 41,
                                                        "nodeType": "ExpressionStatement",
                                                        "src": "473:20:0"
                                                    }
                                                ]
                                            },
                                            "condition": {
                                                "commonType": {
                                                    "typeIdentifier": "t_uint256",
                                                    "typeString": "uint256"
                                                },
                                                "id": 32,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "lValueRequested": false,
                                                "leftExpression": {
                                                    "id": 29,
                                                    "name": "i",
                                                    "nodeType": "Identifier",
                                                    "overloadedDeclarations": [],
                                                    "referencedDeclaration": 26,
                                                    "src": "431:1:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_uint256",
                                                        "typeString": "uint256"
                                                    }
                                                },
                                                "nodeType": "BinaryOperation",
                                                "operator": "<",
                                                "rightExpression": {
                                                    "expression": {
                                                        "id": 30,
                                                        "name": "largeArray",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 4,
                                                        "src": "435:10:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_array$_t_uint256_$dyn_storage",
                                                            "typeString": "uint256[] storage ref"
                                                        }
                                                    },
                                                    "id": 31,
                                                    "isConstant": false,
                                                    "isLValue": false,
                                                    "isPure": false,
                                                    "lValueRequested": false,
                                                    "memberLocation": "446:6:0",
                                                    "memberName": "length",
                                                    "nodeType": "MemberAccess",
                                                    "src": "435:17:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_uint256",
                                                        "typeString": "uint256"
                                                    }
                                                },
                                                "src": "431:21:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_bool",
                                                    "typeString": "bool"
                                                }
                                            },
                                            "id": 43,
                                            "initializationExpression": {
                                                "assignments": [
                                                    26
                                                ],
                                                "declarations": [
                                                    {
                                                        "constant": false,
                                                        "id": 26,
                                                        "mutability": "mutable",
                                                        "name": "i",
                                                        "nameLocation": "424:1:0",
                                                        "nodeType": "VariableDeclaration",
                                                        "scope": 43,
                                                        "src": "416:9:0",
                                                        "stateVariable": false,
                                                        "storageLocation": "default",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_uint256",
                                                            "typeString": "uint256"
                                                        },
                                                        "typeName": {
                                                            "id": 25,
                                                            "name": "uint256",
                                                            "nodeType": "ElementaryTypeName",
                                                            "src": "416:7:0",
                                                            "typeDescriptions": {
                                                                "typeIdentifier": "t_uint256",
                                                                "typeString": "uint256"
                                                            }
                                                        },
                                                        "visibility": "internal"
                                                    }
                                                ],
                                                "id": 28,
                                                "initialValue": {
                                                    "hexValue": "30",
                                                    "id": 27,
                                                    "isConstant": false,
                                                    "isLValue": false,
                                                    "isPure": true,
                                                    "kind": "number",
                                                    "lValueRequested": false,
                                                    "nodeType": "Literal",
                                                    "src": "428:1:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_rational_0_by_1",
                                                        "typeString": "int_const 0"
                                                    },
                                                    "value": "0"
                                                },
                                                "nodeType": "VariableDeclarationStatement",
                                                "src": "416:13:0"
                                            },
                                            "loopExpression": {
                                                "expression": {
                                                    "id": 34,
                                                    "isConstant": false,
                                                    "isLValue": false,
                                                    "isPure": false,
                                                    "lValueRequested": false,
                                                    "nodeType": "UnaryOperation",
                                                    "operator": "++",
                                                    "prefix": false,
                                                    "src": "454:3:0",
                                                    "subExpression": {
                                                        "id": 33,
                                                        "name": "i",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 26,
                                                        "src": "454:1:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_uint256",
                                                            "typeString": "uint256"
                                                        }
                                                    },
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_uint256",
                                                        "typeString": "uint256"
                                                    }
                                                },
                                                "id": 35,
                                                "nodeType": "ExpressionStatement",
                                                "src": "454:3:0"
                                            },
                                            "nodeType": "ForStatement",
                                            "src": "411:93:0"
                                        }
                                    ]
                                },
                                "functionSelector": "59360eab",
                                "id": 45,
                                "implemented": true,
                                "kind": "function",
                                "modifiers": [],
                                "name": "updateSum",
                                "nameLocation": "357:9:0",
                                "nodeType": "FunctionDefinition",
                                "parameters": {
                                    "id": 19,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "366:2:0"
                                },
                                "returnParameters": {
                                    "id": 20,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "376:0:0"
                                },
                                "scope": 46,
                                "src": "348:162:0",
                                "stateMutability": "nonpayable",
                                "virtual": false,
                                "visibility": "public"
                            }
                        ],
                        "scope": 47,
                        "src": "57:455:0",
                        "usedErrors": [],
                        "usedEvents": []
                    }
                ],
                "src": "32:481:0"
            },
            "id": 0
        }
    }
}"""
    return json.loads(ast_json)


def test_unbounded_loop(vulnerable_ast):
    ast_json, src_file_list = reduce_json(vulnerable_ast)
    results = process_yaml(
        "eburger/templates/unbounded_loop.yaml",
        ast_json,
        src_file_list,
    )
    assert "Line 15 Columns 9-58" in results["results"][0]["lines"]
