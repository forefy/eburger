import json
import pytest
from eburger.serializer import reduce_json
from eburger.yaml_parser import process_yaml


@pytest.fixture
def vulnerable_ast() -> tuple[dict, list]:
    ast_json = """{
    "contracts": {
        "vulnerable_contracts/emit_after_external_call.sol:MistakenContract": {
            "abi": [
                {
                    "anonymous": false,
                    "inputs": [
                        {
                            "indexed": false,
                            "internalType": "uint256",
                            "name": "amount",
                            "type": "uint256"
                        }
                    ],
                    "name": "Transfer",
                    "type": "event"
                },
                {
                    "inputs": [
                        {
                            "internalType": "address",
                            "name": "_unexpectedInteractorContract",
                            "type": "address"
                        }
                    ],
                    "name": "addOtherContract",
                    "outputs": [],
                    "stateMutability": "nonpayable",
                    "type": "function"
                },
                {
                    "inputs": [],
                    "name": "amountToTransfer",
                    "outputs": [
                        {
                            "internalType": "uint256",
                            "name": "",
                            "type": "uint256"
                        }
                    ],
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "inputs": [],
                    "name": "transferMoneyFromBridge",
                    "outputs": [],
                    "stateMutability": "payable",
                    "type": "function"
                },
                {
                    "inputs": [],
                    "name": "unexpectedInteractorContract",
                    "outputs": [
                        {
                            "internalType": "contract UnexpectedInteractorContract",
                            "name": "",
                            "type": "address"
                        }
                    ],
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "inputs": [
                        {
                            "internalType": "uint256",
                            "name": "newAmount",
                            "type": "uint256"
                        }
                    ],
                    "name": "updateAmountToTransfer",
                    "outputs": [],
                    "stateMutability": "nonpayable",
                    "type": "function"
                }
            ],
            "bin": "608060405234801561000f575f80fd5b506103e58061001d5f395ff3fe608060405260043610610049575f3560e01c80635556b0e91461004d5780635dc8733714610077578063b21ce4251461009f578063d3174c3a146100c9578063e8c42627146100d3575b5f80fd5b348015610058575f80fd5b506100616100fb565b60405161006e91906102a6565b60405180910390f35b348015610082575f80fd5b5061009d600480360381019061009891906102fe565b61011e565b005b3480156100aa575f80fd5b506100b3610160565b6040516100c09190610341565b60405180910390f35b6100d1610166565b005b3480156100de575f80fd5b506100f960048036038101906100f49190610384565b610222565b005b5f8054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b805f806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555050565b60015481565b346001819055505f8054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166303b4aa7f6040518163ffffffff1660e01b81526004015f604051808303815f87803b1580156101d1575f80fd5b505af11580156101e3573d5f803e3d5ffd5b505050507f248dd4076d0a389d795107efafd558ce7f31ae37b441ccb9a599c60868f480d56001546040516102189190610341565b60405180910390a1565b8060018190555050565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f819050919050565b5f61026e6102696102648461022c565b61024b565b61022c565b9050919050565b5f61027f82610254565b9050919050565b5f61029082610275565b9050919050565b6102a081610286565b82525050565b5f6020820190506102b95f830184610297565b92915050565b5f80fd5b5f6102cd8261022c565b9050919050565b6102dd816102c3565b81146102e7575f80fd5b50565b5f813590506102f8816102d4565b92915050565b5f60208284031215610313576103126102bf565b5b5f610320848285016102ea565b91505092915050565b5f819050919050565b61033b81610329565b82525050565b5f6020820190506103545f830184610332565b92915050565b61036381610329565b811461036d575f80fd5b50565b5f8135905061037e8161035a565b92915050565b5f60208284031215610399576103986102bf565b5b5f6103a684828501610370565b9150509291505056fea26469706673582212206cd18900d1f8cfd98ff9d2fb701e61065dfc8a7f2f4d8702187f1dfa7e981a2664736f6c63430008140033",
            "bin-runtime": "608060405260043610610049575f3560e01c80635556b0e91461004d5780635dc8733714610077578063b21ce4251461009f578063d3174c3a146100c9578063e8c42627146100d3575b5f80fd5b348015610058575f80fd5b506100616100fb565b60405161006e91906102a6565b60405180910390f35b348015610082575f80fd5b5061009d600480360381019061009891906102fe565b61011e565b005b3480156100aa575f80fd5b506100b3610160565b6040516100c09190610341565b60405180910390f35b6100d1610166565b005b3480156100de575f80fd5b506100f960048036038101906100f49190610384565b610222565b005b5f8054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b805f806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555050565b60015481565b346001819055505f8054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166303b4aa7f6040518163ffffffff1660e01b81526004015f604051808303815f87803b1580156101d1575f80fd5b505af11580156101e3573d5f803e3d5ffd5b505050507f248dd4076d0a389d795107efafd558ce7f31ae37b441ccb9a599c60868f480d56001546040516102189190610341565b60405180910390a1565b8060018190555050565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f819050919050565b5f61026e6102696102648461022c565b61024b565b61022c565b9050919050565b5f61027f82610254565b9050919050565b5f61029082610275565b9050919050565b6102a081610286565b82525050565b5f6020820190506102b95f830184610297565b92915050565b5f80fd5b5f6102cd8261022c565b9050919050565b6102dd816102c3565b81146102e7575f80fd5b50565b5f813590506102f8816102d4565b92915050565b5f60208284031215610313576103126102bf565b5b5f610320848285016102ea565b91505092915050565b5f819050919050565b61033b81610329565b82525050565b5f6020820190506103545f830184610332565b92915050565b61036381610329565b811461036d575f80fd5b50565b5f8135905061037e8161035a565b92915050565b5f60208284031215610399576103986102bf565b5b5f6103a684828501610370565b9150509291505056fea26469706673582212206cd18900d1f8cfd98ff9d2fb701e61065dfc8a7f2f4d8702187f1dfa7e981a2664736f6c63430008140033",
            "devdoc": {
                "kind": "dev",
                "methods": {},
                "version": 1
            },
            "hashes": {
                "addOtherContract(address)": "5dc87337",
                "amountToTransfer()": "b21ce425",
                "transferMoneyFromBridge()": "d3174c3a",
                "unexpectedInteractorContract()": "5556b0e9",
                "updateAmountToTransfer(uint256)": "e8c42627"
            },
            "srcmap": "57:1946:0:-:0;;;;;;;;;;;;;;;;;;;",
            "srcmap-runtime": "57:1946:0:-:0;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;89:64;;;;;;;;;;;;;:::i;:::-;;;;;;;:::i;:::-;;;;;;;;446:179;;;;;;;;;;;;;;;;;;;;;;;:::i;:::-;;:::i;:::-;;196:31;;;;;;;;;;;;;:::i;:::-;;;;;;;:::i;:::-;;;;;;;;964:1037;;;:::i;:::-;;757:103;;;;;;;;;;;;;;;;;;;;;;;:::i;:::-;;:::i;:::-;;89:64;;;;;;;;;;;;:::o;446:179::-;588:29;528:28;;:90;;;;;;;;;;;;;;;;;;446:179;:::o;196:31::-;;;;:::o;964:1037::-;1043:9;1024:16;:28;;;;1492;;;;;;;;;;:37;;;:39;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;1967:26;1976:16;;1967:26;;;;;;:::i;:::-;;;;;;;;964:1037::o;757:103::-;844:9;825:16;:28;;;;757:103;:::o;7:126:1:-;44:7;84:42;77:5;73:54;62:65;;7:126;;;:::o;139:60::-;167:3;188:5;181:12;;139:60;;;:::o;205:142::-;255:9;288:53;306:34;315:24;333:5;315:24;:::i;:::-;306:34;:::i;:::-;288:53;:::i;:::-;275:66;;205:142;;;:::o;353:126::-;403:9;436:37;467:5;436:37;:::i;:::-;423:50;;353:126;;;:::o;485:161::-;570:9;603:37;634:5;603:37;:::i;:::-;590:50;;485:161;;;:::o;652:201::-;774:72;840:5;774:72;:::i;:::-;769:3;762:85;652:201;;:::o;859:292::-;987:4;1025:2;1014:9;1010:18;1002:26;;1038:106;1141:1;1130:9;1126:17;1117:6;1038:106;:::i;:::-;859:292;;;;:::o;1238:117::-;1347:1;1344;1337:12;1484:96;1521:7;1550:24;1568:5;1550:24;:::i;:::-;1539:35;;1484:96;;;:::o;1586:122::-;1659:24;1677:5;1659:24;:::i;:::-;1652:5;1649:35;1639:63;;1698:1;1695;1688:12;1639:63;1586:122;:::o;1714:139::-;1760:5;1798:6;1785:20;1776:29;;1814:33;1841:5;1814:33;:::i;:::-;1714:139;;;;:::o;1859:329::-;1918:6;1967:2;1955:9;1946:7;1942:23;1938:32;1935:119;;;1973:79;;:::i;:::-;1935:119;2093:1;2118:53;2163:7;2154:6;2143:9;2139:22;2118:53;:::i;:::-;2108:63;;2064:117;1859:329;;;;:::o;2194:77::-;2231:7;2260:5;2249:16;;2194:77;;;:::o;2277:118::-;2364:24;2382:5;2364:24;:::i;:::-;2359:3;2352:37;2277:118;;:::o;2401:222::-;2494:4;2532:2;2521:9;2517:18;2509:26;;2545:71;2613:1;2602:9;2598:17;2589:6;2545:71;:::i;:::-;2401:222;;;;:::o;2629:122::-;2702:24;2720:5;2702:24;:::i;:::-;2695:5;2692:35;2682:63;;2741:1;2738;2731:12;2682:63;2629:122;:::o;2757:139::-;2803:5;2841:6;2828:20;2819:29;;2857:33;2884:5;2857:33;:::i;:::-;2757:139;;;;:::o;2902:329::-;2961:6;3010:2;2998:9;2989:7;2985:23;2981:32;2978:119;;;3016:79;;:::i;:::-;2978:119;3136:1;3161:53;3206:7;3197:6;3186:9;3182:22;3161:53;:::i;:::-;3151:63;;3107:117;2902:329;;;;:::o",
            "userdoc": {
                "kind": "user",
                "methods": {},
                "version": 1
            }
        },
        "vulnerable_contracts/emit_after_external_call.sol:UnexpectedInteractorContract": {
            "abi": [
                {
                    "inputs": [
                        {
                            "internalType": "address",
                            "name": "_mistakenContract",
                            "type": "address"
                        }
                    ],
                    "stateMutability": "nonpayable",
                    "type": "constructor"
                },
                {
                    "inputs": [],
                    "name": "doChores",
                    "outputs": [],
                    "stateMutability": "payable",
                    "type": "function"
                },
                {
                    "inputs": [],
                    "name": "mistakenContract",
                    "outputs": [
                        {
                            "internalType": "contract MistakenContract",
                            "name": "",
                            "type": "address"
                        }
                    ],
                    "stateMutability": "view",
                    "type": "function"
                }
            ],
            "bin": "608060405234801561000f575f80fd5b50604051610330380380610330833981810160405281019061003191906100d4565b805f806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550506100ff565b5f80fd5b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f6100a38261007a565b9050919050565b6100b381610099565b81146100bd575f80fd5b50565b5f815190506100ce816100aa565b92915050565b5f602082840312156100e9576100e8610076565b5b5f6100f6848285016100c0565b91505092915050565b6102248061010c5f395ff3fe608060405260043610610028575f3560e01c806303b4aa7f1461002c57806366af70b814610036575b5f80fd5b610034610060565b005b348015610041575f80fd5b5061004a610107565b60405161005791906101a4565b60405180910390f35b5f8054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1663e8c426277fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff6040518263ffffffff1660e01b81526004016100d891906101d5565b5f604051808303815f87803b1580156100ef575f80fd5b505af1158015610101573d5f803e3d5ffd5b50505050565b5f8054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f819050919050565b5f61016c6101676101628461012a565b610149565b61012a565b9050919050565b5f61017d82610152565b9050919050565b5f61018e82610173565b9050919050565b61019e81610184565b82525050565b5f6020820190506101b75f830184610195565b92915050565b5f819050919050565b6101cf816101bd565b82525050565b5f6020820190506101e85f8301846101c6565b9291505056fea2646970667358221220063337c2df02b611a4b76158c7f83842b3f7456a112700d2878b7e03487ac09664736f6c63430008140033",
            "bin-runtime": "608060405260043610610028575f3560e01c806303b4aa7f1461002c57806366af70b814610036575b5f80fd5b610034610060565b005b348015610041575f80fd5b5061004a610107565b60405161005791906101a4565b60405180910390f35b5f8054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1663e8c426277fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff6040518263ffffffff1660e01b81526004016100d891906101d5565b5f604051808303815f87803b1580156100ef575f80fd5b505af1158015610101573d5f803e3d5ffd5b50505050565b5f8054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f819050919050565b5f61016c6101676101628461012a565b610149565b61012a565b9050919050565b5f61017d82610152565b9050919050565b5f61018e82610173565b9050919050565b61019e81610184565b82525050565b5f6020820190506101b75f830184610195565b92915050565b5f819050919050565b6101cf816101bd565b82525050565b5f6020820190506101e85f8301846101c6565b9291505056fea2646970667358221220063337c2df02b611a4b76158c7f83842b3f7456a112700d2878b7e03487ac09664736f6c63430008140033",
            "devdoc": {
                "kind": "dev",
                "methods": {},
                "version": 1
            },
            "hashes": {
                "doChores()": "03b4aa7f",
                "mistakenContract()": "66af70b8"
            },
            "srcmap": "2076:416:0:-:0;;;2167:110;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:::i;:::-;2252:17;2216:16;;:54;;;;;;;;;;;;;;;;;;2167:110;2076:416;;88:117:1;197:1;194;187:12;334:126;371:7;411:42;404:5;400:54;389:65;;334:126;;;:::o;466:96::-;503:7;532:24;550:5;532:24;:::i;:::-;521:35;;466:96;;;:::o;568:122::-;641:24;659:5;641:24;:::i;:::-;634:5;631:35;621:63;;680:1;677;670:12;621:63;568:122;:::o;696:143::-;753:5;784:6;778:13;769:22;;800:33;827:5;800:33;:::i;:::-;696:143;;;;:::o;845:351::-;915:6;964:2;952:9;943:7;939:23;935:32;932:119;;;970:79;;:::i;:::-;932:119;1090:1;1115:64;1171:7;1162:6;1151:9;1147:22;1115:64;:::i;:::-;1105:74;;1061:128;845:351;;;;:::o;2076:416:0:-;;;;;;;",
            "srcmap-runtime": "2076:416:0:-:0;;;;;;;;;;;;;;;;;;;;;;;;;;2283:207;;;:::i;:::-;;2120:40;;;;;;;;;;;;;:::i;:::-;;;;;;;:::i;:::-;;;;;;;;2283:207;2410:16;;;;;;;;;;:39;;;2450:17;2410:58;;;;;;;;;;;;;;;:::i;:::-;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;2283:207::o;2120:40::-;;;;;;;;;;;;:::o;7:126:1:-;44:7;84:42;77:5;73:54;62:65;;7:126;;;:::o;139:60::-;167:3;188:5;181:12;;139:60;;;:::o;205:142::-;255:9;288:53;306:34;315:24;333:5;315:24;:::i;:::-;306:34;:::i;:::-;288:53;:::i;:::-;275:66;;205:142;;;:::o;353:126::-;403:9;436:37;467:5;436:37;:::i;:::-;423:50;;353:126;;;:::o;485:149::-;558:9;591:37;622:5;591:37;:::i;:::-;578:50;;485:149;;;:::o;640:177::-;750:60;804:5;750:60;:::i;:::-;745:3;738:73;640:177;;:::o;823:268::-;939:4;977:2;966:9;962:18;954:26;;990:94;1081:1;1070:9;1066:17;1057:6;990:94;:::i;:::-;823:268;;;;:::o;1097:77::-;1134:7;1163:5;1152:16;;1097:77;;;:::o;1180:118::-;1267:24;1285:5;1267:24;:::i;:::-;1262:3;1255:37;1180:118;;:::o;1304:222::-;1397:4;1435:2;1424:9;1420:18;1412:26;;1448:71;1516:1;1505:9;1501:17;1492:6;1448:71;:::i;:::-;1304:222;;;;:::o",
            "userdoc": {
                "kind": "user",
                "methods": {},
                "version": 1
            }
        }
    },
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
