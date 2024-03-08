import json
import pytest
from eburger.serializer import reduce_json
from eburger.yaml_parser import process_yaml


@pytest.fixture
def vulnerable_ast() -> tuple[dict, list]:
    ast_json = """{
    "sources": {
        "vulnerable_contracts/use_of_unsafe_mint/contracts/BadContractor.sol": {
            "ast": {
                "absolutePath": "vulnerable_contracts/use_of_unsafe_mint/contracts/BadContractor.sol",
                "exportedSymbols": {
                    "BadNFT": [
                        3231
                    ],
                    "ERC721": [
                        1145
                    ],
                    "ERC721Enumerable": [
                        1664
                    ],
                    "IERC165": [
                        2045
                    ],
                    "IERC721Enumerable": [
                        1696
                    ]
                },
                "id": 3232,
                "license": "MIT",
                "nodeType": "SourceUnit",
                "nodes": [
                    {
                        "id": 3206,
                        "literals": [
                            "solidity",
                            "^",
                            "0.8",
                            ".20"
                        ],
                        "nodeType": "PragmaDirective",
                        "src": "32:24:13"
                    },
                    {
                        "absolutePath": "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol",
                        "file": "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol",
                        "id": 3207,
                        "nameLocation": "-1:-1:-1",
                        "nodeType": "ImportDirective",
                        "scope": 3232,
                        "sourceUnit": 1665,
                        "src": "58:78:13",
                        "symbolAliases": [],
                        "unitAlias": ""
                    },
                    {
                        "abstract": false,
                        "baseContracts": [
                            {
                                "baseName": {
                                    "id": 3208,
                                    "name": "ERC721Enumerable",
                                    "nameLocations": [
                                        "156:16:13"
                                    ],
                                    "nodeType": "IdentifierPath",
                                    "referencedDeclaration": 1664,
                                    "src": "156:16:13"
                                },
                                "id": 3209,
                                "nodeType": "InheritanceSpecifier",
                                "src": "156:16:13"
                            }
                        ],
                        "canonicalName": "BadNFT",
                        "contractDependencies": [],
                        "contractKind": "contract",
                        "fullyImplemented": true,
                        "id": 3231,
                        "linearizedBaseContracts": [
                            3231,
                            1664,
                            1696,
                            1145,
                            89,
                            1724,
                            1262,
                            2033,
                            2045,
                            1754
                        ],
                        "name": "BadNFT",
                        "nameLocation": "146:6:13",
                        "nodeType": "ContractDefinition",
                        "nodes": [
                            {
                                "body": {
                                    "id": 3216,
                                    "nodeType": "Block",
                                    "src": "218:2:13",
                                    "statements": []
                                },
                                "id": 3217,
                                "implemented": true,
                                "kind": "constructor",
                                "modifiers": [
                                    {
                                        "arguments": [
                                            {
                                                "hexValue": "4261644e4654",
                                                "id": 3212,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": true,
                                                "kind": "string",
                                                "lValueRequested": false,
                                                "nodeType": "Literal",
                                                "src": "200:8:13",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_stringliteral_ba680b0b9df4e31ef0559b5b2494fdf07f8a3ff8669c03cc9e520ef2014d457f",
                                                    "typeString": "literal_string 'BadNFT'"
                                                },
                                                "value": "BadNFT"
                                            },
                                            {
                                                "hexValue": "424e4654",
                                                "id": 3213,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": true,
                                                "kind": "string",
                                                "lValueRequested": false,
                                                "nodeType": "Literal",
                                                "src": "210:6:13",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_stringliteral_9e6745b3cfc67f270bc8e59f2a9eb2eade3f9ba1f67e62d12af610af4cc76070",
                                                    "typeString": "literal_string 'BNFT'"
                                                },
                                                "value": "BNFT"
                                            }
                                        ],
                                        "id": 3214,
                                        "kind": "baseConstructorSpecifier",
                                        "modifierName": {
                                            "id": 3211,
                                            "name": "ERC721",
                                            "nameLocations": [
                                                "193:6:13"
                                            ],
                                            "nodeType": "IdentifierPath",
                                            "referencedDeclaration": 1145,
                                            "src": "193:6:13"
                                        },
                                        "nodeType": "ModifierInvocation",
                                        "src": "193:24:13"
                                    }
                                ],
                                "name": "",
                                "nameLocation": "-1:-1:-1",
                                "nodeType": "FunctionDefinition",
                                "parameters": {
                                    "id": 3210,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "190:2:13"
                                },
                                "returnParameters": {
                                    "id": 3215,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "218:0:13"
                                },
                                "scope": 3231,
                                "src": "179:41:13",
                                "stateMutability": "nonpayable",
                                "virtual": false,
                                "visibility": "public"
                            },
                            {
                                "body": {
                                    "id": 3229,
                                    "nodeType": "Block",
                                    "src": "276:35:13",
                                    "statements": [
                                        {
                                            "expression": {
                                                "arguments": [
                                                    {
                                                        "id": 3225,
                                                        "name": "to",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 3219,
                                                        "src": "292:2:13",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_address",
                                                            "typeString": "address"
                                                        }
                                                    },
                                                    {
                                                        "id": 3226,
                                                        "name": "tokenId",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 3221,
                                                        "src": "296:7:13",
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
                                                    "id": 3224,
                                                    "name": "_mint",
                                                    "nodeType": "Identifier",
                                                    "overloadedDeclarations": [],
                                                    "referencedDeclaration": 752,
                                                    "src": "286:5:13",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_function_internal_nonpayable$_t_address_$_t_uint256_$returns$__$",
                                                        "typeString": "function (address,uint256)"
                                                    }
                                                },
                                                "id": 3227,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "kind": "functionCall",
                                                "lValueRequested": false,
                                                "nameLocations": [],
                                                "names": [],
                                                "nodeType": "FunctionCall",
                                                "src": "286:18:13",
                                                "tryCall": false,
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_tuple$__$",
                                                    "typeString": "tuple()"
                                                }
                                            },
                                            "id": 3228,
                                            "nodeType": "ExpressionStatement",
                                            "src": "286:18:13"
                                        }
                                    ]
                                },
                                "functionSelector": "40c10f19",
                                "id": 3230,
                                "implemented": true,
                                "kind": "function",
                                "modifiers": [],
                                "name": "mint",
                                "nameLocation": "235:4:13",
                                "nodeType": "FunctionDefinition",
                                "parameters": {
                                    "id": 3222,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 3219,
                                            "mutability": "mutable",
                                            "name": "to",
                                            "nameLocation": "248:2:13",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 3230,
                                            "src": "240:10:13",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_address",
                                                "typeString": "address"
                                            },
                                            "typeName": {
                                                "id": 3218,
                                                "name": "address",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "240:7:13",
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
                                            "id": 3221,
                                            "mutability": "mutable",
                                            "name": "tokenId",
                                            "nameLocation": "260:7:13",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 3230,
                                            "src": "252:15:13",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_uint256",
                                                "typeString": "uint256"
                                            },
                                            "typeName": {
                                                "id": 3220,
                                                "name": "uint256",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "252:7:13",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint256",
                                                    "typeString": "uint256"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "239:29:13"
                                },
                                "returnParameters": {
                                    "id": 3223,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "276:0:13"
                                },
                                "scope": 3231,
                                "src": "226:85:13",
                                "stateMutability": "nonpayable",
                                "virtual": false,
                                "visibility": "public"
                            }
                        ],
                        "scope": 3232,
                        "src": "137:176:13",
                        "usedErrors": [
                            47,
                            52,
                            61,
                            66,
                            71,
                            78,
                            83,
                            88,
                            1317,
                            1320
                        ],
                        "usedEvents": [
                            1161,
                            1170,
                            1179
                        ]
                    }
                ],
                "src": "32:281:13"
            },
            "id": 13
        }
    }
}"""
    return json.loads(ast_json)


def test_use_of_unsafe_mint(vulnerable_ast):
    ast_json, src_paths = reduce_json(vulnerable_ast)
    results = process_yaml(
        "eburger/templates/use_of_unsafe_mint.yaml",
        ast_json,
        src_paths,
    )
    assert "Line 9 Columns 9-27" in results["results"][0]["lines"]
