import json
import pytest
from eburger.serializer import reduce_json
from eburger.yaml_parser import process_yaml


@pytest.fixture
def vulnerable_ast() -> tuple[dict, list]:
    ast_json = """{
    "sources": {
        "vulnerable_contracts/unverified_from_address_in_transfer/src/unverified_from_address_in_transfer.sol": {
            "id": 8,
            "ast": {
                "absolutePath": "vulnerable_contracts/unverified_from_address_in_transfer/src/unverified_from_address_in_transfer.sol",
                "id": 937,
                "exportedSymbols": {
                    "Address": [
                        849
                    ],
                    "IERC1363": [
                        81
                    ],
                    "IERC20": [
                        167
                    ],
                    "InsecureTokenTransfer": [
                        936
                    ],
                    "SafeERC20": [
                        590
                    ]
                },
                "nodeType": "SourceUnit",
                "src": "32:796:8",
                "nodes": [
                    {
                        "id": 880,
                        "nodeType": "PragmaDirective",
                        "src": "32:23:8",
                        "nodes": [],
                        "literals": [
                            "solidity",
                            "0.8",
                            ".20"
                        ]
                    },
                    {
                        "id": 881,
                        "nodeType": "ImportDirective",
                        "src": "57:72:8",
                        "nodes": [],
                        "absolutePath": "lib/openzeppelin-contracts/contracts/token/ERC20/IERC20.sol",
                        "file": "../lib/openzeppelin-contracts/contracts/token/ERC20/IERC20.sol",
                        "nameLocation": "-1:-1:-1",
                        "scope": 937,
                        "sourceUnit": 168,
                        "symbolAliases": [],
                        "unitAlias": ""
                    },
                    {
                        "id": 882,
                        "nodeType": "ImportDirective",
                        "src": "130:81:8",
                        "nodes": [],
                        "absolutePath": "lib/openzeppelin-contracts/contracts/token/ERC20/utils/SafeERC20.sol",
                        "file": "../lib/openzeppelin-contracts/contracts/token/ERC20/utils/SafeERC20.sol",
                        "nameLocation": "-1:-1:-1",
                        "scope": 937,
                        "sourceUnit": 591,
                        "symbolAliases": [],
                        "unitAlias": ""
                    },
                    {
                        "id": 936,
                        "nodeType": "ContractDefinition",
                        "src": "213:614:8",
                        "nodes": [
                            {
                                "id": 886,
                                "nodeType": "UsingForDirective",
                                "src": "250:27:8",
                                "nodes": [],
                                "global": false,
                                "libraryName": {
                                    "id": 883,
                                    "name": "SafeERC20",
                                    "nameLocations": [
                                        "256:9:8"
                                    ],
                                    "nodeType": "IdentifierPath",
                                    "referencedDeclaration": 590,
                                    "src": "256:9:8"
                                },
                                "typeName": {
                                    "id": 885,
                                    "nodeType": "UserDefinedTypeName",
                                    "pathNode": {
                                        "id": 884,
                                        "name": "IERC20",
                                        "nameLocations": [
                                            "270:6:8"
                                        ],
                                        "nodeType": "IdentifierPath",
                                        "referencedDeclaration": 167,
                                        "src": "270:6:8"
                                    },
                                    "referencedDeclaration": 167,
                                    "src": "270:6:8",
                                    "typeDescriptions": {
                                        "typeIdentifier": "t_contract$_IERC20_$167",
                                        "typeString": "contract IERC20"
                                    }
                                }
                            },
                            {
                                "id": 889,
                                "nodeType": "VariableDeclaration",
                                "src": "283:21:8",
                                "nodes": [],
                                "constant": false,
                                "mutability": "mutable",
                                "name": "_token",
                                "nameLocation": "298:6:8",
                                "scope": 936,
                                "stateVariable": true,
                                "storageLocation": "default",
                                "typeDescriptions": {
                                    "typeIdentifier": "t_contract$_IERC20_$167",
                                    "typeString": "contract IERC20"
                                },
                                "typeName": {
                                    "id": 888,
                                    "nodeType": "UserDefinedTypeName",
                                    "pathNode": {
                                        "id": 887,
                                        "name": "IERC20",
                                        "nameLocations": [
                                            "283:6:8"
                                        ],
                                        "nodeType": "IdentifierPath",
                                        "referencedDeclaration": 167,
                                        "src": "283:6:8"
                                    },
                                    "referencedDeclaration": 167,
                                    "src": "283:6:8",
                                    "typeDescriptions": {
                                        "typeIdentifier": "t_contract$_IERC20_$167",
                                        "typeString": "contract IERC20"
                                    }
                                },
                                "visibility": "private"
                            },
                            {
                                "id": 900,
                                "nodeType": "FunctionDefinition",
                                "src": "311:71:8",
                                "nodes": [],
                                "body": {
                                    "id": 899,
                                    "nodeType": "Block",
                                    "src": "344:38:8",
                                    "nodes": [],
                                    "statements": [
                                        {
                                            "expression": {
                                                "id": 897,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "lValueRequested": false,
                                                "leftHandSide": {
                                                    "id": 895,
                                                    "name": "_token",
                                                    "nodeType": "Identifier",
                                                    "overloadedDeclarations": [],
                                                    "referencedDeclaration": 889,
                                                    "src": "354:6:8",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_contract$_IERC20_$167",
                                                        "typeString": "contract IERC20"
                                                    }
                                                },
                                                "nodeType": "Assignment",
                                                "operator": "=",
                                                "rightHandSide": {
                                                    "id": 896,
                                                    "name": "tokenAddress",
                                                    "nodeType": "Identifier",
                                                    "overloadedDeclarations": [],
                                                    "referencedDeclaration": 892,
                                                    "src": "363:12:8",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_contract$_IERC20_$167",
                                                        "typeString": "contract IERC20"
                                                    }
                                                },
                                                "src": "354:21:8",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_contract$_IERC20_$167",
                                                    "typeString": "contract IERC20"
                                                }
                                            },
                                            "id": 898,
                                            "nodeType": "ExpressionStatement",
                                            "src": "354:21:8"
                                        }
                                    ]
                                },
                                "implemented": true,
                                "kind": "constructor",
                                "modifiers": [],
                                "name": "",
                                "nameLocation": "-1:-1:-1",
                                "parameters": {
                                    "id": 893,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 892,
                                            "mutability": "mutable",
                                            "name": "tokenAddress",
                                            "nameLocation": "330:12:8",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 900,
                                            "src": "323:19:8",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_contract$_IERC20_$167",
                                                "typeString": "contract IERC20"
                                            },
                                            "typeName": {
                                                "id": 891,
                                                "nodeType": "UserDefinedTypeName",
                                                "pathNode": {
                                                    "id": 890,
                                                    "name": "IERC20",
                                                    "nameLocations": [
                                                        "323:6:8"
                                                    ],
                                                    "nodeType": "IdentifierPath",
                                                    "referencedDeclaration": 167,
                                                    "src": "323:6:8"
                                                },
                                                "referencedDeclaration": 167,
                                                "src": "323:6:8",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_contract$_IERC20_$167",
                                                    "typeString": "contract IERC20"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "322:21:8"
                                },
                                "returnParameters": {
                                    "id": 894,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "344:0:8"
                                },
                                "scope": 936,
                                "stateMutability": "nonpayable",
                                "virtual": false,
                                "visibility": "public"
                            },
                            {
                                "id": 918,
                                "nodeType": "FunctionDefinition",
                                "src": "388:145:8",
                                "nodes": [],
                                "body": {
                                    "id": 917,
                                    "nodeType": "Block",
                                    "src": "471:62:8",
                                    "nodes": [],
                                    "statements": [
                                        {
                                            "expression": {
                                                "arguments": [
                                                    {
                                                        "id": 912,
                                                        "name": "sender",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 902,
                                                        "src": "501:6:8",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_address",
                                                            "typeString": "address"
                                                        }
                                                    },
                                                    {
                                                        "id": 913,
                                                        "name": "recipient",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 904,
                                                        "src": "509:9:8",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_address",
                                                            "typeString": "address"
                                                        }
                                                    },
                                                    {
                                                        "id": 914,
                                                        "name": "value",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 906,
                                                        "src": "520:5:8",
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
                                                        "id": 909,
                                                        "name": "_token",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 889,
                                                        "src": "481:6:8",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_contract$_IERC20_$167",
                                                            "typeString": "contract IERC20"
                                                        }
                                                    },
                                                    "id": 911,
                                                    "isConstant": false,
                                                    "isLValue": false,
                                                    "isPure": false,
                                                    "lValueRequested": false,
                                                    "memberLocation": "488:12:8",
                                                    "memberName": "transferFrom",
                                                    "nodeType": "MemberAccess",
                                                    "referencedDeclaration": 166,
                                                    "src": "481:19:8",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_function_external_nonpayable$_t_address_$_t_address_$_t_uint256_$returns$_t_bool_$",
                                                        "typeString": "function (address,address,uint256) external returns (bool)"
                                                    }
                                                },
                                                "id": 915,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "kind": "functionCall",
                                                "lValueRequested": false,
                                                "nameLocations": [],
                                                "names": [],
                                                "nodeType": "FunctionCall",
                                                "src": "481:45:8",
                                                "tryCall": false,
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_bool",
                                                    "typeString": "bool"
                                                }
                                            },
                                            "id": 916,
                                            "nodeType": "ExpressionStatement",
                                            "src": "481:45:8"
                                        }
                                    ]
                                },
                                "functionSelector": "36c26e1b",
                                "implemented": true,
                                "kind": "function",
                                "modifiers": [],
                                "name": "insecureTransfer",
                                "nameLocation": "397:16:8",
                                "parameters": {
                                    "id": 907,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 902,
                                            "mutability": "mutable",
                                            "name": "sender",
                                            "nameLocation": "422:6:8",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 918,
                                            "src": "414:14:8",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_address",
                                                "typeString": "address"
                                            },
                                            "typeName": {
                                                "id": 901,
                                                "name": "address",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "414:7:8",
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
                                            "id": 904,
                                            "mutability": "mutable",
                                            "name": "recipient",
                                            "nameLocation": "438:9:8",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 918,
                                            "src": "430:17:8",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_address",
                                                "typeString": "address"
                                            },
                                            "typeName": {
                                                "id": 903,
                                                "name": "address",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "430:7:8",
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
                                            "id": 906,
                                            "mutability": "mutable",
                                            "name": "value",
                                            "nameLocation": "457:5:8",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 918,
                                            "src": "449:13:8",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_uint256",
                                                "typeString": "uint256"
                                            },
                                            "typeName": {
                                                "id": 905,
                                                "name": "uint256",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "449:7:8",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint256",
                                                    "typeString": "uint256"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "413:50:8"
                                },
                                "returnParameters": {
                                    "id": 908,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "471:0:8"
                                },
                                "scope": 936,
                                "stateMutability": "nonpayable",
                                "virtual": false,
                                "visibility": "public"
                            },
                            {
                                "id": 935,
                                "nodeType": "FunctionDefinition",
                                "src": "598:226:8",
                                "nodes": [],
                                "body": {
                                    "id": 934,
                                    "nodeType": "Block",
                                    "src": "665:159:8",
                                    "nodes": [],
                                    "statements": [
                                        {
                                            "expression": {
                                                "arguments": [
                                                    {
                                                        "expression": {
                                                            "id": 928,
                                                            "name": "msg",
                                                            "nodeType": "Identifier",
                                                            "overloadedDeclarations": [],
                                                            "referencedDeclaration": -15,
                                                            "src": "788:3:8",
                                                            "typeDescriptions": {
                                                                "typeIdentifier": "t_magic_message",
                                                                "typeString": "msg"
                                                            }
                                                        },
                                                        "id": 929,
                                                        "isConstant": false,
                                                        "isLValue": false,
                                                        "isPure": false,
                                                        "lValueRequested": false,
                                                        "memberLocation": "792:6:8",
                                                        "memberName": "sender",
                                                        "nodeType": "MemberAccess",
                                                        "src": "788:10:8",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_address",
                                                            "typeString": "address"
                                                        }
                                                    },
                                                    {
                                                        "id": 930,
                                                        "name": "recipient",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 920,
                                                        "src": "800:9:8",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_address",
                                                            "typeString": "address"
                                                        }
                                                    },
                                                    {
                                                        "id": 931,
                                                        "name": "value",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 922,
                                                        "src": "811:5:8",
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
                                                        "id": 925,
                                                        "name": "_token",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 889,
                                                        "src": "768:6:8",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_contract$_IERC20_$167",
                                                            "typeString": "contract IERC20"
                                                        }
                                                    },
                                                    "id": 927,
                                                    "isConstant": false,
                                                    "isLValue": false,
                                                    "isPure": false,
                                                    "lValueRequested": false,
                                                    "memberLocation": "775:12:8",
                                                    "memberName": "transferFrom",
                                                    "nodeType": "MemberAccess",
                                                    "referencedDeclaration": 166,
                                                    "src": "768:19:8",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_function_external_nonpayable$_t_address_$_t_address_$_t_uint256_$returns$_t_bool_$",
                                                        "typeString": "function (address,address,uint256) external returns (bool)"
                                                    }
                                                },
                                                "id": 932,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "kind": "functionCall",
                                                "lValueRequested": false,
                                                "nameLocations": [],
                                                "names": [],
                                                "nodeType": "FunctionCall",
                                                "src": "768:49:8",
                                                "tryCall": false,
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_bool",
                                                    "typeString": "bool"
                                                }
                                            },
                                            "id": 933,
                                            "nodeType": "ExpressionStatement",
                                            "src": "768:49:8"
                                        }
                                    ]
                                },
                                "functionSelector": "fda7d818",
                                "implemented": true,
                                "kind": "function",
                                "modifiers": [],
                                "name": "secureTransferTo",
                                "nameLocation": "607:16:8",
                                "parameters": {
                                    "id": 923,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 920,
                                            "mutability": "mutable",
                                            "name": "recipient",
                                            "nameLocation": "632:9:8",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 935,
                                            "src": "624:17:8",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_address",
                                                "typeString": "address"
                                            },
                                            "typeName": {
                                                "id": 919,
                                                "name": "address",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "624:7:8",
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
                                            "id": 922,
                                            "mutability": "mutable",
                                            "name": "value",
                                            "nameLocation": "651:5:8",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 935,
                                            "src": "643:13:8",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_uint256",
                                                "typeString": "uint256"
                                            },
                                            "typeName": {
                                                "id": 921,
                                                "name": "uint256",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "643:7:8",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint256",
                                                    "typeString": "uint256"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "623:34:8"
                                },
                                "returnParameters": {
                                    "id": 924,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "665:0:8"
                                },
                                "scope": 936,
                                "stateMutability": "nonpayable",
                                "virtual": false,
                                "visibility": "public"
                            }
                        ],
                        "abstract": false,
                        "baseContracts": [],
                        "canonicalName": "InsecureTokenTransfer",
                        "contractDependencies": [],
                        "contractKind": "contract",
                        "fullyImplemented": true,
                        "linearizedBaseContracts": [
                            936
                        ],
                        "name": "InsecureTokenTransfer",
                        "nameLocation": "222:21:8",
                        "scope": 937,
                        "usedErrors": [],
                        "usedEvents": []
                    }
                ],
                "license": "MIT"
            }
        }
    }
}"""
    return json.loads(ast_json)


def test_unverified_from_address_in_transfer(vulnerable_ast):
    ast_json, src_paths = reduce_json(vulnerable_ast)
    results = process_yaml(
        "eburger/templates/unverified_from_address_in_transfer.yaml",
        ast_json,
        src_paths,
    )
    assert "Line 17 Columns 9-54" in results["results"][0]["lines"]
