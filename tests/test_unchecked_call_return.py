import json
import pytest
from eburger.serializer import reduce_json
from eburger.yaml_parser import process_yaml


@pytest.fixture
def vulnerable_ast() -> tuple[dict, list]:
    unchecked_ast = """{
    "sources": {
        "vulnerable_contracts/unchecked_call_return.sol": {
            "AST": {
                "absolutePath": "vulnerable_contracts/unchecked_call_return.sol",
                "exportedSymbols": {
                    "VulnerableContract": [
                        44
                    ]
                },
                "id": 45,
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
                        "canonicalName": "VulnerableContract",
                        "contractDependencies": [],
                        "contractKind": "contract",
                        "fullyImplemented": true,
                        "id": 44,
                        "linearizedBaseContracts": [
                            44
                        ],
                        "name": "VulnerableContract",
                        "nameLocation": "65:18:0",
                        "nodeType": "ContractDefinition",
                        "nodes": [
                            {
                                "constant": false,
                                "id": 3,
                                "mutability": "mutable",
                                "name": "owner",
                                "nameLocation": "106:5:0",
                                "nodeType": "VariableDeclaration",
                                "scope": 44,
                                "src": "90:21:0",
                                "stateVariable": true,
                                "storageLocation": "default",
                                "typeDescriptions": {
                                    "typeIdentifier": "t_address_payable",
                                    "typeString": "address payable"
                                },
                                "typeName": {
                                    "id": 2,
                                    "name": "address",
                                    "nodeType": "ElementaryTypeName",
                                    "src": "90:15:0",
                                    "stateMutability": "payable",
                                    "typeDescriptions": {
                                        "typeIdentifier": "t_address_payable",
                                        "typeString": "address payable"
                                    }
                                },
                                "visibility": "internal"
                            },
                            {
                                "body": {
                                    "id": 14,
                                    "nodeType": "Block",
                                    "src": "131:44:0",
                                    "statements": [
                                        {
                                            "expression": {
                                                "id": 12,
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
                                                    "src": "141:5:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_address_payable",
                                                        "typeString": "address payable"
                                                    }
                                                },
                                                "nodeType": "Assignment",
                                                "operator": "=",
                                                "rightHandSide": {
                                                    "arguments": [
                                                        {
                                                            "expression": {
                                                                "id": 9,
                                                                "name": "msg",
                                                                "nodeType": "Identifier",
                                                                "overloadedDeclarations": [],
                                                                "referencedDeclaration": -15,
                                                                "src": "157:3:0",
                                                                "typeDescriptions": {
                                                                    "typeIdentifier": "t_magic_message",
                                                                    "typeString": "msg"
                                                                }
                                                            },
                                                            "id": 10,
                                                            "isConstant": false,
                                                            "isLValue": false,
                                                            "isPure": false,
                                                            "lValueRequested": false,
                                                            "memberLocation": "161:6:0",
                                                            "memberName": "sender",
                                                            "nodeType": "MemberAccess",
                                                            "src": "157:10:0",
                                                            "typeDescriptions": {
                                                                "typeIdentifier": "t_address",
                                                                "typeString": "address"
                                                            }
                                                        }
                                                    ],
                                                    "expression": {
                                                        "argumentTypes": [
                                                            {
                                                                "typeIdentifier": "t_address",
                                                                "typeString": "address"
                                                            }
                                                        ],
                                                        "id": 8,
                                                        "isConstant": false,
                                                        "isLValue": false,
                                                        "isPure": true,
                                                        "lValueRequested": false,
                                                        "nodeType": "ElementaryTypeNameExpression",
                                                        "src": "149:8:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_type$_t_address_payable_$",
                                                            "typeString": "type(address payable)"
                                                        },
                                                        "typeName": {
                                                            "id": 7,
                                                            "name": "address",
                                                            "nodeType": "ElementaryTypeName",
                                                            "src": "149:8:0",
                                                            "stateMutability": "payable",
                                                            "typeDescriptions": {}
                                                        }
                                                    },
                                                    "id": 11,
                                                    "isConstant": false,
                                                    "isLValue": false,
                                                    "isPure": false,
                                                    "kind": "typeConversion",
                                                    "lValueRequested": false,
                                                    "nameLocations": [],
                                                    "names": [],
                                                    "nodeType": "FunctionCall",
                                                    "src": "149:19:0",
                                                    "tryCall": false,
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_address_payable",
                                                        "typeString": "address payable"
                                                    }
                                                },
                                                "src": "141:27:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_address_payable",
                                                    "typeString": "address payable"
                                                }
                                            },
                                            "id": 13,
                                            "nodeType": "ExpressionStatement",
                                            "src": "141:27:0"
                                        }
                                    ]
                                },
                                "id": 15,
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
                                    "src": "128:2:0"
                                },
                                "returnParameters": {
                                    "id": 5,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "131:0:0"
                                },
                                "scope": 44,
                                "src": "117:58:0",
                                "stateMutability": "nonpayable",
                                "virtual": false,
                                "visibility": "public"
                            },
                            {
                                "body": {
                                    "id": 38,
                                    "nodeType": "Block",
                                    "src": "319:188:0",
                                    "statements": [
                                        {
                                            "expression": {
                                                "arguments": [
                                                    {
                                                        "commonType": {
                                                            "typeIdentifier": "t_address",
                                                            "typeString": "address"
                                                        },
                                                        "id": 26,
                                                        "isConstant": false,
                                                        "isLValue": false,
                                                        "isPure": false,
                                                        "lValueRequested": false,
                                                        "leftExpression": {
                                                            "expression": {
                                                                "id": 23,
                                                                "name": "msg",
                                                                "nodeType": "Identifier",
                                                                "overloadedDeclarations": [],
                                                                "referencedDeclaration": -15,
                                                                "src": "337:3:0",
                                                                "typeDescriptions": {
                                                                    "typeIdentifier": "t_magic_message",
                                                                    "typeString": "msg"
                                                                }
                                                            },
                                                            "id": 24,
                                                            "isConstant": false,
                                                            "isLValue": false,
                                                            "isPure": false,
                                                            "lValueRequested": false,
                                                            "memberLocation": "341:6:0",
                                                            "memberName": "sender",
                                                            "nodeType": "MemberAccess",
                                                            "src": "337:10:0",
                                                            "typeDescriptions": {
                                                                "typeIdentifier": "t_address",
                                                                "typeString": "address"
                                                            }
                                                        },
                                                        "nodeType": "BinaryOperation",
                                                        "operator": "==",
                                                        "rightExpression": {
                                                            "id": 25,
                                                            "name": "owner",
                                                            "nodeType": "Identifier",
                                                            "overloadedDeclarations": [],
                                                            "referencedDeclaration": 3,
                                                            "src": "351:5:0",
                                                            "typeDescriptions": {
                                                                "typeIdentifier": "t_address_payable",
                                                                "typeString": "address payable"
                                                            }
                                                        },
                                                        "src": "337:19:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_bool",
                                                            "typeString": "bool"
                                                        }
                                                    },
                                                    {
                                                        "hexValue": "43616c6c6572206973206e6f7420746865206f776e6572",
                                                        "id": 27,
                                                        "isConstant": false,
                                                        "isLValue": false,
                                                        "isPure": true,
                                                        "kind": "string",
                                                        "lValueRequested": false,
                                                        "nodeType": "Literal",
                                                        "src": "358:25:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_stringliteral_15ed5034391ed5ef65b8bb8dbcb08f9b6c4034ebcf89f76344a17e1651e92b33",
                                                            "typeString": "literal_string Caller is not the owner"
                                                        },
                                                        "value": "Caller is not the owner"
                                                    }
                                                ],
                                                "expression": {
                                                    "argumentTypes": [
                                                        {
                                                            "typeIdentifier": "t_bool",
                                                            "typeString": "bool"
                                                        },
                                                        {
                                                            "typeIdentifier": "t_stringliteral_15ed5034391ed5ef65b8bb8dbcb08f9b6c4034ebcf89f76344a17e1651e92b33",
                                                            "typeString": "literal_string Caller is not the owner"
                                                        }
                                                    ],
                                                    "id": 22,
                                                    "name": "require",
                                                    "nodeType": "Identifier",
                                                    "overloadedDeclarations": [
                                                        -18,
                                                        -18
                                                    ],
                                                    "referencedDeclaration": -18,
                                                    "src": "329:7:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_function_require_pure$_t_bool_$_t_string_memory_ptr_$returns$__$",
                                                        "typeString": "function (bool,string memory) pure"
                                                    }
                                                },
                                                "id": 28,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "kind": "functionCall",
                                                "lValueRequested": false,
                                                "nameLocations": [],
                                                "names": [],
                                                "nodeType": "FunctionCall",
                                                "src": "329:55:0",
                                                "tryCall": false,
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_tuple$__$",
                                                    "typeString": "tuple()"
                                                }
                                            },
                                            "id": 29,
                                            "nodeType": "ExpressionStatement",
                                            "src": "329:55:0"
                                        },
                                        {
                                            "expression": {
                                                "arguments": [
                                                    {
                                                        "hexValue": "",
                                                        "id": 35,
                                                        "isConstant": false,
                                                        "isLValue": false,
                                                        "isPure": true,
                                                        "kind": "string",
                                                        "lValueRequested": false,
                                                        "nodeType": "Literal",
                                                        "src": "497:2:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_stringliteral_c5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470",
                                                            "typeString": "literal_string "
                                                        },
                                                        "value": ""
                                                    }
                                                ],
                                                "expression": {
                                                    "argumentTypes": [
                                                        {
                                                            "typeIdentifier": "t_stringliteral_c5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470",
                                                            "typeString": "literal_string "
                                                        }
                                                    ],
                                                    "expression": {
                                                        "argumentTypes": [
                                                            {
                                                                "typeIdentifier": "t_stringliteral_c5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470",
                                                                "typeString": "literal_string "
                                                            }
                                                        ],
                                                        "expression": {
                                                            "id": 30,
                                                            "name": "receiver",
                                                            "nodeType": "Identifier",
                                                            "overloadedDeclarations": [],
                                                            "referencedDeclaration": 17,
                                                            "src": "468:8:0",
                                                            "typeDescriptions": {
                                                                "typeIdentifier": "t_address_payable",
                                                                "typeString": "address payable"
                                                            }
                                                        },
                                                        "id": 32,
                                                        "isConstant": false,
                                                        "isLValue": false,
                                                        "isPure": false,
                                                        "lValueRequested": false,
                                                        "memberLocation": "477:4:0",
                                                        "memberName": "call",
                                                        "nodeType": "MemberAccess",
                                                        "src": "468:13:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_function_barecall_payable$_t_bytes_memory_ptr_$returns$_t_bool_$_t_bytes_memory_ptr_$",
                                                            "typeString": "function (bytes memory) payable returns (bool,bytes memory)"
                                                        }
                                                    },
                                                    "id": 34,
                                                    "isConstant": false,
                                                    "isLValue": false,
                                                    "isPure": false,
                                                    "lValueRequested": false,
                                                    "names": [
                                                        "value"
                                                    ],
                                                    "nodeType": "FunctionCallOptions",
                                                    "options": [
                                                        {
                                                            "id": 33,
                                                            "name": "amount",
                                                            "nodeType": "Identifier",
                                                            "overloadedDeclarations": [],
                                                            "referencedDeclaration": 19,
                                                            "src": "489:6:0",
                                                            "typeDescriptions": {
                                                                "typeIdentifier": "t_uint256",
                                                                "typeString": "uint256"
                                                            }
                                                        }
                                                    ],
                                                    "src": "468:28:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_function_barecall_payable$_t_bytes_memory_ptr_$returns$_t_bool_$_t_bytes_memory_ptr_$value",
                                                        "typeString": "function (bytes memory) payable returns (bool,bytes memory)"
                                                    }
                                                },
                                                "id": 36,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "kind": "functionCall",
                                                "lValueRequested": false,
                                                "nameLocations": [],
                                                "names": [],
                                                "nodeType": "FunctionCall",
                                                "src": "468:32:0",
                                                "tryCall": false,
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_tuple$_t_bool_$_t_bytes_memory_ptr_$",
                                                    "typeString": "tuple(bool,bytes memory)"
                                                }
                                            },
                                            "id": 37,
                                            "nodeType": "ExpressionStatement",
                                            "src": "468:32:0"
                                        }
                                    ]
                                },
                                "functionSelector": "102d2760",
                                "id": 39,
                                "implemented": true,
                                "kind": "function",
                                "modifiers": [],
                                "name": "unsafeSend",
                                "nameLocation": "262:10:0",
                                "nodeType": "FunctionDefinition",
                                "parameters": {
                                    "id": 20,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 17,
                                            "mutability": "mutable",
                                            "name": "receiver",
                                            "nameLocation": "289:8:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 39,
                                            "src": "273:24:0",
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
                                                "src": "273:15:0",
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
                                            "nameLocation": "304:6:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 39,
                                            "src": "299:11:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_uint256",
                                                "typeString": "uint256"
                                            },
                                            "typeName": {
                                                "id": 18,
                                                "name": "uint",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "299:4:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint256",
                                                    "typeString": "uint256"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "272:39:0"
                                },
                                "returnParameters": {
                                    "id": 21,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "319:0:0"
                                },
                                "scope": 44,
                                "src": "253:254:0",
                                "stateMutability": "nonpayable",
                                "virtual": false,
                                "visibility": "public"
                            },
                            {
                                "body": {
                                    "id": 42,
                                    "nodeType": "Block",
                                    "src": "595:2:0",
                                    "statements": []
                                },
                                "id": 43,
                                "implemented": true,
                                "kind": "receive",
                                "modifiers": [],
                                "name": "",
                                "nameLocation": "-1:-1:-1",
                                "nodeType": "FunctionDefinition",
                                "parameters": {
                                    "id": 40,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "575:2:0"
                                },
                                "returnParameters": {
                                    "id": 41,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "595:0:0"
                                },
                                "scope": 44,
                                "src": "568:29:0",
                                "stateMutability": "payable",
                                "virtual": false,
                                "visibility": "external"
                            }
                        ],
                        "scope": 45,
                        "src": "56:543:0",
                        "usedErrors": [],
                        "usedEvents": []
                    }
                ],
                "src": "32:568:0"
            },
            "id": 0
        }
    }
}"""
    return json.loads(unchecked_ast)


def test_unchecked_call_return(vulnerable_ast):
    ast_json, src_paths = reduce_json(vulnerable_ast)
    results = process_yaml(
        "eburger/templates/unchecked_call_return.yaml",
        ast_json,
        src_paths,
    )
    assert "Line 14 Columns 9-37" in results["results"][0]["lines"]
