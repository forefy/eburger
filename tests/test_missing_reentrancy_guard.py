import json
import pytest
from eburger.serializer import reduce_json
from eburger.yaml_parser import process_yaml


@pytest.fixture
def vulnerable_ast() -> tuple[dict, list]:
    ast_json = """{
    "sources": {
        "script/Attacker.sol": {
            "id": 0,
            "ast": {
                "absolutePath": "script/Attacker.sol",
                "id": 54,
                "exportedSymbols": {
                    "Attacker": [
                        53
                    ],
                    "ProblematicContract": [
                        120
                    ]
                },
                "nodeType": "SourceUnit",
                "src": "32:588:0",
                "nodes": [
                    {
                        "id": 1,
                        "nodeType": "PragmaDirective",
                        "src": "32:23:0",
                        "nodes": [],
                        "literals": [
                            "solidity",
                            "0.8",
                            ".20"
                        ]
                    },
                    {
                        "id": 2,
                        "nodeType": "ImportDirective",
                        "src": "57:45:0",
                        "nodes": [],
                        "absolutePath": "vulnerable_contracts/missing_reentrancy_guard/src/missing_reentrancy_guard.sol",
                        "file": "../vulnerable_contracts/missing_reentrancy_guard/src/missing_reentrancy_guard.sol",
                        "nameLocation": "-1:-1:-1",
                        "scope": 54,
                        "sourceUnit": 121,
                        "symbolAliases": [],
                        "unitAlias": ""
                    },
                    {
                        "id": 53,
                        "nodeType": "ContractDefinition",
                        "src": "104:515:0",
                        "nodes": [
                            {
                                "id": 5,
                                "nodeType": "VariableDeclaration",
                                "src": "128:47:0",
                                "nodes": [],
                                "constant": false,
                                "functionSelector": "46142dfd",
                                "mutability": "mutable",
                                "name": "problematic_contract",
                                "nameLocation": "155:20:0",
                                "scope": 53,
                                "stateVariable": true,
                                "storageLocation": "default",
                                "typeDescriptions": {
                                    "typeIdentifier": "t_contract$_ProblematicContract_$120",
                                    "typeString": "contract ProblematicContract"
                                },
                                "typeName": {
                                    "id": 4,
                                    "nodeType": "UserDefinedTypeName",
                                    "pathNode": {
                                        "id": 3,
                                        "name": "ProblematicContract",
                                        "nameLocations": [
                                            "128:19:0"
                                        ],
                                        "nodeType": "IdentifierPath",
                                        "referencedDeclaration": 120,
                                        "src": "128:19:0"
                                    },
                                    "referencedDeclaration": 120,
                                    "src": "128:19:0",
                                    "typeDescriptions": {
                                        "typeIdentifier": "t_contract$_ProblematicContract_$120",
                                        "typeString": "contract ProblematicContract"
                                    }
                                },
                                "visibility": "public"
                            },
                            {
                                "id": 17,
                                "nodeType": "FunctionDefinition",
                                "src": "182:125:0",
                                "nodes": [],
                                "body": {
                                    "id": 16,
                                    "nodeType": "Block",
                                    "src": "225:82:0",
                                    "nodes": [],
                                    "statements": [
                                        {
                                            "expression": {
                                                "id": 14,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "lValueRequested": false,
                                                "leftHandSide": {
                                                    "id": 10,
                                                    "name": "problematic_contract",
                                                    "nodeType": "Identifier",
                                                    "overloadedDeclarations": [],
                                                    "referencedDeclaration": 5,
                                                    "src": "235:20:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_contract$_ProblematicContract_$120",
                                                        "typeString": "contract ProblematicContract"
                                                    }
                                                },
                                                "nodeType": "Assignment",
                                                "operator": "=",
                                                "rightHandSide": {
                                                    "arguments": [
                                                        {
                                                            "id": 12,
                                                            "name": "_problematic_contract",
                                                            "nodeType": "Identifier",
                                                            "overloadedDeclarations": [],
                                                            "referencedDeclaration": 7,
                                                            "src": "278:21:0",
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
                                                        "id": 11,
                                                        "name": "ProblematicContract",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 120,
                                                        "src": "258:19:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_type$_t_contract$_ProblematicContract_$120_$",
                                                            "typeString": "type(contract ProblematicContract)"
                                                        }
                                                    },
                                                    "id": 13,
                                                    "isConstant": false,
                                                    "isLValue": false,
                                                    "isPure": false,
                                                    "kind": "typeConversion",
                                                    "lValueRequested": false,
                                                    "nameLocations": [],
                                                    "names": [],
                                                    "nodeType": "FunctionCall",
                                                    "src": "258:42:0",
                                                    "tryCall": false,
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_contract$_ProblematicContract_$120",
                                                        "typeString": "contract ProblematicContract"
                                                    }
                                                },
                                                "src": "235:65:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_contract$_ProblematicContract_$120",
                                                    "typeString": "contract ProblematicContract"
                                                }
                                            },
                                            "id": 15,
                                            "nodeType": "ExpressionStatement",
                                            "src": "235:65:0"
                                        }
                                    ]
                                },
                                "implemented": true,
                                "kind": "constructor",
                                "modifiers": [],
                                "name": "",
                                "nameLocation": "-1:-1:-1",
                                "parameters": {
                                    "id": 8,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 7,
                                            "mutability": "mutable",
                                            "name": "_problematic_contract",
                                            "nameLocation": "202:21:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 17,
                                            "src": "194:29:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_address",
                                                "typeString": "address"
                                            },
                                            "typeName": {
                                                "id": 6,
                                                "name": "address",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "194:7:0",
                                                "stateMutability": "nonpayable",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_address",
                                                    "typeString": "address"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "193:31:0"
                                },
                                "returnParameters": {
                                    "id": 9,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "225:0:0"
                                },
                                "scope": 53,
                                "stateMutability": "nonpayable",
                                "virtual": false,
                                "visibility": "public"
                            },
                            {
                                "id": 34,
                                "nodeType": "FunctionDefinition",
                                "src": "313:141:0",
                                "nodes": [],
                                "body": {
                                    "id": 33,
                                    "nodeType": "Block",
                                    "src": "348:106:0",
                                    "nodes": [],
                                    "statements": [
                                        {
                                            "expression": {
                                                "arguments": [],
                                                "expression": {
                                                    "argumentTypes": [],
                                                    "expression": {
                                                        "argumentTypes": [],
                                                        "expression": {
                                                            "id": 20,
                                                            "name": "problematic_contract",
                                                            "nodeType": "Identifier",
                                                            "overloadedDeclarations": [],
                                                            "referencedDeclaration": 5,
                                                            "src": "358:20:0",
                                                            "typeDescriptions": {
                                                                "typeIdentifier": "t_contract$_ProblematicContract_$120",
                                                                "typeString": "contract ProblematicContract"
                                                            }
                                                        },
                                                        "id": 22,
                                                        "isConstant": false,
                                                        "isLValue": false,
                                                        "isPure": false,
                                                        "lValueRequested": false,
                                                        "memberLocation": "379:7:0",
                                                        "memberName": "deposit",
                                                        "nodeType": "MemberAccess",
                                                        "referencedDeclaration": 79,
                                                        "src": "358:28:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_function_external_payable$__$returns$__$",
                                                            "typeString": "function () payable external"
                                                        }
                                                    },
                                                    "id": 25,
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
                                                            "expression": {
                                                                "id": 23,
                                                                "name": "msg",
                                                                "nodeType": "Identifier",
                                                                "overloadedDeclarations": [],
                                                                "referencedDeclaration": -15,
                                                                "src": "394:3:0",
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
                                                            "memberLocation": "398:5:0",
                                                            "memberName": "value",
                                                            "nodeType": "MemberAccess",
                                                            "src": "394:9:0",
                                                            "typeDescriptions": {
                                                                "typeIdentifier": "t_uint256",
                                                                "typeString": "uint256"
                                                            }
                                                        }
                                                    ],
                                                    "src": "358:46:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_function_external_payable$__$returns$__$value",
                                                        "typeString": "function () payable external"
                                                    }
                                                },
                                                "id": 26,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "kind": "functionCall",
                                                "lValueRequested": false,
                                                "nameLocations": [],
                                                "names": [],
                                                "nodeType": "FunctionCall",
                                                "src": "358:48:0",
                                                "tryCall": false,
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_tuple$__$",
                                                    "typeString": "tuple()"
                                                }
                                            },
                                            "id": 27,
                                            "nodeType": "ExpressionStatement",
                                            "src": "358:48:0"
                                        },
                                        {
                                            "expression": {
                                                "arguments": [],
                                                "expression": {
                                                    "argumentTypes": [],
                                                    "expression": {
                                                        "id": 28,
                                                        "name": "problematic_contract",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 5,
                                                        "src": "416:20:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_contract$_ProblematicContract_$120",
                                                            "typeString": "contract ProblematicContract"
                                                        }
                                                    },
                                                    "id": 30,
                                                    "isConstant": false,
                                                    "isLValue": false,
                                                    "isPure": false,
                                                    "lValueRequested": false,
                                                    "memberLocation": "437:8:0",
                                                    "memberName": "withdraw",
                                                    "nodeType": "MemberAccess",
                                                    "referencedDeclaration": 119,
                                                    "src": "416:29:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_function_external_nonpayable$__$returns$__$",
                                                        "typeString": "function () external"
                                                    }
                                                },
                                                "id": 31,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "kind": "functionCall",
                                                "lValueRequested": false,
                                                "nameLocations": [],
                                                "names": [],
                                                "nodeType": "FunctionCall",
                                                "src": "416:31:0",
                                                "tryCall": false,
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_tuple$__$",
                                                    "typeString": "tuple()"
                                                }
                                            },
                                            "id": 32,
                                            "nodeType": "ExpressionStatement",
                                            "src": "416:31:0"
                                        }
                                    ]
                                },
                                "functionSelector": "9e5faafc",
                                "implemented": true,
                                "kind": "function",
                                "modifiers": [],
                                "name": "attack",
                                "nameLocation": "322:6:0",
                                "parameters": {
                                    "id": 18,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "328:2:0"
                                },
                                "returnParameters": {
                                    "id": 19,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "348:0:0"
                                },
                                "scope": 53,
                                "stateMutability": "payable",
                                "virtual": false,
                                "visibility": "external"
                            },
                            {
                                "id": 52,
                                "nodeType": "FunctionDefinition",
                                "src": "464:153:0",
                                "nodes": [],
                                "body": {
                                    "id": 51,
                                    "nodeType": "Block",
                                    "src": "491:126:0",
                                    "nodes": [],
                                    "statements": [
                                        {
                                            "condition": {
                                                "commonType": {
                                                    "typeIdentifier": "t_uint256",
                                                    "typeString": "uint256"
                                                },
                                                "id": 43,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "lValueRequested": false,
                                                "leftExpression": {
                                                    "expression": {
                                                        "arguments": [
                                                            {
                                                                "id": 39,
                                                                "name": "problematic_contract",
                                                                "nodeType": "Identifier",
                                                                "overloadedDeclarations": [],
                                                                "referencedDeclaration": 5,
                                                                "src": "513:20:0",
                                                                "typeDescriptions": {
                                                                    "typeIdentifier": "t_contract$_ProblematicContract_$120",
                                                                    "typeString": "contract ProblematicContract"
                                                                }
                                                            }
                                                        ],
                                                        "expression": {
                                                            "argumentTypes": [
                                                                {
                                                                    "typeIdentifier": "t_contract$_ProblematicContract_$120",
                                                                    "typeString": "contract ProblematicContract"
                                                                }
                                                            ],
                                                            "id": 38,
                                                            "isConstant": false,
                                                            "isLValue": false,
                                                            "isPure": true,
                                                            "lValueRequested": false,
                                                            "nodeType": "ElementaryTypeNameExpression",
                                                            "src": "505:7:0",
                                                            "typeDescriptions": {
                                                                "typeIdentifier": "t_type$_t_address_$",
                                                                "typeString": "type(address)"
                                                            },
                                                            "typeName": {
                                                                "id": 37,
                                                                "name": "address",
                                                                "nodeType": "ElementaryTypeName",
                                                                "src": "505:7:0",
                                                                "typeDescriptions": {}
                                                            }
                                                        },
                                                        "id": 40,
                                                        "isConstant": false,
                                                        "isLValue": false,
                                                        "isPure": false,
                                                        "kind": "typeConversion",
                                                        "lValueRequested": false,
                                                        "nameLocations": [],
                                                        "names": [],
                                                        "nodeType": "FunctionCall",
                                                        "src": "505:29:0",
                                                        "tryCall": false,
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_address",
                                                            "typeString": "address"
                                                        }
                                                    },
                                                    "id": 41,
                                                    "isConstant": false,
                                                    "isLValue": false,
                                                    "isPure": false,
                                                    "lValueRequested": false,
                                                    "memberLocation": "535:7:0",
                                                    "memberName": "balance",
                                                    "nodeType": "MemberAccess",
                                                    "src": "505:37:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_uint256",
                                                        "typeString": "uint256"
                                                    }
                                                },
                                                "nodeType": "BinaryOperation",
                                                "operator": ">=",
                                                "rightExpression": {
                                                    "hexValue": "31",
                                                    "id": 42,
                                                    "isConstant": false,
                                                    "isLValue": false,
                                                    "isPure": true,
                                                    "kind": "number",
                                                    "lValueRequested": false,
                                                    "nodeType": "Literal",
                                                    "src": "546:7:0",
                                                    "subdenomination": "ether",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_rational_1000000000000000000_by_1",
                                                        "typeString": "int_const 1000000000000000000"
                                                    },
                                                    "value": "1"
                                                },
                                                "src": "505:48:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_bool",
                                                    "typeString": "bool"
                                                }
                                            },
                                            "id": 50,
                                            "nodeType": "IfStatement",
                                            "src": "501:110:0",
                                            "trueBody": {
                                                "id": 49,
                                                "nodeType": "Block",
                                                "src": "555:56:0",
                                                "statements": [
                                                    {
                                                        "expression": {
                                                            "arguments": [],
                                                            "expression": {
                                                                "argumentTypes": [],
                                                                "expression": {
                                                                    "id": 44,
                                                                    "name": "problematic_contract",
                                                                    "nodeType": "Identifier",
                                                                    "overloadedDeclarations": [],
                                                                    "referencedDeclaration": 5,
                                                                    "src": "569:20:0",
                                                                    "typeDescriptions": {
                                                                        "typeIdentifier": "t_contract$_ProblematicContract_$120",
                                                                        "typeString": "contract ProblematicContract"
                                                                    }
                                                                },
                                                                "id": 46,
                                                                "isConstant": false,
                                                                "isLValue": false,
                                                                "isPure": false,
                                                                "lValueRequested": false,
                                                                "memberLocation": "590:8:0",
                                                                "memberName": "withdraw",
                                                                "nodeType": "MemberAccess",
                                                                "referencedDeclaration": 119,
                                                                "src": "569:29:0",
                                                                "typeDescriptions": {
                                                                    "typeIdentifier": "t_function_external_nonpayable$__$returns$__$",
                                                                    "typeString": "function () external"
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
                                                            "src": "569:31:0",
                                                            "tryCall": false,
                                                            "typeDescriptions": {
                                                                "typeIdentifier": "t_tuple$__$",
                                                                "typeString": "tuple()"
                                                            }
                                                        },
                                                        "id": 48,
                                                        "nodeType": "ExpressionStatement",
                                                        "src": "569:31:0"
                                                    }
                                                ]
                                            }
                                        }
                                    ]
                                },
                                "implemented": true,
                                "kind": "receive",
                                "modifiers": [],
                                "name": "",
                                "nameLocation": "-1:-1:-1",
                                "parameters": {
                                    "id": 35,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "471:2:0"
                                },
                                "returnParameters": {
                                    "id": 36,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "491:0:0"
                                },
                                "scope": 53,
                                "stateMutability": "payable",
                                "virtual": false,
                                "visibility": "external"
                            }
                        ],
                        "abstract": false,
                        "baseContracts": [],
                        "canonicalName": "Attacker",
                        "contractDependencies": [],
                        "contractKind": "contract",
                        "fullyImplemented": true,
                        "linearizedBaseContracts": [
                            53
                        ],
                        "name": "Attacker",
                        "nameLocation": "113:8:0",
                        "scope": 54,
                        "usedErrors": [],
                        "usedEvents": []
                    }
                ],
                "license": "MIT"
            }
        },
        "vulnerable_contracts/missing_reentrancy_guard/src/missing_reentrancy_guard.sol": {
            "id": 1,
            "ast": {
                "absolutePath": "vulnerable_contracts/missing_reentrancy_guard/src/missing_reentrancy_guard.sol",
                "id": 121,
                "exportedSymbols": {
                    "ProblematicContract": [
                        120
                    ]
                },
                "nodeType": "SourceUnit",
                "src": "32:1122:1",
                "nodes": [
                    {
                        "id": 55,
                        "nodeType": "PragmaDirective",
                        "src": "32:23:1",
                        "nodes": [],
                        "literals": [
                            "solidity",
                            "0.8",
                            ".20"
                        ]
                    },
                    {
                        "id": 120,
                        "nodeType": "ContractDefinition",
                        "src": "57:1097:1",
                        "nodes": [
                            {
                                "id": 59,
                                "nodeType": "VariableDeclaration",
                                "src": "92:40:1",
                                "nodes": [],
                                "constant": false,
                                "functionSelector": "27e235e3",
                                "mutability": "mutable",
                                "name": "balances",
                                "nameLocation": "124:8:1",
                                "scope": 120,
                                "stateVariable": true,
                                "storageLocation": "default",
                                "typeDescriptions": {
                                    "typeIdentifier": "t_mapping$_t_address_$_t_uint256_$",
                                    "typeString": "mapping(address => uint256)"
                                },
                                "typeName": {
                                    "id": 58,
                                    "keyName": "",
                                    "keyNameLocation": "-1:-1:-1",
                                    "keyType": {
                                        "id": 56,
                                        "name": "address",
                                        "nodeType": "ElementaryTypeName",
                                        "src": "100:7:1",
                                        "typeDescriptions": {
                                            "typeIdentifier": "t_address",
                                            "typeString": "address"
                                        }
                                    },
                                    "nodeType": "Mapping",
                                    "src": "92:24:1",
                                    "typeDescriptions": {
                                        "typeIdentifier": "t_mapping$_t_address_$_t_uint256_$",
                                        "typeString": "mapping(address => uint256)"
                                    },
                                    "valueName": "",
                                    "valueNameLocation": "-1:-1:-1",
                                    "valueType": {
                                        "id": 57,
                                        "name": "uint",
                                        "nodeType": "ElementaryTypeName",
                                        "src": "111:4:1",
                                        "typeDescriptions": {
                                            "typeIdentifier": "t_uint256",
                                            "typeString": "uint256"
                                        }
                                    }
                                },
                                "visibility": "public"
                            },
                            {
                                "id": 79,
                                "nodeType": "FunctionDefinition",
                                "src": "139:157:1",
                                "nodes": [],
                                "body": {
                                    "id": 78,
                                    "nodeType": "Block",
                                    "src": "173:123:1",
                                    "nodes": [],
                                    "statements": [
                                        {
                                            "expression": {
                                                "arguments": [
                                                    {
                                                        "commonType": {
                                                            "typeIdentifier": "t_uint256",
                                                            "typeString": "uint256"
                                                        },
                                                        "id": 66,
                                                        "isConstant": false,
                                                        "isLValue": false,
                                                        "isPure": false,
                                                        "lValueRequested": false,
                                                        "leftExpression": {
                                                            "expression": {
                                                                "id": 63,
                                                                "name": "msg",
                                                                "nodeType": "Identifier",
                                                                "overloadedDeclarations": [],
                                                                "referencedDeclaration": -15,
                                                                "src": "191:3:1",
                                                                "typeDescriptions": {
                                                                    "typeIdentifier": "t_magic_message",
                                                                    "typeString": "msg"
                                                                }
                                                            },
                                                            "id": 64,
                                                            "isConstant": false,
                                                            "isLValue": false,
                                                            "isPure": false,
                                                            "lValueRequested": false,
                                                            "memberLocation": "195:5:1",
                                                            "memberName": "value",
                                                            "nodeType": "MemberAccess",
                                                            "src": "191:9:1",
                                                            "typeDescriptions": {
                                                                "typeIdentifier": "t_uint256",
                                                                "typeString": "uint256"
                                                            }
                                                        },
                                                        "nodeType": "BinaryOperation",
                                                        "operator": ">",
                                                        "rightExpression": {
                                                            "hexValue": "30",
                                                            "id": 65,
                                                            "isConstant": false,
                                                            "isLValue": false,
                                                            "isPure": true,
                                                            "kind": "number",
                                                            "lValueRequested": false,
                                                            "nodeType": "Literal",
                                                            "src": "203:1:1",
                                                            "typeDescriptions": {
                                                                "typeIdentifier": "t_rational_0_by_1",
                                                                "typeString": "int_const 0"
                                                            },
                                                            "value": "0"
                                                        },
                                                        "src": "191:13:1",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_bool",
                                                            "typeString": "bool"
                                                        }
                                                    },
                                                    {
                                                        "hexValue": "4465706f73697420616d6f756e74206d7573742062652067726561746572207468616e2030",
                                                        "id": 67,
                                                        "isConstant": false,
                                                        "isLValue": false,
                                                        "isPure": true,
                                                        "kind": "string",
                                                        "lValueRequested": false,
                                                        "nodeType": "Literal",
                                                        "src": "206:39:1",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_stringliteral_1cf5370f25734823c5feac6853b836d05520862485f150310f24689e28c1f9e6",
                                                            "typeString": "literal_string Deposit amount must be greater than 0"
                                                        },
                                                        "value": "Deposit amount must be greater than 0"
                                                    }
                                                ],
                                                "expression": {
                                                    "argumentTypes": [
                                                        {
                                                            "typeIdentifier": "t_bool",
                                                            "typeString": "bool"
                                                        },
                                                        {
                                                            "typeIdentifier": "t_stringliteral_1cf5370f25734823c5feac6853b836d05520862485f150310f24689e28c1f9e6",
                                                            "typeString": "literal_string Deposit amount must be greater than 0"
                                                        }
                                                    ],
                                                    "id": 62,
                                                    "name": "require",
                                                    "nodeType": "Identifier",
                                                    "overloadedDeclarations": [
                                                        -18,
                                                        -18
                                                    ],
                                                    "referencedDeclaration": -18,
                                                    "src": "183:7:1",
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
                                                "src": "183:63:1",
                                                "tryCall": false,
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_tuple$__$",
                                                    "typeString": "tuple()"
                                                }
                                            },
                                            "id": 69,
                                            "nodeType": "ExpressionStatement",
                                            "src": "183:63:1"
                                        },
                                        {
                                            "expression": {
                                                "id": 76,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "lValueRequested": false,
                                                "leftHandSide": {
                                                    "baseExpression": {
                                                        "id": 70,
                                                        "name": "balances",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 59,
                                                        "src": "256:8:1",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_mapping$_t_address_$_t_uint256_$",
                                                            "typeString": "mapping(address => uint256)"
                                                        }
                                                    },
                                                    "id": 73,
                                                    "indexExpression": {
                                                        "expression": {
                                                            "id": 71,
                                                            "name": "msg",
                                                            "nodeType": "Identifier",
                                                            "overloadedDeclarations": [],
                                                            "referencedDeclaration": -15,
                                                            "src": "265:3:1",
                                                            "typeDescriptions": {
                                                                "typeIdentifier": "t_magic_message",
                                                                "typeString": "msg"
                                                            }
                                                        },
                                                        "id": 72,
                                                        "isConstant": false,
                                                        "isLValue": false,
                                                        "isPure": false,
                                                        "lValueRequested": false,
                                                        "memberLocation": "269:6:1",
                                                        "memberName": "sender",
                                                        "nodeType": "MemberAccess",
                                                        "src": "265:10:1",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_address",
                                                            "typeString": "address"
                                                        }
                                                    },
                                                    "isConstant": false,
                                                    "isLValue": true,
                                                    "isPure": false,
                                                    "lValueRequested": true,
                                                    "nodeType": "IndexAccess",
                                                    "src": "256:20:1",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_uint256",
                                                        "typeString": "uint256"
                                                    }
                                                },
                                                "nodeType": "Assignment",
                                                "operator": "+=",
                                                "rightHandSide": {
                                                    "expression": {
                                                        "id": 74,
                                                        "name": "msg",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": -15,
                                                        "src": "280:3:1",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_magic_message",
                                                            "typeString": "msg"
                                                        }
                                                    },
                                                    "id": 75,
                                                    "isConstant": false,
                                                    "isLValue": false,
                                                    "isPure": false,
                                                    "lValueRequested": false,
                                                    "memberLocation": "284:5:1",
                                                    "memberName": "value",
                                                    "nodeType": "MemberAccess",
                                                    "src": "280:9:1",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_uint256",
                                                        "typeString": "uint256"
                                                    }
                                                },
                                                "src": "256:33:1",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint256",
                                                    "typeString": "uint256"
                                                }
                                            },
                                            "id": 77,
                                            "nodeType": "ExpressionStatement",
                                            "src": "256:33:1"
                                        }
                                    ]
                                },
                                "functionSelector": "d0e30db0",
                                "implemented": true,
                                "kind": "function",
                                "modifiers": [],
                                "name": "deposit",
                                "nameLocation": "148:7:1",
                                "parameters": {
                                    "id": 60,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "155:2:1"
                                },
                                "returnParameters": {
                                    "id": 61,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "173:0:1"
                                },
                                "scope": 120,
                                "stateMutability": "payable",
                                "virtual": false,
                                "visibility": "public"
                            },
                            {
                                "id": 119,
                                "nodeType": "FunctionDefinition",
                                "src": "302:850:1",
                                "nodes": [],
                                "body": {
                                    "id": 118,
                                    "nodeType": "Block",
                                    "src": "329:823:1",
                                    "nodes": [],
                                    "statements": [
                                        {
                                            "assignments": [
                                                83
                                            ],
                                            "declarations": [
                                                {
                                                    "constant": false,
                                                    "id": 83,
                                                    "mutability": "mutable",
                                                    "name": "balance",
                                                    "nameLocation": "344:7:1",
                                                    "nodeType": "VariableDeclaration",
                                                    "scope": 118,
                                                    "src": "339:12:1",
                                                    "stateVariable": false,
                                                    "storageLocation": "default",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_uint256",
                                                        "typeString": "uint256"
                                                    },
                                                    "typeName": {
                                                        "id": 82,
                                                        "name": "uint",
                                                        "nodeType": "ElementaryTypeName",
                                                        "src": "339:4:1",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_uint256",
                                                            "typeString": "uint256"
                                                        }
                                                    },
                                                    "visibility": "internal"
                                                }
                                            ],
                                            "id": 88,
                                            "initialValue": {
                                                "baseExpression": {
                                                    "id": 84,
                                                    "name": "balances",
                                                    "nodeType": "Identifier",
                                                    "overloadedDeclarations": [],
                                                    "referencedDeclaration": 59,
                                                    "src": "354:8:1",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_mapping$_t_address_$_t_uint256_$",
                                                        "typeString": "mapping(address => uint256)"
                                                    }
                                                },
                                                "id": 87,
                                                "indexExpression": {
                                                    "expression": {
                                                        "id": 85,
                                                        "name": "msg",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": -15,
                                                        "src": "363:3:1",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_magic_message",
                                                            "typeString": "msg"
                                                        }
                                                    },
                                                    "id": 86,
                                                    "isConstant": false,
                                                    "isLValue": false,
                                                    "isPure": false,
                                                    "lValueRequested": false,
                                                    "memberLocation": "367:6:1",
                                                    "memberName": "sender",
                                                    "nodeType": "MemberAccess",
                                                    "src": "363:10:1",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_address",
                                                        "typeString": "address"
                                                    }
                                                },
                                                "isConstant": false,
                                                "isLValue": true,
                                                "isPure": false,
                                                "lValueRequested": false,
                                                "nodeType": "IndexAccess",
                                                "src": "354:20:1",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint256",
                                                    "typeString": "uint256"
                                                }
                                            },
                                            "nodeType": "VariableDeclarationStatement",
                                            "src": "339:35:1"
                                        },
                                        {
                                            "expression": {
                                                "arguments": [
                                                    {
                                                        "commonType": {
                                                            "typeIdentifier": "t_uint256",
                                                            "typeString": "uint256"
                                                        },
                                                        "id": 92,
                                                        "isConstant": false,
                                                        "isLValue": false,
                                                        "isPure": false,
                                                        "lValueRequested": false,
                                                        "leftExpression": {
                                                            "id": 90,
                                                            "name": "balance",
                                                            "nodeType": "Identifier",
                                                            "overloadedDeclarations": [],
                                                            "referencedDeclaration": 83,
                                                            "src": "392:7:1",
                                                            "typeDescriptions": {
                                                                "typeIdentifier": "t_uint256",
                                                                "typeString": "uint256"
                                                            }
                                                        },
                                                        "nodeType": "BinaryOperation",
                                                        "operator": ">",
                                                        "rightExpression": {
                                                            "hexValue": "30",
                                                            "id": 91,
                                                            "isConstant": false,
                                                            "isLValue": false,
                                                            "isPure": true,
                                                            "kind": "number",
                                                            "lValueRequested": false,
                                                            "nodeType": "Literal",
                                                            "src": "402:1:1",
                                                            "typeDescriptions": {
                                                                "typeIdentifier": "t_rational_0_by_1",
                                                                "typeString": "int_const 0"
                                                            },
                                                            "value": "0"
                                                        },
                                                        "src": "392:11:1",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_bool",
                                                            "typeString": "bool"
                                                        }
                                                    },
                                                    {
                                                        "hexValue": "496e73756666696369656e742066756e6473",
                                                        "id": 93,
                                                        "isConstant": false,
                                                        "isLValue": false,
                                                        "isPure": true,
                                                        "kind": "string",
                                                        "lValueRequested": false,
                                                        "nodeType": "Literal",
                                                        "src": "405:20:1",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_stringliteral_63452317cb6d597bef833f023ed2962a84dbd24c571e27629ed1e3056d6cfd8d",
                                                            "typeString": "literal_string Insufficient funds"
                                                        },
                                                        "value": "Insufficient funds"
                                                    }
                                                ],
                                                "expression": {
                                                    "argumentTypes": [
                                                        {
                                                            "typeIdentifier": "t_bool",
                                                            "typeString": "bool"
                                                        },
                                                        {
                                                            "typeIdentifier": "t_stringliteral_63452317cb6d597bef833f023ed2962a84dbd24c571e27629ed1e3056d6cfd8d",
                                                            "typeString": "literal_string Insufficient funds"
                                                        }
                                                    ],
                                                    "id": 89,
                                                    "name": "require",
                                                    "nodeType": "Identifier",
                                                    "overloadedDeclarations": [
                                                        -18,
                                                        -18
                                                    ],
                                                    "referencedDeclaration": -18,
                                                    "src": "384:7:1",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_function_require_pure$_t_bool_$_t_string_memory_ptr_$returns$__$",
                                                        "typeString": "function (bool,string memory) pure"
                                                    }
                                                },
                                                "id": 94,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "kind": "functionCall",
                                                "lValueRequested": false,
                                                "nameLocations": [],
                                                "names": [],
                                                "nodeType": "FunctionCall",
                                                "src": "384:42:1",
                                                "tryCall": false,
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_tuple$__$",
                                                    "typeString": "tuple()"
                                                }
                                            },
                                            "id": 95,
                                            "nodeType": "ExpressionStatement",
                                            "src": "384:42:1"
                                        },
                                        {
                                            "assignments": [
                                                97,
                                                null
                                            ],
                                            "declarations": [
                                                {
                                                    "constant": false,
                                                    "id": 97,
                                                    "mutability": "mutable",
                                                    "name": "sent",
                                                    "nameLocation": "957:4:1",
                                                    "nodeType": "VariableDeclaration",
                                                    "scope": 118,
                                                    "src": "952:9:1",
                                                    "stateVariable": false,
                                                    "storageLocation": "default",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_bool",
                                                        "typeString": "bool"
                                                    },
                                                    "typeName": {
                                                        "id": 96,
                                                        "name": "bool",
                                                        "nodeType": "ElementaryTypeName",
                                                        "src": "952:4:1",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_bool",
                                                            "typeString": "bool"
                                                        }
                                                    },
                                                    "visibility": "internal"
                                                },
                                                null
                                            ],
                                            "id": 105,
                                            "initialValue": {
                                                "arguments": [
                                                    {
                                                        "hexValue": "",
                                                        "id": 103,
                                                        "isConstant": false,
                                                        "isLValue": false,
                                                        "isPure": true,
                                                        "kind": "string",
                                                        "lValueRequested": false,
                                                        "nodeType": "Literal",
                                                        "src": "999:2:1",
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
                                                            "expression": {
                                                                "id": 98,
                                                                "name": "msg",
                                                                "nodeType": "Identifier",
                                                                "overloadedDeclarations": [],
                                                                "referencedDeclaration": -15,
                                                                "src": "967:3:1",
                                                                "typeDescriptions": {
                                                                    "typeIdentifier": "t_magic_message",
                                                                    "typeString": "msg"
                                                                }
                                                            },
                                                            "id": 99,
                                                            "isConstant": false,
                                                            "isLValue": false,
                                                            "isPure": false,
                                                            "lValueRequested": false,
                                                            "memberLocation": "971:6:1",
                                                            "memberName": "sender",
                                                            "nodeType": "MemberAccess",
                                                            "src": "967:10:1",
                                                            "typeDescriptions": {
                                                                "typeIdentifier": "t_address",
                                                                "typeString": "address"
                                                            }
                                                        },
                                                        "id": 100,
                                                        "isConstant": false,
                                                        "isLValue": false,
                                                        "isPure": false,
                                                        "lValueRequested": false,
                                                        "memberLocation": "978:4:1",
                                                        "memberName": "call",
                                                        "nodeType": "MemberAccess",
                                                        "src": "967:15:1",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_function_barecall_payable$_t_bytes_memory_ptr_$returns$_t_bool_$_t_bytes_memory_ptr_$",
                                                            "typeString": "function (bytes memory) payable returns (bool,bytes memory)"
                                                        }
                                                    },
                                                    "id": 102,
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
                                                            "id": 101,
                                                            "name": "balance",
                                                            "nodeType": "Identifier",
                                                            "overloadedDeclarations": [],
                                                            "referencedDeclaration": 83,
                                                            "src": "990:7:1",
                                                            "typeDescriptions": {
                                                                "typeIdentifier": "t_uint256",
                                                                "typeString": "uint256"
                                                            }
                                                        }
                                                    ],
                                                    "src": "967:31:1",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_function_barecall_payable$_t_bytes_memory_ptr_$returns$_t_bool_$_t_bytes_memory_ptr_$value",
                                                        "typeString": "function (bytes memory) payable returns (bool,bytes memory)"
                                                    }
                                                },
                                                "id": 104,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "kind": "functionCall",
                                                "lValueRequested": false,
                                                "nameLocations": [],
                                                "names": [],
                                                "nodeType": "FunctionCall",
                                                "src": "967:35:1",
                                                "tryCall": false,
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_tuple$_t_bool_$_t_bytes_memory_ptr_$",
                                                    "typeString": "tuple(bool,bytes memory)"
                                                }
                                            },
                                            "nodeType": "VariableDeclarationStatement",
                                            "src": "951:51:1"
                                        },
                                        {
                                            "expression": {
                                                "arguments": [
                                                    {
                                                        "id": 107,
                                                        "name": "sent",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 97,
                                                        "src": "1020:4:1",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_bool",
                                                            "typeString": "bool"
                                                        }
                                                    },
                                                    {
                                                        "hexValue": "4661696c656420746f2073656e64204574686572",
                                                        "id": 108,
                                                        "isConstant": false,
                                                        "isLValue": false,
                                                        "isPure": true,
                                                        "kind": "string",
                                                        "lValueRequested": false,
                                                        "nodeType": "Literal",
                                                        "src": "1026:22:1",
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
                                                    "id": 106,
                                                    "name": "require",
                                                    "nodeType": "Identifier",
                                                    "overloadedDeclarations": [
                                                        -18,
                                                        -18
                                                    ],
                                                    "referencedDeclaration": -18,
                                                    "src": "1012:7:1",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_function_require_pure$_t_bool_$_t_string_memory_ptr_$returns$__$",
                                                        "typeString": "function (bool,string memory) pure"
                                                    }
                                                },
                                                "id": 109,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "kind": "functionCall",
                                                "lValueRequested": false,
                                                "nameLocations": [],
                                                "names": [],
                                                "nodeType": "FunctionCall",
                                                "src": "1012:37:1",
                                                "tryCall": false,
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_tuple$__$",
                                                    "typeString": "tuple()"
                                                }
                                            },
                                            "id": 110,
                                            "nodeType": "ExpressionStatement",
                                            "src": "1012:37:1"
                                        },
                                        {
                                            "expression": {
                                                "id": 116,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "lValueRequested": false,
                                                "leftHandSide": {
                                                    "baseExpression": {
                                                        "id": 111,
                                                        "name": "balances",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 59,
                                                        "src": "1121:8:1",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_mapping$_t_address_$_t_uint256_$",
                                                            "typeString": "mapping(address => uint256)"
                                                        }
                                                    },
                                                    "id": 114,
                                                    "indexExpression": {
                                                        "expression": {
                                                            "id": 112,
                                                            "name": "msg",
                                                            "nodeType": "Identifier",
                                                            "overloadedDeclarations": [],
                                                            "referencedDeclaration": -15,
                                                            "src": "1130:3:1",
                                                            "typeDescriptions": {
                                                                "typeIdentifier": "t_magic_message",
                                                                "typeString": "msg"
                                                            }
                                                        },
                                                        "id": 113,
                                                        "isConstant": false,
                                                        "isLValue": false,
                                                        "isPure": false,
                                                        "lValueRequested": false,
                                                        "memberLocation": "1134:6:1",
                                                        "memberName": "sender",
                                                        "nodeType": "MemberAccess",
                                                        "src": "1130:10:1",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_address",
                                                            "typeString": "address"
                                                        }
                                                    },
                                                    "isConstant": false,
                                                    "isLValue": true,
                                                    "isPure": false,
                                                    "lValueRequested": true,
                                                    "nodeType": "IndexAccess",
                                                    "src": "1121:20:1",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_uint256",
                                                        "typeString": "uint256"
                                                    }
                                                },
                                                "nodeType": "Assignment",
                                                "operator": "=",
                                                "rightHandSide": {
                                                    "hexValue": "30",
                                                    "id": 115,
                                                    "isConstant": false,
                                                    "isLValue": false,
                                                    "isPure": true,
                                                    "kind": "number",
                                                    "lValueRequested": false,
                                                    "nodeType": "Literal",
                                                    "src": "1144:1:1",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_rational_0_by_1",
                                                        "typeString": "int_const 0"
                                                    },
                                                    "value": "0"
                                                },
                                                "src": "1121:24:1",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint256",
                                                    "typeString": "uint256"
                                                }
                                            },
                                            "id": 117,
                                            "nodeType": "ExpressionStatement",
                                            "src": "1121:24:1"
                                        }
                                    ]
                                },
                                "functionSelector": "3ccfd60b",
                                "implemented": true,
                                "kind": "function",
                                "modifiers": [],
                                "name": "withdraw",
                                "nameLocation": "311:8:1",
                                "parameters": {
                                    "id": 80,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "319:2:1"
                                },
                                "returnParameters": {
                                    "id": 81,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "329:0:1"
                                },
                                "scope": 120,
                                "stateMutability": "nonpayable",
                                "virtual": false,
                                "visibility": "public"
                            }
                        ],
                        "abstract": false,
                        "baseContracts": [],
                        "canonicalName": "ProblematicContract",
                        "contractDependencies": [],
                        "contractKind": "contract",
                        "fullyImplemented": true,
                        "linearizedBaseContracts": [
                            120
                        ],
                        "name": "ProblematicContract",
                        "nameLocation": "66:19:1",
                        "scope": 121,
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


def test_missing_reentrancy_guard(vulnerable_ast):
    ast_json, src_paths = reduce_json(vulnerable_ast)
    results = process_yaml(
        "eburger/templates/missing_reentrancy_guard.yaml",
        ast_json,
        src_paths,
    )
    assert "Line 12 Columns 4-33" in results["results"][0]["lines"]
