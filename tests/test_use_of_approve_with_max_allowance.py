import json
import pytest
from eburger.serializer import reduce_json
from eburger.yaml_parser import process_yaml


@pytest.fixture
def vulnerable_ast() -> tuple[dict, list]:
    ast_json = """{
    "sources": {
        "vulnerable_contracts/use_of_approve_with_max_allowance.sol": {
            "AST": {
                "absolutePath": "vulnerable_contracts/use_of_approve_with_max_allowance.sol",
                "exportedSymbols": {
                    "IERC20": [
                        22
                    ],
                    "VulnerableApproval": [
                        72
                    ]
                },
                "id": 73,
                "license": "MIT",
                "nodeType": "SourceUnit",
                "nodes": [
                    {
                        "id": 1,
                        "literals": [
                            "solidity",
                            "^",
                            "0.8",
                            ".20"
                        ],
                        "nodeType": "PragmaDirective",
                        "src": "32:24:0"
                    },
                    {
                        "abstract": false,
                        "baseContracts": [],
                        "canonicalName": "IERC20",
                        "contractDependencies": [],
                        "contractKind": "interface",
                        "fullyImplemented": false,
                        "id": 22,
                        "linearizedBaseContracts": [
                            22
                        ],
                        "name": "IERC20",
                        "nameLocation": "68:6:0",
                        "nodeType": "ContractDefinition",
                        "nodes": [
                            {
                                "functionSelector": "095ea7b3",
                                "id": 10,
                                "implemented": false,
                                "kind": "function",
                                "modifiers": [],
                                "name": "approve",
                                "nameLocation": "90:7:0",
                                "nodeType": "FunctionDefinition",
                                "parameters": {
                                    "id": 6,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 3,
                                            "mutability": "mutable",
                                            "name": "spender",
                                            "nameLocation": "106:7:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 10,
                                            "src": "98:15:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_address",
                                                "typeString": "address"
                                            },
                                            "typeName": {
                                                "id": 2,
                                                "name": "address",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "98:7:0",
                                                "stateMutability": "nonpayable",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_address",
                                                    "typeString": "address"
                                                }
                                            },
                                            "visibility": "internal"
                                        },
                                        {
                                            "constant": false,
                                            "id": 5,
                                            "mutability": "mutable",
                                            "name": "amount",
                                            "nameLocation": "123:6:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 10,
                                            "src": "115:14:0",
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
                                                "src": "115:7:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint256",
                                                    "typeString": "uint256"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "97:33:0"
                                },
                                "returnParameters": {
                                    "id": 9,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 8,
                                            "mutability": "mutable",
                                            "name": "",
                                            "nameLocation": "-1:-1:-1",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 10,
                                            "src": "149:4:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_bool",
                                                "typeString": "bool"
                                            },
                                            "typeName": {
                                                "id": 7,
                                                "name": "bool",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "149:4:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_bool",
                                                    "typeString": "bool"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "148:6:0"
                                },
                                "scope": 22,
                                "src": "81:74:0",
                                "stateMutability": "nonpayable",
                                "virtual": false,
                                "visibility": "external"
                            },
                            {
                                "functionSelector": "23b872dd",
                                "id": 21,
                                "implemented": false,
                                "kind": "function",
                                "modifiers": [],
                                "name": "transferFrom",
                                "nameLocation": "169:12:0",
                                "nodeType": "FunctionDefinition",
                                "parameters": {
                                    "id": 17,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 12,
                                            "mutability": "mutable",
                                            "name": "sender",
                                            "nameLocation": "190:6:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 21,
                                            "src": "182:14:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_address",
                                                "typeString": "address"
                                            },
                                            "typeName": {
                                                "id": 11,
                                                "name": "address",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "182:7:0",
                                                "stateMutability": "nonpayable",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_address",
                                                    "typeString": "address"
                                                }
                                            },
                                            "visibility": "internal"
                                        },
                                        {
                                            "constant": false,
                                            "id": 14,
                                            "mutability": "mutable",
                                            "name": "recipient",
                                            "nameLocation": "206:9:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 21,
                                            "src": "198:17:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_address",
                                                "typeString": "address"
                                            },
                                            "typeName": {
                                                "id": 13,
                                                "name": "address",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "198:7:0",
                                                "stateMutability": "nonpayable",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_address",
                                                    "typeString": "address"
                                                }
                                            },
                                            "visibility": "internal"
                                        },
                                        {
                                            "constant": false,
                                            "id": 16,
                                            "mutability": "mutable",
                                            "name": "amount",
                                            "nameLocation": "225:6:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 21,
                                            "src": "217:14:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_uint256",
                                                "typeString": "uint256"
                                            },
                                            "typeName": {
                                                "id": 15,
                                                "name": "uint256",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "217:7:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint256",
                                                    "typeString": "uint256"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "181:51:0"
                                },
                                "returnParameters": {
                                    "id": 20,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 19,
                                            "mutability": "mutable",
                                            "name": "",
                                            "nameLocation": "-1:-1:-1",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 21,
                                            "src": "251:4:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_bool",
                                                "typeString": "bool"
                                            },
                                            "typeName": {
                                                "id": 18,
                                                "name": "bool",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "251:4:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_bool",
                                                    "typeString": "bool"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "250:6:0"
                                },
                                "scope": 22,
                                "src": "160:97:0",
                                "stateMutability": "nonpayable",
                                "virtual": false,
                                "visibility": "external"
                            }
                        ],
                        "scope": 73,
                        "src": "58:201:0",
                        "usedErrors": [],
                        "usedEvents": []
                    },
                    {
                        "abstract": false,
                        "baseContracts": [],
                        "canonicalName": "VulnerableApproval",
                        "contractDependencies": [],
                        "contractKind": "contract",
                        "fullyImplemented": true,
                        "id": 72,
                        "linearizedBaseContracts": [
                            72
                        ],
                        "name": "VulnerableApproval",
                        "nameLocation": "270:18:0",
                        "nodeType": "ContractDefinition",
                        "nodes": [
                            {
                                "body": {
                                    "id": 41,
                                    "nodeType": "Block",
                                    "src": "429:66:0",
                                    "statements": [
                                        {
                                            "expression": {
                                                "arguments": [
                                                    {
                                                        "id": 33,
                                                        "name": "spender",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 26,
                                                        "src": "461:7:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_address",
                                                            "typeString": "address"
                                                        }
                                                    },
                                                    {
                                                        "expression": {
                                                            "arguments": [
                                                                {
                                                                    "id": 36,
                                                                    "isConstant": false,
                                                                    "isLValue": false,
                                                                    "isPure": true,
                                                                    "lValueRequested": false,
                                                                    "nodeType": "ElementaryTypeNameExpression",
                                                                    "src": "475:7:0",
                                                                    "typeDescriptions": {
                                                                        "typeIdentifier": "t_type$_t_uint256_$",
                                                                        "typeString": "type(uint256)"
                                                                    },
                                                                    "typeName": {
                                                                        "id": 35,
                                                                        "name": "uint256",
                                                                        "nodeType": "ElementaryTypeName",
                                                                        "src": "475:7:0",
                                                                        "typeDescriptions": {}
                                                                    }
                                                                }
                                                            ],
                                                            "expression": {
                                                                "argumentTypes": [
                                                                    {
                                                                        "typeIdentifier": "t_type$_t_uint256_$",
                                                                        "typeString": "type(uint256)"
                                                                    }
                                                                ],
                                                                "id": 34,
                                                                "name": "type",
                                                                "nodeType": "Identifier",
                                                                "overloadedDeclarations": [],
                                                                "referencedDeclaration": -27,
                                                                "src": "470:4:0",
                                                                "typeDescriptions": {
                                                                    "typeIdentifier": "t_function_metatype_pure$__$returns$__$",
                                                                    "typeString": "function () pure"
                                                                }
                                                            },
                                                            "id": 37,
                                                            "isConstant": false,
                                                            "isLValue": false,
                                                            "isPure": true,
                                                            "kind": "functionCall",
                                                            "lValueRequested": false,
                                                            "nameLocations": [],
                                                            "names": [],
                                                            "nodeType": "FunctionCall",
                                                            "src": "470:13:0",
                                                            "tryCall": false,
                                                            "typeDescriptions": {
                                                                "typeIdentifier": "t_magic_meta_type_t_uint256",
                                                                "typeString": "type(uint256)"
                                                            }
                                                        },
                                                        "id": 38,
                                                        "isConstant": false,
                                                        "isLValue": false,
                                                        "isPure": true,
                                                        "lValueRequested": false,
                                                        "memberLocation": "484:3:0",
                                                        "memberName": "max",
                                                        "nodeType": "MemberAccess",
                                                        "src": "470:17:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_uint256",
                                                            "typeString": "uint256"
                                                        }
                                                    }
                                                ],
                                                "expression": {
                                                    "argumentTypes": [
                                                        {
                                                            "typeIdentifier": "t_address",
                                                            "typeString": "address"
                                                        },
                                                        {
                                                            "typeIdentifier": "t_uint256",
                                                            "typeString": "uint256"
                                                        }
                                                    ],
                                                    "expression": {
                                                        "arguments": [
                                                            {
                                                                "id": 30,
                                                                "name": "token",
                                                                "nodeType": "Identifier",
                                                                "overloadedDeclarations": [],
                                                                "referencedDeclaration": 24,
                                                                "src": "446:5:0",
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
                                                            "id": 29,
                                                            "name": "IERC20",
                                                            "nodeType": "Identifier",
                                                            "overloadedDeclarations": [],
                                                            "referencedDeclaration": 22,
                                                            "src": "439:6:0",
                                                            "typeDescriptions": {
                                                                "typeIdentifier": "t_type$_t_contract$_IERC20_$22_$",
                                                                "typeString": "type(contract IERC20)"
                                                            }
                                                        },
                                                        "id": 31,
                                                        "isConstant": false,
                                                        "isLValue": false,
                                                        "isPure": false,
                                                        "kind": "typeConversion",
                                                        "lValueRequested": false,
                                                        "nameLocations": [],
                                                        "names": [],
                                                        "nodeType": "FunctionCall",
                                                        "src": "439:13:0",
                                                        "tryCall": false,
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_contract$_IERC20_$22",
                                                            "typeString": "contract IERC20"
                                                        }
                                                    },
                                                    "id": 32,
                                                    "isConstant": false,
                                                    "isLValue": false,
                                                    "isPure": false,
                                                    "lValueRequested": false,
                                                    "memberLocation": "453:7:0",
                                                    "memberName": "approve",
                                                    "nodeType": "MemberAccess",
                                                    "referencedDeclaration": 10,
                                                    "src": "439:21:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_function_external_nonpayable$_t_address_$_t_uint256_$returns$_t_bool_$",
                                                        "typeString": "function (address,uint256) external returns (bool)"
                                                    }
                                                },
                                                "id": 39,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "kind": "functionCall",
                                                "lValueRequested": false,
                                                "nameLocations": [],
                                                "names": [],
                                                "nodeType": "FunctionCall",
                                                "src": "439:49:0",
                                                "tryCall": false,
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_bool",
                                                    "typeString": "bool"
                                                }
                                            },
                                            "id": 40,
                                            "nodeType": "ExpressionStatement",
                                            "src": "439:49:0"
                                        }
                                    ]
                                },
                                "functionSelector": "836ae25f",
                                "id": 42,
                                "implemented": true,
                                "kind": "function",
                                "modifiers": [],
                                "name": "approveInfinite",
                                "nameLocation": "372:15:0",
                                "nodeType": "FunctionDefinition",
                                "parameters": {
                                    "id": 27,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 24,
                                            "mutability": "mutable",
                                            "name": "token",
                                            "nameLocation": "396:5:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 42,
                                            "src": "388:13:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_address",
                                                "typeString": "address"
                                            },
                                            "typeName": {
                                                "id": 23,
                                                "name": "address",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "388:7:0",
                                                "stateMutability": "nonpayable",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_address",
                                                    "typeString": "address"
                                                }
                                            },
                                            "visibility": "internal"
                                        },
                                        {
                                            "constant": false,
                                            "id": 26,
                                            "mutability": "mutable",
                                            "name": "spender",
                                            "nameLocation": "411:7:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 42,
                                            "src": "403:15:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_address",
                                                "typeString": "address"
                                            },
                                            "typeName": {
                                                "id": 25,
                                                "name": "address",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "403:7:0",
                                                "stateMutability": "nonpayable",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_address",
                                                    "typeString": "address"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "387:32:0"
                                },
                                "returnParameters": {
                                    "id": 28,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "429:0:0"
                                },
                                "scope": 72,
                                "src": "363:132:0",
                                "stateMutability": "nonpayable",
                                "virtual": false,
                                "visibility": "external"
                            },
                            {
                                "body": {
                                    "id": 70,
                                    "nodeType": "Block",
                                    "src": "598:135:0",
                                    "statements": [
                                        {
                                            "assignments": [
                                                55
                                            ],
                                            "declarations": [
                                                {
                                                    "constant": false,
                                                    "id": 55,
                                                    "mutability": "mutable",
                                                    "name": "tokenContract",
                                                    "nameLocation": "615:13:0",
                                                    "nodeType": "VariableDeclaration",
                                                    "scope": 70,
                                                    "src": "608:20:0",
                                                    "stateVariable": false,
                                                    "storageLocation": "default",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_contract$_IERC20_$22",
                                                        "typeString": "contract IERC20"
                                                    },
                                                    "typeName": {
                                                        "id": 54,
                                                        "nodeType": "UserDefinedTypeName",
                                                        "pathNode": {
                                                            "id": 53,
                                                            "name": "IERC20",
                                                            "nameLocations": [
                                                                "608:6:0"
                                                            ],
                                                            "nodeType": "IdentifierPath",
                                                            "referencedDeclaration": 22,
                                                            "src": "608:6:0"
                                                        },
                                                        "referencedDeclaration": 22,
                                                        "src": "608:6:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_contract$_IERC20_$22",
                                                            "typeString": "contract IERC20"
                                                        }
                                                    },
                                                    "visibility": "internal"
                                                }
                                            ],
                                            "id": 59,
                                            "initialValue": {
                                                "arguments": [
                                                    {
                                                        "id": 57,
                                                        "name": "token",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 44,
                                                        "src": "638:5:0",
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
                                                    "id": 56,
                                                    "name": "IERC20",
                                                    "nodeType": "Identifier",
                                                    "overloadedDeclarations": [],
                                                    "referencedDeclaration": 22,
                                                    "src": "631:6:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_type$_t_contract$_IERC20_$22_$",
                                                        "typeString": "type(contract IERC20)"
                                                    }
                                                },
                                                "id": 58,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "kind": "typeConversion",
                                                "lValueRequested": false,
                                                "nameLocations": [],
                                                "names": [],
                                                "nodeType": "FunctionCall",
                                                "src": "631:13:0",
                                                "tryCall": false,
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_contract$_IERC20_$22",
                                                    "typeString": "contract IERC20"
                                                }
                                            },
                                            "nodeType": "VariableDeclarationStatement",
                                            "src": "608:36:0"
                                        },
                                        {
                                            "expression": {
                                                "arguments": [
                                                    {
                                                        "arguments": [
                                                            {
                                                                "id": 63,
                                                                "name": "from",
                                                                "nodeType": "Identifier",
                                                                "overloadedDeclarations": [],
                                                                "referencedDeclaration": 46,
                                                                "src": "689:4:0",
                                                                "typeDescriptions": {
                                                                    "typeIdentifier": "t_address",
                                                                    "typeString": "address"
                                                                }
                                                            },
                                                            {
                                                                "id": 64,
                                                                "name": "to",
                                                                "nodeType": "Identifier",
                                                                "overloadedDeclarations": [],
                                                                "referencedDeclaration": 48,
                                                                "src": "695:2:0",
                                                                "typeDescriptions": {
                                                                    "typeIdentifier": "t_address",
                                                                    "typeString": "address"
                                                                }
                                                            },
                                                            {
                                                                "id": 65,
                                                                "name": "amount",
                                                                "nodeType": "Identifier",
                                                                "overloadedDeclarations": [],
                                                                "referencedDeclaration": 50,
                                                                "src": "699:6:0",
                                                                "typeDescriptions": {
                                                                    "typeIdentifier": "t_uint256",
                                                                    "typeString": "uint256"
                                                                }
                                                            }
                                                        ],
                                                        "expression": {
                                                            "argumentTypes": [
                                                                {
                                                                    "typeIdentifier": "t_address",
                                                                    "typeString": "address"
                                                                },
                                                                {
                                                                    "typeIdentifier": "t_address",
                                                                    "typeString": "address"
                                                                },
                                                                {
                                                                    "typeIdentifier": "t_uint256",
                                                                    "typeString": "uint256"
                                                                }
                                                            ],
                                                            "expression": {
                                                                "id": 61,
                                                                "name": "tokenContract",
                                                                "nodeType": "Identifier",
                                                                "overloadedDeclarations": [],
                                                                "referencedDeclaration": 55,
                                                                "src": "662:13:0",
                                                                "typeDescriptions": {
                                                                    "typeIdentifier": "t_contract$_IERC20_$22",
                                                                    "typeString": "contract IERC20"
                                                                }
                                                            },
                                                            "id": 62,
                                                            "isConstant": false,
                                                            "isLValue": false,
                                                            "isPure": false,
                                                            "lValueRequested": false,
                                                            "memberLocation": "676:12:0",
                                                            "memberName": "transferFrom",
                                                            "nodeType": "MemberAccess",
                                                            "referencedDeclaration": 21,
                                                            "src": "662:26:0",
                                                            "typeDescriptions": {
                                                                "typeIdentifier": "t_function_external_nonpayable$_t_address_$_t_address_$_t_uint256_$returns$_t_bool_$",
                                                                "typeString": "function (address,address,uint256) external returns (bool)"
                                                            }
                                                        },
                                                        "id": 66,
                                                        "isConstant": false,
                                                        "isLValue": false,
                                                        "isPure": false,
                                                        "kind": "functionCall",
                                                        "lValueRequested": false,
                                                        "nameLocations": [],
                                                        "names": [],
                                                        "nodeType": "FunctionCall",
                                                        "src": "662:44:0",
                                                        "tryCall": false,
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_bool",
                                                            "typeString": "bool"
                                                        }
                                                    },
                                                    {
                                                        "hexValue": "5472616e73666572206661696c6564",
                                                        "id": 67,
                                                        "isConstant": false,
                                                        "isLValue": false,
                                                        "isPure": true,
                                                        "kind": "string",
                                                        "lValueRequested": false,
                                                        "nodeType": "Literal",
                                                        "src": "708:17:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_stringliteral_25adaa6d082ce15f901e0d8a3d393e7462ef9edf2e6bc8321fa14d1615b6fc51",
                                                            "typeString": "literal_string 'Transfer failed'"
                                                        },
                                                        "value": "Transfer failed"
                                                    }
                                                ],
                                                "expression": {
                                                    "argumentTypes": [
                                                        {
                                                            "typeIdentifier": "t_bool",
                                                            "typeString": "bool"
                                                        },
                                                        {
                                                            "typeIdentifier": "t_stringliteral_25adaa6d082ce15f901e0d8a3d393e7462ef9edf2e6bc8321fa14d1615b6fc51",
                                                            "typeString": "literal_string 'Transfer failed'"
                                                        }
                                                    ],
                                                    "id": 60,
                                                    "name": "require",
                                                    "nodeType": "Identifier",
                                                    "overloadedDeclarations": [
                                                        -18,
                                                        -18
                                                    ],
                                                    "referencedDeclaration": -18,
                                                    "src": "654:7:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_function_require_pure$_t_bool_$_t_string_memory_ptr_$returns$__$",
                                                        "typeString": "function (bool,string memory) pure"
                                                    }
                                                },
                                                "id": 68,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "kind": "functionCall",
                                                "lValueRequested": false,
                                                "nameLocations": [],
                                                "names": [],
                                                "nodeType": "FunctionCall",
                                                "src": "654:72:0",
                                                "tryCall": false,
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_tuple$__$",
                                                    "typeString": "tuple()"
                                                }
                                            },
                                            "id": 69,
                                            "nodeType": "ExpressionStatement",
                                            "src": "654:72:0"
                                        }
                                    ]
                                },
                                "functionSelector": "febc7c82",
                                "id": 71,
                                "implemented": true,
                                "kind": "function",
                                "modifiers": [],
                                "name": "transferWithApproval",
                                "nameLocation": "511:20:0",
                                "nodeType": "FunctionDefinition",
                                "parameters": {
                                    "id": 51,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 44,
                                            "mutability": "mutable",
                                            "name": "token",
                                            "nameLocation": "540:5:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 71,
                                            "src": "532:13:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_address",
                                                "typeString": "address"
                                            },
                                            "typeName": {
                                                "id": 43,
                                                "name": "address",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "532:7:0",
                                                "stateMutability": "nonpayable",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_address",
                                                    "typeString": "address"
                                                }
                                            },
                                            "visibility": "internal"
                                        },
                                        {
                                            "constant": false,
                                            "id": 46,
                                            "mutability": "mutable",
                                            "name": "from",
                                            "nameLocation": "555:4:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 71,
                                            "src": "547:12:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_address",
                                                "typeString": "address"
                                            },
                                            "typeName": {
                                                "id": 45,
                                                "name": "address",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "547:7:0",
                                                "stateMutability": "nonpayable",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_address",
                                                    "typeString": "address"
                                                }
                                            },
                                            "visibility": "internal"
                                        },
                                        {
                                            "constant": false,
                                            "id": 48,
                                            "mutability": "mutable",
                                            "name": "to",
                                            "nameLocation": "569:2:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 71,
                                            "src": "561:10:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_address",
                                                "typeString": "address"
                                            },
                                            "typeName": {
                                                "id": 47,
                                                "name": "address",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "561:7:0",
                                                "stateMutability": "nonpayable",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_address",
                                                    "typeString": "address"
                                                }
                                            },
                                            "visibility": "internal"
                                        },
                                        {
                                            "constant": false,
                                            "id": 50,
                                            "mutability": "mutable",
                                            "name": "amount",
                                            "nameLocation": "581:6:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 71,
                                            "src": "573:14:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_uint256",
                                                "typeString": "uint256"
                                            },
                                            "typeName": {
                                                "id": 49,
                                                "name": "uint256",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "573:7:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint256",
                                                    "typeString": "uint256"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "531:57:0"
                                },
                                "returnParameters": {
                                    "id": 52,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "598:0:0"
                                },
                                "scope": 72,
                                "src": "502:231:0",
                                "stateMutability": "nonpayable",
                                "virtual": false,
                                "visibility": "external"
                            }
                        ],
                        "scope": 73,
                        "src": "261:474:0",
                        "usedErrors": [],
                        "usedEvents": []
                    }
                ],
                "src": "32:704:0"
            },
            "id": 0
        }
    }
}"""
    return json.loads(ast_json)


def test_use_of_approve_with_max_allowance(vulnerable_ast):
    ast_json, src_file_list = reduce_json(vulnerable_ast)
    results = process_yaml(
        "eburger/templates/use_of_approve_with_max_allowance.yaml",
        ast_json,
        src_file_list,
    )
    assert "Line 12 Columns 9-58" in results["results"][0]["lines"]
