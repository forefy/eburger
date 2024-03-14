import json
import pytest
from eburger.serializer import reduce_json
from eburger.yaml_parser import process_yaml


@pytest.fixture
def vulnerable_ast() -> tuple[dict, list]:
    ast_json = """{
    "sources": {
        "vulnerable_contracts/use_of_safetransferlib/src/use_of_safetransferlib.sol": {
            "id": 2,
            "ast": {
                "absolutePath": "vulnerable_contracts/use_of_safetransferlib/src/use_of_safetransferlib.sol",
                "id": 501,
                "exportedSymbols": {
                    "ERC20": [
                        387
                    ],
                    "NotSoSafe": [
                        500
                    ],
                    "SafeTransferLib": [
                        472
                    ]
                },
                "nodeType": "SourceUnit",
                "src": "32:296:2",
                "nodes": [
                    {
                        "id": 474,
                        "nodeType": "PragmaDirective",
                        "src": "32:23:2",
                        "nodes": [],
                        "literals": [
                            "solidity",
                            "0.8",
                            ".20"
                        ]
                    },
                    {
                        "id": 477,
                        "nodeType": "ImportDirective",
                        "src": "56:84:2",
                        "nodes": [],
                        "absolutePath": "lib/solmate/src/utils/SafeTransferLib.sol",
                        "file": "../lib/solmate/src/utils/SafeTransferLib.sol",
                        "nameLocation": "-1:-1:-1",
                        "scope": 501,
                        "sourceUnit": 473,
                        "symbolAliases": [
                            {
                                "foreign": {
                                    "id": 475,
                                    "name": "ERC20",
                                    "nodeType": "Identifier",
                                    "overloadedDeclarations": [],
                                    "referencedDeclaration": 387,
                                    "src": "64:5:2",
                                    "typeDescriptions": {}
                                },
                                "nameLocation": "-1:-1:-1"
                            },
                            {
                                "foreign": {
                                    "id": 476,
                                    "name": "SafeTransferLib",
                                    "nodeType": "Identifier",
                                    "overloadedDeclarations": [],
                                    "referencedDeclaration": 472,
                                    "src": "71:15:2",
                                    "typeDescriptions": {}
                                },
                                "nameLocation": "-1:-1:-1"
                            }
                        ],
                        "unitAlias": ""
                    },
                    {
                        "id": 500,
                        "nodeType": "ContractDefinition",
                        "src": "142:186:2",
                        "nodes": [
                            {
                                "id": 481,
                                "nodeType": "UsingForDirective",
                                "src": "167:32:2",
                                "nodes": [],
                                "global": false,
                                "libraryName": {
                                    "id": 478,
                                    "name": "SafeTransferLib",
                                    "nameLocations": [
                                        "173:15:2"
                                    ],
                                    "nodeType": "IdentifierPath",
                                    "referencedDeclaration": 472,
                                    "src": "173:15:2"
                                },
                                "typeName": {
                                    "id": 480,
                                    "nodeType": "UserDefinedTypeName",
                                    "pathNode": {
                                        "id": 479,
                                        "name": "ERC20",
                                        "nameLocations": [
                                            "193:5:2"
                                        ],
                                        "nodeType": "IdentifierPath",
                                        "referencedDeclaration": 387,
                                        "src": "193:5:2"
                                    },
                                    "referencedDeclaration": 387,
                                    "src": "193:5:2",
                                    "typeDescriptions": {
                                        "typeIdentifier": "t_contract$_ERC20_$387",
                                        "typeString": "contract ERC20"
                                    }
                                }
                            },
                            {
                                "id": 499,
                                "nodeType": "FunctionDefinition",
                                "src": "205:121:2",
                                "nodes": [],
                                "body": {
                                    "id": 498,
                                    "nodeType": "Block",
                                    "src": "279:47:2",
                                    "nodes": [],
                                    "statements": [
                                        {
                                            "expression": {
                                                "arguments": [
                                                    {
                                                        "id": 494,
                                                        "name": "to",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 486,
                                                        "src": "308:2:2",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_address",
                                                            "typeString": "address"
                                                        }
                                                    },
                                                    {
                                                        "id": 495,
                                                        "name": "amount",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 488,
                                                        "src": "312:6:2",
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
                                                        "id": 491,
                                                        "name": "token",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 484,
                                                        "src": "289:5:2",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_contract$_ERC20_$387",
                                                            "typeString": "contract ERC20"
                                                        }
                                                    },
                                                    "id": 493,
                                                    "isConstant": false,
                                                    "isLValue": false,
                                                    "isPure": false,
                                                    "lValueRequested": false,
                                                    "memberLocation": "295:12:2",
                                                    "memberName": "safeTransfer",
                                                    "nodeType": "MemberAccess",
                                                    "referencedDeclaration": 451,
                                                    "src": "289:18:2",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_function_internal_nonpayable$_t_contract$_ERC20_$387_$_t_address_$_t_uint256_$returns$__$attached_to$_t_contract$_ERC20_$387_$",
                                                        "typeString": "function (contract ERC20,address,uint256)"
                                                    }
                                                },
                                                "id": 496,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "kind": "functionCall",
                                                "lValueRequested": false,
                                                "nameLocations": [],
                                                "names": [],
                                                "nodeType": "FunctionCall",
                                                "src": "289:30:2",
                                                "tryCall": false,
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_tuple$__$",
                                                    "typeString": "tuple()"
                                                }
                                            },
                                            "id": 497,
                                            "nodeType": "ExpressionStatement",
                                            "src": "289:30:2"
                                        }
                                    ]
                                },
                                "functionSelector": "328373f0",
                                "implemented": true,
                                "kind": "function",
                                "modifiers": [],
                                "name": "sendSomeTokens",
                                "nameLocation": "214:14:2",
                                "parameters": {
                                    "id": 489,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 484,
                                            "mutability": "mutable",
                                            "name": "token",
                                            "nameLocation": "235:5:2",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 499,
                                            "src": "229:11:2",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_contract$_ERC20_$387",
                                                "typeString": "contract ERC20"
                                            },
                                            "typeName": {
                                                "id": 483,
                                                "nodeType": "UserDefinedTypeName",
                                                "pathNode": {
                                                    "id": 482,
                                                    "name": "ERC20",
                                                    "nameLocations": [
                                                        "229:5:2"
                                                    ],
                                                    "nodeType": "IdentifierPath",
                                                    "referencedDeclaration": 387,
                                                    "src": "229:5:2"
                                                },
                                                "referencedDeclaration": 387,
                                                "src": "229:5:2",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_contract$_ERC20_$387",
                                                    "typeString": "contract ERC20"
                                                }
                                            },
                                            "visibility": "internal"
                                        },
                                        {
                                            "constant": false,
                                            "id": 486,
                                            "mutability": "mutable",
                                            "name": "to",
                                            "nameLocation": "250:2:2",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 499,
                                            "src": "242:10:2",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_address",
                                                "typeString": "address"
                                            },
                                            "typeName": {
                                                "id": 485,
                                                "name": "address",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "242:7:2",
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
                                            "id": 488,
                                            "mutability": "mutable",
                                            "name": "amount",
                                            "nameLocation": "262:6:2",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 499,
                                            "src": "254:14:2",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_uint256",
                                                "typeString": "uint256"
                                            },
                                            "typeName": {
                                                "id": 487,
                                                "name": "uint256",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "254:7:2",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint256",
                                                    "typeString": "uint256"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "228:41:2"
                                },
                                "returnParameters": {
                                    "id": 490,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "279:0:2"
                                },
                                "scope": 500,
                                "stateMutability": "nonpayable",
                                "virtual": false,
                                "visibility": "external"
                            }
                        ],
                        "abstract": false,
                        "baseContracts": [],
                        "canonicalName": "NotSoSafe",
                        "contractDependencies": [],
                        "contractKind": "contract",
                        "fullyImplemented": true,
                        "linearizedBaseContracts": [
                            500
                        ],
                        "name": "NotSoSafe",
                        "nameLocation": "151:9:2",
                        "scope": 501,
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


def test_use_of_safetransferlib(vulnerable_ast):
    ast_json, src_paths = reduce_json(vulnerable_ast)
    results = process_yaml(
        "eburger/templates/use_of_safetransferlib.yaml",
        ast_json,
        src_paths,
    )
    assert "Line 3 Columns 1-85" in results["results"][0]["lines"]
