import json
import pytest
from eburger.serializer import reduce_json
from eburger.yaml_parser import process_yaml


@pytest.fixture
def vulnerable_ast() -> tuple[dict, list]:
    ast_json = """{
    "sources": {
        "lib/chainlink-brownie-contracts/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol": {
            "id": 0,
            "ast": {
                "absolutePath": "lib/chainlink-brownie-contracts/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol",
                "id": 46,
                "exportedSymbols": {
                    "AggregatorV3Interface": [
                        45
                    ]
                },
                "nodeType": "SourceUnit",
                "src": "32:929:0",
                "nodes": [
                    {
                        "id": 1,
                        "nodeType": "PragmaDirective",
                        "src": "32:23:0",
                        "nodes": [],
                        "literals": [
                            "solidity",
                            "^",
                            "0.8",
                            ".0"
                        ]
                    },
                    {
                        "id": 45,
                        "nodeType": "ContractDefinition",
                        "src": "57:903:0",
                        "nodes": [
                            {
                                "id": 6,
                                "nodeType": "FunctionDefinition",
                                "src": "94:74:0",
                                "nodes": [],
                                "functionSelector": "313ce567",
                                "implemented": false,
                                "kind": "function",
                                "modifiers": [],
                                "name": "decimals",
                                "nameLocation": "103:8:0",
                                "parameters": {
                                    "id": 2,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "111:2:0"
                                },
                                "returnParameters": {
                                    "id": 5,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 4,
                                            "mutability": "mutable",
                                            "name": "",
                                            "nameLocation": "-1:-1:-1",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 6,
                                            "src": "156:5:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_uint8",
                                                "typeString": "uint8"
                                            },
                                            "typeName": {
                                                "id": 3,
                                                "name": "uint8",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "156:5:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint8",
                                                    "typeString": "uint8"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "148:19:0"
                                },
                                "scope": 45,
                                "stateMutability": "view",
                                "virtual": false,
                                "visibility": "external"
                            },
                            {
                                "id": 11,
                                "nodeType": "FunctionDefinition",
                                "src": "172:85:0",
                                "nodes": [],
                                "functionSelector": "7284e416",
                                "implemented": false,
                                "kind": "function",
                                "modifiers": [],
                                "name": "description",
                                "nameLocation": "181:11:0",
                                "parameters": {
                                    "id": 7,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "192:2:0"
                                },
                                "returnParameters": {
                                    "id": 10,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 9,
                                            "mutability": "mutable",
                                            "name": "",
                                            "nameLocation": "-1:-1:-1",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 11,
                                            "src": "237:13:0",
                                            "stateVariable": false,
                                            "storageLocation": "memory",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_string_memory_ptr",
                                                "typeString": "string"
                                            },
                                            "typeName": {
                                                "id": 8,
                                                "name": "string",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "237:6:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_string_storage_ptr",
                                                    "typeString": "string"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "229:27:0"
                                },
                                "scope": 45,
                                "stateMutability": "view",
                                "virtual": false,
                                "visibility": "external"
                            },
                            {
                                "id": 16,
                                "nodeType": "FunctionDefinition",
                                "src": "261:75:0",
                                "nodes": [],
                                "functionSelector": "54fd4d50",
                                "implemented": false,
                                "kind": "function",
                                "modifiers": [],
                                "name": "version",
                                "nameLocation": "270:7:0",
                                "parameters": {
                                    "id": 12,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "277:2:0"
                                },
                                "returnParameters": {
                                    "id": 15,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 14,
                                            "mutability": "mutable",
                                            "name": "",
                                            "nameLocation": "-1:-1:-1",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 16,
                                            "src": "322:7:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_uint256",
                                                "typeString": "uint256"
                                            },
                                            "typeName": {
                                                "id": 13,
                                                "name": "uint256",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "322:7:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint256",
                                                    "typeString": "uint256"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "314:21:0"
                                },
                                "scope": 45,
                                "stateMutability": "view",
                                "virtual": false,
                                "visibility": "external"
                            },
                            {
                                "id": 31,
                                "nodeType": "FunctionDefinition",
                                "src": "551:211:0",
                                "nodes": [],
                                "functionSelector": "9a6fc8f5",
                                "implemented": false,
                                "kind": "function",
                                "modifiers": [],
                                "name": "getRoundData",
                                "nameLocation": "560:12:0",
                                "parameters": {
                                    "id": 19,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 18,
                                            "mutability": "mutable",
                                            "name": "_roundId",
                                            "nameLocation": "585:8:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 31,
                                            "src": "578:15:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_uint80",
                                                "typeString": "uint80"
                                            },
                                            "typeName": {
                                                "id": 17,
                                                "name": "uint80",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "578:6:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint80",
                                                    "typeString": "uint80"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "572:25:0"
                                },
                                "returnParameters": {
                                    "id": 30,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 21,
                                            "mutability": "mutable",
                                            "name": "roundId",
                                            "nameLocation": "647:7:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 31,
                                            "src": "640:14:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_uint80",
                                                "typeString": "uint80"
                                            },
                                            "typeName": {
                                                "id": 20,
                                                "name": "uint80",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "640:6:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint80",
                                                    "typeString": "uint80"
                                                }
                                            },
                                            "visibility": "internal"
                                        },
                                        {
                                            "constant": false,
                                            "id": 23,
                                            "mutability": "mutable",
                                            "name": "answer",
                                            "nameLocation": "669:6:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 31,
                                            "src": "662:13:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_int256",
                                                "typeString": "int256"
                                            },
                                            "typeName": {
                                                "id": 22,
                                                "name": "int256",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "662:6:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_int256",
                                                    "typeString": "int256"
                                                }
                                            },
                                            "visibility": "internal"
                                        },
                                        {
                                            "constant": false,
                                            "id": 25,
                                            "mutability": "mutable",
                                            "name": "startedAt",
                                            "nameLocation": "691:9:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 31,
                                            "src": "683:17:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_uint256",
                                                "typeString": "uint256"
                                            },
                                            "typeName": {
                                                "id": 24,
                                                "name": "uint256",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "683:7:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint256",
                                                    "typeString": "uint256"
                                                }
                                            },
                                            "visibility": "internal"
                                        },
                                        {
                                            "constant": false,
                                            "id": 27,
                                            "mutability": "mutable",
                                            "name": "updatedAt",
                                            "nameLocation": "716:9:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 31,
                                            "src": "708:17:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_uint256",
                                                "typeString": "uint256"
                                            },
                                            "typeName": {
                                                "id": 26,
                                                "name": "uint256",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "708:7:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint256",
                                                    "typeString": "uint256"
                                                }
                                            },
                                            "visibility": "internal"
                                        },
                                        {
                                            "constant": false,
                                            "id": 29,
                                            "mutability": "mutable",
                                            "name": "answeredInRound",
                                            "nameLocation": "740:15:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 31,
                                            "src": "733:22:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_uint80",
                                                "typeString": "uint80"
                                            },
                                            "typeName": {
                                                "id": 28,
                                                "name": "uint80",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "733:6:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint80",
                                                    "typeString": "uint80"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "632:129:0"
                                },
                                "scope": 45,
                                "stateMutability": "view",
                                "virtual": false,
                                "visibility": "external"
                            },
                            {
                                "id": 44,
                                "nodeType": "FunctionDefinition",
                                "src": "766:191:0",
                                "nodes": [],
                                "functionSelector": "feaf968c",
                                "implemented": false,
                                "kind": "function",
                                "modifiers": [],
                                "name": "latestRoundData",
                                "nameLocation": "775:15:0",
                                "parameters": {
                                    "id": 32,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "790:2:0"
                                },
                                "returnParameters": {
                                    "id": 43,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 34,
                                            "mutability": "mutable",
                                            "name": "roundId",
                                            "nameLocation": "842:7:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 44,
                                            "src": "835:14:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_uint80",
                                                "typeString": "uint80"
                                            },
                                            "typeName": {
                                                "id": 33,
                                                "name": "uint80",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "835:6:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint80",
                                                    "typeString": "uint80"
                                                }
                                            },
                                            "visibility": "internal"
                                        },
                                        {
                                            "constant": false,
                                            "id": 36,
                                            "mutability": "mutable",
                                            "name": "answer",
                                            "nameLocation": "864:6:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 44,
                                            "src": "857:13:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_int256",
                                                "typeString": "int256"
                                            },
                                            "typeName": {
                                                "id": 35,
                                                "name": "int256",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "857:6:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_int256",
                                                    "typeString": "int256"
                                                }
                                            },
                                            "visibility": "internal"
                                        },
                                        {
                                            "constant": false,
                                            "id": 38,
                                            "mutability": "mutable",
                                            "name": "startedAt",
                                            "nameLocation": "886:9:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 44,
                                            "src": "878:17:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_uint256",
                                                "typeString": "uint256"
                                            },
                                            "typeName": {
                                                "id": 37,
                                                "name": "uint256",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "878:7:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint256",
                                                    "typeString": "uint256"
                                                }
                                            },
                                            "visibility": "internal"
                                        },
                                        {
                                            "constant": false,
                                            "id": 40,
                                            "mutability": "mutable",
                                            "name": "updatedAt",
                                            "nameLocation": "911:9:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 44,
                                            "src": "903:17:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_uint256",
                                                "typeString": "uint256"
                                            },
                                            "typeName": {
                                                "id": 39,
                                                "name": "uint256",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "903:7:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint256",
                                                    "typeString": "uint256"
                                                }
                                            },
                                            "visibility": "internal"
                                        },
                                        {
                                            "constant": false,
                                            "id": 42,
                                            "mutability": "mutable",
                                            "name": "answeredInRound",
                                            "nameLocation": "935:15:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 44,
                                            "src": "928:22:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_uint80",
                                                "typeString": "uint80"
                                            },
                                            "typeName": {
                                                "id": 41,
                                                "name": "uint80",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "928:6:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint80",
                                                    "typeString": "uint80"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "827:129:0"
                                },
                                "scope": 45,
                                "stateMutability": "view",
                                "virtual": false,
                                "visibility": "external"
                            }
                        ],
                        "abstract": false,
                        "baseContracts": [],
                        "canonicalName": "AggregatorV3Interface",
                        "contractDependencies": [],
                        "contractKind": "interface",
                        "fullyImplemented": false,
                        "linearizedBaseContracts": [
                            45
                        ],
                        "name": "AggregatorV3Interface",
                        "nameLocation": "67:21:0",
                        "scope": 46,
                        "usedErrors": [],
                        "usedEvents": []
                    }
                ],
                "license": "MIT"
            }
        },
        "src/LatestBadContract.sol": {
            "id": 1,
            "ast": {
                "absolutePath": "src/LatestBadContract.sol",
                "id": 110,
                "exportedSymbols": {
                    "AggregatorV3Interface": [
                        45
                    ],
                    "LatestBadContract": [
                        109
                    ]
                },
                "nodeType": "SourceUnit",
                "src": "32:1336:1",
                "nodes": [
                    {
                        "id": 47,
                        "nodeType": "PragmaDirective",
                        "src": "32:24:1",
                        "nodes": [],
                        "literals": [
                            "solidity",
                            "^",
                            "0.8",
                            ".20"
                        ]
                    },
                    {
                        "id": 48,
                        "nodeType": "ImportDirective",
                        "src": "104:93:1",
                        "nodes": [],
                        "absolutePath": "lib/chainlink-brownie-contracts/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol",
                        "file": "chainlink-brownie-contracts/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol",
                        "nameLocation": "-1:-1:-1",
                        "scope": 110,
                        "sourceUnit": 46,
                        "symbolAliases": [],
                        "unitAlias": ""
                    },
                    {
                        "id": 109,
                        "nodeType": "ContractDefinition",
                        "src": "199:1168:1",
                        "nodes": [
                            {
                                "id": 51,
                                "nodeType": "VariableDeclaration",
                                "src": "232:40:1",
                                "nodes": [],
                                "constant": false,
                                "mutability": "mutable",
                                "name": "priceFeed",
                                "nameLocation": "263:9:1",
                                "scope": 109,
                                "stateVariable": true,
                                "storageLocation": "default",
                                "typeDescriptions": {
                                    "typeIdentifier": "t_contract$_AggregatorV3Interface_$45",
                                    "typeString": "contract AggregatorV3Interface"
                                },
                                "typeName": {
                                    "id": 50,
                                    "nodeType": "UserDefinedTypeName",
                                    "pathNode": {
                                        "id": 49,
                                        "name": "AggregatorV3Interface",
                                        "nameLocations": [
                                            "232:21:1"
                                        ],
                                        "nodeType": "IdentifierPath",
                                        "referencedDeclaration": 45,
                                        "src": "232:21:1"
                                    },
                                    "referencedDeclaration": 45,
                                    "src": "232:21:1",
                                    "typeDescriptions": {
                                        "typeIdentifier": "t_contract$_AggregatorV3Interface_$45",
                                        "typeString": "contract AggregatorV3Interface"
                                    }
                                },
                                "visibility": "internal"
                            },
                            {
                                "id": 53,
                                "nodeType": "VariableDeclaration",
                                "src": "278:23:1",
                                "nodes": [],
                                "constant": false,
                                "functionSelector": "22adbc78",
                                "mutability": "mutable",
                                "name": "minAnswer",
                                "nameLocation": "292:9:1",
                                "scope": 109,
                                "stateVariable": true,
                                "storageLocation": "default",
                                "typeDescriptions": {
                                    "typeIdentifier": "t_int256",
                                    "typeString": "int256"
                                },
                                "typeName": {
                                    "id": 52,
                                    "name": "int256",
                                    "nodeType": "ElementaryTypeName",
                                    "src": "278:6:1",
                                    "typeDescriptions": {
                                        "typeIdentifier": "t_int256",
                                        "typeString": "int256"
                                    }
                                },
                                "visibility": "public"
                            },
                            {
                                "id": 72,
                                "nodeType": "FunctionDefinition",
                                "src": "396:182:1",
                                "nodes": [],
                                "body": {
                                    "id": 71,
                                    "nodeType": "Block",
                                    "src": "447:131:1",
                                    "nodes": [],
                                    "statements": [
                                        {
                                            "expression": {
                                                "id": 65,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "lValueRequested": false,
                                                "leftHandSide": {
                                                    "id": 61,
                                                    "name": "priceFeed",
                                                    "nodeType": "Identifier",
                                                    "overloadedDeclarations": [],
                                                    "referencedDeclaration": 51,
                                                    "src": "457:9:1",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_contract$_AggregatorV3Interface_$45",
                                                        "typeString": "contract AggregatorV3Interface"
                                                    }
                                                },
                                                "nodeType": "Assignment",
                                                "operator": "=",
                                                "rightHandSide": {
                                                    "arguments": [
                                                        {
                                                            "id": 63,
                                                            "name": "_priceFeed",
                                                            "nodeType": "Identifier",
                                                            "overloadedDeclarations": [],
                                                            "referencedDeclaration": 56,
                                                            "src": "491:10:1",
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
                                                        "id": 62,
                                                        "name": "AggregatorV3Interface",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 45,
                                                        "src": "469:21:1",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_type$_t_contract$_AggregatorV3Interface_$45_$",
                                                            "typeString": "type(contract AggregatorV3Interface)"
                                                        }
                                                    },
                                                    "id": 64,
                                                    "isConstant": false,
                                                    "isLValue": false,
                                                    "isPure": false,
                                                    "kind": "typeConversion",
                                                    "lValueRequested": false,
                                                    "nameLocations": [],
                                                    "names": [],
                                                    "nodeType": "FunctionCall",
                                                    "src": "469:33:1",
                                                    "tryCall": false,
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_contract$_AggregatorV3Interface_$45",
                                                        "typeString": "contract AggregatorV3Interface"
                                                    }
                                                },
                                                "src": "457:45:1",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_contract$_AggregatorV3Interface_$45",
                                                    "typeString": "contract AggregatorV3Interface"
                                                }
                                            },
                                            "id": 66,
                                            "nodeType": "ExpressionStatement",
                                            "src": "457:45:1"
                                        },
                                        {
                                            "expression": {
                                                "id": 69,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "lValueRequested": false,
                                                "leftHandSide": {
                                                    "id": 67,
                                                    "name": "minAnswer",
                                                    "nodeType": "Identifier",
                                                    "overloadedDeclarations": [],
                                                    "referencedDeclaration": 53,
                                                    "src": "512:9:1",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_int256",
                                                        "typeString": "int256"
                                                    }
                                                },
                                                "nodeType": "Assignment",
                                                "operator": "=",
                                                "rightHandSide": {
                                                    "id": 68,
                                                    "name": "_minAnswer",
                                                    "nodeType": "Identifier",
                                                    "overloadedDeclarations": [],
                                                    "referencedDeclaration": 58,
                                                    "src": "524:10:1",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_int256",
                                                        "typeString": "int256"
                                                    }
                                                },
                                                "src": "512:22:1",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_int256",
                                                    "typeString": "int256"
                                                }
                                            },
                                            "id": 70,
                                            "nodeType": "ExpressionStatement",
                                            "src": "512:22:1"
                                        }
                                    ]
                                },
                                "documentation": {
                                    "id": 54,
                                    "nodeType": "StructuredDocumentation",
                                    "src": "308:83:1",
                                    "text": " Constructor takes the address of a Chainlink Data Feed contract."
                                },
                                "implemented": true,
                                "kind": "constructor",
                                "modifiers": [],
                                "name": "",
                                "nameLocation": "-1:-1:-1",
                                "parameters": {
                                    "id": 59,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 56,
                                            "mutability": "mutable",
                                            "name": "_priceFeed",
                                            "nameLocation": "416:10:1",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 72,
                                            "src": "408:18:1",
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
                                                "src": "408:7:1",
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
                                            "id": 58,
                                            "mutability": "mutable",
                                            "name": "_minAnswer",
                                            "nameLocation": "435:10:1",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 72,
                                            "src": "428:17:1",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_int256",
                                                "typeString": "int256"
                                            },
                                            "typeName": {
                                                "id": 57,
                                                "name": "int256",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "428:6:1",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_int256",
                                                    "typeString": "int256"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "407:39:1"
                                },
                                "returnParameters": {
                                    "id": 60,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "447:0:1"
                                },
                                "scope": 109,
                                "stateMutability": "nonpayable",
                                "virtual": false,
                                "visibility": "public"
                            },
                            {
                                "id": 108,
                                "nodeType": "FunctionDefinition",
                                "src": "667:698:1",
                                "nodes": [],
                                "body": {
                                    "id": 107,
                                    "nodeType": "Block",
                                    "src": "909:456:1",
                                    "nodes": [],
                                    "statements": [
                                        {
                                            "assignments": [
                                                87,
                                                89,
                                                91,
                                                93,
                                                95
                                            ],
                                            "declarations": [
                                                {
                                                    "constant": false,
                                                    "id": 87,
                                                    "mutability": "mutable",
                                                    "name": "id",
                                                    "nameLocation": "940:2:1",
                                                    "nodeType": "VariableDeclaration",
                                                    "scope": 107,
                                                    "src": "933:9:1",
                                                    "stateVariable": false,
                                                    "storageLocation": "default",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_uint80",
                                                        "typeString": "uint80"
                                                    },
                                                    "typeName": {
                                                        "id": 86,
                                                        "name": "uint80",
                                                        "nodeType": "ElementaryTypeName",
                                                        "src": "933:6:1",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_uint80",
                                                            "typeString": "uint80"
                                                        }
                                                    },
                                                    "visibility": "internal"
                                                },
                                                {
                                                    "constant": false,
                                                    "id": 89,
                                                    "mutability": "mutable",
                                                    "name": "price",
                                                    "nameLocation": "963:5:1",
                                                    "nodeType": "VariableDeclaration",
                                                    "scope": 107,
                                                    "src": "956:12:1",
                                                    "stateVariable": false,
                                                    "storageLocation": "default",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_int256",
                                                        "typeString": "int256"
                                                    },
                                                    "typeName": {
                                                        "id": 88,
                                                        "name": "int256",
                                                        "nodeType": "ElementaryTypeName",
                                                        "src": "956:6:1",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_int256",
                                                            "typeString": "int256"
                                                        }
                                                    },
                                                    "visibility": "internal"
                                                },
                                                {
                                                    "constant": false,
                                                    "id": 91,
                                                    "mutability": "mutable",
                                                    "name": "started",
                                                    "nameLocation": "990:7:1",
                                                    "nodeType": "VariableDeclaration",
                                                    "scope": 107,
                                                    "src": "982:15:1",
                                                    "stateVariable": false,
                                                    "storageLocation": "default",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_uint256",
                                                        "typeString": "uint256"
                                                    },
                                                    "typeName": {
                                                        "id": 90,
                                                        "name": "uint256",
                                                        "nodeType": "ElementaryTypeName",
                                                        "src": "982:7:1",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_uint256",
                                                            "typeString": "uint256"
                                                        }
                                                    },
                                                    "visibility": "internal"
                                                },
                                                {
                                                    "constant": false,
                                                    "id": 93,
                                                    "mutability": "mutable",
                                                    "name": "updated",
                                                    "nameLocation": "1019:7:1",
                                                    "nodeType": "VariableDeclaration",
                                                    "scope": 107,
                                                    "src": "1011:15:1",
                                                    "stateVariable": false,
                                                    "storageLocation": "default",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_uint256",
                                                        "typeString": "uint256"
                                                    },
                                                    "typeName": {
                                                        "id": 92,
                                                        "name": "uint256",
                                                        "nodeType": "ElementaryTypeName",
                                                        "src": "1011:7:1",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_uint256",
                                                            "typeString": "uint256"
                                                        }
                                                    },
                                                    "visibility": "internal"
                                                },
                                                {
                                                    "constant": false,
                                                    "id": 95,
                                                    "mutability": "mutable",
                                                    "name": "answeredRound",
                                                    "nameLocation": "1047:13:1",
                                                    "nodeType": "VariableDeclaration",
                                                    "scope": 107,
                                                    "src": "1040:20:1",
                                                    "stateVariable": false,
                                                    "storageLocation": "default",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_uint80",
                                                        "typeString": "uint80"
                                                    },
                                                    "typeName": {
                                                        "id": 94,
                                                        "name": "uint80",
                                                        "nodeType": "ElementaryTypeName",
                                                        "src": "1040:6:1",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_uint80",
                                                            "typeString": "uint80"
                                                        }
                                                    },
                                                    "visibility": "internal"
                                                }
                                            ],
                                            "id": 99,
                                            "initialValue": {
                                                "arguments": [],
                                                "expression": {
                                                    "argumentTypes": [],
                                                    "expression": {
                                                        "id": 96,
                                                        "name": "priceFeed",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 51,
                                                        "src": "1073:9:1",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_contract$_AggregatorV3Interface_$45",
                                                            "typeString": "contract AggregatorV3Interface"
                                                        }
                                                    },
                                                    "id": 97,
                                                    "isConstant": false,
                                                    "isLValue": false,
                                                    "isPure": false,
                                                    "lValueRequested": false,
                                                    "memberLocation": "1083:15:1",
                                                    "memberName": "latestRoundData",
                                                    "nodeType": "MemberAccess",
                                                    "referencedDeclaration": 44,
                                                    "src": "1073:25:1",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_function_external_view$__$returns$_t_uint80_$_t_int256_$_t_uint256_$_t_uint256_$_t_uint80_$",
                                                        "typeString": "function () view external returns (uint80,int256,uint256,uint256,uint80)"
                                                    }
                                                },
                                                "id": 98,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "kind": "functionCall",
                                                "lValueRequested": false,
                                                "nameLocations": [],
                                                "names": [],
                                                "nodeType": "FunctionCall",
                                                "src": "1073:27:1",
                                                "tryCall": false,
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_tuple$_t_uint80_$_t_int256_$_t_uint256_$_t_uint256_$_t_uint80_$",
                                                    "typeString": "tuple(uint80,int256,uint256,uint256,uint80)"
                                                }
                                            },
                                            "nodeType": "VariableDeclarationStatement",
                                            "src": "919:181:1"
                                        },
                                        {
                                            "expression": {
                                                "components": [
                                                    {
                                                        "id": 100,
                                                        "name": "id",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 87,
                                                        "src": "1315:2:1",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_uint80",
                                                            "typeString": "uint80"
                                                        }
                                                    },
                                                    {
                                                        "id": 101,
                                                        "name": "price",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 89,
                                                        "src": "1319:5:1",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_int256",
                                                            "typeString": "int256"
                                                        }
                                                    },
                                                    {
                                                        "id": 102,
                                                        "name": "started",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 91,
                                                        "src": "1326:7:1",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_uint256",
                                                            "typeString": "uint256"
                                                        }
                                                    },
                                                    {
                                                        "id": 103,
                                                        "name": "updated",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 93,
                                                        "src": "1335:7:1",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_uint256",
                                                            "typeString": "uint256"
                                                        }
                                                    },
                                                    {
                                                        "id": 104,
                                                        "name": "answeredRound",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 95,
                                                        "src": "1344:13:1",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_uint80",
                                                            "typeString": "uint80"
                                                        }
                                                    }
                                                ],
                                                "id": 105,
                                                "isConstant": false,
                                                "isInlineArray": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "lValueRequested": false,
                                                "nodeType": "TupleExpression",
                                                "src": "1314:44:1",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_tuple$_t_uint80_$_t_int256_$_t_uint256_$_t_uint256_$_t_uint80_$",
                                                    "typeString": "tuple(uint80,int256,uint256,uint256,uint80)"
                                                }
                                            },
                                            "functionReturnParameters": 85,
                                            "id": 106,
                                            "nodeType": "Return",
                                            "src": "1307:51:1"
                                        }
                                    ]
                                },
                                "documentation": {
                                    "id": 73,
                                    "nodeType": "StructuredDocumentation",
                                    "src": "584:78:1",
                                    "text": " Returns the latest round data from the Chainlink Data Feed."
                                },
                                "functionSelector": "2daae2f3",
                                "implemented": true,
                                "kind": "function",
                                "modifiers": [],
                                "name": "getLatestRoundData",
                                "nameLocation": "676:18:1",
                                "parameters": {
                                    "id": 74,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "694:2:1"
                                },
                                "returnParameters": {
                                    "id": 85,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 76,
                                            "mutability": "mutable",
                                            "name": "roundId",
                                            "nameLocation": "762:7:1",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 108,
                                            "src": "755:14:1",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_uint80",
                                                "typeString": "uint80"
                                            },
                                            "typeName": {
                                                "id": 75,
                                                "name": "uint80",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "755:6:1",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint80",
                                                    "typeString": "uint80"
                                                }
                                            },
                                            "visibility": "internal"
                                        },
                                        {
                                            "constant": false,
                                            "id": 78,
                                            "mutability": "mutable",
                                            "name": "answer",
                                            "nameLocation": "790:6:1",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 108,
                                            "src": "783:13:1",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_int256",
                                                "typeString": "int256"
                                            },
                                            "typeName": {
                                                "id": 77,
                                                "name": "int256",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "783:6:1",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_int256",
                                                    "typeString": "int256"
                                                }
                                            },
                                            "visibility": "internal"
                                        },
                                        {
                                            "constant": false,
                                            "id": 80,
                                            "mutability": "mutable",
                                            "name": "startedAt",
                                            "nameLocation": "818:9:1",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 108,
                                            "src": "810:17:1",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_uint256",
                                                "typeString": "uint256"
                                            },
                                            "typeName": {
                                                "id": 79,
                                                "name": "uint256",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "810:7:1",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint256",
                                                    "typeString": "uint256"
                                                }
                                            },
                                            "visibility": "internal"
                                        },
                                        {
                                            "constant": false,
                                            "id": 82,
                                            "mutability": "mutable",
                                            "name": "updatedAt",
                                            "nameLocation": "849:9:1",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 108,
                                            "src": "841:17:1",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_uint256",
                                                "typeString": "uint256"
                                            },
                                            "typeName": {
                                                "id": 81,
                                                "name": "uint256",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "841:7:1",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint256",
                                                    "typeString": "uint256"
                                                }
                                            },
                                            "visibility": "internal"
                                        },
                                        {
                                            "constant": false,
                                            "id": 84,
                                            "mutability": "mutable",
                                            "name": "answeredInRound",
                                            "nameLocation": "879:15:1",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 108,
                                            "src": "872:22:1",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_uint80",
                                                "typeString": "uint80"
                                            },
                                            "typeName": {
                                                "id": 83,
                                                "name": "uint80",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "872:6:1",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint80",
                                                    "typeString": "uint80"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "741:163:1"
                                },
                                "scope": 109,
                                "stateMutability": "view",
                                "virtual": false,
                                "visibility": "public"
                            }
                        ],
                        "abstract": false,
                        "baseContracts": [],
                        "canonicalName": "LatestBadContract",
                        "contractDependencies": [],
                        "contractKind": "contract",
                        "fullyImplemented": true,
                        "linearizedBaseContracts": [
                            109
                        ],
                        "name": "LatestBadContract",
                        "nameLocation": "208:17:1",
                        "scope": 110,
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


def test_unchecked_chainlink_oracle_price(vulnerable_ast):
    ast_json, src_file_list = reduce_json(vulnerable_ast)
    results = process_yaml(
        "eburger/templates/unchecked_chainlink_oracle_price.yaml",
        ast_json,
        src_file_list,
    )
    
    assert "Line 22 Columns 5-34" in results["results"][0]["lines"]
