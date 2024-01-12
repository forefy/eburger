import json
import pytest
from eburger.serializer import reduce_json
from eburger.template_utils import parse_code_highlight

from eburger.yaml_parser import process_yaml


@pytest.fixture
def vulnerable_ast() -> (dict, list):
    ast_json = """{
    "contracts": {
        "vulnerable_contracts/use_of_call_or_send_on_payable.sol:UngoodContract": {
            "abi": [
                {
                    "inputs": [
                        {
                            "internalType": "address payable",
                            "name": "recipient",
                            "type": "address"
                        },
                        {
                            "internalType": "uint256",
                            "name": "amount",
                            "type": "uint256"
                        }
                    ],
                    "name": "sendEther",
                    "outputs": [],
                    "stateMutability": "nonpayable",
                    "type": "function"
                },
                {
                    "inputs": [
                        {
                            "internalType": "address payable",
                            "name": "recipient",
                            "type": "address"
                        },
                        {
                            "internalType": "uint256",
                            "name": "amount",
                            "type": "uint256"
                        }
                    ],
                    "name": "transferEther",
                    "outputs": [],
                    "stateMutability": "nonpayable",
                    "type": "function"
                }
            ],
            "bin": "608060405234801561000f575f80fd5b506102b18061001d5f395ff3fe608060405234801561000f575f80fd5b5060043610610034575f3560e01c806305b1137b14610038578063c1756a2c14610054575b5f80fd5b610052600480360381019061004d91906101c5565b610070565b005b61006e600480360381019061006991906101c5565b6100b8565b005b8173ffffffffffffffffffffffffffffffffffffffff166108fc8290811502906040515f60405180830381858888f193505050501580156100b3573d5f803e3d5ffd5b505050565b5f8273ffffffffffffffffffffffffffffffffffffffff166108fc8390811502906040515f60405180830381858888f1935050505090508061012f576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016101269061025d565b60405180910390fd5b505050565b5f80fd5b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f61016182610138565b9050919050565b61017181610157565b811461017b575f80fd5b50565b5f8135905061018c81610168565b92915050565b5f819050919050565b6101a481610192565b81146101ae575f80fd5b50565b5f813590506101bf8161019b565b92915050565b5f80604083850312156101db576101da610134565b5b5f6101e88582860161017e565b92505060206101f9858286016101b1565b9150509250929050565b5f82825260208201905092915050565b7f4661696c656420746f2073656e642045746865720000000000000000000000005f82015250565b5f610247601483610203565b915061025282610213565b602082019050919050565b5f6020820190508181035f8301526102748161023b565b905091905056fea26469706673582212206b982a478b85b0e9ed67f6444d7497bcedad7c285e9a796d467882a610a8d6d364736f6c63430008140033",
            "bin-runtime": "608060405234801561000f575f80fd5b5060043610610034575f3560e01c806305b1137b14610038578063c1756a2c14610054575b5f80fd5b610052600480360381019061004d91906101c5565b610070565b005b61006e600480360381019061006991906101c5565b6100b8565b005b8173ffffffffffffffffffffffffffffffffffffffff166108fc8290811502906040515f60405180830381858888f193505050501580156100b3573d5f803e3d5ffd5b505050565b5f8273ffffffffffffffffffffffffffffffffffffffff166108fc8390811502906040515f60405180830381858888f1935050505090508061012f576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016101269061025d565b60405180910390fd5b505050565b5f80fd5b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f61016182610138565b9050919050565b61017181610157565b811461017b575f80fd5b50565b5f8135905061018c81610168565b92915050565b5f819050919050565b6101a481610192565b81146101ae575f80fd5b50565b5f813590506101bf8161019b565b92915050565b5f80604083850312156101db576101da610134565b5b5f6101e88582860161017e565b92505060206101f9858286016101b1565b9150509250929050565b5f82825260208201905092915050565b7f4661696c656420746f2073656e642045746865720000000000000000000000005f82015250565b5f610247601483610203565b915061025282610213565b602082019050919050565b5f6020820190508181035f8301526102748161023b565b905091905056fea26469706673582212206b982a478b85b0e9ed67f6444d7497bcedad7c285e9a796d467882a610a8d6d364736f6c63430008140033",
            "devdoc": {
                "kind": "dev",
                "methods": {},
                "version": 1
            },
            "hashes": {
                "sendEther(address,uint256)": "c1756a2c",
                "transferEther(address,uint256)": "05b1137b"
            },
            "srcmap": "57:435:0:-:0;;;;;;;;;;;;;;;;;;;",
            "srcmap-runtime": "57:435:0:-:0;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;87:175;;;;;;;;;;;;;:::i;:::-;;:::i;:::-;;268:222;;;;;;;;;;;;;:::i;:::-;;:::i;:::-;;87:175;229:9;:18;;:26;248:6;229:26;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;87:175;;:::o;268:222::-;402:9;414;:14;;:22;429:6;414:22;;;;;;;;;;;;;;;;;;;;;;;402:34;;454:4;446:37;;;;;;;;;;;;:::i;:::-;;;;;;;;;337:153;268:222;;:::o;88:117:1:-;197:1;194;187:12;334:126;371:7;411:42;404:5;400:54;389:65;;334:126;;;:::o;466:104::-;511:7;540:24;558:5;540:24;:::i;:::-;529:35;;466:104;;;:::o;576:138::-;657:32;683:5;657:32;:::i;:::-;650:5;647:43;637:71;;704:1;701;694:12;637:71;576:138;:::o;720:155::-;774:5;812:6;799:20;790:29;;828:41;863:5;828:41;:::i;:::-;720:155;;;;:::o;881:77::-;918:7;947:5;936:16;;881:77;;;:::o;964:122::-;1037:24;1055:5;1037:24;:::i;:::-;1030:5;1027:35;1017:63;;1076:1;1073;1066:12;1017:63;964:122;:::o;1092:139::-;1138:5;1176:6;1163:20;1154:29;;1192:33;1219:5;1192:33;:::i;:::-;1092:139;;;;:::o;1237:490::-;1313:6;1321;1370:2;1358:9;1349:7;1345:23;1341:32;1338:119;;;1376:79;;:::i;:::-;1338:119;1496:1;1521:61;1574:7;1565:6;1554:9;1550:22;1521:61;:::i;:::-;1511:71;;1467:125;1631:2;1657:53;1702:7;1693:6;1682:9;1678:22;1657:53;:::i;:::-;1647:63;;1602:118;1237:490;;;;;:::o;1733:169::-;1817:11;1851:6;1846:3;1839:19;1891:4;1886:3;1882:14;1867:29;;1733:169;;;;:::o;1908:170::-;2048:22;2044:1;2036:6;2032:14;2025:46;1908:170;:::o;2084:366::-;2226:3;2247:67;2311:2;2306:3;2247:67;:::i;:::-;2240:74;;2323:93;2412:3;2323:93;:::i;:::-;2441:2;2436:3;2432:12;2425:19;;2084:366;;;:::o;2456:419::-;2622:4;2660:2;2649:9;2645:18;2637:26;;2709:9;2703:4;2699:20;2695:1;2684:9;2680:17;2673:47;2737:131;2863:4;2737:131;:::i;:::-;2729:139;;2456:419;;;:::o",
            "userdoc": {
                "kind": "user",
                "methods": {},
                "version": 1
            }
        }
    },
    "sourceList": [
        "vulnerable_contracts/use_of_call_or_send_on_payable.sol"
    ],
    "sources": {
        "vulnerable_contracts/use_of_call_or_send_on_payable.sol": {
            "AST": {
                "absolutePath": "vulnerable_contracts/use_of_call_or_send_on_payable.sol",
                "exportedSymbols": {
                    "UngoodContract": [
                        36
                    ]
                },
                "id": 37,
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
                        "canonicalName": "UngoodContract",
                        "contractDependencies": [],
                        "contractKind": "contract",
                        "fullyImplemented": true,
                        "id": 36,
                        "linearizedBaseContracts": [
                            36
                        ],
                        "name": "UngoodContract",
                        "nameLocation": "66:14:0",
                        "nodeType": "ContractDefinition",
                        "nodes": [
                            {
                                "body": {
                                    "id": 14,
                                    "nodeType": "Block",
                                    "src": "160:102:0",
                                    "statements": [
                                        {
                                            "expression": {
                                                "arguments": [
                                                    {
                                                        "id": 11,
                                                        "name": "amount",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 5,
                                                        "src": "248:6:0",
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
                                                        "id": 8,
                                                        "name": "recipient",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 3,
                                                        "src": "229:9:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_address_payable",
                                                            "typeString": "address payable"
                                                        }
                                                    },
                                                    "id": 10,
                                                    "isConstant": false,
                                                    "isLValue": false,
                                                    "isPure": false,
                                                    "lValueRequested": false,
                                                    "memberLocation": "239:8:0",
                                                    "memberName": "transfer",
                                                    "nodeType": "MemberAccess",
                                                    "src": "229:18:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_function_transfer_nonpayable$_t_uint256_$returns$__$",
                                                        "typeString": "function (uint256)"
                                                    }
                                                },
                                                "id": 12,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "kind": "functionCall",
                                                "lValueRequested": false,
                                                "nameLocations": [],
                                                "names": [],
                                                "nodeType": "FunctionCall",
                                                "src": "229:26:0",
                                                "tryCall": false,
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_tuple$__$",
                                                    "typeString": "tuple()"
                                                }
                                            },
                                            "id": 13,
                                            "nodeType": "ExpressionStatement",
                                            "src": "229:26:0"
                                        }
                                    ]
                                },
                                "functionSelector": "05b1137b",
                                "id": 15,
                                "implemented": true,
                                "kind": "function",
                                "modifiers": [],
                                "name": "transferEther",
                                "nameLocation": "96:13:0",
                                "nodeType": "FunctionDefinition",
                                "parameters": {
                                    "id": 6,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 3,
                                            "mutability": "mutable",
                                            "name": "recipient",
                                            "nameLocation": "126:9:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 15,
                                            "src": "110:25:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_address_payable",
                                                "typeString": "address payable"
                                            },
                                            "typeName": {
                                                "id": 2,
                                                "name": "address",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "110:15:0",
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
                                            "id": 5,
                                            "mutability": "mutable",
                                            "name": "amount",
                                            "nameLocation": "145:6:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 15,
                                            "src": "137:14:0",
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
                                                "src": "137:7:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint256",
                                                    "typeString": "uint256"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "109:43:0"
                                },
                                "returnParameters": {
                                    "id": 7,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "160:0:0"
                                },
                                "scope": 36,
                                "src": "87:175:0",
                                "stateMutability": "nonpayable",
                                "virtual": false,
                                "visibility": "public"
                            },
                            {
                                "body": {
                                    "id": 34,
                                    "nodeType": "Block",
                                    "src": "337:153:0",
                                    "statements": [
                                        {
                                            "assignments": [
                                                23
                                            ],
                                            "declarations": [
                                                {
                                                    "constant": false,
                                                    "id": 23,
                                                    "mutability": "mutable",
                                                    "name": "sent",
                                                    "nameLocation": "407:4:0",
                                                    "nodeType": "VariableDeclaration",
                                                    "scope": 34,
                                                    "src": "402:9:0",
                                                    "stateVariable": false,
                                                    "storageLocation": "default",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_bool",
                                                        "typeString": "bool"
                                                    },
                                                    "typeName": {
                                                        "id": 22,
                                                        "name": "bool",
                                                        "nodeType": "ElementaryTypeName",
                                                        "src": "402:4:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_bool",
                                                            "typeString": "bool"
                                                        }
                                                    },
                                                    "visibility": "internal"
                                                }
                                            ],
                                            "id": 28,
                                            "initialValue": {
                                                "arguments": [
                                                    {
                                                        "id": 26,
                                                        "name": "amount",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 19,
                                                        "src": "429:6:0",
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
                                                        "id": 24,
                                                        "name": "recipient",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 17,
                                                        "src": "414:9:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_address_payable",
                                                            "typeString": "address payable"
                                                        }
                                                    },
                                                    "id": 25,
                                                    "isConstant": false,
                                                    "isLValue": false,
                                                    "isPure": false,
                                                    "lValueRequested": false,
                                                    "memberLocation": "424:4:0",
                                                    "memberName": "send",
                                                    "nodeType": "MemberAccess",
                                                    "src": "414:14:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_function_send_nonpayable$_t_uint256_$returns$_t_bool_$",
                                                        "typeString": "function (uint256) returns (bool)"
                                                    }
                                                },
                                                "id": 27,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "kind": "functionCall",
                                                "lValueRequested": false,
                                                "nameLocations": [],
                                                "names": [],
                                                "nodeType": "FunctionCall",
                                                "src": "414:22:0",
                                                "tryCall": false,
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_bool",
                                                    "typeString": "bool"
                                                }
                                            },
                                            "nodeType": "VariableDeclarationStatement",
                                            "src": "402:34:0"
                                        },
                                        {
                                            "expression": {
                                                "arguments": [
                                                    {
                                                        "id": 30,
                                                        "name": "sent",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": 23,
                                                        "src": "454:4:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_bool",
                                                            "typeString": "bool"
                                                        }
                                                    },
                                                    {
                                                        "hexValue": "4661696c656420746f2073656e64204574686572",
                                                        "id": 31,
                                                        "isConstant": false,
                                                        "isLValue": false,
                                                        "isPure": true,
                                                        "kind": "string",
                                                        "lValueRequested": false,
                                                        "nodeType": "Literal",
                                                        "src": "460:22:0",
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
                                                    "id": 29,
                                                    "name": "require",
                                                    "nodeType": "Identifier",
                                                    "overloadedDeclarations": [
                                                        -18,
                                                        -18
                                                    ],
                                                    "referencedDeclaration": -18,
                                                    "src": "446:7:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_function_require_pure$_t_bool_$_t_string_memory_ptr_$returns$__$",
                                                        "typeString": "function (bool,string memory) pure"
                                                    }
                                                },
                                                "id": 32,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "kind": "functionCall",
                                                "lValueRequested": false,
                                                "nameLocations": [],
                                                "names": [],
                                                "nodeType": "FunctionCall",
                                                "src": "446:37:0",
                                                "tryCall": false,
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_tuple$__$",
                                                    "typeString": "tuple()"
                                                }
                                            },
                                            "id": 33,
                                            "nodeType": "ExpressionStatement",
                                            "src": "446:37:0"
                                        }
                                    ]
                                },
                                "functionSelector": "c1756a2c",
                                "id": 35,
                                "implemented": true,
                                "kind": "function",
                                "modifiers": [],
                                "name": "sendEther",
                                "nameLocation": "277:9:0",
                                "nodeType": "FunctionDefinition",
                                "parameters": {
                                    "id": 20,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 17,
                                            "mutability": "mutable",
                                            "name": "recipient",
                                            "nameLocation": "303:9:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 35,
                                            "src": "287:25:0",
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
                                                "src": "287:15:0",
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
                                            "nameLocation": "322:6:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 35,
                                            "src": "314:14:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_uint256",
                                                "typeString": "uint256"
                                            },
                                            "typeName": {
                                                "id": 18,
                                                "name": "uint256",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "314:7:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint256",
                                                    "typeString": "uint256"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "286:43:0"
                                },
                                "returnParameters": {
                                    "id": 21,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "337:0:0"
                                },
                                "scope": 36,
                                "src": "268:222:0",
                                "stateMutability": "nonpayable",
                                "virtual": false,
                                "visibility": "public"
                            }
                        ],
                        "scope": 37,
                        "src": "57:435:0",
                        "usedErrors": [],
                        "usedEvents": []
                    }
                ],
                "src": "32:460:0"
            },
            "id": 0
        }
    },
    "version": "0.8.20+commit.a1b79de6.Darwin.appleclang"
}"""
    return json.loads(ast_json)


def test_use_of_call_or_send_on_payable(vulnerable_ast):
    ast_json, src_file_list = reduce_json(vulnerable_ast)
    results = process_yaml(
        "eburger/templates/use_of_call_or_send_on_payable.yaml",
        ast_json,
        src_file_list,
    )
    assert "Line 7 Columns 9-35" in results["results"][0]["lines"]
