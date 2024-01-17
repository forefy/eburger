import json
import pytest
from eburger.serializer import reduce_json
from eburger.yaml_parser import process_yaml


@pytest.fixture
def vulnerable_ast() -> (dict, list):
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
    },
    "contracts": {
        "script/Attacker.sol": {
            "Attacker": {
                "abi": [
                    {
                        "type": "constructor",
                        "inputs": [
                            {
                                "name": "_problematic_contract",
                                "type": "address",
                                "internalType": "address"
                            }
                        ],
                        "stateMutability": "nonpayable"
                    },
                    {
                        "type": "receive",
                        "stateMutability": "payable"
                    },
                    {
                        "type": "function",
                        "name": "attack",
                        "inputs": [],
                        "outputs": [],
                        "stateMutability": "payable"
                    },
                    {
                        "type": "function",
                        "name": "problematic_contract",
                        "inputs": [],
                        "outputs": [
                            {
                                "name": "",
                                "type": "address",
                                "internalType": "contract ProblematicContract"
                            }
                        ],
                        "stateMutability": "view"
                    }
                ],
                "metadata": "{compiler:{version:0.8.20+commit.a1b79de6},language:Solidity,output:{abi:[{inputs:[{internalType:address,name:_problematic_contract,type:address}],stateMutability:nonpayable,type:constructor},{inputs:[],name:attack,outputs:[],stateMutability:payable,type:function},{inputs:[],name:problematic_contract,outputs:[{internalType:contract ProblematicContract,name:,type:address}],stateMutability:view,type:function},{stateMutability:payable,type:receive}],devdoc:{kind:dev,methods:{},version:1},userdoc:{kind:user,methods:{},version:1}},settings:{compilationTarget:{script/Attacker.sol:Attacker},evmVersion:paris,libraries:{},metadata:{bytecodeHash:ipfs},optimizer:{enabled:true,runs:200},remappings:[:ds-test/=lib/forge-std/lib/ds-test/src/,:forge-std/=lib/forge-std/src/]},sources:{script/Attacker.sol:{keccak256:0x3ddf9b0429a65587bc1967f4fa6dcea6f3a3525ff28b7b3a7e37c09735b0e587,license:MIT,urls:[bzz-raw://9756a0ed7a770bfd3ad6d4d191b34f3719c85e8b4116f01a55b79ceb5398d895,dweb:/ipfs/QmdHLCDdU7N4JLihamHhrjktGpAmnY7NAj8L8UP8yqJtUg]},vulnerable_contracts/missing_reentrancy_guard/src/missing_reentrancy_guard.sol:{keccak256:0x75b4f79a65c8ace40ead7212de8cf8677beeeb4e87958a925af4c1b514c1a576,license:MIT,urls:[bzz-raw://fd7a023ce1139d1f0237f37139280cd56c68b34eabba1ae4df6e54dbc76e0543,dweb:/ipfs/QmaPWHdLh2UoUTDp3fSmuJUSyTyFQgepZSPyYN9E4yEFRx]}},version:1}",
                "userdoc": {},
                "devdoc": {},
                "evm": {
                    "bytecode": {
                        "functionDebugData": {
                            "@_17": {
                                "entryPoint": null,
                                "id": 17,
                                "parameterSlots": 1,
                                "returnSlots": 0
                            },
                            "abi_decode_tuple_t_address_fromMemory": {
                                "entryPoint": 84,
                                "id": null,
                                "parameterSlots": 2,
                                "returnSlots": 1
                            }
                        },
                        "object": "608060405234801561001057600080fd5b5060405161027b38038061027b83398101604081905261002f91610054565b600080546001600160a01b0319166001600160a01b0392909216919091179055610084565b60006020828403121561006657600080fd5b81516001600160a01b038116811461007d57600080fd5b9392505050565b6101e8806100936000396000f3fe60806040526004361061002d5760003560e01c806346142dfd146100b05780639e5faafc146100ec57600080fd5b366100ab57600054670de0b6b3a76400006001600160a01b0390911631106100a9576000805460408051633ccfd60b60e01b815290516001600160a01b0390921692633ccfd60b9260048084019382900301818387803b15801561009057600080fd5b505af11580156100a4573d6000803e3d6000fd5b505050505b005b600080fd5b3480156100bc57600080fd5b506000546100d0906001600160a01b031681565b6040516001600160a01b03909116815260200160405180910390f35b6100a960008054906101000a90046001600160a01b03166001600160a01b031663d0e30db0346040518263ffffffff1660e01b81526004016000604051808303818588803b15801561013d57600080fd5b505af1158015610151573d6000803e3d6000fd5b50506000805460408051633ccfd60b60e01b815290516001600160a01b039092169550633ccfd60b9450600480820194509082900301818387803b15801561019857600080fd5b505af11580156101ac573d6000803e3d6000fd5b5050505056fea264697066735822122056618f6063940d6c103d413550b93ee0153f968b63d06df7220458453ff5027064736f6c63430008140033",
                        "opcodes": "PUSH1 0x80 PUSH1 0x40 MSTORE CALLVALUE DUP1 ISZERO PUSH2 0x10 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST POP PUSH1 0x40 MLOAD PUSH2 0x27B CODESIZE SUB DUP1 PUSH2 0x27B DUP4 CODECOPY DUP2 ADD PUSH1 0x40 DUP2 SWAP1 MSTORE PUSH2 0x2F SWAP2 PUSH2 0x54 JUMP JUMPDEST PUSH1 0x0 DUP1 SLOAD PUSH1 0x1 PUSH1 0x1 PUSH1 0xA0 SHL SUB NOT AND PUSH1 0x1 PUSH1 0x1 PUSH1 0xA0 SHL SUB SWAP3 SWAP1 SWAP3 AND SWAP2 SWAP1 SWAP2 OR SWAP1 SSTORE PUSH2 0x84 JUMP JUMPDEST PUSH1 0x0 PUSH1 0x20 DUP3 DUP5 SUB SLT ISZERO PUSH2 0x66 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST DUP2 MLOAD PUSH1 0x1 PUSH1 0x1 PUSH1 0xA0 SHL SUB DUP2 AND DUP2 EQ PUSH2 0x7D JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST SWAP4 SWAP3 POP POP POP JUMP JUMPDEST PUSH2 0x1E8 DUP1 PUSH2 0x93 PUSH1 0x0 CODECOPY PUSH1 0x0 RETURN INVALID PUSH1 0x80 PUSH1 0x40 MSTORE PUSH1 0x4 CALLDATASIZE LT PUSH2 0x2D JUMPI PUSH1 0x0 CALLDATALOAD PUSH1 0xE0 SHR DUP1 PUSH4 0x46142DFD EQ PUSH2 0xB0 JUMPI DUP1 PUSH4 0x9E5FAAFC EQ PUSH2 0xEC JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST CALLDATASIZE PUSH2 0xAB JUMPI PUSH1 0x0 SLOAD PUSH8 0xDE0B6B3A7640000 PUSH1 0x1 PUSH1 0x1 PUSH1 0xA0 SHL SUB SWAP1 SWAP2 AND BALANCE LT PUSH2 0xA9 JUMPI PUSH1 0x0 DUP1 SLOAD PUSH1 0x40 DUP1 MLOAD PUSH4 0x3CCFD60B PUSH1 0xE0 SHL DUP2 MSTORE SWAP1 MLOAD PUSH1 0x1 PUSH1 0x1 PUSH1 0xA0 SHL SUB SWAP1 SWAP3 AND SWAP3 PUSH4 0x3CCFD60B SWAP3 PUSH1 0x4 DUP1 DUP5 ADD SWAP4 DUP3 SWAP1 SUB ADD DUP2 DUP4 DUP8 DUP1 EXTCODESIZE ISZERO DUP1 ISZERO PUSH2 0x90 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST POP GAS CALL ISZERO DUP1 ISZERO PUSH2 0xA4 JUMPI RETURNDATASIZE PUSH1 0x0 DUP1 RETURNDATACOPY RETURNDATASIZE PUSH1 0x0 REVERT JUMPDEST POP POP POP POP JUMPDEST STOP JUMPDEST PUSH1 0x0 DUP1 REVERT JUMPDEST CALLVALUE DUP1 ISZERO PUSH2 0xBC JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST POP PUSH1 0x0 SLOAD PUSH2 0xD0 SWAP1 PUSH1 0x1 PUSH1 0x1 PUSH1 0xA0 SHL SUB AND DUP2 JUMP JUMPDEST PUSH1 0x40 MLOAD PUSH1 0x1 PUSH1 0x1 PUSH1 0xA0 SHL SUB SWAP1 SWAP2 AND DUP2 MSTORE PUSH1 0x20 ADD PUSH1 0x40 MLOAD DUP1 SWAP2 SUB SWAP1 RETURN JUMPDEST PUSH2 0xA9 PUSH1 0x0 DUP1 SLOAD SWAP1 PUSH2 0x100 EXP SWAP1 DIV PUSH1 0x1 PUSH1 0x1 PUSH1 0xA0 SHL SUB AND PUSH1 0x1 PUSH1 0x1 PUSH1 0xA0 SHL SUB AND PUSH4 0xD0E30DB0 CALLVALUE PUSH1 0x40 MLOAD DUP3 PUSH4 0xFFFFFFFF AND PUSH1 0xE0 SHL DUP2 MSTORE PUSH1 0x4 ADD PUSH1 0x0 PUSH1 0x40 MLOAD DUP1 DUP4 SUB DUP2 DUP6 DUP9 DUP1 EXTCODESIZE ISZERO DUP1 ISZERO PUSH2 0x13D JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST POP GAS CALL ISZERO DUP1 ISZERO PUSH2 0x151 JUMPI RETURNDATASIZE PUSH1 0x0 DUP1 RETURNDATACOPY RETURNDATASIZE PUSH1 0x0 REVERT JUMPDEST POP POP PUSH1 0x0 DUP1 SLOAD PUSH1 0x40 DUP1 MLOAD PUSH4 0x3CCFD60B PUSH1 0xE0 SHL DUP2 MSTORE SWAP1 MLOAD PUSH1 0x1 PUSH1 0x1 PUSH1 0xA0 SHL SUB SWAP1 SWAP3 AND SWAP6 POP PUSH4 0x3CCFD60B SWAP5 POP PUSH1 0x4 DUP1 DUP3 ADD SWAP5 POP SWAP1 DUP3 SWAP1 SUB ADD DUP2 DUP4 DUP8 DUP1 EXTCODESIZE ISZERO DUP1 ISZERO PUSH2 0x198 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST POP GAS CALL ISZERO DUP1 ISZERO PUSH2 0x1AC JUMPI RETURNDATASIZE PUSH1 0x0 DUP1 RETURNDATACOPY RETURNDATASIZE PUSH1 0x0 REVERT JUMPDEST POP POP POP POP JUMP INVALID LOG2 PUSH5 0x6970667358 0x22 SLT KECCAK256 JUMP PUSH2 0x8F60 PUSH4 0x940D6C10 RETURNDATASIZE COINBASE CALLDATALOAD POP 0xB9 RETURNDATACOPY 0xE0 ISZERO EXTCODEHASH SWAP7 DUP12 PUSH4 0xD06DF722 DIV PC GASLIMIT EXTCODEHASH CREATE2 MUL PUSH17 0x64736F6C63430008140033000000000000 ",
                        "sourceMap": "104:515:0:-:0;;;182:125;;;;;;;;;;;;;;;;;;;;;;;;;;;;:::i;:::-;235:20;:65;;-1:-1:-1;;;;;;235:65:0;-1:-1:-1;;;;;235:65:0;;;;;;;;;;104:515;;14:290:2;84:6;137:2;125:9;116:7;112:23;108:32;105:52;;;153:1;150;143:12;105:52;179:16;;-1:-1:-1;;;;;224:31:2;;214:42;;204:70;;270:1;267;260:12;204:70;293:5;14:290;-1:-1:-1;;;14:290:2:o;:::-;104:515:0;;;;;;",
                        "generatedSources": [
                            {
                                "ast": {
                                    "nodeType": "YulBlock",
                                    "src": "0:306:2",
                                    "statements": [
                                        {
                                            "nodeType": "YulBlock",
                                            "src": "6:3:2",
                                            "statements": []
                                        },
                                        {
                                            "body": {
                                                "nodeType": "YulBlock",
                                                "src": "95:209:2",
                                                "statements": [
                                                    {
                                                        "body": {
                                                            "nodeType": "YulBlock",
                                                            "src": "141:16:2",
                                                            "statements": [
                                                                {
                                                                    "expression": {
                                                                        "arguments": [
                                                                            {
                                                                                "kind": "number",
                                                                                "nodeType": "YulLiteral",
                                                                                "src": "150:1:2",
                                                                                "type": "",
                                                                                "value": "0"
                                                                            },
                                                                            {
                                                                                "kind": "number",
                                                                                "nodeType": "YulLiteral",
                                                                                "src": "153:1:2",
                                                                                "type": "",
                                                                                "value": "0"
                                                                            }
                                                                        ],
                                                                        "functionName": {
                                                                            "name": "revert",
                                                                            "nodeType": "YulIdentifier",
                                                                            "src": "143:6:2"
                                                                        },
                                                                        "nodeType": "YulFunctionCall",
                                                                        "src": "143:12:2"
                                                                    },
                                                                    "nodeType": "YulExpressionStatement",
                                                                    "src": "143:12:2"
                                                                }
                                                            ]
                                                        },
                                                        "condition": {
                                                            "arguments": [
                                                                {
                                                                    "arguments": [
                                                                        {
                                                                            "name": "dataEnd",
                                                                            "nodeType": "YulIdentifier",
                                                                            "src": "116:7:2"
                                                                        },
                                                                        {
                                                                            "name": "headStart",
                                                                            "nodeType": "YulIdentifier",
                                                                            "src": "125:9:2"
                                                                        }
                                                                    ],
                                                                    "functionName": {
                                                                        "name": "sub",
                                                                        "nodeType": "YulIdentifier",
                                                                        "src": "112:3:2"
                                                                    },
                                                                    "nodeType": "YulFunctionCall",
                                                                    "src": "112:23:2"
                                                                },
                                                                {
                                                                    "kind": "number",
                                                                    "nodeType": "YulLiteral",
                                                                    "src": "137:2:2",
                                                                    "type": "",
                                                                    "value": "32"
                                                                }
                                                            ],
                                                            "functionName": {
                                                                "name": "slt",
                                                                "nodeType": "YulIdentifier",
                                                                "src": "108:3:2"
                                                            },
                                                            "nodeType": "YulFunctionCall",
                                                            "src": "108:32:2"
                                                        },
                                                        "nodeType": "YulIf",
                                                        "src": "105:52:2"
                                                    },
                                                    {
                                                        "nodeType": "YulVariableDeclaration",
                                                        "src": "166:29:2",
                                                        "value": {
                                                            "arguments": [
                                                                {
                                                                    "name": "headStart",
                                                                    "nodeType": "YulIdentifier",
                                                                    "src": "185:9:2"
                                                                }
                                                            ],
                                                            "functionName": {
                                                                "name": "mload",
                                                                "nodeType": "YulIdentifier",
                                                                "src": "179:5:2"
                                                            },
                                                            "nodeType": "YulFunctionCall",
                                                            "src": "179:16:2"
                                                        },
                                                        "variables": [
                                                            {
                                                                "name": "value",
                                                                "nodeType": "YulTypedName",
                                                                "src": "170:5:2",
                                                                "type": ""
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "body": {
                                                            "nodeType": "YulBlock",
                                                            "src": "258:16:2",
                                                            "statements": [
                                                                {
                                                                    "expression": {
                                                                        "arguments": [
                                                                            {
                                                                                "kind": "number",
                                                                                "nodeType": "YulLiteral",
                                                                                "src": "267:1:2",
                                                                                "type": "",
                                                                                "value": "0"
                                                                            },
                                                                            {
                                                                                "kind": "number",
                                                                                "nodeType": "YulLiteral",
                                                                                "src": "270:1:2",
                                                                                "type": "",
                                                                                "value": "0"
                                                                            }
                                                                        ],
                                                                        "functionName": {
                                                                            "name": "revert",
                                                                            "nodeType": "YulIdentifier",
                                                                            "src": "260:6:2"
                                                                        },
                                                                        "nodeType": "YulFunctionCall",
                                                                        "src": "260:12:2"
                                                                    },
                                                                    "nodeType": "YulExpressionStatement",
                                                                    "src": "260:12:2"
                                                                }
                                                            ]
                                                        },
                                                        "condition": {
                                                            "arguments": [
                                                                {
                                                                    "arguments": [
                                                                        {
                                                                            "name": "value",
                                                                            "nodeType": "YulIdentifier",
                                                                            "src": "217:5:2"
                                                                        },
                                                                        {
                                                                            "arguments": [
                                                                                {
                                                                                    "name": "value",
                                                                                    "nodeType": "YulIdentifier",
                                                                                    "src": "228:5:2"
                                                                                },
                                                                                {
                                                                                    "arguments": [
                                                                                        {
                                                                                            "arguments": [
                                                                                                {
                                                                                                    "kind": "number",
                                                                                                    "nodeType": "YulLiteral",
                                                                                                    "src": "243:3:2",
                                                                                                    "type": "",
                                                                                                    "value": "160"
                                                                                                },
                                                                                                {
                                                                                                    "kind": "number",
                                                                                                    "nodeType": "YulLiteral",
                                                                                                    "src": "248:1:2",
                                                                                                    "type": "",
                                                                                                    "value": "1"
                                                                                                }
                                                                                            ],
                                                                                            "functionName": {
                                                                                                "name": "shl",
                                                                                                "nodeType": "YulIdentifier",
                                                                                                "src": "239:3:2"
                                                                                            },
                                                                                            "nodeType": "YulFunctionCall",
                                                                                            "src": "239:11:2"
                                                                                        },
                                                                                        {
                                                                                            "kind": "number",
                                                                                            "nodeType": "YulLiteral",
                                                                                            "src": "252:1:2",
                                                                                            "type": "",
                                                                                            "value": "1"
                                                                                        }
                                                                                    ],
                                                                                    "functionName": {
                                                                                        "name": "sub",
                                                                                        "nodeType": "YulIdentifier",
                                                                                        "src": "235:3:2"
                                                                                    },
                                                                                    "nodeType": "YulFunctionCall",
                                                                                    "src": "235:19:2"
                                                                                }
                                                                            ],
                                                                            "functionName": {
                                                                                "name": "and",
                                                                                "nodeType": "YulIdentifier",
                                                                                "src": "224:3:2"
                                                                            },
                                                                            "nodeType": "YulFunctionCall",
                                                                            "src": "224:31:2"
                                                                        }
                                                                    ],
                                                                    "functionName": {
                                                                        "name": "eq",
                                                                        "nodeType": "YulIdentifier",
                                                                        "src": "214:2:2"
                                                                    },
                                                                    "nodeType": "YulFunctionCall",
                                                                    "src": "214:42:2"
                                                                }
                                                            ],
                                                            "functionName": {
                                                                "name": "iszero",
                                                                "nodeType": "YulIdentifier",
                                                                "src": "207:6:2"
                                                            },
                                                            "nodeType": "YulFunctionCall",
                                                            "src": "207:50:2"
                                                        },
                                                        "nodeType": "YulIf",
                                                        "src": "204:70:2"
                                                    },
                                                    {
                                                        "nodeType": "YulAssignment",
                                                        "src": "283:15:2",
                                                        "value": {
                                                            "name": "value",
                                                            "nodeType": "YulIdentifier",
                                                            "src": "293:5:2"
                                                        },
                                                        "variableNames": [
                                                            {
                                                                "name": "value0",
                                                                "nodeType": "YulIdentifier",
                                                                "src": "283:6:2"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            "name": "abi_decode_tuple_t_address_fromMemory",
                                            "nodeType": "YulFunctionDefinition",
                                            "parameters": [
                                                {
                                                    "name": "headStart",
                                                    "nodeType": "YulTypedName",
                                                    "src": "61:9:2",
                                                    "type": ""
                                                },
                                                {
                                                    "name": "dataEnd",
                                                    "nodeType": "YulTypedName",
                                                    "src": "72:7:2",
                                                    "type": ""
                                                }
                                            ],
                                            "returnVariables": [
                                                {
                                                    "name": "value0",
                                                    "nodeType": "YulTypedName",
                                                    "src": "84:6:2",
                                                    "type": ""
                                                }
                                            ],
                                            "src": "14:290:2"
                                        }
                                    ]
                                },
                                "contents": "{    { }    function abi_decode_tuple_t_address_fromMemory(headStart, dataEnd) -> value0    {        if slt(sub(dataEnd, headStart), 32) { revert(0, 0) }        let value := mload(headStart)        if iszero(eq(value, and(value, sub(shl(160, 1), 1)))) { revert(0, 0) }        value0 := value    }}",
                                "id": 2,
                                "language": "Yul",
                                "name": "#utility.yul"
                            }
                        ],
                        "linkReferences": {}
                    },
                    "deployedBytecode": {
                        "functionDebugData": {
                            "@_52": {
                                "entryPoint": null,
                                "id": 52,
                                "parameterSlots": 0,
                                "returnSlots": 0
                            },
                            "@attack_34": {
                                "entryPoint": null,
                                "id": 34,
                                "parameterSlots": 0,
                                "returnSlots": 0
                            },
                            "@problematic_contract_5": {
                                "entryPoint": null,
                                "id": 5,
                                "parameterSlots": 0,
                                "returnSlots": 0
                            },
                            "abi_encode_tuple_t_contract$_ProblematicContract_$120__to_t_address__fromStack_reversed": {
                                "entryPoint": null,
                                "id": null,
                                "parameterSlots": 2,
                                "returnSlots": 1
                            }
                        },
                        "object": "60806040526004361061002d5760003560e01c806346142dfd146100b05780639e5faafc146100ec57600080fd5b366100ab57600054670de0b6b3a76400006001600160a01b0390911631106100a9576000805460408051633ccfd60b60e01b815290516001600160a01b0390921692633ccfd60b9260048084019382900301818387803b15801561009057600080fd5b505af11580156100a4573d6000803e3d6000fd5b505050505b005b600080fd5b3480156100bc57600080fd5b506000546100d0906001600160a01b031681565b6040516001600160a01b03909116815260200160405180910390f35b6100a960008054906101000a90046001600160a01b03166001600160a01b031663d0e30db0346040518263ffffffff1660e01b81526004016000604051808303818588803b15801561013d57600080fd5b505af1158015610151573d6000803e3d6000fd5b50506000805460408051633ccfd60b60e01b815290516001600160a01b039092169550633ccfd60b9450600480820194509082900301818387803b15801561019857600080fd5b505af11580156101ac573d6000803e3d6000fd5b5050505056fea264697066735822122056618f6063940d6c103d413550b93ee0153f968b63d06df7220458453ff5027064736f6c63430008140033",
                        "opcodes": "PUSH1 0x80 PUSH1 0x40 MSTORE PUSH1 0x4 CALLDATASIZE LT PUSH2 0x2D JUMPI PUSH1 0x0 CALLDATALOAD PUSH1 0xE0 SHR DUP1 PUSH4 0x46142DFD EQ PUSH2 0xB0 JUMPI DUP1 PUSH4 0x9E5FAAFC EQ PUSH2 0xEC JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST CALLDATASIZE PUSH2 0xAB JUMPI PUSH1 0x0 SLOAD PUSH8 0xDE0B6B3A7640000 PUSH1 0x1 PUSH1 0x1 PUSH1 0xA0 SHL SUB SWAP1 SWAP2 AND BALANCE LT PUSH2 0xA9 JUMPI PUSH1 0x0 DUP1 SLOAD PUSH1 0x40 DUP1 MLOAD PUSH4 0x3CCFD60B PUSH1 0xE0 SHL DUP2 MSTORE SWAP1 MLOAD PUSH1 0x1 PUSH1 0x1 PUSH1 0xA0 SHL SUB SWAP1 SWAP3 AND SWAP3 PUSH4 0x3CCFD60B SWAP3 PUSH1 0x4 DUP1 DUP5 ADD SWAP4 DUP3 SWAP1 SUB ADD DUP2 DUP4 DUP8 DUP1 EXTCODESIZE ISZERO DUP1 ISZERO PUSH2 0x90 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST POP GAS CALL ISZERO DUP1 ISZERO PUSH2 0xA4 JUMPI RETURNDATASIZE PUSH1 0x0 DUP1 RETURNDATACOPY RETURNDATASIZE PUSH1 0x0 REVERT JUMPDEST POP POP POP POP JUMPDEST STOP JUMPDEST PUSH1 0x0 DUP1 REVERT JUMPDEST CALLVALUE DUP1 ISZERO PUSH2 0xBC JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST POP PUSH1 0x0 SLOAD PUSH2 0xD0 SWAP1 PUSH1 0x1 PUSH1 0x1 PUSH1 0xA0 SHL SUB AND DUP2 JUMP JUMPDEST PUSH1 0x40 MLOAD PUSH1 0x1 PUSH1 0x1 PUSH1 0xA0 SHL SUB SWAP1 SWAP2 AND DUP2 MSTORE PUSH1 0x20 ADD PUSH1 0x40 MLOAD DUP1 SWAP2 SUB SWAP1 RETURN JUMPDEST PUSH2 0xA9 PUSH1 0x0 DUP1 SLOAD SWAP1 PUSH2 0x100 EXP SWAP1 DIV PUSH1 0x1 PUSH1 0x1 PUSH1 0xA0 SHL SUB AND PUSH1 0x1 PUSH1 0x1 PUSH1 0xA0 SHL SUB AND PUSH4 0xD0E30DB0 CALLVALUE PUSH1 0x40 MLOAD DUP3 PUSH4 0xFFFFFFFF AND PUSH1 0xE0 SHL DUP2 MSTORE PUSH1 0x4 ADD PUSH1 0x0 PUSH1 0x40 MLOAD DUP1 DUP4 SUB DUP2 DUP6 DUP9 DUP1 EXTCODESIZE ISZERO DUP1 ISZERO PUSH2 0x13D JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST POP GAS CALL ISZERO DUP1 ISZERO PUSH2 0x151 JUMPI RETURNDATASIZE PUSH1 0x0 DUP1 RETURNDATACOPY RETURNDATASIZE PUSH1 0x0 REVERT JUMPDEST POP POP PUSH1 0x0 DUP1 SLOAD PUSH1 0x40 DUP1 MLOAD PUSH4 0x3CCFD60B PUSH1 0xE0 SHL DUP2 MSTORE SWAP1 MLOAD PUSH1 0x1 PUSH1 0x1 PUSH1 0xA0 SHL SUB SWAP1 SWAP3 AND SWAP6 POP PUSH4 0x3CCFD60B SWAP5 POP PUSH1 0x4 DUP1 DUP3 ADD SWAP5 POP SWAP1 DUP3 SWAP1 SUB ADD DUP2 DUP4 DUP8 DUP1 EXTCODESIZE ISZERO DUP1 ISZERO PUSH2 0x198 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST POP GAS CALL ISZERO DUP1 ISZERO PUSH2 0x1AC JUMPI RETURNDATASIZE PUSH1 0x0 DUP1 RETURNDATACOPY RETURNDATASIZE PUSH1 0x0 REVERT JUMPDEST POP POP POP POP JUMP INVALID LOG2 PUSH5 0x6970667358 0x22 SLT KECCAK256 JUMP PUSH2 0x8F60 PUSH4 0x940D6C10 RETURNDATASIZE COINBASE CALLDATALOAD POP 0xB9 RETURNDATACOPY 0xE0 ISZERO EXTCODEHASH SWAP7 DUP12 PUSH4 0xD06DF722 DIV PC GASLIMIT EXTCODEHASH CREATE2 MUL PUSH17 0x64736F6C63430008140033000000000000 ",
                        "sourceMap": "104:515:0:-:0;;;;;;;;;;;;;;;;;;;;;;;;;;;;;513:20;;546:7;-1:-1:-1;;;;;513:20:0;;;505:37;:48;501:110;;569:20;;;:31;;;-1:-1:-1;;;569:31:0;;;;-1:-1:-1;;;;;569:20:0;;;;:29;;:31;;;;;;;;;;:20;;:31;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;501:110;104:515;;;;;128:47;;;;;;;;;;-1:-1:-1;128:47:0;;;;-1:-1:-1;;;;;128:47:0;;;;;;-1:-1:-1;;;;;205:32:2;;;187:51;;175:2;160:18;128:47:0;;;;;;;313:141;;358:20;;;;;;;;-1:-1:-1;;;;;358:20:0;-1:-1:-1;;;;;358:28:0;;394:9;358:48;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;-1:-1:-1;;416:20:0;;;:31;;;-1:-1:-1;;;416:31:0;;;;-1:-1:-1;;;;;416:20:0;;;;-1:-1:-1;416:29:0;;-1:-1:-1;416:31:0;;;;;-1:-1:-1;416:31:0;;;;;;:20;;:31;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;313:141::o",
                        "generatedSources": [
                            {
                                "ast": {
                                    "nodeType": "YulBlock",
                                    "src": "0:246:2",
                                    "statements": [
                                        {
                                            "nodeType": "YulBlock",
                                            "src": "6:3:2",
                                            "statements": []
                                        },
                                        {
                                            "body": {
                                                "nodeType": "YulBlock",
                                                "src": "142:102:2",
                                                "statements": [
                                                    {
                                                        "nodeType": "YulAssignment",
                                                        "src": "152:26:2",
                                                        "value": {
                                                            "arguments": [
                                                                {
                                                                    "name": "headStart",
                                                                    "nodeType": "YulIdentifier",
                                                                    "src": "164:9:2"
                                                                },
                                                                {
                                                                    "kind": "number",
                                                                    "nodeType": "YulLiteral",
                                                                    "src": "175:2:2",
                                                                    "type": "",
                                                                    "value": "32"
                                                                }
                                                            ],
                                                            "functionName": {
                                                                "name": "add",
                                                                "nodeType": "YulIdentifier",
                                                                "src": "160:3:2"
                                                            },
                                                            "nodeType": "YulFunctionCall",
                                                            "src": "160:18:2"
                                                        },
                                                        "variableNames": [
                                                            {
                                                                "name": "tail",
                                                                "nodeType": "YulIdentifier",
                                                                "src": "152:4:2"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "expression": {
                                                            "arguments": [
                                                                {
                                                                    "name": "headStart",
                                                                    "nodeType": "YulIdentifier",
                                                                    "src": "194:9:2"
                                                                },
                                                                {
                                                                    "arguments": [
                                                                        {
                                                                            "name": "value0",
                                                                            "nodeType": "YulIdentifier",
                                                                            "src": "209:6:2"
                                                                        },
                                                                        {
                                                                            "arguments": [
                                                                                {
                                                                                    "arguments": [
                                                                                        {
                                                                                            "kind": "number",
                                                                                            "nodeType": "YulLiteral",
                                                                                            "src": "225:3:2",
                                                                                            "type": "",
                                                                                            "value": "160"
                                                                                        },
                                                                                        {
                                                                                            "kind": "number",
                                                                                            "nodeType": "YulLiteral",
                                                                                            "src": "230:1:2",
                                                                                            "type": "",
                                                                                            "value": "1"
                                                                                        }
                                                                                    ],
                                                                                    "functionName": {
                                                                                        "name": "shl",
                                                                                        "nodeType": "YulIdentifier",
                                                                                        "src": "221:3:2"
                                                                                    },
                                                                                    "nodeType": "YulFunctionCall",
                                                                                    "src": "221:11:2"
                                                                                },
                                                                                {
                                                                                    "kind": "number",
                                                                                    "nodeType": "YulLiteral",
                                                                                    "src": "234:1:2",
                                                                                    "type": "",
                                                                                    "value": "1"
                                                                                }
                                                                            ],
                                                                            "functionName": {
                                                                                "name": "sub",
                                                                                "nodeType": "YulIdentifier",
                                                                                "src": "217:3:2"
                                                                            },
                                                                            "nodeType": "YulFunctionCall",
                                                                            "src": "217:19:2"
                                                                        }
                                                                    ],
                                                                    "functionName": {
                                                                        "name": "and",
                                                                        "nodeType": "YulIdentifier",
                                                                        "src": "205:3:2"
                                                                    },
                                                                    "nodeType": "YulFunctionCall",
                                                                    "src": "205:32:2"
                                                                }
                                                            ],
                                                            "functionName": {
                                                                "name": "mstore",
                                                                "nodeType": "YulIdentifier",
                                                                "src": "187:6:2"
                                                            },
                                                            "nodeType": "YulFunctionCall",
                                                            "src": "187:51:2"
                                                        },
                                                        "nodeType": "YulExpressionStatement",
                                                        "src": "187:51:2"
                                                    }
                                                ]
                                            },
                                            "name": "abi_encode_tuple_t_contract$_ProblematicContract_$120__to_t_address__fromStack_reversed",
                                            "nodeType": "YulFunctionDefinition",
                                            "parameters": [
                                                {
                                                    "name": "headStart",
                                                    "nodeType": "YulTypedName",
                                                    "src": "111:9:2",
                                                    "type": ""
                                                },
                                                {
                                                    "name": "value0",
                                                    "nodeType": "YulTypedName",
                                                    "src": "122:6:2",
                                                    "type": ""
                                                }
                                            ],
                                            "returnVariables": [
                                                {
                                                    "name": "tail",
                                                    "nodeType": "YulTypedName",
                                                    "src": "133:4:2",
                                                    "type": ""
                                                }
                                            ],
                                            "src": "14:230:2"
                                        }
                                    ]
                                },
                                "contents": "{    { }    function abi_encode_tuple_t_contract$_ProblematicContract_$120__to_t_address__fromStack_reversed(headStart, value0) -> tail    {        tail := add(headStart, 32)        mstore(headStart, and(value0, sub(shl(160, 1), 1)))    }}",
                                "id": 2,
                                "language": "Yul",
                                "name": "#utility.yul"
                            }
                        ],
                        "linkReferences": {}
                    },
                    "methodIdentifiers": {
                        "attack()": "9e5faafc",
                        "problematic_contract()": "46142dfd"
                    }
                }
            }
        },
        "vulnerable_contracts/missing_reentrancy_guard/src/missing_reentrancy_guard.sol": {
            "ProblematicContract": {
                "abi": [
                    {
                        "type": "function",
                        "name": "balances",
                        "inputs": [
                            {
                                "name": "",
                                "type": "address",
                                "internalType": "address"
                            }
                        ],
                        "outputs": [
                            {
                                "name": "",
                                "type": "uint256",
                                "internalType": "uint256"
                            }
                        ],
                        "stateMutability": "view"
                    },
                    {
                        "type": "function",
                        "name": "deposit",
                        "inputs": [],
                        "outputs": [],
                        "stateMutability": "payable"
                    },
                    {
                        "type": "function",
                        "name": "withdraw",
                        "inputs": [],
                        "outputs": [],
                        "stateMutability": "nonpayable"
                    }
                ],
                "metadata": "{compiler:{version:0.8.20+commit.a1b79de6},language:Solidity,output:{abi:[{inputs:[{internalType:address,name:,type:address}],name:balances,outputs:[{internalType:uint256,name:,type:uint256}],stateMutability:view,type:function},{inputs:[],name:deposit,outputs:[],stateMutability:payable,type:function},{inputs:[],name:withdraw,outputs:[],stateMutability:nonpayable,type:function}],devdoc:{kind:dev,methods:{},version:1},userdoc:{kind:user,methods:{},version:1}},settings:{compilationTarget:{vulnerable_contracts/missing_reentrancy_guard/src/missing_reentrancy_guard.sol:ProblematicContract},evmVersion:paris,libraries:{},metadata:{bytecodeHash:ipfs},optimizer:{enabled:true,runs:200},remappings:[:ds-test/=lib/forge-std/lib/ds-test/src/,:forge-std/=lib/forge-std/src/]},sources:{vulnerable_contracts/missing_reentrancy_guard/src/missing_reentrancy_guard.sol:{keccak256:0x75b4f79a65c8ace40ead7212de8cf8677beeeb4e87958a925af4c1b514c1a576,license:MIT,urls:[bzz-raw://fd7a023ce1139d1f0237f37139280cd56c68b34eabba1ae4df6e54dbc76e0543,dweb:/ipfs/QmaPWHdLh2UoUTDp3fSmuJUSyTyFQgepZSPyYN9E4yEFRx]}},version:1}",
                "userdoc": {},
                "devdoc": {},
                "evm": {
                    "bytecode": {
                        "object": "608060405234801561001057600080fd5b506102a2806100206000396000f3fe6080604052600436106100345760003560e01c806327e235e3146100395780633ccfd60b14610078578063d0e30db01461008f575b600080fd5b34801561004557600080fd5b50610066610054366004610215565b60006020819052908152604090205481565b60405190815260200160405180910390f35b34801561008457600080fd5b5061008d610097565b005b61008d610191565b33600090815260208190526040902054806100ee5760405162461bcd60e51b8152602060048201526012602482015271496e73756666696369656e742066756e647360701b60448201526064015b60405180910390fd5b604051600090339083908381818185875af1925050503d8060008114610130576040519150601f19603f3d011682016040523d82523d6000602084013e610135565b606091505b505090508061017d5760405162461bcd60e51b81526020600482015260146024820152732330b4b632b2103a379039b2b7321022ba3432b960611b60448201526064016100e5565b505033600090815260208190526040812055565b600034116101ef5760405162461bcd60e51b815260206004820152602560248201527f4465706f73697420616d6f756e74206d75737420626520677265617465722074604482015264068616e20360dc1b60648201526084016100e5565b336000908152602081905260408120805434929061020e908490610245565b9091555050565b60006020828403121561022757600080fd5b81356001600160a01b038116811461023e57600080fd5b9392505050565b8082018082111561026657634e487b7160e01b600052601160045260246000fd5b9291505056fea26469706673582212206acd70e2709b696d93786a4e852ae49d79551cef078b16d93a6372377fb74e0d64736f6c63430008140033",
                        "opcodes": "PUSH1 0x80 PUSH1 0x40 MSTORE CALLVALUE DUP1 ISZERO PUSH2 0x10 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST POP PUSH2 0x2A2 DUP1 PUSH2 0x20 PUSH1 0x0 CODECOPY PUSH1 0x0 RETURN INVALID PUSH1 0x80 PUSH1 0x40 MSTORE PUSH1 0x4 CALLDATASIZE LT PUSH2 0x34 JUMPI PUSH1 0x0 CALLDATALOAD PUSH1 0xE0 SHR DUP1 PUSH4 0x27E235E3 EQ PUSH2 0x39 JUMPI DUP1 PUSH4 0x3CCFD60B EQ PUSH2 0x78 JUMPI DUP1 PUSH4 0xD0E30DB0 EQ PUSH2 0x8F JUMPI JUMPDEST PUSH1 0x0 DUP1 REVERT JUMPDEST CALLVALUE DUP1 ISZERO PUSH2 0x45 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST POP PUSH2 0x66 PUSH2 0x54 CALLDATASIZE PUSH1 0x4 PUSH2 0x215 JUMP JUMPDEST PUSH1 0x0 PUSH1 0x20 DUP2 SWAP1 MSTORE SWAP1 DUP2 MSTORE PUSH1 0x40 SWAP1 KECCAK256 SLOAD DUP2 JUMP JUMPDEST PUSH1 0x40 MLOAD SWAP1 DUP2 MSTORE PUSH1 0x20 ADD PUSH1 0x40 MLOAD DUP1 SWAP2 SUB SWAP1 RETURN JUMPDEST CALLVALUE DUP1 ISZERO PUSH2 0x84 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST POP PUSH2 0x8D PUSH2 0x97 JUMP JUMPDEST STOP JUMPDEST PUSH2 0x8D PUSH2 0x191 JUMP JUMPDEST CALLER PUSH1 0x0 SWAP1 DUP2 MSTORE PUSH1 0x20 DUP2 SWAP1 MSTORE PUSH1 0x40 SWAP1 KECCAK256 SLOAD DUP1 PUSH2 0xEE JUMPI PUSH1 0x40 MLOAD PUSH3 0x461BCD PUSH1 0xE5 SHL DUP2 MSTORE PUSH1 0x20 PUSH1 0x4 DUP3 ADD MSTORE PUSH1 0x12 PUSH1 0x24 DUP3 ADD MSTORE PUSH18 0x496E73756666696369656E742066756E6473 PUSH1 0x70 SHL PUSH1 0x44 DUP3 ADD MSTORE PUSH1 0x64 ADD JUMPDEST PUSH1 0x40 MLOAD DUP1 SWAP2 SUB SWAP1 REVERT JUMPDEST PUSH1 0x40 MLOAD PUSH1 0x0 SWAP1 CALLER SWAP1 DUP4 SWAP1 DUP4 DUP2 DUP2 DUP2 DUP6 DUP8 GAS CALL SWAP3 POP POP POP RETURNDATASIZE DUP1 PUSH1 0x0 DUP2 EQ PUSH2 0x130 JUMPI PUSH1 0x40 MLOAD SWAP2 POP PUSH1 0x1F NOT PUSH1 0x3F RETURNDATASIZE ADD AND DUP3 ADD PUSH1 0x40 MSTORE RETURNDATASIZE DUP3 MSTORE RETURNDATASIZE PUSH1 0x0 PUSH1 0x20 DUP5 ADD RETURNDATACOPY PUSH2 0x135 JUMP JUMPDEST PUSH1 0x60 SWAP2 POP JUMPDEST POP POP SWAP1 POP DUP1 PUSH2 0x17D JUMPI PUSH1 0x40 MLOAD PUSH3 0x461BCD PUSH1 0xE5 SHL DUP2 MSTORE PUSH1 0x20 PUSH1 0x4 DUP3 ADD MSTORE PUSH1 0x14 PUSH1 0x24 DUP3 ADD MSTORE PUSH20 0x2330B4B632B2103A379039B2B7321022BA3432B9 PUSH1 0x61 SHL PUSH1 0x44 DUP3 ADD MSTORE PUSH1 0x64 ADD PUSH2 0xE5 JUMP JUMPDEST POP POP CALLER PUSH1 0x0 SWAP1 DUP2 MSTORE PUSH1 0x20 DUP2 SWAP1 MSTORE PUSH1 0x40 DUP2 KECCAK256 SSTORE JUMP JUMPDEST PUSH1 0x0 CALLVALUE GT PUSH2 0x1EF JUMPI PUSH1 0x40 MLOAD PUSH3 0x461BCD PUSH1 0xE5 SHL DUP2 MSTORE PUSH1 0x20 PUSH1 0x4 DUP3 ADD MSTORE PUSH1 0x25 PUSH1 0x24 DUP3 ADD MSTORE PUSH32 0x4465706F73697420616D6F756E74206D75737420626520677265617465722074 PUSH1 0x44 DUP3 ADD MSTORE PUSH5 0x68616E203 PUSH1 0xDC SHL PUSH1 0x64 DUP3 ADD MSTORE PUSH1 0x84 ADD PUSH2 0xE5 JUMP JUMPDEST CALLER PUSH1 0x0 SWAP1 DUP2 MSTORE PUSH1 0x20 DUP2 SWAP1 MSTORE PUSH1 0x40 DUP2 KECCAK256 DUP1 SLOAD CALLVALUE SWAP3 SWAP1 PUSH2 0x20E SWAP1 DUP5 SWAP1 PUSH2 0x245 JUMP JUMPDEST SWAP1 SWAP2 SSTORE POP POP JUMP JUMPDEST PUSH1 0x0 PUSH1 0x20 DUP3 DUP5 SUB SLT ISZERO PUSH2 0x227 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST DUP2 CALLDATALOAD PUSH1 0x1 PUSH1 0x1 PUSH1 0xA0 SHL SUB DUP2 AND DUP2 EQ PUSH2 0x23E JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST SWAP4 SWAP3 POP POP POP JUMP JUMPDEST DUP1 DUP3 ADD DUP1 DUP3 GT ISZERO PUSH2 0x266 JUMPI PUSH4 0x4E487B71 PUSH1 0xE0 SHL PUSH1 0x0 MSTORE PUSH1 0x11 PUSH1 0x4 MSTORE PUSH1 0x24 PUSH1 0x0 REVERT JUMPDEST SWAP3 SWAP2 POP POP JUMP INVALID LOG2 PUSH5 0x6970667358 0x22 SLT KECCAK256 PUSH11 0xCD70E2709B696D93786A4E DUP6 0x2A 0xE4 SWAP14 PUSH26 0x551CEF078B16D93A6372377FB74E0D64736F6C63430008140033 ",
                        "sourceMap": "57:1097:1:-:0;;;;;;;;;;;;;;;;;;;",
                        "linkReferences": {}
                    },
                    "deployedBytecode": {
                        "functionDebugData": {
                            "@balances_59": {
                                "entryPoint": null,
                                "id": 59,
                                "parameterSlots": 0,
                                "returnSlots": 0
                            },
                            "@deposit_79": {
                                "entryPoint": 401,
                                "id": 79,
                                "parameterSlots": 0,
                                "returnSlots": 0
                            },
                            "@withdraw_119": {
                                "entryPoint": 151,
                                "id": 119,
                                "parameterSlots": 0,
                                "returnSlots": 0
                            },
                            "abi_decode_tuple_t_address": {
                                "entryPoint": 533,
                                "id": null,
                                "parameterSlots": 2,
                                "returnSlots": 1
                            },
                            "abi_encode_tuple_packed_t_stringliteral_c5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470__to_t_bytes_memory_ptr__nonPadded_inplace_fromStack_reversed": {
                                "entryPoint": null,
                                "id": null,
                                "parameterSlots": 1,
                                "returnSlots": 1
                            },
                            "abi_encode_tuple_t_stringliteral_1cf5370f25734823c5feac6853b836d05520862485f150310f24689e28c1f9e6__to_t_string_memory_ptr__fromStack_reversed": {
                                "entryPoint": null,
                                "id": null,
                                "parameterSlots": 1,
                                "returnSlots": 1
                            },
                            "abi_encode_tuple_t_stringliteral_445140255c9d889994129d349e64078d6f76b4b37ec896948f7e858f9b8a0dcb__to_t_string_memory_ptr__fromStack_reversed": {
                                "entryPoint": null,
                                "id": null,
                                "parameterSlots": 1,
                                "returnSlots": 1
                            },
                            "abi_encode_tuple_t_stringliteral_63452317cb6d597bef833f023ed2962a84dbd24c571e27629ed1e3056d6cfd8d__to_t_string_memory_ptr__fromStack_reversed": {
                                "entryPoint": null,
                                "id": null,
                                "parameterSlots": 1,
                                "returnSlots": 1
                            },
                            "abi_encode_tuple_t_uint256__to_t_uint256__fromStack_reversed": {
                                "entryPoint": null,
                                "id": null,
                                "parameterSlots": 2,
                                "returnSlots": 1
                            },
                            "checked_add_t_uint256": {
                                "entryPoint": 581,
                                "id": null,
                                "parameterSlots": 2,
                                "returnSlots": 1
                            }
                        },
                        "object": "6080604052600436106100345760003560e01c806327e235e3146100395780633ccfd60b14610078578063d0e30db01461008f575b600080fd5b34801561004557600080fd5b50610066610054366004610215565b60006020819052908152604090205481565b60405190815260200160405180910390f35b34801561008457600080fd5b5061008d610097565b005b61008d610191565b33600090815260208190526040902054806100ee5760405162461bcd60e51b8152602060048201526012602482015271496e73756666696369656e742066756e647360701b60448201526064015b60405180910390fd5b604051600090339083908381818185875af1925050503d8060008114610130576040519150601f19603f3d011682016040523d82523d6000602084013e610135565b606091505b505090508061017d5760405162461bcd60e51b81526020600482015260146024820152732330b4b632b2103a379039b2b7321022ba3432b960611b60448201526064016100e5565b505033600090815260208190526040812055565b600034116101ef5760405162461bcd60e51b815260206004820152602560248201527f4465706f73697420616d6f756e74206d75737420626520677265617465722074604482015264068616e20360dc1b60648201526084016100e5565b336000908152602081905260408120805434929061020e908490610245565b9091555050565b60006020828403121561022757600080fd5b81356001600160a01b038116811461023e57600080fd5b9392505050565b8082018082111561026657634e487b7160e01b600052601160045260246000fd5b9291505056fea26469706673582212206acd70e2709b696d93786a4e852ae49d79551cef078b16d93a6372377fb74e0d64736f6c63430008140033",
                        "opcodes": "PUSH1 0x80 PUSH1 0x40 MSTORE PUSH1 0x4 CALLDATASIZE LT PUSH2 0x34 JUMPI PUSH1 0x0 CALLDATALOAD PUSH1 0xE0 SHR DUP1 PUSH4 0x27E235E3 EQ PUSH2 0x39 JUMPI DUP1 PUSH4 0x3CCFD60B EQ PUSH2 0x78 JUMPI DUP1 PUSH4 0xD0E30DB0 EQ PUSH2 0x8F JUMPI JUMPDEST PUSH1 0x0 DUP1 REVERT JUMPDEST CALLVALUE DUP1 ISZERO PUSH2 0x45 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST POP PUSH2 0x66 PUSH2 0x54 CALLDATASIZE PUSH1 0x4 PUSH2 0x215 JUMP JUMPDEST PUSH1 0x0 PUSH1 0x20 DUP2 SWAP1 MSTORE SWAP1 DUP2 MSTORE PUSH1 0x40 SWAP1 KECCAK256 SLOAD DUP2 JUMP JUMPDEST PUSH1 0x40 MLOAD SWAP1 DUP2 MSTORE PUSH1 0x20 ADD PUSH1 0x40 MLOAD DUP1 SWAP2 SUB SWAP1 RETURN JUMPDEST CALLVALUE DUP1 ISZERO PUSH2 0x84 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST POP PUSH2 0x8D PUSH2 0x97 JUMP JUMPDEST STOP JUMPDEST PUSH2 0x8D PUSH2 0x191 JUMP JUMPDEST CALLER PUSH1 0x0 SWAP1 DUP2 MSTORE PUSH1 0x20 DUP2 SWAP1 MSTORE PUSH1 0x40 SWAP1 KECCAK256 SLOAD DUP1 PUSH2 0xEE JUMPI PUSH1 0x40 MLOAD PUSH3 0x461BCD PUSH1 0xE5 SHL DUP2 MSTORE PUSH1 0x20 PUSH1 0x4 DUP3 ADD MSTORE PUSH1 0x12 PUSH1 0x24 DUP3 ADD MSTORE PUSH18 0x496E73756666696369656E742066756E6473 PUSH1 0x70 SHL PUSH1 0x44 DUP3 ADD MSTORE PUSH1 0x64 ADD JUMPDEST PUSH1 0x40 MLOAD DUP1 SWAP2 SUB SWAP1 REVERT JUMPDEST PUSH1 0x40 MLOAD PUSH1 0x0 SWAP1 CALLER SWAP1 DUP4 SWAP1 DUP4 DUP2 DUP2 DUP2 DUP6 DUP8 GAS CALL SWAP3 POP POP POP RETURNDATASIZE DUP1 PUSH1 0x0 DUP2 EQ PUSH2 0x130 JUMPI PUSH1 0x40 MLOAD SWAP2 POP PUSH1 0x1F NOT PUSH1 0x3F RETURNDATASIZE ADD AND DUP3 ADD PUSH1 0x40 MSTORE RETURNDATASIZE DUP3 MSTORE RETURNDATASIZE PUSH1 0x0 PUSH1 0x20 DUP5 ADD RETURNDATACOPY PUSH2 0x135 JUMP JUMPDEST PUSH1 0x60 SWAP2 POP JUMPDEST POP POP SWAP1 POP DUP1 PUSH2 0x17D JUMPI PUSH1 0x40 MLOAD PUSH3 0x461BCD PUSH1 0xE5 SHL DUP2 MSTORE PUSH1 0x20 PUSH1 0x4 DUP3 ADD MSTORE PUSH1 0x14 PUSH1 0x24 DUP3 ADD MSTORE PUSH20 0x2330B4B632B2103A379039B2B7321022BA3432B9 PUSH1 0x61 SHL PUSH1 0x44 DUP3 ADD MSTORE PUSH1 0x64 ADD PUSH2 0xE5 JUMP JUMPDEST POP POP CALLER PUSH1 0x0 SWAP1 DUP2 MSTORE PUSH1 0x20 DUP2 SWAP1 MSTORE PUSH1 0x40 DUP2 KECCAK256 SSTORE JUMP JUMPDEST PUSH1 0x0 CALLVALUE GT PUSH2 0x1EF JUMPI PUSH1 0x40 MLOAD PUSH3 0x461BCD PUSH1 0xE5 SHL DUP2 MSTORE PUSH1 0x20 PUSH1 0x4 DUP3 ADD MSTORE PUSH1 0x25 PUSH1 0x24 DUP3 ADD MSTORE PUSH32 0x4465706F73697420616D6F756E74206D75737420626520677265617465722074 PUSH1 0x44 DUP3 ADD MSTORE PUSH5 0x68616E203 PUSH1 0xDC SHL PUSH1 0x64 DUP3 ADD MSTORE PUSH1 0x84 ADD PUSH2 0xE5 JUMP JUMPDEST CALLER PUSH1 0x0 SWAP1 DUP2 MSTORE PUSH1 0x20 DUP2 SWAP1 MSTORE PUSH1 0x40 DUP2 KECCAK256 DUP1 SLOAD CALLVALUE SWAP3 SWAP1 PUSH2 0x20E SWAP1 DUP5 SWAP1 PUSH2 0x245 JUMP JUMPDEST SWAP1 SWAP2 SSTORE POP POP JUMP JUMPDEST PUSH1 0x0 PUSH1 0x20 DUP3 DUP5 SUB SLT ISZERO PUSH2 0x227 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST DUP2 CALLDATALOAD PUSH1 0x1 PUSH1 0x1 PUSH1 0xA0 SHL SUB DUP2 AND DUP2 EQ PUSH2 0x23E JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST SWAP4 SWAP3 POP POP POP JUMP JUMPDEST DUP1 DUP3 ADD DUP1 DUP3 GT ISZERO PUSH2 0x266 JUMPI PUSH4 0x4E487B71 PUSH1 0xE0 SHL PUSH1 0x0 MSTORE PUSH1 0x11 PUSH1 0x4 MSTORE PUSH1 0x24 PUSH1 0x0 REVERT JUMPDEST SWAP3 SWAP2 POP POP JUMP INVALID LOG2 PUSH5 0x6970667358 0x22 SLT KECCAK256 PUSH11 0xCD70E2709B696D93786A4E DUP6 0x2A 0xE4 SWAP14 PUSH26 0x551CEF078B16D93A6372377FB74E0D64736F6C63430008140033 ",
                        "sourceMap": "57:1097:1:-:0;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;92:40;;;;;;;;;;-1:-1:-1;92:40:1;;;;;:::i;:::-;;;;;;;;;;;;;;;;;;451:25:2;;;439:2;424:18;92:40:1;;;;;;;302:850;;;;;;;;;;;;;:::i;:::-;;139:157;;;:::i;302:850::-;363:10;339:12;354:20;;;;;;;;;;;392:11;384:42;;;;-1:-1:-1;;;384:42:1;;689:2:2;384:42:1;;;671:21:2;728:2;708:18;;;701:30;-1:-1:-1;;;747:18:2;;;740:48;805:18;;384:42:1;;;;;;;;;967:35;;952:9;;967:10;;990:7;;952:9;967:35;952:9;967:35;990:7;967:10;:35;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;951:51;;;1020:4;1012:37;;;;-1:-1:-1;;;1012:37:1;;1246:2:2;1012:37:1;;;1228:21:2;1285:2;1265:18;;;1258:30;-1:-1:-1;;;1304:18:2;;;1297:50;1364:18;;1012:37:1;1044:344:2;1012:37:1;-1:-1:-1;;1130:10:1;1144:1;1121:20;;;;;;;;;;:24;302:850::o;139:157::-;203:1;191:9;:13;183:63;;;;-1:-1:-1;;;183:63:1;;1595:2:2;183:63:1;;;1577:21:2;1634:2;1614:18;;;1607:30;1673:34;1653:18;;;1646:62;-1:-1:-1;;;1724:18:2;;;1717:35;1769:19;;183:63:1;1393:401:2;183:63:1;265:10;256:8;:20;;;;;;;;;;:33;;280:9;;256:8;:33;;280:9;;256:33;:::i;:::-;;;;-1:-1:-1;;139:157:1:o;14:286:2:-;73:6;126:2;114:9;105:7;101:23;97:32;94:52;;;142:1;139;132:12;94:52;168:23;;-1:-1:-1;;;;;220:31:2;;210:42;;200:70;;266:1;263;256:12;200:70;289:5;14:286;-1:-1:-1;;;14:286:2:o;1799:222::-;1864:9;;;1885:10;;;1882:133;;;1937:10;1932:3;1928:20;1925:1;1918:31;1972:4;1969:1;1962:15;2000:4;1997:1;1990:15;1882:133;1799:222;;;;:::o",
                        "generatedSources": [
                            {
                                "ast": {
                                    "nodeType": "YulBlock",
                                    "src": "0:2023:2",
                                    "statements": [
                                        {
                                            "nodeType": "YulBlock",
                                            "src": "6:3:2",
                                            "statements": []
                                        },
                                        {
                                            "body": {
                                                "nodeType": "YulBlock",
                                                "src": "84:216:2",
                                                "statements": [
                                                    {
                                                        "body": {
                                                            "nodeType": "YulBlock",
                                                            "src": "130:16:2",
                                                            "statements": [
                                                                {
                                                                    "expression": {
                                                                        "arguments": [
                                                                            {
                                                                                "kind": "number",
                                                                                "nodeType": "YulLiteral",
                                                                                "src": "139:1:2",
                                                                                "type": "",
                                                                                "value": "0"
                                                                            },
                                                                            {
                                                                                "kind": "number",
                                                                                "nodeType": "YulLiteral",
                                                                                "src": "142:1:2",
                                                                                "type": "",
                                                                                "value": "0"
                                                                            }
                                                                        ],
                                                                        "functionName": {
                                                                            "name": "revert",
                                                                            "nodeType": "YulIdentifier",
                                                                            "src": "132:6:2"
                                                                        },
                                                                        "nodeType": "YulFunctionCall",
                                                                        "src": "132:12:2"
                                                                    },
                                                                    "nodeType": "YulExpressionStatement",
                                                                    "src": "132:12:2"
                                                                }
                                                            ]
                                                        },
                                                        "condition": {
                                                            "arguments": [
                                                                {
                                                                    "arguments": [
                                                                        {
                                                                            "name": "dataEnd",
                                                                            "nodeType": "YulIdentifier",
                                                                            "src": "105:7:2"
                                                                        },
                                                                        {
                                                                            "name": "headStart",
                                                                            "nodeType": "YulIdentifier",
                                                                            "src": "114:9:2"
                                                                        }
                                                                    ],
                                                                    "functionName": {
                                                                        "name": "sub",
                                                                        "nodeType": "YulIdentifier",
                                                                        "src": "101:3:2"
                                                                    },
                                                                    "nodeType": "YulFunctionCall",
                                                                    "src": "101:23:2"
                                                                },
                                                                {
                                                                    "kind": "number",
                                                                    "nodeType": "YulLiteral",
                                                                    "src": "126:2:2",
                                                                    "type": "",
                                                                    "value": "32"
                                                                }
                                                            ],
                                                            "functionName": {
                                                                "name": "slt",
                                                                "nodeType": "YulIdentifier",
                                                                "src": "97:3:2"
                                                            },
                                                            "nodeType": "YulFunctionCall",
                                                            "src": "97:32:2"
                                                        },
                                                        "nodeType": "YulIf",
                                                        "src": "94:52:2"
                                                    },
                                                    {
                                                        "nodeType": "YulVariableDeclaration",
                                                        "src": "155:36:2",
                                                        "value": {
                                                            "arguments": [
                                                                {
                                                                    "name": "headStart",
                                                                    "nodeType": "YulIdentifier",
                                                                    "src": "181:9:2"
                                                                }
                                                            ],
                                                            "functionName": {
                                                                "name": "calldataload",
                                                                "nodeType": "YulIdentifier",
                                                                "src": "168:12:2"
                                                            },
                                                            "nodeType": "YulFunctionCall",
                                                            "src": "168:23:2"
                                                        },
                                                        "variables": [
                                                            {
                                                                "name": "value",
                                                                "nodeType": "YulTypedName",
                                                                "src": "159:5:2",
                                                                "type": ""
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "body": {
                                                            "nodeType": "YulBlock",
                                                            "src": "254:16:2",
                                                            "statements": [
                                                                {
                                                                    "expression": {
                                                                        "arguments": [
                                                                            {
                                                                                "kind": "number",
                                                                                "nodeType": "YulLiteral",
                                                                                "src": "263:1:2",
                                                                                "type": "",
                                                                                "value": "0"
                                                                            },
                                                                            {
                                                                                "kind": "number",
                                                                                "nodeType": "YulLiteral",
                                                                                "src": "266:1:2",
                                                                                "type": "",
                                                                                "value": "0"
                                                                            }
                                                                        ],
                                                                        "functionName": {
                                                                            "name": "revert",
                                                                            "nodeType": "YulIdentifier",
                                                                            "src": "256:6:2"
                                                                        },
                                                                        "nodeType": "YulFunctionCall",
                                                                        "src": "256:12:2"
                                                                    },
                                                                    "nodeType": "YulExpressionStatement",
                                                                    "src": "256:12:2"
                                                                }
                                                            ]
                                                        },
                                                        "condition": {
                                                            "arguments": [
                                                                {
                                                                    "arguments": [
                                                                        {
                                                                            "name": "value",
                                                                            "nodeType": "YulIdentifier",
                                                                            "src": "213:5:2"
                                                                        },
                                                                        {
                                                                            "arguments": [
                                                                                {
                                                                                    "name": "value",
                                                                                    "nodeType": "YulIdentifier",
                                                                                    "src": "224:5:2"
                                                                                },
                                                                                {
                                                                                    "arguments": [
                                                                                        {
                                                                                            "arguments": [
                                                                                                {
                                                                                                    "kind": "number",
                                                                                                    "nodeType": "YulLiteral",
                                                                                                    "src": "239:3:2",
                                                                                                    "type": "",
                                                                                                    "value": "160"
                                                                                                },
                                                                                                {
                                                                                                    "kind": "number",
                                                                                                    "nodeType": "YulLiteral",
                                                                                                    "src": "244:1:2",
                                                                                                    "type": "",
                                                                                                    "value": "1"
                                                                                                }
                                                                                            ],
                                                                                            "functionName": {
                                                                                                "name": "shl",
                                                                                                "nodeType": "YulIdentifier",
                                                                                                "src": "235:3:2"
                                                                                            },
                                                                                            "nodeType": "YulFunctionCall",
                                                                                            "src": "235:11:2"
                                                                                        },
                                                                                        {
                                                                                            "kind": "number",
                                                                                            "nodeType": "YulLiteral",
                                                                                            "src": "248:1:2",
                                                                                            "type": "",
                                                                                            "value": "1"
                                                                                        }
                                                                                    ],
                                                                                    "functionName": {
                                                                                        "name": "sub",
                                                                                        "nodeType": "YulIdentifier",
                                                                                        "src": "231:3:2"
                                                                                    },
                                                                                    "nodeType": "YulFunctionCall",
                                                                                    "src": "231:19:2"
                                                                                }
                                                                            ],
                                                                            "functionName": {
                                                                                "name": "and",
                                                                                "nodeType": "YulIdentifier",
                                                                                "src": "220:3:2"
                                                                            },
                                                                            "nodeType": "YulFunctionCall",
                                                                            "src": "220:31:2"
                                                                        }
                                                                    ],
                                                                    "functionName": {
                                                                        "name": "eq",
                                                                        "nodeType": "YulIdentifier",
                                                                        "src": "210:2:2"
                                                                    },
                                                                    "nodeType": "YulFunctionCall",
                                                                    "src": "210:42:2"
                                                                }
                                                            ],
                                                            "functionName": {
                                                                "name": "iszero",
                                                                "nodeType": "YulIdentifier",
                                                                "src": "203:6:2"
                                                            },
                                                            "nodeType": "YulFunctionCall",
                                                            "src": "203:50:2"
                                                        },
                                                        "nodeType": "YulIf",
                                                        "src": "200:70:2"
                                                    },
                                                    {
                                                        "nodeType": "YulAssignment",
                                                        "src": "279:15:2",
                                                        "value": {
                                                            "name": "value",
                                                            "nodeType": "YulIdentifier",
                                                            "src": "289:5:2"
                                                        },
                                                        "variableNames": [
                                                            {
                                                                "name": "value0",
                                                                "nodeType": "YulIdentifier",
                                                                "src": "279:6:2"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            "name": "abi_decode_tuple_t_address",
                                            "nodeType": "YulFunctionDefinition",
                                            "parameters": [
                                                {
                                                    "name": "headStart",
                                                    "nodeType": "YulTypedName",
                                                    "src": "50:9:2",
                                                    "type": ""
                                                },
                                                {
                                                    "name": "dataEnd",
                                                    "nodeType": "YulTypedName",
                                                    "src": "61:7:2",
                                                    "type": ""
                                                }
                                            ],
                                            "returnVariables": [
                                                {
                                                    "name": "value0",
                                                    "nodeType": "YulTypedName",
                                                    "src": "73:6:2",
                                                    "type": ""
                                                }
                                            ],
                                            "src": "14:286:2"
                                        },
                                        {
                                            "body": {
                                                "nodeType": "YulBlock",
                                                "src": "406:76:2",
                                                "statements": [
                                                    {
                                                        "nodeType": "YulAssignment",
                                                        "src": "416:26:2",
                                                        "value": {
                                                            "arguments": [
                                                                {
                                                                    "name": "headStart",
                                                                    "nodeType": "YulIdentifier",
                                                                    "src": "428:9:2"
                                                                },
                                                                {
                                                                    "kind": "number",
                                                                    "nodeType": "YulLiteral",
                                                                    "src": "439:2:2",
                                                                    "type": "",
                                                                    "value": "32"
                                                                }
                                                            ],
                                                            "functionName": {
                                                                "name": "add",
                                                                "nodeType": "YulIdentifier",
                                                                "src": "424:3:2"
                                                            },
                                                            "nodeType": "YulFunctionCall",
                                                            "src": "424:18:2"
                                                        },
                                                        "variableNames": [
                                                            {
                                                                "name": "tail",
                                                                "nodeType": "YulIdentifier",
                                                                "src": "416:4:2"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "expression": {
                                                            "arguments": [
                                                                {
                                                                    "name": "headStart",
                                                                    "nodeType": "YulIdentifier",
                                                                    "src": "458:9:2"
                                                                },
                                                                {
                                                                    "name": "value0",
                                                                    "nodeType": "YulIdentifier",
                                                                    "src": "469:6:2"
                                                                }
                                                            ],
                                                            "functionName": {
                                                                "name": "mstore",
                                                                "nodeType": "YulIdentifier",
                                                                "src": "451:6:2"
                                                            },
                                                            "nodeType": "YulFunctionCall",
                                                            "src": "451:25:2"
                                                        },
                                                        "nodeType": "YulExpressionStatement",
                                                        "src": "451:25:2"
                                                    }
                                                ]
                                            },
                                            "name": "abi_encode_tuple_t_uint256__to_t_uint256__fromStack_reversed",
                                            "nodeType": "YulFunctionDefinition",
                                            "parameters": [
                                                {
                                                    "name": "headStart",
                                                    "nodeType": "YulTypedName",
                                                    "src": "375:9:2",
                                                    "type": ""
                                                },
                                                {
                                                    "name": "value0",
                                                    "nodeType": "YulTypedName",
                                                    "src": "386:6:2",
                                                    "type": ""
                                                }
                                            ],
                                            "returnVariables": [
                                                {
                                                    "name": "tail",
                                                    "nodeType": "YulTypedName",
                                                    "src": "397:4:2",
                                                    "type": ""
                                                }
                                            ],
                                            "src": "305:177:2"
                                        },
                                        {
                                            "body": {
                                                "nodeType": "YulBlock",
                                                "src": "661:168:2",
                                                "statements": [
                                                    {
                                                        "expression": {
                                                            "arguments": [
                                                                {
                                                                    "name": "headStart",
                                                                    "nodeType": "YulIdentifier",
                                                                    "src": "678:9:2"
                                                                },
                                                                {
                                                                    "kind": "number",
                                                                    "nodeType": "YulLiteral",
                                                                    "src": "689:2:2",
                                                                    "type": "",
                                                                    "value": "32"
                                                                }
                                                            ],
                                                            "functionName": {
                                                                "name": "mstore",
                                                                "nodeType": "YulIdentifier",
                                                                "src": "671:6:2"
                                                            },
                                                            "nodeType": "YulFunctionCall",
                                                            "src": "671:21:2"
                                                        },
                                                        "nodeType": "YulExpressionStatement",
                                                        "src": "671:21:2"
                                                    },
                                                    {
                                                        "expression": {
                                                            "arguments": [
                                                                {
                                                                    "arguments": [
                                                                        {
                                                                            "name": "headStart",
                                                                            "nodeType": "YulIdentifier",
                                                                            "src": "712:9:2"
                                                                        },
                                                                        {
                                                                            "kind": "number",
                                                                            "nodeType": "YulLiteral",
                                                                            "src": "723:2:2",
                                                                            "type": "",
                                                                            "value": "32"
                                                                        }
                                                                    ],
                                                                    "functionName": {
                                                                        "name": "add",
                                                                        "nodeType": "YulIdentifier",
                                                                        "src": "708:3:2"
                                                                    },
                                                                    "nodeType": "YulFunctionCall",
                                                                    "src": "708:18:2"
                                                                },
                                                                {
                                                                    "kind": "number",
                                                                    "nodeType": "YulLiteral",
                                                                    "src": "728:2:2",
                                                                    "type": "",
                                                                    "value": "18"
                                                                }
                                                            ],
                                                            "functionName": {
                                                                "name": "mstore",
                                                                "nodeType": "YulIdentifier",
                                                                "src": "701:6:2"
                                                            },
                                                            "nodeType": "YulFunctionCall",
                                                            "src": "701:30:2"
                                                        },
                                                        "nodeType": "YulExpressionStatement",
                                                        "src": "701:30:2"
                                                    },
                                                    {
                                                        "expression": {
                                                            "arguments": [
                                                                {
                                                                    "arguments": [
                                                                        {
                                                                            "name": "headStart",
                                                                            "nodeType": "YulIdentifier",
                                                                            "src": "751:9:2"
                                                                        },
                                                                        {
                                                                            "kind": "number",
                                                                            "nodeType": "YulLiteral",
                                                                            "src": "762:2:2",
                                                                            "type": "",
                                                                            "value": "64"
                                                                        }
                                                                    ],
                                                                    "functionName": {
                                                                        "name": "add",
                                                                        "nodeType": "YulIdentifier",
                                                                        "src": "747:3:2"
                                                                    },
                                                                    "nodeType": "YulFunctionCall",
                                                                    "src": "747:18:2"
                                                                },
                                                                {
                                                                    "hexValue": "496e73756666696369656e742066756e6473",
                                                                    "kind": "string",
                                                                    "nodeType": "YulLiteral",
                                                                    "src": "767:20:2",
                                                                    "type": "",
                                                                    "value": "Insufficient funds"
                                                                }
                                                            ],
                                                            "functionName": {
                                                                "name": "mstore",
                                                                "nodeType": "YulIdentifier",
                                                                "src": "740:6:2"
                                                            },
                                                            "nodeType": "YulFunctionCall",
                                                            "src": "740:48:2"
                                                        },
                                                        "nodeType": "YulExpressionStatement",
                                                        "src": "740:48:2"
                                                    },
                                                    {
                                                        "nodeType": "YulAssignment",
                                                        "src": "797:26:2",
                                                        "value": {
                                                            "arguments": [
                                                                {
                                                                    "name": "headStart",
                                                                    "nodeType": "YulIdentifier",
                                                                    "src": "809:9:2"
                                                                },
                                                                {
                                                                    "kind": "number",
                                                                    "nodeType": "YulLiteral",
                                                                    "src": "820:2:2",
                                                                    "type": "",
                                                                    "value": "96"
                                                                }
                                                            ],
                                                            "functionName": {
                                                                "name": "add",
                                                                "nodeType": "YulIdentifier",
                                                                "src": "805:3:2"
                                                            },
                                                            "nodeType": "YulFunctionCall",
                                                            "src": "805:18:2"
                                                        },
                                                        "variableNames": [
                                                            {
                                                                "name": "tail",
                                                                "nodeType": "YulIdentifier",
                                                                "src": "797:4:2"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            "name": "abi_encode_tuple_t_stringliteral_63452317cb6d597bef833f023ed2962a84dbd24c571e27629ed1e3056d6cfd8d__to_t_string_memory_ptr__fromStack_reversed",
                                            "nodeType": "YulFunctionDefinition",
                                            "parameters": [
                                                {
                                                    "name": "headStart",
                                                    "nodeType": "YulTypedName",
                                                    "src": "638:9:2",
                                                    "type": ""
                                                }
                                            ],
                                            "returnVariables": [
                                                {
                                                    "name": "tail",
                                                    "nodeType": "YulTypedName",
                                                    "src": "652:4:2",
                                                    "type": ""
                                                }
                                            ],
                                            "src": "487:342:2"
                                        },
                                        {
                                            "body": {
                                                "nodeType": "YulBlock",
                                                "src": "1025:14:2",
                                                "statements": [
                                                    {
                                                        "nodeType": "YulAssignment",
                                                        "src": "1027:10:2",
                                                        "value": {
                                                            "name": "pos",
                                                            "nodeType": "YulIdentifier",
                                                            "src": "1034:3:2"
                                                        },
                                                        "variableNames": [
                                                            {
                                                                "name": "end",
                                                                "nodeType": "YulIdentifier",
                                                                "src": "1027:3:2"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            "name": "abi_encode_tuple_packed_t_stringliteral_c5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470__to_t_bytes_memory_ptr__nonPadded_inplace_fromStack_reversed",
                                            "nodeType": "YulFunctionDefinition",
                                            "parameters": [
                                                {
                                                    "name": "pos",
                                                    "nodeType": "YulTypedName",
                                                    "src": "1009:3:2",
                                                    "type": ""
                                                }
                                            ],
                                            "returnVariables": [
                                                {
                                                    "name": "end",
                                                    "nodeType": "YulTypedName",
                                                    "src": "1017:3:2",
                                                    "type": ""
                                                }
                                            ],
                                            "src": "834:205:2"
                                        },
                                        {
                                            "body": {
                                                "nodeType": "YulBlock",
                                                "src": "1218:170:2",
                                                "statements": [
                                                    {
                                                        "expression": {
                                                            "arguments": [
                                                                {
                                                                    "name": "headStart",
                                                                    "nodeType": "YulIdentifier",
                                                                    "src": "1235:9:2"
                                                                },
                                                                {
                                                                    "kind": "number",
                                                                    "nodeType": "YulLiteral",
                                                                    "src": "1246:2:2",
                                                                    "type": "",
                                                                    "value": "32"
                                                                }
                                                            ],
                                                            "functionName": {
                                                                "name": "mstore",
                                                                "nodeType": "YulIdentifier",
                                                                "src": "1228:6:2"
                                                            },
                                                            "nodeType": "YulFunctionCall",
                                                            "src": "1228:21:2"
                                                        },
                                                        "nodeType": "YulExpressionStatement",
                                                        "src": "1228:21:2"
                                                    },
                                                    {
                                                        "expression": {
                                                            "arguments": [
                                                                {
                                                                    "arguments": [
                                                                        {
                                                                            "name": "headStart",
                                                                            "nodeType": "YulIdentifier",
                                                                            "src": "1269:9:2"
                                                                        },
                                                                        {
                                                                            "kind": "number",
                                                                            "nodeType": "YulLiteral",
                                                                            "src": "1280:2:2",
                                                                            "type": "",
                                                                            "value": "32"
                                                                        }
                                                                    ],
                                                                    "functionName": {
                                                                        "name": "add",
                                                                        "nodeType": "YulIdentifier",
                                                                        "src": "1265:3:2"
                                                                    },
                                                                    "nodeType": "YulFunctionCall",
                                                                    "src": "1265:18:2"
                                                                },
                                                                {
                                                                    "kind": "number",
                                                                    "nodeType": "YulLiteral",
                                                                    "src": "1285:2:2",
                                                                    "type": "",
                                                                    "value": "20"
                                                                }
                                                            ],
                                                            "functionName": {
                                                                "name": "mstore",
                                                                "nodeType": "YulIdentifier",
                                                                "src": "1258:6:2"
                                                            },
                                                            "nodeType": "YulFunctionCall",
                                                            "src": "1258:30:2"
                                                        },
                                                        "nodeType": "YulExpressionStatement",
                                                        "src": "1258:30:2"
                                                    },
                                                    {
                                                        "expression": {
                                                            "arguments": [
                                                                {
                                                                    "arguments": [
                                                                        {
                                                                            "name": "headStart",
                                                                            "nodeType": "YulIdentifier",
                                                                            "src": "1308:9:2"
                                                                        },
                                                                        {
                                                                            "kind": "number",
                                                                            "nodeType": "YulLiteral",
                                                                            "src": "1319:2:2",
                                                                            "type": "",
                                                                            "value": "64"
                                                                        }
                                                                    ],
                                                                    "functionName": {
                                                                        "name": "add",
                                                                        "nodeType": "YulIdentifier",
                                                                        "src": "1304:3:2"
                                                                    },
                                                                    "nodeType": "YulFunctionCall",
                                                                    "src": "1304:18:2"
                                                                },
                                                                {
                                                                    "hexValue": "4661696c656420746f2073656e64204574686572",
                                                                    "kind": "string",
                                                                    "nodeType": "YulLiteral",
                                                                    "src": "1324:22:2",
                                                                    "type": "",
                                                                    "value": "Failed to send Ether"
                                                                }
                                                            ],
                                                            "functionName": {
                                                                "name": "mstore",
                                                                "nodeType": "YulIdentifier",
                                                                "src": "1297:6:2"
                                                            },
                                                            "nodeType": "YulFunctionCall",
                                                            "src": "1297:50:2"
                                                        },
                                                        "nodeType": "YulExpressionStatement",
                                                        "src": "1297:50:2"
                                                    },
                                                    {
                                                        "nodeType": "YulAssignment",
                                                        "src": "1356:26:2",
                                                        "value": {
                                                            "arguments": [
                                                                {
                                                                    "name": "headStart",
                                                                    "nodeType": "YulIdentifier",
                                                                    "src": "1368:9:2"
                                                                },
                                                                {
                                                                    "kind": "number",
                                                                    "nodeType": "YulLiteral",
                                                                    "src": "1379:2:2",
                                                                    "type": "",
                                                                    "value": "96"
                                                                }
                                                            ],
                                                            "functionName": {
                                                                "name": "add",
                                                                "nodeType": "YulIdentifier",
                                                                "src": "1364:3:2"
                                                            },
                                                            "nodeType": "YulFunctionCall",
                                                            "src": "1364:18:2"
                                                        },
                                                        "variableNames": [
                                                            {
                                                                "name": "tail",
                                                                "nodeType": "YulIdentifier",
                                                                "src": "1356:4:2"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            "name": "abi_encode_tuple_t_stringliteral_445140255c9d889994129d349e64078d6f76b4b37ec896948f7e858f9b8a0dcb__to_t_string_memory_ptr__fromStack_reversed",
                                            "nodeType": "YulFunctionDefinition",
                                            "parameters": [
                                                {
                                                    "name": "headStart",
                                                    "nodeType": "YulTypedName",
                                                    "src": "1195:9:2",
                                                    "type": ""
                                                }
                                            ],
                                            "returnVariables": [
                                                {
                                                    "name": "tail",
                                                    "nodeType": "YulTypedName",
                                                    "src": "1209:4:2",
                                                    "type": ""
                                                }
                                            ],
                                            "src": "1044:344:2"
                                        },
                                        {
                                            "body": {
                                                "nodeType": "YulBlock",
                                                "src": "1567:227:2",
                                                "statements": [
                                                    {
                                                        "expression": {
                                                            "arguments": [
                                                                {
                                                                    "name": "headStart",
                                                                    "nodeType": "YulIdentifier",
                                                                    "src": "1584:9:2"
                                                                },
                                                                {
                                                                    "kind": "number",
                                                                    "nodeType": "YulLiteral",
                                                                    "src": "1595:2:2",
                                                                    "type": "",
                                                                    "value": "32"
                                                                }
                                                            ],
                                                            "functionName": {
                                                                "name": "mstore",
                                                                "nodeType": "YulIdentifier",
                                                                "src": "1577:6:2"
                                                            },
                                                            "nodeType": "YulFunctionCall",
                                                            "src": "1577:21:2"
                                                        },
                                                        "nodeType": "YulExpressionStatement",
                                                        "src": "1577:21:2"
                                                    },
                                                    {
                                                        "expression": {
                                                            "arguments": [
                                                                {
                                                                    "arguments": [
                                                                        {
                                                                            "name": "headStart",
                                                                            "nodeType": "YulIdentifier",
                                                                            "src": "1618:9:2"
                                                                        },
                                                                        {
                                                                            "kind": "number",
                                                                            "nodeType": "YulLiteral",
                                                                            "src": "1629:2:2",
                                                                            "type": "",
                                                                            "value": "32"
                                                                        }
                                                                    ],
                                                                    "functionName": {
                                                                        "name": "add",
                                                                        "nodeType": "YulIdentifier",
                                                                        "src": "1614:3:2"
                                                                    },
                                                                    "nodeType": "YulFunctionCall",
                                                                    "src": "1614:18:2"
                                                                },
                                                                {
                                                                    "kind": "number",
                                                                    "nodeType": "YulLiteral",
                                                                    "src": "1634:2:2",
                                                                    "type": "",
                                                                    "value": "37"
                                                                }
                                                            ],
                                                            "functionName": {
                                                                "name": "mstore",
                                                                "nodeType": "YulIdentifier",
                                                                "src": "1607:6:2"
                                                            },
                                                            "nodeType": "YulFunctionCall",
                                                            "src": "1607:30:2"
                                                        },
                                                        "nodeType": "YulExpressionStatement",
                                                        "src": "1607:30:2"
                                                    },
                                                    {
                                                        "expression": {
                                                            "arguments": [
                                                                {
                                                                    "arguments": [
                                                                        {
                                                                            "name": "headStart",
                                                                            "nodeType": "YulIdentifier",
                                                                            "src": "1657:9:2"
                                                                        },
                                                                        {
                                                                            "kind": "number",
                                                                            "nodeType": "YulLiteral",
                                                                            "src": "1668:2:2",
                                                                            "type": "",
                                                                            "value": "64"
                                                                        }
                                                                    ],
                                                                    "functionName": {
                                                                        "name": "add",
                                                                        "nodeType": "YulIdentifier",
                                                                        "src": "1653:3:2"
                                                                    },
                                                                    "nodeType": "YulFunctionCall",
                                                                    "src": "1653:18:2"
                                                                },
                                                                {
                                                                    "hexValue": "4465706f73697420616d6f756e74206d75737420626520677265617465722074",
                                                                    "kind": "string",
                                                                    "nodeType": "YulLiteral",
                                                                    "src": "1673:34:2",
                                                                    "type": "",
                                                                    "value": "Deposit amount must be greater t"
                                                                }
                                                            ],
                                                            "functionName": {
                                                                "name": "mstore",
                                                                "nodeType": "YulIdentifier",
                                                                "src": "1646:6:2"
                                                            },
                                                            "nodeType": "YulFunctionCall",
                                                            "src": "1646:62:2"
                                                        },
                                                        "nodeType": "YulExpressionStatement",
                                                        "src": "1646:62:2"
                                                    },
                                                    {
                                                        "expression": {
                                                            "arguments": [
                                                                {
                                                                    "arguments": [
                                                                        {
                                                                            "name": "headStart",
                                                                            "nodeType": "YulIdentifier",
                                                                            "src": "1728:9:2"
                                                                        },
                                                                        {
                                                                            "kind": "number",
                                                                            "nodeType": "YulLiteral",
                                                                            "src": "1739:2:2",
                                                                            "type": "",
                                                                            "value": "96"
                                                                        }
                                                                    ],
                                                                    "functionName": {
                                                                        "name": "add",
                                                                        "nodeType": "YulIdentifier",
                                                                        "src": "1724:3:2"
                                                                    },
                                                                    "nodeType": "YulFunctionCall",
                                                                    "src": "1724:18:2"
                                                                },
                                                                {
                                                                    "hexValue": "68616e2030",
                                                                    "kind": "string",
                                                                    "nodeType": "YulLiteral",
                                                                    "src": "1744:7:2",
                                                                    "type": "",
                                                                    "value": "han 0"
                                                                }
                                                            ],
                                                            "functionName": {
                                                                "name": "mstore",
                                                                "nodeType": "YulIdentifier",
                                                                "src": "1717:6:2"
                                                            },
                                                            "nodeType": "YulFunctionCall",
                                                            "src": "1717:35:2"
                                                        },
                                                        "nodeType": "YulExpressionStatement",
                                                        "src": "1717:35:2"
                                                    },
                                                    {
                                                        "nodeType": "YulAssignment",
                                                        "src": "1761:27:2",
                                                        "value": {
                                                            "arguments": [
                                                                {
                                                                    "name": "headStart",
                                                                    "nodeType": "YulIdentifier",
                                                                    "src": "1773:9:2"
                                                                },
                                                                {
                                                                    "kind": "number",
                                                                    "nodeType": "YulLiteral",
                                                                    "src": "1784:3:2",
                                                                    "type": "",
                                                                    "value": "128"
                                                                }
                                                            ],
                                                            "functionName": {
                                                                "name": "add",
                                                                "nodeType": "YulIdentifier",
                                                                "src": "1769:3:2"
                                                            },
                                                            "nodeType": "YulFunctionCall",
                                                            "src": "1769:19:2"
                                                        },
                                                        "variableNames": [
                                                            {
                                                                "name": "tail",
                                                                "nodeType": "YulIdentifier",
                                                                "src": "1761:4:2"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            "name": "abi_encode_tuple_t_stringliteral_1cf5370f25734823c5feac6853b836d05520862485f150310f24689e28c1f9e6__to_t_string_memory_ptr__fromStack_reversed",
                                            "nodeType": "YulFunctionDefinition",
                                            "parameters": [
                                                {
                                                    "name": "headStart",
                                                    "nodeType": "YulTypedName",
                                                    "src": "1544:9:2",
                                                    "type": ""
                                                }
                                            ],
                                            "returnVariables": [
                                                {
                                                    "name": "tail",
                                                    "nodeType": "YulTypedName",
                                                    "src": "1558:4:2",
                                                    "type": ""
                                                }
                                            ],
                                            "src": "1393:401:2"
                                        },
                                        {
                                            "body": {
                                                "nodeType": "YulBlock",
                                                "src": "1847:174:2",
                                                "statements": [
                                                    {
                                                        "nodeType": "YulAssignment",
                                                        "src": "1857:16:2",
                                                        "value": {
                                                            "arguments": [
                                                                {
                                                                    "name": "x",
                                                                    "nodeType": "YulIdentifier",
                                                                    "src": "1868:1:2"
                                                                },
                                                                {
                                                                    "name": "y",
                                                                    "nodeType": "YulIdentifier",
                                                                    "src": "1871:1:2"
                                                                }
                                                            ],
                                                            "functionName": {
                                                                "name": "add",
                                                                "nodeType": "YulIdentifier",
                                                                "src": "1864:3:2"
                                                            },
                                                            "nodeType": "YulFunctionCall",
                                                            "src": "1864:9:2"
                                                        },
                                                        "variableNames": [
                                                            {
                                                                "name": "sum",
                                                                "nodeType": "YulIdentifier",
                                                                "src": "1857:3:2"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "body": {
                                                            "nodeType": "YulBlock",
                                                            "src": "1904:111:2",
                                                            "statements": [
                                                                {
                                                                    "expression": {
                                                                        "arguments": [
                                                                            {
                                                                                "kind": "number",
                                                                                "nodeType": "YulLiteral",
                                                                                "src": "1925:1:2",
                                                                                "type": "",
                                                                                "value": "0"
                                                                            },
                                                                            {
                                                                                "arguments": [
                                                                                    {
                                                                                        "kind": "number",
                                                                                        "nodeType": "YulLiteral",
                                                                                        "src": "1932:3:2",
                                                                                        "type": "",
                                                                                        "value": "224"
                                                                                    },
                                                                                    {
                                                                                        "kind": "number",
                                                                                        "nodeType": "YulLiteral",
                                                                                        "src": "1937:10:2",
                                                                                        "type": "",
                                                                                        "value": "0x4e487b71"
                                                                                    }
                                                                                ],
                                                                                "functionName": {
                                                                                    "name": "shl",
                                                                                    "nodeType": "YulIdentifier",
                                                                                    "src": "1928:3:2"
                                                                                },
                                                                                "nodeType": "YulFunctionCall",
                                                                                "src": "1928:20:2"
                                                                            }
                                                                        ],
                                                                        "functionName": {
                                                                            "name": "mstore",
                                                                            "nodeType": "YulIdentifier",
                                                                            "src": "1918:6:2"
                                                                        },
                                                                        "nodeType": "YulFunctionCall",
                                                                        "src": "1918:31:2"
                                                                    },
                                                                    "nodeType": "YulExpressionStatement",
                                                                    "src": "1918:31:2"
                                                                },
                                                                {
                                                                    "expression": {
                                                                        "arguments": [
                                                                            {
                                                                                "kind": "number",
                                                                                "nodeType": "YulLiteral",
                                                                                "src": "1969:1:2",
                                                                                "type": "",
                                                                                "value": "4"
                                                                            },
                                                                            {
                                                                                "kind": "number",
                                                                                "nodeType": "YulLiteral",
                                                                                "src": "1972:4:2",
                                                                                "type": "",
                                                                                "value": "0x11"
                                                                            }
                                                                        ],
                                                                        "functionName": {
                                                                            "name": "mstore",
                                                                            "nodeType": "YulIdentifier",
                                                                            "src": "1962:6:2"
                                                                        },
                                                                        "nodeType": "YulFunctionCall",
                                                                        "src": "1962:15:2"
                                                                    },
                                                                    "nodeType": "YulExpressionStatement",
                                                                    "src": "1962:15:2"
                                                                },
                                                                {
                                                                    "expression": {
                                                                        "arguments": [
                                                                            {
                                                                                "kind": "number",
                                                                                "nodeType": "YulLiteral",
                                                                                "src": "1997:1:2",
                                                                                "type": "",
                                                                                "value": "0"
                                                                            },
                                                                            {
                                                                                "kind": "number",
                                                                                "nodeType": "YulLiteral",
                                                                                "src": "2000:4:2",
                                                                                "type": "",
                                                                                "value": "0x24"
                                                                            }
                                                                        ],
                                                                        "functionName": {
                                                                            "name": "revert",
                                                                            "nodeType": "YulIdentifier",
                                                                            "src": "1990:6:2"
                                                                        },
                                                                        "nodeType": "YulFunctionCall",
                                                                        "src": "1990:15:2"
                                                                    },
                                                                    "nodeType": "YulExpressionStatement",
                                                                    "src": "1990:15:2"
                                                                }
                                                            ]
                                                        },
                                                        "condition": {
                                                            "arguments": [
                                                                {
                                                                    "name": "x",
                                                                    "nodeType": "YulIdentifier",
                                                                    "src": "1888:1:2"
                                                                },
                                                                {
                                                                    "name": "sum",
                                                                    "nodeType": "YulIdentifier",
                                                                    "src": "1891:3:2"
                                                                }
                                                            ],
                                                            "functionName": {
                                                                "name": "gt",
                                                                "nodeType": "YulIdentifier",
                                                                "src": "1885:2:2"
                                                            },
                                                            "nodeType": "YulFunctionCall",
                                                            "src": "1885:10:2"
                                                        },
                                                        "nodeType": "YulIf",
                                                        "src": "1882:133:2"
                                                    }
                                                ]
                                            },
                                            "name": "checked_add_t_uint256",
                                            "nodeType": "YulFunctionDefinition",
                                            "parameters": [
                                                {
                                                    "name": "x",
                                                    "nodeType": "YulTypedName",
                                                    "src": "1830:1:2",
                                                    "type": ""
                                                },
                                                {
                                                    "name": "y",
                                                    "nodeType": "YulTypedName",
                                                    "src": "1833:1:2",
                                                    "type": ""
                                                }
                                            ],
                                            "returnVariables": [
                                                {
                                                    "name": "sum",
                                                    "nodeType": "YulTypedName",
                                                    "src": "1839:3:2",
                                                    "type": ""
                                                }
                                            ],
                                            "src": "1799:222:2"
                                        }
                                    ]
                                },
                                "contents": "{    { }    function abi_decode_tuple_t_address(headStart, dataEnd) -> value0    {        if slt(sub(dataEnd, headStart), 32) { revert(0, 0) }        let value := calldataload(headStart)        if iszero(eq(value, and(value, sub(shl(160, 1), 1)))) { revert(0, 0) }        value0 := value    }    function abi_encode_tuple_t_uint256__to_t_uint256__fromStack_reversed(headStart, value0) -> tail    {        tail := add(headStart, 32)        mstore(headStart, value0)    }    function abi_encode_tuple_t_stringliteral_63452317cb6d597bef833f023ed2962a84dbd24c571e27629ed1e3056d6cfd8d__to_t_string_memory_ptr__fromStack_reversed(headStart) -> tail    {        mstore(headStart, 32)        mstore(add(headStart, 32), 18)        mstore(add(headStart, 64), Insufficient funds)        tail := add(headStart, 96)    }    function abi_encode_tuple_packed_t_stringliteral_c5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470__to_t_bytes_memory_ptr__nonPadded_inplace_fromStack_reversed(pos) -> end    { end := pos }    function abi_encode_tuple_t_stringliteral_445140255c9d889994129d349e64078d6f76b4b37ec896948f7e858f9b8a0dcb__to_t_string_memory_ptr__fromStack_reversed(headStart) -> tail    {        mstore(headStart, 32)        mstore(add(headStart, 32), 20)        mstore(add(headStart, 64), Failed to send Ether)        tail := add(headStart, 96)    }    function abi_encode_tuple_t_stringliteral_1cf5370f25734823c5feac6853b836d05520862485f150310f24689e28c1f9e6__to_t_string_memory_ptr__fromStack_reversed(headStart) -> tail    {        mstore(headStart, 32)        mstore(add(headStart, 32), 37)        mstore(add(headStart, 64), Deposit amount must be greater t)        mstore(add(headStart, 96), han 0)        tail := add(headStart, 128)    }    function checked_add_t_uint256(x, y) -> sum    {        sum := add(x, y)        if gt(x, sum)        {            mstore(0, shl(224, 0x4e487b71))            mstore(4, 0x11)            revert(0, 0x24)        }    }}",
                                "id": 2,
                                "language": "Yul",
                                "name": "#utility.yul"
                            }
                        ],
                        "linkReferences": {}
                    },
                    "methodIdentifiers": {
                        "balances(address)": "27e235e3",
                        "deposit()": "d0e30db0",
                        "withdraw()": "3ccfd60b"
                    }
                }
            }
        }
    }
}"""
    return json.loads(ast_json)


def test_missing_reentrancy_guard(vulnerable_ast):
    ast_json, src_file_list = reduce_json(vulnerable_ast)
    results = process_yaml(
        "eburger/templates/missing_reentrancy_guard.yaml",
        ast_json,
        src_file_list,
    )
    assert "Line 12 Columns 5-33" in results["results"][0]["lines"]
