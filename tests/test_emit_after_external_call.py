import json
import pytest
from eburger.serializer import reduce_json
from eburger.yaml_parser import process_yaml


@pytest.fixture
def vulnerable_ast() -> tuple[dict, list]:
    ast_json = """{
    "sources": {
        "vulnerable_contracts/emit_after_external_call.sol": {
            "AST": {
                "absolutePath": "vulnerable_contracts/emit_after_external_call.sol",
                "exportedSymbols": {
                    "MistakenContract": [
                        51
                    ],
                    "UnexpectedInteractorContract": [
                        81
                    ]
                },
                "id": 82,
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
                        "canonicalName": "MistakenContract",
                        "contractDependencies": [],
                        "contractKind": "contract",
                        "fullyImplemented": true,
                        "id": 51,
                        "linearizedBaseContracts": [
                            51
                        ],
                        "name": "MistakenContract",
                        "nameLocation": "66:16:0",
                        "nodeType": "ContractDefinition",
                        "nodes": [
                            {
                                "constant": false,
                                "functionSelector": "5556b0e9",
                                "id": 4,
                                "mutability": "mutable",
                                "name": "unexpectedInteractorContract",
                                "nameLocation": "125:28:0",
                                "nodeType": "VariableDeclaration",
                                "scope": 51,
                                "src": "89:64:0",
                                "stateVariable": true,
                                "storageLocation": "default",
                                "typeDescriptions": {
                                    "typeIdentifier": "t_contract$_UnexpectedInteractorContract_$81",
                                    "typeString": "contract UnexpectedInteractorContract"
                                },
                                "typeName": {
                                    "id": 3,
                                    "nodeType": "UserDefinedTypeName",
                                    "pathNode": {
                                        "id": 2,
                                        "name": "UnexpectedInteractorContract",
                                        "nameLocations": [
                                            "89:28:0"
                                        ],
                                        "nodeType": "IdentifierPath",
                                        "referencedDeclaration": 81,
                                        "src": "89:28:0"
                                    },
                                    "referencedDeclaration": 81,
                                    "src": "89:28:0",
                                    "typeDescriptions": {
                                        "typeIdentifier": "t_contract$_UnexpectedInteractorContract_$81",
                                        "typeString": "contract UnexpectedInteractorContract"
                                    }
                                },
                                "visibility": "public"
                            },
                            {
                                "constant": false,
                                "functionSelector": "b21ce425",
                                "id": 6,
                                "mutability": "mutable",
                                "name": "amountToTransfer",
                                "nameLocation": "211:16:0",
                                "nodeType": "VariableDeclaration",
                                "scope": 51,
                                "src": "196:31:0",
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
                                    "src": "196:7:0",
                                    "typeDescriptions": {
                                        "typeIdentifier": "t_uint256",
                                        "typeString": "uint256"
                                    }
                                },
                                "visibility": "public"
                            },
                            {
                                "anonymous": false,
                                "eventSelector": "248dd4076d0a389d795107efafd558ce7f31ae37b441ccb9a599c60868f480d5",
                                "id": 10,
                                "name": "Transfer",
                                "nameLocation": "302:8:0",
                                "nodeType": "EventDefinition",
                                "parameters": {
                                    "id": 9,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 8,
                                            "indexed": false,
                                            "mutability": "mutable",
                                            "name": "amount",
                                            "nameLocation": "319:6:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 10,
                                            "src": "311:14:0",
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
                                                "src": "311:7:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint256",
                                                    "typeString": "uint256"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "310:16:0"
                                },
                                "src": "296:31:0"
                            },
                            {
                                "body": {
                                    "id": 21,
                                    "nodeType": "Block",
                                    "src": "518:107:0",
                                    "statements": [
                                        {
                                            "expression": {
                                                "id": 19,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "lValueRequested": false,
                                                "leftHandSide": {
                                                    "id": 15,
                                                    "name": "unexpectedInteractorContract",
                                                    "nodeType": "Identifier",
                                                    "overloadedDeclarations": [],
                                                    "referencedDeclaration": 4,
                                                    "src": "528:28:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_contract$_UnexpectedInteractorContract_$81",
                                                        "typeString": "contract UnexpectedInteractorContract"
                                                    }
                                                },
                                                "nodeType": "Assignment",
                                                "operator": "=",
                                                "rightHandSide": {
                                                    "arguments": [
                                                        {
                                                            "id": 17,
                                                            "name": "_unexpectedInteractorContract",
                                                            "nodeType": "Identifier",
                                                            "overloadedDeclarations": [],
                                                            "referencedDeclaration": 12,
                                                            "src": "588:29:0",
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
                                                        "id": 16,
                                                        "name": "UnexpectedInteractorContract",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 81,
                                                        "src": "559:28:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_type$_t_contract$_UnexpectedInteractorContract_$81_$",
                                                            "typeString": "type(contract UnexpectedInteractorContract)"
                                                        }
                                                    },
                                                    "id": 18,
                                                    "isConstant": false,
                                                    "isLValue": false,
                                                    "isPure": false,
                                                    "kind": "typeConversion",
                                                    "lValueRequested": false,
                                                    "nameLocations": [],
                                                    "names": [],
                                                    "nodeType": "FunctionCall",
                                                    "src": "559:59:0",
                                                    "tryCall": false,
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_contract$_UnexpectedInteractorContract_$81",
                                                        "typeString": "contract UnexpectedInteractorContract"
                                                    }
                                                },
                                                "src": "528:90:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_contract$_UnexpectedInteractorContract_$81",
                                                    "typeString": "contract UnexpectedInteractorContract"
                                                }
                                            },
                                            "id": 20,
                                            "nodeType": "ExpressionStatement",
                                            "src": "528:90:0"
                                        }
                                    ]
                                },
                                "functionSelector": "5dc87337",
                                "id": 22,
                                "implemented": true,
                                "kind": "function",
                                "modifiers": [],
                                "name": "addOtherContract",
                                "nameLocation": "455:16:0",
                                "nodeType": "FunctionDefinition",
                                "parameters": {
                                    "id": 13,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 12,
                                            "mutability": "mutable",
                                            "name": "_unexpectedInteractorContract",
                                            "nameLocation": "480:29:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 22,
                                            "src": "472:37:0",
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
                                                "src": "472:7:0",
                                                "stateMutability": "nonpayable",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_address",
                                                    "typeString": "address"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "471:39:0"
                                },
                                "returnParameters": {
                                    "id": 14,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "518:0:0"
                                },
                                "scope": 51,
                                "src": "446:179:0",
                                "stateMutability": "nonpayable",
                                "virtual": false,
                                "visibility": "public"
                            },
                            {
                                "body": {
                                    "id": 31,
                                    "nodeType": "Block",
                                    "src": "815:45:0",
                                    "statements": [
                                        {
                                            "expression": {
                                                "id": 29,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "lValueRequested": false,
                                                "leftHandSide": {
                                                    "id": 27,
                                                    "name": "amountToTransfer",
                                                    "nodeType": "Identifier",
                                                    "overloadedDeclarations": [],
                                                    "referencedDeclaration": 6,
                                                    "src": "825:16:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_uint256",
                                                        "typeString": "uint256"
                                                    }
                                                },
                                                "nodeType": "Assignment",
                                                "operator": "=",
                                                "rightHandSide": {
                                                    "id": 28,
                                                    "name": "newAmount",
                                                    "nodeType": "Identifier",
                                                    "overloadedDeclarations": [],
                                                    "referencedDeclaration": 24,
                                                    "src": "844:9:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_uint256",
                                                        "typeString": "uint256"
                                                    }
                                                },
                                                "src": "825:28:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint256",
                                                    "typeString": "uint256"
                                                }
                                            },
                                            "id": 30,
                                            "nodeType": "ExpressionStatement",
                                            "src": "825:28:0"
                                        }
                                    ]
                                },
                                "functionSelector": "e8c42627",
                                "id": 32,
                                "implemented": true,
                                "kind": "function",
                                "modifiers": [],
                                "name": "updateAmountToTransfer",
                                "nameLocation": "766:22:0",
                                "nodeType": "FunctionDefinition",
                                "parameters": {
                                    "id": 25,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 24,
                                            "mutability": "mutable",
                                            "name": "newAmount",
                                            "nameLocation": "797:9:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 32,
                                            "src": "789:17:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_uint256",
                                                "typeString": "uint256"
                                            },
                                            "typeName": {
                                                "id": 23,
                                                "name": "uint256",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "789:7:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint256",
                                                    "typeString": "uint256"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "788:19:0"
                                },
                                "returnParameters": {
                                    "id": 26,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "815:0:0"
                                },
                                "scope": 51,
                                "src": "757:103:0",
                                "stateMutability": "nonpayable",
                                "virtual": false,
                                "visibility": "public"
                            },
                            {
                                "body": {
                                    "id": 49,
                                    "nodeType": "Block",
                                    "src": "1014:987:0",
                                    "statements": [
                                        {
                                            "expression": {
                                                "id": 38,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "lValueRequested": false,
                                                "leftHandSide": {
                                                    "id": 35,
                                                    "name": "amountToTransfer",
                                                    "nodeType": "Identifier",
                                                    "overloadedDeclarations": [],
                                                    "referencedDeclaration": 6,
                                                    "src": "1024:16:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_uint256",
                                                        "typeString": "uint256"
                                                    }
                                                },
                                                "nodeType": "Assignment",
                                                "operator": "=",
                                                "rightHandSide": {
                                                    "expression": {
                                                        "id": 36,
                                                        "name": "msg",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": -15,
                                                        "src": "1043:3:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_magic_message",
                                                            "typeString": "msg"
                                                        }
                                                    },
                                                    "id": 37,
                                                    "isConstant": false,
                                                    "isLValue": false,
                                                    "isPure": false,
                                                    "lValueRequested": false,
                                                    "memberLocation": "1047:5:0",
                                                    "memberName": "value",
                                                    "nodeType": "MemberAccess",
                                                    "src": "1043:9:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_uint256",
                                                        "typeString": "uint256"
                                                    }
                                                },
                                                "src": "1024:28:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint256",
                                                    "typeString": "uint256"
                                                }
                                            },
                                            "id": 39,
                                            "nodeType": "ExpressionStatement",
                                            "src": "1024:28:0"
                                        },
                                        {
                                            "expression": {
                                                "arguments": [],
                                                "expression": {
                                                    "argumentTypes": [],
                                                    "expression": {
                                                        "id": 40,
                                                        "name": "unexpectedInteractorContract",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 4,
                                                        "src": "1492:28:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_contract$_UnexpectedInteractorContract_$81",
                                                            "typeString": "contract UnexpectedInteractorContract"
                                                        }
                                                    },
                                                    "id": 42,
                                                    "isConstant": false,
                                                    "isLValue": false,
                                                    "isPure": false,
                                                    "lValueRequested": false,
                                                    "memberLocation": "1521:8:0",
                                                    "memberName": "doChores",
                                                    "nodeType": "MemberAccess",
                                                    "referencedDeclaration": 80,
                                                    "src": "1492:37:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_function_external_payable$__$returns$__$",
                                                        "typeString": "function () payable external"
                                                    }
                                                },
                                                "id": 43,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "kind": "functionCall",
                                                "lValueRequested": false,
                                                "nameLocations": [],
                                                "names": [],
                                                "nodeType": "FunctionCall",
                                                "src": "1492:39:0",
                                                "tryCall": false,
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_tuple$__$",
                                                    "typeString": "tuple()"
                                                }
                                            },
                                            "id": 44,
                                            "nodeType": "ExpressionStatement",
                                            "src": "1492:39:0"
                                        },
                                        {
                                            "eventCall": {
                                                "arguments": [
                                                    {
                                                        "id": 46,
                                                        "name": "amountToTransfer",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 6,
                                                        "src": "1976:16:0",
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
                                                    "id": 45,
                                                    "name": "Transfer",
                                                    "nodeType": "Identifier",
                                                    "overloadedDeclarations": [],
                                                    "referencedDeclaration": 10,
                                                    "src": "1967:8:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_function_event_nonpayable$_t_uint256_$returns$__$",
                                                        "typeString": "function (uint256)"
                                                    }
                                                },
                                                "id": 47,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "kind": "functionCall",
                                                "lValueRequested": false,
                                                "nameLocations": [],
                                                "names": [],
                                                "nodeType": "FunctionCall",
                                                "src": "1967:26:0",
                                                "tryCall": false,
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_tuple$__$",
                                                    "typeString": "tuple()"
                                                }
                                            },
                                            "id": 48,
                                            "nodeType": "EmitStatement",
                                            "src": "1962:31:0"
                                        }
                                    ]
                                },
                                "functionSelector": "d3174c3a",
                                "id": 50,
                                "implemented": true,
                                "kind": "function",
                                "modifiers": [],
                                "name": "transferMoneyFromBridge",
                                "nameLocation": "973:23:0",
                                "nodeType": "FunctionDefinition",
                                "parameters": {
                                    "id": 33,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "996:2:0"
                                },
                                "returnParameters": {
                                    "id": 34,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "1014:0:0"
                                },
                                "scope": 51,
                                "src": "964:1037:0",
                                "stateMutability": "payable",
                                "virtual": false,
                                "visibility": "public"
                            }
                        ],
                        "scope": 82,
                        "src": "57:1946:0",
                        "usedErrors": [],
                        "usedEvents": [
                            10
                        ]
                    },
                    {
                        "abstract": false,
                        "baseContracts": [],
                        "canonicalName": "UnexpectedInteractorContract",
                        "contractDependencies": [],
                        "contractKind": "contract",
                        "fullyImplemented": true,
                        "id": 81,
                        "linearizedBaseContracts": [
                            81
                        ],
                        "name": "UnexpectedInteractorContract",
                        "nameLocation": "2085:28:0",
                        "nodeType": "ContractDefinition",
                        "nodes": [
                            {
                                "constant": false,
                                "functionSelector": "66af70b8",
                                "id": 54,
                                "mutability": "mutable",
                                "name": "mistakenContract",
                                "nameLocation": "2144:16:0",
                                "nodeType": "VariableDeclaration",
                                "scope": 81,
                                "src": "2120:40:0",
                                "stateVariable": true,
                                "storageLocation": "default",
                                "typeDescriptions": {
                                    "typeIdentifier": "t_contract$_MistakenContract_$51",
                                    "typeString": "contract MistakenContract"
                                },
                                "typeName": {
                                    "id": 53,
                                    "nodeType": "UserDefinedTypeName",
                                    "pathNode": {
                                        "id": 52,
                                        "name": "MistakenContract",
                                        "nameLocations": [
                                            "2120:16:0"
                                        ],
                                        "nodeType": "IdentifierPath",
                                        "referencedDeclaration": 51,
                                        "src": "2120:16:0"
                                    },
                                    "referencedDeclaration": 51,
                                    "src": "2120:16:0",
                                    "typeDescriptions": {
                                        "typeIdentifier": "t_contract$_MistakenContract_$51",
                                        "typeString": "contract MistakenContract"
                                    }
                                },
                                "visibility": "public"
                            },
                            {
                                "body": {
                                    "id": 65,
                                    "nodeType": "Block",
                                    "src": "2206:71:0",
                                    "statements": [
                                        {
                                            "expression": {
                                                "id": 63,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "lValueRequested": false,
                                                "leftHandSide": {
                                                    "id": 59,
                                                    "name": "mistakenContract",
                                                    "nodeType": "Identifier",
                                                    "overloadedDeclarations": [],
                                                    "referencedDeclaration": 54,
                                                    "src": "2216:16:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_contract$_MistakenContract_$51",
                                                        "typeString": "contract MistakenContract"
                                                    }
                                                },
                                                "nodeType": "Assignment",
                                                "operator": "=",
                                                "rightHandSide": {
                                                    "arguments": [
                                                        {
                                                            "id": 61,
                                                            "name": "_mistakenContract",
                                                            "nodeType": "Identifier",
                                                            "overloadedDeclarations": [],
                                                            "referencedDeclaration": 56,
                                                            "src": "2252:17:0",
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
                                                        "id": 60,
                                                        "name": "MistakenContract",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 51,
                                                        "src": "2235:16:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_type$_t_contract$_MistakenContract_$51_$",
                                                            "typeString": "type(contract MistakenContract)"
                                                        }
                                                    },
                                                    "id": 62,
                                                    "isConstant": false,
                                                    "isLValue": false,
                                                    "isPure": false,
                                                    "kind": "typeConversion",
                                                    "lValueRequested": false,
                                                    "nameLocations": [],
                                                    "names": [],
                                                    "nodeType": "FunctionCall",
                                                    "src": "2235:35:0",
                                                    "tryCall": false,
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_contract$_MistakenContract_$51",
                                                        "typeString": "contract MistakenContract"
                                                    }
                                                },
                                                "src": "2216:54:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_contract$_MistakenContract_$51",
                                                    "typeString": "contract MistakenContract"
                                                }
                                            },
                                            "id": 64,
                                            "nodeType": "ExpressionStatement",
                                            "src": "2216:54:0"
                                        }
                                    ]
                                },
                                "id": 66,
                                "implemented": true,
                                "kind": "constructor",
                                "modifiers": [],
                                "name": "",
                                "nameLocation": "-1:-1:-1",
                                "nodeType": "FunctionDefinition",
                                "parameters": {
                                    "id": 57,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 56,
                                            "mutability": "mutable",
                                            "name": "_mistakenContract",
                                            "nameLocation": "2187:17:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 66,
                                            "src": "2179:25:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_address",
                                                "typeString": "address"
                                            },
                                            "typeName": {
                                                "id": 55,
                                                "name": "address",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "2179:7:0",
                                                "stateMutability": "nonpayable",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_address",
                                                    "typeString": "address"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "2178:27:0"
                                },
                                "returnParameters": {
                                    "id": 58,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "2206:0:0"
                                },
                                "scope": 81,
                                "src": "2167:110:0",
                                "stateMutability": "nonpayable",
                                "virtual": false,
                                "visibility": "public"
                            },
                            {
                                "body": {
                                    "id": 79,
                                    "nodeType": "Block",
                                    "src": "2318:172:0",
                                    "statements": [
                                        {
                                            "expression": {
                                                "arguments": [
                                                    {
                                                        "expression": {
                                                            "arguments": [
                                                                {
                                                                    "id": 74,
                                                                    "isConstant": false,
                                                                    "isLValue": false,
                                                                    "isPure": true,
                                                                    "lValueRequested": false,
                                                                    "nodeType": "ElementaryTypeNameExpression",
                                                                    "src": "2455:7:0",
                                                                    "typeDescriptions": {
                                                                        "typeIdentifier": "t_type$_t_uint256_$",
                                                                        "typeString": "type(uint256)"
                                                                    },
                                                                    "typeName": {
                                                                        "id": 73,
                                                                        "name": "uint256",
                                                                        "nodeType": "ElementaryTypeName",
                                                                        "src": "2455:7:0",
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
                                                                "id": 72,
                                                                "name": "type",
                                                                "nodeType": "Identifier",
                                                                "overloadedDeclarations": [],
                                                                "referencedDeclaration": -27,
                                                                "src": "2450:4:0",
                                                                "typeDescriptions": {
                                                                    "typeIdentifier": "t_function_metatype_pure$__$returns$__$",
                                                                    "typeString": "function () pure"
                                                                }
                                                            },
                                                            "id": 75,
                                                            "isConstant": false,
                                                            "isLValue": false,
                                                            "isPure": true,
                                                            "kind": "functionCall",
                                                            "lValueRequested": false,
                                                            "nameLocations": [],
                                                            "names": [],
                                                            "nodeType": "FunctionCall",
                                                            "src": "2450:13:0",
                                                            "tryCall": false,
                                                            "typeDescriptions": {
                                                                "typeIdentifier": "t_magic_meta_type_t_uint256",
                                                                "typeString": "type(uint256)"
                                                            }
                                                        },
                                                        "id": 76,
                                                        "isConstant": false,
                                                        "isLValue": false,
                                                        "isPure": true,
                                                        "lValueRequested": false,
                                                        "memberLocation": "2464:3:0",
                                                        "memberName": "max",
                                                        "nodeType": "MemberAccess",
                                                        "src": "2450:17:0",
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
                                                        "id": 69,
                                                        "name": "mistakenContract",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 54,
                                                        "src": "2410:16:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_contract$_MistakenContract_$51",
                                                            "typeString": "contract MistakenContract"
                                                        }
                                                    },
                                                    "id": 71,
                                                    "isConstant": false,
                                                    "isLValue": false,
                                                    "isPure": false,
                                                    "lValueRequested": false,
                                                    "memberLocation": "2427:22:0",
                                                    "memberName": "updateAmountToTransfer",
                                                    "nodeType": "MemberAccess",
                                                    "referencedDeclaration": 32,
                                                    "src": "2410:39:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_function_external_nonpayable$_t_uint256_$returns$__$",
                                                        "typeString": "function (uint256) external"
                                                    }
                                                },
                                                "id": 77,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "kind": "functionCall",
                                                "lValueRequested": false,
                                                "nameLocations": [],
                                                "names": [],
                                                "nodeType": "FunctionCall",
                                                "src": "2410:58:0",
                                                "tryCall": false,
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_tuple$__$",
                                                    "typeString": "tuple()"
                                                }
                                            },
                                            "id": 78,
                                            "nodeType": "ExpressionStatement",
                                            "src": "2410:58:0"
                                        }
                                    ]
                                },
                                "functionSelector": "03b4aa7f",
                                "id": 80,
                                "implemented": true,
                                "kind": "function",
                                "modifiers": [],
                                "name": "doChores",
                                "nameLocation": "2292:8:0",
                                "nodeType": "FunctionDefinition",
                                "parameters": {
                                    "id": 67,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "2300:2:0"
                                },
                                "returnParameters": {
                                    "id": 68,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "2318:0:0"
                                },
                                "scope": 81,
                                "src": "2283:207:0",
                                "stateMutability": "payable",
                                "virtual": false,
                                "visibility": "public"
                            }
                        ],
                        "scope": 82,
                        "src": "2076:416:0",
                        "usedErrors": [],
                        "usedEvents": []
                    }
                ],
                "src": "32:2461:0"
            },
            "id": 0
        }
    }
}"""
    return json.loads(ast_json)


def test_emit_after_external_call(vulnerable_ast):
    ast_json, src_paths = reduce_json(vulnerable_ast)
    results = process_yaml(
        "eburger/templates/emit_after_external_call.yaml",
        ast_json,
        src_paths,
    )
    assert "Line 40 Columns 9-40" in results["results"][0]["lines"]
