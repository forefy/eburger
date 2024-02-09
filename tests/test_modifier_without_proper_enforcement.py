import json
import pytest
from eburger.serializer import reduce_json
from eburger.yaml_parser import process_yaml


@pytest.fixture
def vulnerable_ast() -> tuple[dict, list]:
    ast_json = """{
    "contracts": {
        "vulnerable_contracts/modifier_without_proper_enforcement.sol:BuggieContract": {
            "abi": [
                {
                    "inputs": [],
                    "stateMutability": "nonpayable",
                    "type": "constructor"
                },
                {
                    "inputs": [
                        {
                            "internalType": "address",
                            "name": "_newOwner",
                            "type": "address"
                        }
                    ],
                    "name": "changeOwner",
                    "outputs": [],
                    "stateMutability": "nonpayable",
                    "type": "function"
                },
                {
                    "inputs": [],
                    "name": "owner",
                    "outputs": [
                        {
                            "internalType": "address",
                            "name": "",
                            "type": "address"
                        }
                    ],
                    "stateMutability": "view",
                    "type": "function"
                }
            ],
            "bin": "608060405234801561000f575f80fd5b50335f806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506101e18061005c5f395ff3fe608060405234801561000f575f80fd5b5060043610610034575f3560e01c80638da5cb5b14610038578063a6f9dae114610056575b5f80fd5b610040610072565b60405161004d9190610139565b60405180910390f35b610070600480360381019061006b9190610180565b610095565b005b5f8054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b3373ffffffffffffffffffffffffffffffffffffffff165f8054906101000a90505050805f806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555050565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f610123826100fa565b9050919050565b61013381610119565b82525050565b5f60208201905061014c5f83018461012a565b92915050565b5f80fd5b61015f81610119565b8114610169575f80fd5b50565b5f8135905061017a81610156565b92915050565b5f6020828403121561019557610194610152565b5b5f6101a28482850161016c565b9150509291505056fea26469706673582212204dfdf9cdf39c2629ee7ab4252d3f4b30cf7baa53e291837111ad42c15e4936ed64736f6c63430008140033",
            "bin-runtime": "608060405234801561000f575f80fd5b5060043610610034575f3560e01c80638da5cb5b14610038578063a6f9dae114610056575b5f80fd5b610040610072565b60405161004d9190610139565b60405180910390f35b610070600480360381019061006b9190610180565b610095565b005b5f8054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b3373ffffffffffffffffffffffffffffffffffffffff165f8054906101000a90505050805f806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555050565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f610123826100fa565b9050919050565b61013381610119565b82525050565b5f60208201905061014c5f83018461012a565b92915050565b5f80fd5b61015f81610119565b8114610169575f80fd5b50565b5f8135905061017a81610156565b92915050565b5f6020828403121561019557610194610152565b5b5f6101a28482850161016c565b9150509291505056fea26469706673582212204dfdf9cdf39c2629ee7ab4252d3f4b30cf7baa53e291837111ad42c15e4936ed64736f6c63430008140033",
            "devdoc": {
                "kind": "dev",
                "methods": {},
                "version": 1
            },
            "hashes": {
                "changeOwner(address)": "a6f9dae1",
                "owner()": "8da5cb5b"
            },
            "srcmap": "24:507:0:-:0;;;80:49;;;;;;;;;;112:10;104:5;;:18;;;;;;;;;;;;;;;;;;24:507;;;;;;",
            "srcmap-runtime": "24:507:0:-:0;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;54:20;;;:::i;:::-;;;;;;;:::i;:::-;;;;;;;;280:249;;;;;;;;;;;;;:::i;:::-;;:::i;:::-;;54:20;;;;;;;;;;;;:::o;280:249::-;246:10;237:19;;:5;;;;;;;;;:19;513:9:::1;505:5;::::0;:17:::1;;;;;;;;;;;;;;;;;;280:249:::0;:::o;7:126:1:-;44:7;84:42;77:5;73:54;62:65;;7:126;;;:::o;139:96::-;176:7;205:24;223:5;205:24;:::i;:::-;194:35;;139:96;;;:::o;241:118::-;328:24;346:5;328:24;:::i;:::-;323:3;316:37;241:118;;:::o;365:222::-;458:4;496:2;485:9;481:18;473:26;;509:71;577:1;566:9;562:17;553:6;509:71;:::i;:::-;365:222;;;;:::o;674:117::-;783:1;780;773:12;920:122;993:24;1011:5;993:24;:::i;:::-;986:5;983:35;973:63;;1032:1;1029;1022:12;973:63;920:122;:::o;1048:139::-;1094:5;1132:6;1119:20;1110:29;;1148:33;1175:5;1148:33;:::i;:::-;1048:139;;;;:::o;1193:329::-;1252:6;1301:2;1289:9;1280:7;1276:23;1272:32;1269:119;;;1307:79;;:::i;:::-;1269:119;1427:1;1452:53;1497:7;1488:6;1477:9;1473:22;1452:53;:::i;:::-;1442:63;;1398:117;1193:329;;;;:::o",
            "userdoc": {
                "kind": "user",
                "methods": {},
                "version": 1
            }
        }
    },
    "sourceList": [
        "vulnerable_contracts/modifier_without_proper_enforcement.sol"
    ],
    "sources": {
        "vulnerable_contracts/modifier_without_proper_enforcement.sol": {
            "AST": {
                "absolutePath": "vulnerable_contracts/modifier_without_proper_enforcement.sol",
                "exportedSymbols": {
                    "BuggieContract": [
                        34
                    ]
                },
                "id": 35,
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
                        "src": "0:23:0"
                    },
                    {
                        "abstract": false,
                        "baseContracts": [],
                        "canonicalName": "BuggieContract",
                        "contractDependencies": [],
                        "contractKind": "contract",
                        "fullyImplemented": true,
                        "id": 34,
                        "linearizedBaseContracts": [
                            34
                        ],
                        "name": "BuggieContract",
                        "nameLocation": "33:14:0",
                        "nodeType": "ContractDefinition",
                        "nodes": [
                            {
                                "constant": false,
                                "functionSelector": "8da5cb5b",
                                "id": 3,
                                "mutability": "mutable",
                                "name": "owner",
                                "nameLocation": "69:5:0",
                                "nodeType": "VariableDeclaration",
                                "scope": 34,
                                "src": "54:20:0",
                                "stateVariable": true,
                                "storageLocation": "default",
                                "typeDescriptions": {
                                    "typeIdentifier": "t_address",
                                    "typeString": "address"
                                },
                                "typeName": {
                                    "id": 2,
                                    "name": "address",
                                    "nodeType": "ElementaryTypeName",
                                    "src": "54:7:0",
                                    "stateMutability": "nonpayable",
                                    "typeDescriptions": {
                                        "typeIdentifier": "t_address",
                                        "typeString": "address"
                                    }
                                },
                                "visibility": "public"
                            },
                            {
                                "body": {
                                    "id": 11,
                                    "nodeType": "Block",
                                    "src": "94:35:0",
                                    "statements": [
                                        {
                                            "expression": {
                                                "id": 9,
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
                                                    "src": "104:5:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_address",
                                                        "typeString": "address"
                                                    }
                                                },
                                                "nodeType": "Assignment",
                                                "operator": "=",
                                                "rightHandSide": {
                                                    "expression": {
                                                        "id": 7,
                                                        "name": "msg",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": -15,
                                                        "src": "112:3:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_magic_message",
                                                            "typeString": "msg"
                                                        }
                                                    },
                                                    "id": 8,
                                                    "isConstant": false,
                                                    "isLValue": false,
                                                    "isPure": false,
                                                    "lValueRequested": false,
                                                    "memberLocation": "116:6:0",
                                                    "memberName": "sender",
                                                    "nodeType": "MemberAccess",
                                                    "src": "112:10:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_address",
                                                        "typeString": "address"
                                                    }
                                                },
                                                "src": "104:18:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_address",
                                                    "typeString": "address"
                                                }
                                            },
                                            "id": 10,
                                            "nodeType": "ExpressionStatement",
                                            "src": "104:18:0"
                                        }
                                    ]
                                },
                                "id": 12,
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
                                    "src": "91:2:0"
                                },
                                "returnParameters": {
                                    "id": 5,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "94:0:0"
                                },
                                "scope": 34,
                                "src": "80:49:0",
                                "stateMutability": "nonpayable",
                                "virtual": false,
                                "visibility": "public"
                            },
                            {
                                "body": {
                                    "id": 20,
                                    "nodeType": "Block",
                                    "src": "156:118:0",
                                    "statements": [
                                        {
                                            "expression": {
                                                "commonType": {
                                                    "typeIdentifier": "t_address",
                                                    "typeString": "address"
                                                },
                                                "id": 17,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "lValueRequested": false,
                                                "leftExpression": {
                                                    "id": 14,
                                                    "name": "owner",
                                                    "nodeType": "Identifier",
                                                    "overloadedDeclarations": [],
                                                    "referencedDeclaration": 3,
                                                    "src": "237:5:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_address",
                                                        "typeString": "address"
                                                    }
                                                },
                                                "nodeType": "BinaryOperation",
                                                "operator": "==",
                                                "rightExpression": {
                                                    "expression": {
                                                        "id": 15,
                                                        "name": "msg",
                                                        "nodeType": "Identifier",
                                                        "overloadedDeclarations": [],
                                                        "referencedDeclaration": -15,
                                                        "src": "246:3:0",
                                                        "typeDescriptions": {
                                                            "typeIdentifier": "t_magic_message",
                                                            "typeString": "msg"
                                                        }
                                                    },
                                                    "id": 16,
                                                    "isConstant": false,
                                                    "isLValue": false,
                                                    "isPure": false,
                                                    "lValueRequested": false,
                                                    "memberLocation": "250:6:0",
                                                    "memberName": "sender",
                                                    "nodeType": "MemberAccess",
                                                    "src": "246:10:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_address",
                                                        "typeString": "address"
                                                    }
                                                },
                                                "src": "237:19:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_bool",
                                                    "typeString": "bool"
                                                }
                                            },
                                            "id": 18,
                                            "nodeType": "ExpressionStatement",
                                            "src": "237:19:0"
                                        },
                                        {
                                            "id": 19,
                                            "nodeType": "PlaceholderStatement",
                                            "src": "266:1:0"
                                        }
                                    ]
                                },
                                "id": 21,
                                "name": "onlyOwner",
                                "nameLocation": "144:9:0",
                                "nodeType": "ModifierDefinition",
                                "parameters": {
                                    "id": 13,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "153:2:0"
                                },
                                "src": "135:139:0",
                                "virtual": false,
                                "visibility": "internal"
                            },
                            {
                                "body": {
                                    "id": 32,
                                    "nodeType": "Block",
                                    "src": "337:192:0",
                                    "statements": [
                                        {
                                            "expression": {
                                                "id": 30,
                                                "isConstant": false,
                                                "isLValue": false,
                                                "isPure": false,
                                                "lValueRequested": false,
                                                "leftHandSide": {
                                                    "id": 28,
                                                    "name": "owner",
                                                    "nodeType": "Identifier",
                                                    "overloadedDeclarations": [],
                                                    "referencedDeclaration": 3,
                                                    "src": "505:5:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_address",
                                                        "typeString": "address"
                                                    }
                                                },
                                                "nodeType": "Assignment",
                                                "operator": "=",
                                                "rightHandSide": {
                                                    "id": 29,
                                                    "name": "_newOwner",
                                                    "nodeType": "Identifier",
                                                    "overloadedDeclarations": [],
                                                    "referencedDeclaration": 23,
                                                    "src": "513:9:0",
                                                    "typeDescriptions": {
                                                        "typeIdentifier": "t_address",
                                                        "typeString": "address"
                                                    }
                                                },
                                                "src": "505:17:0",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_address",
                                                    "typeString": "address"
                                                }
                                            },
                                            "id": 31,
                                            "nodeType": "ExpressionStatement",
                                            "src": "505:17:0"
                                        }
                                    ]
                                },
                                "functionSelector": "a6f9dae1",
                                "id": 33,
                                "implemented": true,
                                "kind": "function",
                                "modifiers": [
                                    {
                                        "id": 26,
                                        "kind": "modifierInvocation",
                                        "modifierName": {
                                            "id": 25,
                                            "name": "onlyOwner",
                                            "nameLocations": [
                                                "327:9:0"
                                            ],
                                            "nodeType": "IdentifierPath",
                                            "referencedDeclaration": 21,
                                            "src": "327:9:0"
                                        },
                                        "nodeType": "ModifierInvocation",
                                        "src": "327:9:0"
                                    }
                                ],
                                "name": "changeOwner",
                                "nameLocation": "289:11:0",
                                "nodeType": "FunctionDefinition",
                                "parameters": {
                                    "id": 24,
                                    "nodeType": "ParameterList",
                                    "parameters": [
                                        {
                                            "constant": false,
                                            "id": 23,
                                            "mutability": "mutable",
                                            "name": "_newOwner",
                                            "nameLocation": "309:9:0",
                                            "nodeType": "VariableDeclaration",
                                            "scope": 33,
                                            "src": "301:17:0",
                                            "stateVariable": false,
                                            "storageLocation": "default",
                                            "typeDescriptions": {
                                                "typeIdentifier": "t_address",
                                                "typeString": "address"
                                            },
                                            "typeName": {
                                                "id": 22,
                                                "name": "address",
                                                "nodeType": "ElementaryTypeName",
                                                "src": "301:7:0",
                                                "stateMutability": "nonpayable",
                                                "typeDescriptions": {
                                                    "typeIdentifier": "t_address",
                                                    "typeString": "address"
                                                }
                                            },
                                            "visibility": "internal"
                                        }
                                    ],
                                    "src": "300:19:0"
                                },
                                "returnParameters": {
                                    "id": 27,
                                    "nodeType": "ParameterList",
                                    "parameters": [],
                                    "src": "337:0:0"
                                },
                                "scope": 34,
                                "src": "280:249:0",
                                "stateMutability": "nonpayable",
                                "virtual": false,
                                "visibility": "public"
                            }
                        ],
                        "scope": 35,
                        "src": "24:507:0",
                        "usedErrors": [],
                        "usedEvents": []
                    }
                ],
                "src": "0:532:0"
            },
            "id": 0
        }
    },
    "version": "0.8.20+commit.a1b79de6.Darwin.appleclang"
}"""
    return json.loads(ast_json)


def test_modifier_without_proper_enforcement(vulnerable_ast):
    ast_json, src_file_list = reduce_json(vulnerable_ast)
    results = process_yaml(
        "eburger/templates/modifier_without_proper_enforcement.yaml",
        ast_json,
        src_file_list,
    )
    assert "Line 8 Columns 5-27" in results["results"][0]["lines"]
