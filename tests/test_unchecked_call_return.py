import json
import pytest
from eburger.serializer import reduce_json
from eburger.yaml_parser import process_yaml


@pytest.fixture
def vulnerable_ast() -> tuple[dict, list]:
    unchecked_ast = """{
    "contracts": {
        "vulnerable_contracts/unchecked_call_return.sol:VulnerableContract": {
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
                    "name": "unsafeSend",
                    "outputs": [],
                    "stateMutability": "nonpayable",
                    "type": "function"
                },
                {
                    "stateMutability": "payable",
                    "type": "receive"
                }
            ],
            "bin": "608060405234801561000f575f80fd5b50335f806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506103098061005c5f395ff3fe608060405260043610610021575f3560e01c8063102d27601461002c57610028565b3661002857005b5f80fd5b348015610037575f80fd5b50610052600480360381019061004d91906101dc565b610054565b005b5f8054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16146100e1576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016100d890610274565b60405180910390fd5b8173ffffffffffffffffffffffffffffffffffffffff1681604051610105906102bf565b5f6040518083038185875af1925050503d805f811461013f576040519150601f19603f3d011682016040523d82523d5f602084013e610144565b606091505b5050505050565b5f80fd5b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f6101788261014f565b9050919050565b6101888161016e565b8114610192575f80fd5b50565b5f813590506101a38161017f565b92915050565b5f819050919050565b6101bb816101a9565b81146101c5575f80fd5b50565b5f813590506101d6816101b2565b92915050565b5f80604083850312156101f2576101f161014b565b5b5f6101ff85828601610195565b9250506020610210858286016101c8565b9150509250929050565b5f82825260208201905092915050565b7f43616c6c6572206973206e6f7420746865206f776e65720000000000000000005f82015250565b5f61025e60178361021a565b91506102698261022a565b602082019050919050565b5f6020820190508181035f83015261028b81610252565b9050919050565b5f81905092915050565b50565b5f6102aa5f83610292565b91506102b58261029c565b5f82019050919050565b5f6102c98261029f565b915081905091905056fea2646970667358221220c788a184b32b9abbfafc743d6d5e3b8ceae2bb24ad7162c9d56d45d7e261cf2964736f6c63430008140033",
            "bin-runtime": "608060405260043610610021575f3560e01c8063102d27601461002c57610028565b3661002857005b5f80fd5b348015610037575f80fd5b50610052600480360381019061004d91906101dc565b610054565b005b5f8054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16146100e1576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016100d890610274565b60405180910390fd5b8173ffffffffffffffffffffffffffffffffffffffff1681604051610105906102bf565b5f6040518083038185875af1925050503d805f811461013f576040519150601f19603f3d011682016040523d82523d5f602084013e610144565b606091505b5050505050565b5f80fd5b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f6101788261014f565b9050919050565b6101888161016e565b8114610192575f80fd5b50565b5f813590506101a38161017f565b92915050565b5f819050919050565b6101bb816101a9565b81146101c5575f80fd5b50565b5f813590506101d6816101b2565b92915050565b5f80604083850312156101f2576101f161014b565b5b5f6101ff85828601610195565b9250506020610210858286016101c8565b9150509250929050565b5f82825260208201905092915050565b7f43616c6c6572206973206e6f7420746865206f776e65720000000000000000005f82015250565b5f61025e60178361021a565b91506102698261022a565b602082019050919050565b5f6020820190508181035f83015261028b81610252565b9050919050565b5f81905092915050565b50565b5f6102aa5f83610292565b91506102b58261029c565b5f82019050919050565b5f6102c98261029f565b915081905091905056fea2646970667358221220c788a184b32b9abbfafc743d6d5e3b8ceae2bb24ad7162c9d56d45d7e261cf2964736f6c63430008140033",
            "devdoc": {
                "kind": "dev",
                "methods": {},
                "version": 1
            },
            "hashes": {
                "unsafeSend(address,uint256)": "102d2760"
            },
            "srcmap": "56:543:0:-:0;;;117:58;;;;;;;;;;157:10;141:5;;:27;;;;;;;;;;;;;;;;;;56:543;;;;;;",
            "srcmap-runtime": "56:543:0:-:0;;;;;;;;;;;;;;;;;;;;;;;;;;;;253:254;;;;;;;;;;;;;;;;;;;;;;;:::i;:::-;;:::i;:::-;;;351:5;;;;;;;;;;337:19;;:10;:19;;;329:55;;;;;;;;;;;;:::i;:::-;;;;;;;;;468:8;:13;;489:6;468:32;;;;;:::i;:::-;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;253:254;;:::o;88:117:1:-;197:1;194;187:12;334:126;371:7;411:42;404:5;400:54;389:65;;334:126;;;:::o;466:104::-;511:7;540:24;558:5;540:24;:::i;:::-;529:35;;466:104;;;:::o;576:138::-;657:32;683:5;657:32;:::i;:::-;650:5;647:43;637:71;;704:1;701;694:12;637:71;576:138;:::o;720:155::-;774:5;812:6;799:20;790:29;;828:41;863:5;828:41;:::i;:::-;720:155;;;;:::o;881:77::-;918:7;947:5;936:16;;881:77;;;:::o;964:122::-;1037:24;1055:5;1037:24;:::i;:::-;1030:5;1027:35;1017:63;;1076:1;1073;1066:12;1017:63;964:122;:::o;1092:139::-;1138:5;1176:6;1163:20;1154:29;;1192:33;1219:5;1192:33;:::i;:::-;1092:139;;;;:::o;1237:490::-;1313:6;1321;1370:2;1358:9;1349:7;1345:23;1341:32;1338:119;;;1376:79;;:::i;:::-;1338:119;1496:1;1521:61;1574:7;1565:6;1554:9;1550:22;1521:61;:::i;:::-;1511:71;;1467:125;1631:2;1657:53;1702:7;1693:6;1682:9;1678:22;1657:53;:::i;:::-;1647:63;;1602:118;1237:490;;;;;:::o;1733:169::-;1817:11;1851:6;1846:3;1839:19;1891:4;1886:3;1882:14;1867:29;;1733:169;;;;:::o;1908:173::-;2048:25;2044:1;2036:6;2032:14;2025:49;1908:173;:::o;2087:366::-;2229:3;2250:67;2314:2;2309:3;2250:67;:::i;:::-;2243:74;;2326:93;2415:3;2326:93;:::i;:::-;2444:2;2439:3;2435:12;2428:19;;2087:366;;;:::o;2459:419::-;2625:4;2663:2;2652:9;2648:18;2640:26;;2712:9;2706:4;2702:20;2698:1;2687:9;2683:17;2676:47;2740:131;2866:4;2740:131;:::i;:::-;2732:139;;2459:419;;;:::o;2884:147::-;2985:11;3022:3;3007:18;;2884:147;;;;:::o;3037:114::-;;:::o;3157:398::-;3316:3;3337:83;3418:1;3413:3;3337:83;:::i;:::-;3330:90;;3429:93;3518:3;3429:93;:::i;:::-;3547:1;3542:3;3538:11;3531:18;;3157:398;;;:::o;3561:379::-;3745:3;3767:147;3910:3;3767:147;:::i;:::-;3760:154;;3931:3;3924:10;;3561:379;;;:::o",
            "userdoc": {
                "kind": "user",
                "methods": {},
                "version": 1
            }
        }
    },
    "sourceList": [
        "vulnerable_contracts/unchecked_call_return.sol"
    ],
    "sources": {
        "vulnerable_contracts/unchecked_call_return.sol": {
            "AST": {
                "absolutePath": "vulnerable_contracts/unchecked_call_return.sol",
                "exportedSymbols": {
                    "VulnerableContract": [
                        44
                    ]
                },
                "id": 45,
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
                        "canonicalName": "VulnerableContract",
                        "contractDependencies": [],
                        "contractKind": "contract",
                        "fullyImplemented": true,
                        "id": 44,
                        "linearizedBaseContracts": [
                            44
                        ],
                        "name": "VulnerableContract",
                        "nameLocation": "65:18:0",
                        "nodeType": "ContractDefinition",
                        "nodes": [
                            {
                                "constant": false,
                                "id": 3,
                                "mutability": "mutable",
                                "name": "owner",
                                "nameLocation": "106:5:0",
                                "nodeType": "VariableDeclaration",
                                "scope": 44,
                                "src": "90:21:0",
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
                                    "src": "90:15:0",
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
                                    "src": "131:44:0",
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
                                                    "src": "141:5:0",
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
                                                                "src": "157:3:0",
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
                                                            "memberLocation": "161:6:0",
                                                            "memberName": "sender",
                                                            "nodeType": "MemberAccess",
                                                            "src": "157:10:0",
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
                                                        "src": "149:8:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_type$_t_address_payable_$",
                                                            "typeString": "type(address payable)"
                                                        },
                                                        "typeName": {
                                                            "id": 7,
                                                            "name": "address",
                                                            "nodeType": "ElementaryTypeName",
                                                            "src": "149:8:0",
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
                                                    "src": "149:19:0",
                                                    "tryCall": false,
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_address_payable",
                                                        "typeString": "address payable"
                                                    }
                                                },
                                                "src": "141:27:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_address_payable",
                                                    "typeString": "address payable"
                                                }
                                            },
                                            "id": 13,
                                            "nodeType": "ExpressionStatement",
                                            "src": "141:27:0"
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
                                    "src": "128:2:0"
                                },
                                "returnParameters": {
                                    "id": 5,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "131:0:0"
                                },
                                "scope": 44,
                                "src": "117:58:0",
                                "stateMutability": "nonpayable",
                                "virtual": false,
                                "visibility": "public"
                            },
                            {
                                "body": {
                                    "id": 38,
                                    "nodeType": "Block",
                                    "src": "319:188:0",
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
                                                                "name": "msg",
                                                                "nodeType": "Identifier",
                                                                "overloadedDeclarations": [],
                                                                "referencedDeclaration": -15,
                                                                "src": "337:3:0",
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
                                                            "memberLocation": "341:6:0",
                                                            "memberName": "sender",
                                                            "nodeType": "MemberAccess",
                                                            "src": "337:10:0",
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
                                                            "src": "351:5:0",
                                                            "typeDescriptions": {
                                                                "typeIdentifier": "t_address_payable",
                                                                "typeString": "address payable"
                                                            }
                                                        },
                                                        "src": "337:19:0",
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
                                                        "src": "358:25:0",
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
                                                    "src": "329:7:0",
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
                                                "src": "329:55:0",
                                                "tryCall": false,
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_tuple$__$",
                                                    "typeString": "tuple()"
                                                }
                                            },
                                            "id": 29,
                                            "nodeType": "ExpressionStatement",
                                            "src": "329:55:0"
                                        },
                                        {
                                            "expression": {
                                                "arguments": [
                                                    {
                                                        "hexValue": "",
                                                        "id": 35,
                                                        "isConstant": false,
                                                        "isLValue": false,
                                                        "isPure": true,
                                                        "kind": "string",
                                                        "lValueRequested": false,
                                                        "nodeType": "Literal",
                                                        "src": "497:2:0",
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
                                                            "id": 30,
                                                            "name": "receiver",
                                                            "nodeType": "Identifier",
                                                            "overloadedDeclarations": [],
                                                            "referencedDeclaration": 17,
                                                            "src": "468:8:0",
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
                                                        "memberLocation": "477:4:0",
                                                        "memberName": "call",
                                                        "nodeType": "MemberAccess",
                                                        "src": "468:13:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_function_barecall_payable$_t_bytes_memory_ptr_$returns$_t_bool_$_t_bytes_memory_ptr_$",
                                                            "typeString": "function (bytes memory) payable returns (bool,bytes memory)"
                                                        }
                                                    },
                                                    "id": 34,
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
                                                            "id": 33,
                                                            "name": "amount",
                                                            "nodeType": "Identifier",
                                                            "overloadedDeclarations": [],
                                                            "referencedDeclaration": 19,
                                                            "src": "489:6:0",
                                                            "typeDescriptions": {
                                                                "typeIdentifier": "t_uint256",
                                                                "typeString": "uint256"
                                                            }
                                                        }
                                                    ],
                                                    "src": "468:28:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_function_barecall_payable$_t_bytes_memory_ptr_$returns$_t_bool_$_t_bytes_memory_ptr_$value",
                                                        "typeString": "function (bytes memory) payable returns (bool,bytes memory)"
                                                    }
                                                },
                                                "id": 36,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "kind": "functionCall",
                                                "lValueRequested": false,
                                                "nameLocations": [],
                                                "names": [],
                                                "nodeType": "FunctionCall",
                                                "src": "468:32:0",
                                                "tryCall": false,
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_tuple$_t_bool_$_t_bytes_memory_ptr_$",
                                                    "typeString": "tuple(bool,bytes memory)"
                                                }
                                            },
                                            "id": 37,
                                            "nodeType": "ExpressionStatement",
                                            "src": "468:32:0"
                                        }
                                    ]
                                },
                                "functionSelector": "102d2760",
                                "id": 39,
                                "implemented": true,
                                "kind": "function",
                                "modifiers": [],
                                "name": "unsafeSend",
                                "nameLocation": "262:10:0",
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
                                            "nameLocation": "289:8:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 39,
                                            "src": "273:24:0",
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
                                                "src": "273:15:0",
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
                                            "nameLocation": "304:6:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 39,
                                            "src": "299:11:0",
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
                                                "src": "299:4:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_uint256",
                                                    "typeString": "uint256"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "272:39:0"
                                },
                                "returnParameters": {
                                    "id": 21,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "319:0:0"
                                },
                                "scope": 44,
                                "src": "253:254:0",
                                "stateMutability": "nonpayable",
                                "virtual": false,
                                "visibility": "public"
                            },
                            {
                                "body": {
                                    "id": 42,
                                    "nodeType": "Block",
                                    "src": "595:2:0",
                                    "statements": []
                                },
                                "id": 43,
                                "implemented": true,
                                "kind": "receive",
                                "modifiers": [],
                                "name": "",
                                "nameLocation": "-1:-1:-1",
                                "nodeType": "FunctionDefinition",
                                "parameters": {
                                    "id": 40,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "575:2:0"
                                },
                                "returnParameters": {
                                    "id": 41,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "595:0:0"
                                },
                                "scope": 44,
                                "src": "568:29:0",
                                "stateMutability": "payable",
                                "virtual": false,
                                "visibility": "external"
                            }
                        ],
                        "scope": 45,
                        "src": "56:543:0",
                        "usedErrors": [],
                        "usedEvents": []
                    }
                ],
                "src": "32:568:0"
            },
            "id": 0
        }
    },
    "version": "0.8.20+commit.a1b79de6.Darwin.appleclang"
}"""
    return json.loads(unchecked_ast)


def test_unchecked_call_return(vulnerable_ast):
    ast_json, src_file_list = reduce_json(vulnerable_ast)
    results = process_yaml(
        "eburger/templates/unchecked_call_return.yaml",
        ast_json,
        src_file_list,
    )
    assert "Line 14 Columns 9-37" in results["results"][0]["lines"]
