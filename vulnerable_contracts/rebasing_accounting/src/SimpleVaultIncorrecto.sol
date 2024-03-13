// // SPDX-License-Identifier: MIT
// pragma solidity ^0.8.0;

// interface IERC20 {
//     function totalSupply() external view returns (uint256);
//     function balanceOf(address account) external view returns (uint256);
//     function transfer(address recipient, uint256 amount) external returns (bool);
//     function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
// }

// contract SimpleVaultIncorrecto {
//     address public admin;
//     IERC20 public token;
//     mapping(address => uint256) public deposits; // Cantidad de tokens depositados por usuario

//     constructor(address _token) {
//         admin = msg.sender;
//         token = IERC20(_token);
//     }

//     function deposit(uint256 amount) public {
//         deposits[msg.sender] += amount; // Incrementa el registro de depósito sin considerar rebasing
//         token.transferFrom(msg.sender, address(this), amount); // Transfiere tokens al contrato
//     }

//     function withdraw(uint256 amount) public {
//         require(deposits[msg.sender] >= amount, "Insufficient balance"); // Verifica contra el balance registrado
//         deposits[msg.sender] -= amount; // Decrementa el registro sin ajustar por rebasing
//         token.transfer(msg.sender, amount); // Devuelve tokens al usuario
//     }
// }
