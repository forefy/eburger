import json
import pytest
from eburger.template_utils import parse_code_highlight

from eburger.yaml_parser import process_yaml


@pytest.fixture
def tx_origin_used_for_access_control_ast():
    tx_json = """{
    "contracts": {
        "vulnerable_contracts/tx_origin_used_for_access_control.sol:BadContract": {
            "abi": [
                {
                    "inputs": [],
                    "stateMutability": "nonpayable",
                    "type": "constructor"
                },
                {
                    "inputs": [
                        {
                            "internalType": "address payable",
                            "name": "receiver",
                            "type": "address"
                        },
                        {
                            "internalType": "uint256",
                            "name": "amount",
                            "type": "uint256"
                        }
                    ],
                    "name": "sendTo",
                    "outputs": [],
                    "stateMutability": "nonpayable",
                    "type": "function"
                }
            ],
            "bin": "608060405234801561000f575f80fd5b50335f806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555061029b8061005c5f395ff3fe608060405234801561000f575f80fd5b5060043610610029575f3560e01c80639e1a00aa1461002d575b5f80fd5b610047600480360381019061004291906101af565b610049565b005b5f8054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163273ffffffffffffffffffffffffffffffffffffffff16146100d6576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016100cd90610247565b60405180910390fd5b8173ffffffffffffffffffffffffffffffffffffffff166108fc8290811502906040515f60405180830381858888f19350505050158015610119573d5f803e3d5ffd5b505050565b5f80fd5b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f61014b82610122565b9050919050565b61015b81610141565b8114610165575f80fd5b50565b5f8135905061017681610152565b92915050565b5f819050919050565b61018e8161017c565b8114610198575f80fd5b50565b5f813590506101a981610185565b92915050565b5f80604083850312156101c5576101c461011e565b5b5f6101d285828601610168565b92505060206101e38582860161019b565b9150509250929050565b5f82825260208201905092915050565b7f43616c6c6572206973206e6f7420746865206f776e65720000000000000000005f82015250565b5f6102316017836101ed565b915061023c826101fd565b602082019050919050565b5f6020820190508181035f83015261025e81610225565b905091905056fea26469706673582212205e5f24238deac6ecf38c55c05bf3c3d18ea0d943876bfa082ec6bbdec0ec0ba664736f6c63430008140033",
            "bin-runtime": "608060405234801561000f575f80fd5b5060043610610029575f3560e01c80639e1a00aa1461002d575b5f80fd5b610047600480360381019061004291906101af565b610049565b005b5f8054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163273ffffffffffffffffffffffffffffffffffffffff16146100d6576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016100cd90610247565b60405180910390fd5b8173ffffffffffffffffffffffffffffffffffffffff166108fc8290811502906040515f60405180830381858888f19350505050158015610119573d5f803e3d5ffd5b505050565b5f80fd5b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f61014b82610122565b9050919050565b61015b81610141565b8114610165575f80fd5b50565b5f8135905061017681610152565b92915050565b5f819050919050565b61018e8161017c565b8114610198575f80fd5b50565b5f813590506101a981610185565b92915050565b5f80604083850312156101c5576101c461011e565b5b5f6101d285828601610168565b92505060206101e38582860161019b565b9150509250929050565b5f82825260208201905092915050565b7f43616c6c6572206973206e6f7420746865206f776e65720000000000000000005f82015250565b5f6102316017836101ed565b915061023c826101fd565b602082019050919050565b5f6020820190508181035f83015261025e81610225565b905091905056fea26469706673582212205e5f24238deac6ecf38c55c05bf3c3d18ea0d943876bfa082ec6bbdec0ec0ba664736f6c63430008140033",
            "devdoc": {
                "kind": "dev",
                "methods": {},
                "version": 1
            },
            "hashes": {
                "sendTo(address,uint256)": "9e1a00aa"
            },
            "srcmap": "56:296:0:-:0;;;111:65;;;;;;;;;;158:10;142:5;;:27;;;;;;;;;;;;;;;;;;56:296;;;;;;",
            "srcmap-runtime": "56:296:0:-:0;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;182:168;;;;;;;;;;;;;:::i;:::-;;:::i;:::-;;;275:5;;;;;;;;;;262:18;;:9;:18;;;254:54;;;;;;;;;;;;:::i;:::-;;;;;;;;;318:8;:17;;:25;336:6;318:25;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;182:168;;:::o;88:117:1:-;197:1;194;187:12;334:126;371:7;411:42;404:5;400:54;389:65;;334:126;;;:::o;466:104::-;511:7;540:24;558:5;540:24;:::i;:::-;529:35;;466:104;;;:::o;576:138::-;657:32;683:5;657:32;:::i;:::-;650:5;647:43;637:71;;704:1;701;694:12;637:71;576:138;:::o;720:155::-;774:5;812:6;799:20;790:29;;828:41;863:5;828:41;:::i;:::-;720:155;;;;:::o;881:77::-;918:7;947:5;936:16;;881:77;;;:::o;964:122::-;1037:24;1055:5;1037:24;:::i;:::-;1030:5;1027:35;1017:63;;1076:1;1073;1066:12;1017:63;964:122;:::o;1092:139::-;1138:5;1176:6;1163:20;1154:29;;1192:33;1219:5;1192:33;:::i;:::-;1092:139;;;;:::o;1237:490::-;1313:6;1321;1370:2;1358:9;1349:7;1345:23;1341:32;1338:119;;;1376:79;;:::i;:::-;1338:119;1496:1;1521:61;1574:7;1565:6;1554:9;1550:22;1521:61;:::i;:::-;1511:71;;1467:125;1631:2;1657:53;1702:7;1693:6;1682:9;1678:22;1657:53;:::i;:::-;1647:63;;1602:118;1237:490;;;;;:::o;1733:169::-;1817:11;1851:6;1846:3;1839:19;1891:4;1886:3;1882:14;1867:29;;1733:169;;;;:::o;1908:173::-;2048:25;2044:1;2036:6;2032:14;2025:49;1908:173;:::o;2087:366::-;2229:3;2250:67;2314:2;2309:3;2250:67;:::i;:::-;2243:74;;2326:93;2415:3;2326:93;:::i;:::-;2444:2;2439:3;2435:12;2428:19;;2087:366;;;:::o;2459:419::-;2625:4;2663:2;2652:9;2648:18;2640:26;;2712:9;2706:4;2702:20;2698:1;2687:9;2683:17;2676:47;2740:131;2866:4;2740:131;:::i;:::-;2732:139;;2459:419;;;:::o",
            "userdoc": {
                "kind": "user",
                "methods": {},
                "version": 1
            }
        }
    },
    "sourceList": [
        "vulnerable_contracts/tx_origin_used_for_access_control.sol"
    ],
    "sources": {
        "vulnerable_contracts/tx_origin_used_for_access_control.sol": {
            "AST": {
                "absolutePath": "vulnerable_contracts/tx_origin_used_for_access_control.sol",
                "exportedSymbols": {
                    "BadContract": [
                        38
                    ]
                },
                "id": 39,
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
                        "canonicalName": "BadContract",
                        "contractDependencies": [],
                        "contractKind": "contract",
                        "fullyImplemented": true,
                        "id": 38,
                        "linearizedBaseContracts": [
                            38
                        ],
                        "name": "BadContract",
                        "nameLocation": "65:11:0",
                        "nodeType": "ContractDefinition",
                        "nodes": [
                            {
                                "constant": false,
                                "id": 3,
                                "mutability": "mutable",
                                "name": "owner",
                                "nameLocation": "99:5:0",
                                "nodeType": "VariableDeclaration",
                                "scope": 38,
                                "src": "83:21:0",
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
                                    "src": "83:15:0",
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
                                    "src": "132:44:0",
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
                                                    "src": "142:5:0",
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
                                                                "src": "158:3:0",
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
                                                            "memberLocation": "162:6:0",
                                                            "memberName": "sender",
                                                            "nodeType": "MemberAccess",
                                                            "src": "158:10:0",
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
                                                        "src": "150:8:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_type$_t_address_payable_$",
                                                            "typeString": "type(address payable)"
                                                        },
                                                        "typeName": {
                                                            "id": 7,
                                                            "name": "address",
                                                            "nodeType": "ElementaryTypeName",
                                                            "src": "150:8:0",
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
                                                    "src": "150:19:0",
                                                    "tryCall": false,
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_address_payable",
                                                        "typeString": "address payable"
                                                    }
                                                },
                                                "src": "142:27:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_address_payable",
                                                    "typeString": "address payable"
                                                }
                                            },
                                            "id": 13,
                                            "nodeType": "ExpressionStatement",
                                            "src": "142:27:0"
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
                                    "src": "122:2:0"
                                },
                                "returnParameters": {
                                    "id": 5,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "132:0:0"
                                },
                                "scope": 38,
                                "src": "111:65:0",
                                "stateMutability": "nonpayable",
                                "virtual": false,
                                "visibility": "public"
                            },
                            {
                                "body": {
                                    "id": 36,
                                    "nodeType": "Block",
                                    "src": "244:106:0",
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
                                                                "name": "tx",
                                                                "nodeType": "Identifier",
                                                                "overloadedDeclarations": [],
                                                                "referencedDeclaration": -26,
                                                                "src": "262:2:0",
                                                                "typeDescriptions": {
                                                                    "typeIdentifier": "t_magic_transaction",
                                                                    "typeString": "tx"
                                                                }
                                                            },
                                                            "id": 24,
                                                            "isConstant": false,
                                                            "isLValue": false,
                                                            "isPure": false,
                                                            "lValueRequested": false,
                                                            "memberLocation": "265:6:0",
                                                            "memberName": "origin",
                                                            "nodeType": "MemberAccess",
                                                            "src": "262:9:0",
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
                                                            "src": "275:5:0",
                                                            "typeDescriptions": {
                                                                "typeIdentifier": "t_address_payable",
                                                                "typeString": "address payable"
                                                            }
                                                        },
                                                        "src": "262:18:0",
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
                                                        "src": "282:25:0",
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
                                                    "src": "254:7:0",
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
                                                "src": "254:54:0",
                                                "tryCall": false,
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_tuple$__$",
                                                    "typeString": "tuple()"
                                                }
                                            },
                                            "id": 29,
                                            "nodeType": "ExpressionStatement",
                                            "src": "254:54:0"
                                        },
                                        {
                                            "expression": {
                                                "arguments": [
                                                    {
                                                        "id": 33,
                                                        "name": "amount",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 19,
                                                        "src": "336:6:0",
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
                                                        "id": 30,
                                                        "name": "receiver",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 17,
                                                        "src": "318:8:0",
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
                                                    "memberLocation": "327:8:0",
                                                    "memberName": "transfer",
                                                    "nodeType": "MemberAccess",
                                                    "src": "318:17:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_function_transfer_nonpayable$_t_uint256_$returns$__$",
                                                        "typeString": "function (uint256)"
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
                                                "src": "318:25:0",
                                                "tryCall": false,
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_tuple$__$",
                                                    "typeString": "tuple()"
                                                }
                                            },
                                            "id": 35,
                                            "nodeType": "ExpressionStatement",
                                            "src": "318:25:0"
                                        }
                                    ]
                                },
                                "functionSelector": "9e1a00aa",
                                "id": 37,
                                "implemented": true,
                                "kind": "function",
                                "modifiers": [],
                                "name": "sendTo",
                                "nameLocation": "191:6:0",
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
                                            "nameLocation": "214:8:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 37,
                                            "src": "198:24:0",
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
                                                "src": "198:15:0",
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
                                            "nameLocation": "229:6:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 37,
                                            "src": "224:11:0",
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
                                                "src": "224:4:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint256",
                                                    "typeString": "uint256"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "197:39:0"
                                },
                                "returnParameters": {
                                    "id": 21,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "244:0:0"
                                },
                                "scope": 38,
                                "src": "182:168:0",
                                "stateMutability": "nonpayable",
                                "virtual": false,
                                "visibility": "public"
                            }
                        ],
                        "scope": 39,
                        "src": "56:296:0",
                        "usedErrors": [],
                        "usedEvents": []
                    }
                ],
                "src": "32:320:0"
            },
            "id": 0
        }
    },
    "version": "0.8.20+commit.a1b79de6.Darwin.appleclang"
}"""
    return json.loads(tx_json)


def test_tx_origin_used_for_access_control(tx_origin_used_for_access_control_ast):
    results = process_yaml(
        "eburger/templates/tx_origin_used_for_access_control.yaml",
        tx_origin_used_for_access_control_ast,
    )
    assert "Line 11 Columns 8-62" in results["results"][0]
