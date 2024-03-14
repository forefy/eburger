import json
import pytest
from eburger.serializer import reduce_json
from eburger.yaml_parser import process_yaml


@pytest.fixture
def vulnerable_ast() -> tuple[dict, list]:
    ast_json = """{
    "sources": {
        "vulnerable_contracts/use_of_encodepacked.sol": {
            "AST": {
                "absolutePath": "vulnerable_contracts/use_of_encodepacked.sol",
                "exportedSymbols": {
                    "BadCode": [
                        57
                    ]
                },
                "id": 58,
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
                        "canonicalName": "BadCode",
                        "contractDependencies": [],
                        "contractKind": "contract",
                        "fullyImplemented": true,
                        "id": 57,
                        "linearizedBaseContracts": [
                            57
                        ],
                        "name": "BadCode",
                        "nameLocation": "66:7:0",
                        "nodeType": "ContractDefinition",
                        "nodes": [
                            {
                                "body": {
                                    "id": 18,
                                    "nodeType": "Block",
                                    "src": "178:67:0",
                                    "statements": [
                                        {
                                            "expression": {
                                                "arguments": [
                                                    {
                                                        "arguments": [
                                                            {
                                                                "id": 13,
                                                                "name": "input1",
                                                                "nodeType": "Identifier",
                                                                "overloadedDeclarations": [],
                                                                "referencedDeclaration": 3,
                                                                "src": "222:6:0",
                                                                "typeDescriptions": {
                                                                    "typeIdentifier": "t_string_memory_ptr",
                                                                    "typeString": "string memory"
                                                                }
                                                            },
                                                            {
                                                                "id": 14,
                                                                "name": "input2",
                                                                "nodeType": "Identifier",
                                                                "overloadedDeclarations": [],
                                                                "referencedDeclaration": 5,
                                                                "src": "230:6:0",
                                                                "typeDescriptions": {
                                                                    "typeIdentifier": "t_string_memory_ptr",
                                                                    "typeString": "string memory"
                                                                }
                                                            }
                                                        ],
                                                        "expression": {
                                                            "argumentTypes": [
                                                                {
                                                                    "typeIdentifier": "t_string_memory_ptr",
                                                                    "typeString": "string memory"
                                                                },
                                                                {
                                                                    "typeIdentifier": "t_string_memory_ptr",
                                                                    "typeString": "string memory"
                                                                }
                                                            ],
                                                            "expression": {
                                                                "id": 11,
                                                                "name": "abi",
                                                                "nodeType": "Identifier",
                                                                "overloadedDeclarations": [],
                                                                "referencedDeclaration": -1,
                                                                "src": "205:3:0",
                                                                "typeDescriptions": {
                                                                    "typeIdentifier": "t_magic_abi",
                                                                    "typeString": "abi"
                                                                }
                                                            },
                                                            "id": 12,
                                                            "isConstant": false,
                                                            "isLValue": false,
                                                            "isPure": true,
                                                            "lValueRequested": false,
                                                            "memberLocation": "209:12:0",
                                                            "memberName": "encodePacked",
                                                            "nodeType": "MemberAccess",
                                                            "src": "205:16:0",
                                                            "typeDescriptions": {
                                                                "typeIdentifier": "t_function_abiencodepacked_pure$__$returns$_t_bytes_memory_ptr_$",
                                                                "typeString": "function () pure returns (bytes memory)"
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
                                                        "src": "205:32:0",
                                                        "tryCall": false,
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_bytes_memory_ptr",
                                                            "typeString": "bytes memory"
                                                        }
                                                    }
                                                ],
                                                "expression": {
                                                    "argumentTypes": [
                                                        {
                                                            "typeIdentifier": "t_bytes_memory_ptr",
                                                            "typeString": "bytes memory"
                                                        }
                                                    ],
                                                    "id": 10,
                                                    "name": "keccak256",
                                                    "nodeType": "Identifier",
                                                    "overloadedDeclarations": [],
                                                    "referencedDeclaration": -8,
                                                    "src": "195:9:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_function_keccak256_pure$_t_bytes_memory_ptr_$returns$_t_bytes32_$",
                                                        "typeString": "function (bytes memory) pure returns (bytes32)"
                                                    }
                                                },
                                                "id": 16,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "kind": "functionCall",
                                                "lValueRequested": false,
                                                "nameLocations": [],
                                                "names": [],
                                                "nodeType": "FunctionCall",
                                                "src": "195:43:0",
                                                "tryCall": false,
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_bytes32",
                                                    "typeString": "bytes32"
                                                }
                                            },
                                            "functionReturnParameters": 9,
                                            "id": 17,
                                            "nodeType": "Return",
                                            "src": "188:50:0"
                                        }
                                    ]
                                },
                                "functionSelector": "1661d18a",
                                "id": 19,
                                "implemented": true,
                                "kind": "function",
                                "modifiers": [],
                                "name": "hashCollision1",
                                "nameLocation": "89:14:0",
                                "nodeType": "FunctionDefinition",
                                "parameters": {
                                    "id": 6,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 3,
                                            "mutability": "mutable",
                                            "name": "input1",
                                            "nameLocation": "118:6:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 19,
                                            "src": "104:20:0",
                                            "stateVariable": false,
                                            "storageLocation": "memory",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_string_memory_ptr",
                                                "typeString": "string"
                                            },
                                            "typeName": {
                                                "id": 2,
                                                "name": "string",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "104:6:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_string_storage_ptr",
                                                    "typeString": "string"
                                                }
                                            },
                                            "visibility": "internal"
                                        },
                                        {
                                            "constant": false,
                                            "id": 5,
                                            "mutability": "mutable",
                                            "name": "input2",
                                            "nameLocation": "140:6:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 19,
                                            "src": "126:20:0",
                                            "stateVariable": false,
                                            "storageLocation": "memory",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_string_memory_ptr",
                                                "typeString": "string"
                                            },
                                            "typeName": {
                                                "id": 4,
                                                "name": "string",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "126:6:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_string_storage_ptr",
                                                    "typeString": "string"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "103:44:0"
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
                                            "scope": 19,
                                            "src": "169:7:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_bytes32",
                                                "typeString": "bytes32"
                                            },
                                            "typeName": {
                                                "id": 7,
                                                "name": "bytes32",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "169:7:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_bytes32",
                                                    "typeString": "bytes32"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "168:9:0"
                                },
                                "scope": 57,
                                "src": "80:165:0",
                                "stateMutability": "pure",
                                "virtual": false,
                                "visibility": "public"
                            },
                            {
                                "body": {
                                    "id": 37,
                                    "nodeType": "Block",
                                    "src": "351:67:0",
                                    "statements": [
                                        {
                                            "expression": {
                                                "arguments": [
                                                    {
                                                        "arguments": [
                                                            {
                                                                "id": 32,
                                                                "name": "input1",
                                                                "nodeType": "Identifier",
                                                                "overloadedDeclarations": [],
                                                                "referencedDeclaration": 21,
                                                                "src": "395:6:0",
                                                                "typeDescriptions": {
                                                                    "typeIdentifier": "t_bytes_memory_ptr",
                                                                    "typeString": "bytes memory"
                                                                }
                                                            },
                                                            {
                                                                "id": 33,
                                                                "name": "input2",
                                                                "nodeType": "Identifier",
                                                                "overloadedDeclarations": [],
                                                                "referencedDeclaration": 24,
                                                                "src": "403:6:0",
                                                                "typeDescriptions": {
                                                                    "typeIdentifier": "t_array$_t_uint256_$dyn_memory_ptr",
                                                                    "typeString": "uint256[] memory"
                                                                }
                                                            }
                                                        ],
                                                        "expression": {
                                                            "argumentTypes": [
                                                                {
                                                                    "typeIdentifier": "t_bytes_memory_ptr",
                                                                    "typeString": "bytes memory"
                                                                },
                                                                {
                                                                    "typeIdentifier": "t_array$_t_uint256_$dyn_memory_ptr",
                                                                    "typeString": "uint256[] memory"
                                                                }
                                                            ],
                                                            "expression": {
                                                                "id": 30,
                                                                "name": "abi",
                                                                "nodeType": "Identifier",
                                                                "overloadedDeclarations": [],
                                                                "referencedDeclaration": -1,
                                                                "src": "378:3:0",
                                                                "typeDescriptions": {
                                                                    "typeIdentifier": "t_magic_abi",
                                                                    "typeString": "abi"
                                                                }
                                                            },
                                                            "id": 31,
                                                            "isConstant": false,
                                                            "isLValue": false,
                                                            "isPure": true,
                                                            "lValueRequested": false,
                                                            "memberLocation": "382:12:0",
                                                            "memberName": "encodePacked",
                                                            "nodeType": "MemberAccess",
                                                            "src": "378:16:0",
                                                            "typeDescriptions": {
                                                                "typeIdentifier": "t_function_abiencodepacked_pure$__$returns$_t_bytes_memory_ptr_$",
                                                                "typeString": "function () pure returns (bytes memory)"
                                                            }
                                                        },
                                                        "id": 34,
                                                        "isConstant": false,
                                                        "isLValue": false,
                                                        "isPure": false,
                                                        "kind": "functionCall",
                                                        "lValueRequested": false,
                                                        "nameLocations": [],
                                                        "names": [],
                                                        "nodeType": "FunctionCall",
                                                        "src": "378:32:0",
                                                        "tryCall": false,
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_bytes_memory_ptr",
                                                            "typeString": "bytes memory"
                                                        }
                                                    }
                                                ],
                                                "expression": {
                                                    "argumentTypes": [
                                                        {
                                                            "typeIdentifier": "t_bytes_memory_ptr",
                                                            "typeString": "bytes memory"
                                                        }
                                                    ],
                                                    "id": 29,
                                                    "name": "keccak256",
                                                    "nodeType": "Identifier",
                                                    "overloadedDeclarations": [],
                                                    "referencedDeclaration": -8,
                                                    "src": "368:9:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_function_keccak256_pure$_t_bytes_memory_ptr_$returns$_t_bytes32_$",
                                                        "typeString": "function (bytes memory) pure returns (bytes32)"
                                                    }
                                                },
                                                "id": 35,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "kind": "functionCall",
                                                "lValueRequested": false,
                                                "nameLocations": [],
                                                "names": [],
                                                "nodeType": "FunctionCall",
                                                "src": "368:43:0",
                                                "tryCall": false,
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_bytes32",
                                                    "typeString": "bytes32"
                                                }
                                            },
                                            "functionReturnParameters": 28,
                                            "id": 36,
                                            "nodeType": "Return",
                                            "src": "361:50:0"
                                        }
                                    ]
                                },
                                "functionSelector": "193b1d10",
                                "id": 38,
                                "implemented": true,
                                "kind": "function",
                                "modifiers": [],
                                "name": "hashCollision2",
                                "nameLocation": "260:14:0",
                                "nodeType": "FunctionDefinition",
                                "parameters": {
                                    "id": 25,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 21,
                                            "mutability": "mutable",
                                            "name": "input1",
                                            "nameLocation": "288:6:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 38,
                                            "src": "275:19:0",
                                            "stateVariable": false,
                                            "storageLocation": "memory",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_bytes_memory_ptr",
                                                "typeString": "bytes"
                                            },
                                            "typeName": {
                                                "id": 20,
                                                "name": "bytes",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "275:5:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_bytes_storage_ptr",
                                                    "typeString": "bytes"
                                                }
                                            },
                                            "visibility": "internal"
                                        },
                                        {
                                            "constant": false,
                                            "id": 24,
                                            "mutability": "mutable",
                                            "name": "input2",
                                            "nameLocation": "313:6:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 38,
                                            "src": "296:23:0",
                                            "stateVariable": false,
                                            "storageLocation": "memory",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_array$_t_uint256_$dyn_memory_ptr",
                                                "typeString": "uint256[]"
                                            },
                                            "typeName": {
                                                "baseType": {
                                                    "id": 22,
                                                    "name": "uint256",
                                                    "nodeType": "ElementaryTypeName",
                                                    "src": "296:7:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_uint256",
                                                        "typeString": "uint256"
                                                    }
                                                },
                                                "id": 23,
                                                "nodeType": "ArrayTypeName",
                                                "src": "296:9:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_array$_t_uint256_$dyn_storage_ptr",
                                                    "typeString": "uint256[]"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "274:46:0"
                                },
                                "returnParameters": {
                                    "id": 28,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 27,
                                            "mutability": "mutable",
                                            "name": "",
                                            "nameLocation": "-1:-1:-1",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 38,
                                            "src": "342:7:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_bytes32",
                                                "typeString": "bytes32"
                                            },
                                            "typeName": {
                                                "id": 26,
                                                "name": "bytes32",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "342:7:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_bytes32",
                                                    "typeString": "bytes32"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "341:9:0"
                                },
                                "scope": 57,
                                "src": "251:167:0",
                                "stateMutability": "pure",
                                "virtual": false,
                                "visibility": "public"
                            },
                            {
                                "body": {
                                    "id": 55,
                                    "nodeType": "Block",
                                    "src": "523:61:0",
                                    "statements": [
                                        {
                                            "expression": {
                                                "arguments": [
                                                    {
                                                        "arguments": [
                                                            {
                                                                "id": 50,
                                                                "name": "input1",
                                                                "nodeType": "Identifier",
                                                                "overloadedDeclarations": [],
                                                                "referencedDeclaration": 40,
                                                                "src": "561:6:0",
                                                                "typeDescriptions": {
                                                                    "typeIdentifier": "t_string_memory_ptr",
                                                                    "typeString": "string memory"
                                                                }
                                                            },
                                                            {
                                                                "id": 51,
                                                                "name": "input2",
                                                                "nodeType": "Identifier",
                                                                "overloadedDeclarations": [],
                                                                "referencedDeclaration": 42,
                                                                "src": "569:6:0",
                                                                "typeDescriptions": {
                                                                    "typeIdentifier": "t_string_memory_ptr",
                                                                    "typeString": "string memory"
                                                                }
                                                            }
                                                        ],
                                                        "expression": {
                                                            "argumentTypes": [
                                                                {
                                                                    "typeIdentifier": "t_string_memory_ptr",
                                                                    "typeString": "string memory"
                                                                },
                                                                {
                                                                    "typeIdentifier": "t_string_memory_ptr",
                                                                    "typeString": "string memory"
                                                                }
                                                            ],
                                                            "expression": {
                                                                "id": 48,
                                                                "name": "abi",
                                                                "nodeType": "Identifier",
                                                                "overloadedDeclarations": [],
                                                                "referencedDeclaration": -1,
                                                                "src": "550:3:0",
                                                                "typeDescriptions": {
                                                                    "typeIdentifier": "t_magic_abi",
                                                                    "typeString": "abi"
                                                                }
                                                            },
                                                            "id": 49,
                                                            "isConstant": false,
                                                            "isLValue": false,
                                                            "isPure": true,
                                                            "lValueRequested": false,
                                                            "memberLocation": "554:6:0",
                                                            "memberName": "encode",
                                                            "nodeType": "MemberAccess",
                                                            "src": "550:10:0",
                                                            "typeDescriptions": {
                                                                "typeIdentifier": "t_function_abiencode_pure$__$returns$_t_bytes_memory_ptr_$",
                                                                "typeString": "function () pure returns (bytes memory)"
                                                            }
                                                        },
                                                        "id": 52,
                                                        "isConstant": false,
                                                        "isLValue": false,
                                                        "isPure": false,
                                                        "kind": "functionCall",
                                                        "lValueRequested": false,
                                                        "nameLocations": [],
                                                        "names": [],
                                                        "nodeType": "FunctionCall",
                                                        "src": "550:26:0",
                                                        "tryCall": false,
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_bytes_memory_ptr",
                                                            "typeString": "bytes memory"
                                                        }
                                                    }
                                                ],
                                                "expression": {
                                                    "argumentTypes": [
                                                        {
                                                            "typeIdentifier": "t_bytes_memory_ptr",
                                                            "typeString": "bytes memory"
                                                        }
                                                    ],
                                                    "id": 47,
                                                    "name": "keccak256",
                                                    "nodeType": "Identifier",
                                                    "overloadedDeclarations": [],
                                                    "referencedDeclaration": -8,
                                                    "src": "540:9:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_function_keccak256_pure$_t_bytes_memory_ptr_$returns$_t_bytes32_$",
                                                        "typeString": "function (bytes memory) pure returns (bytes32)"
                                                    }
                                                },
                                                "id": 53,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "kind": "functionCall",
                                                "lValueRequested": false,
                                                "nameLocations": [],
                                                "names": [],
                                                "nodeType": "FunctionCall",
                                                "src": "540:37:0",
                                                "tryCall": false,
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_bytes32",
                                                    "typeString": "bytes32"
                                                }
                                            },
                                            "functionReturnParameters": 46,
                                            "id": 54,
                                            "nodeType": "Return",
                                            "src": "533:44:0"
                                        }
                                    ]
                                },
                                "functionSelector": "4b191d6f",
                                "id": 56,
                                "implemented": true,
                                "kind": "function",
                                "modifiers": [],
                                "name": "noHashCollision",
                                "nameLocation": "433:15:0",
                                "nodeType": "FunctionDefinition",
                                "parameters": {
                                    "id": 43,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 40,
                                            "mutability": "mutable",
                                            "name": "input1",
                                            "nameLocation": "463:6:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 56,
                                            "src": "449:20:0",
                                            "stateVariable": false,
                                            "storageLocation": "memory",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_string_memory_ptr",
                                                "typeString": "string"
                                            },
                                            "typeName": {
                                                "id": 39,
                                                "name": "string",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "449:6:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_string_storage_ptr",
                                                    "typeString": "string"
                                                }
                                            },
                                            "visibility": "internal"
                                        },
                                        {
                                            "constant": false,
                                            "id": 42,
                                            "mutability": "mutable",
                                            "name": "input2",
                                            "nameLocation": "485:6:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 56,
                                            "src": "471:20:0",
                                            "stateVariable": false,
                                            "storageLocation": "memory",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_string_memory_ptr",
                                                "typeString": "string"
                                            },
                                            "typeName": {
                                                "id": 41,
                                                "name": "string",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "471:6:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_string_storage_ptr",
                                                    "typeString": "string"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "448:44:0"
                                },
                                "returnParameters": {
                                    "id": 46,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 45,
                                            "mutability": "mutable",
                                            "name": "",
                                            "nameLocation": "-1:-1:-1",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 56,
                                            "src": "514:7:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_bytes32",
                                                "typeString": "bytes32"
                                            },
                                            "typeName": {
                                                "id": 44,
                                                "name": "bytes32",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "514:7:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_bytes32",
                                                    "typeString": "bytes32"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "513:9:0"
                                },
                                "scope": 57,
                                "src": "424:160:0",
                                "stateMutability": "pure",
                                "virtual": false,
                                "visibility": "public"
                            }
                        ],
                        "scope": 58,
                        "src": "57:529:0",
                        "usedErrors": [],
                        "usedEvents": []
                    }
                ],
                "src": "32:554:0"
            },
            "id": 0
        }
    }
}"""
    return json.loads(ast_json)


def test_use_of_encodepacked(vulnerable_ast):
    ast_json, src_paths = reduce_json(vulnerable_ast)
    results = process_yaml(
        "eburger/templates/use_of_encodepacked.yaml",
        ast_json,
        src_paths,
    )
    assert "Line 6 Columns 26-42" in results["results"][0]["lines"]
