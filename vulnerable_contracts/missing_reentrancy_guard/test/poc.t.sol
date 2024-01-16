// SPDX-License-Identifier: MIT
pragma solidity 0.8.20;

import "forge-std/Test.sol";
import "../src/missing_reentrancy_guard.sol";
import "../script/Attacker.sol";

contract ProblematicContractTest is Test {
    ProblematicContract problematic_contract;
    Attacker attacker;

    function setUp() public {
        problematic_contract = new ProblematicContract();

        // Directly send Ether to the contract without calling a function
        vm.deal(address(problematic_contract), 10 ether); // Ensure contract has Ether

        attacker = new Attacker(address(problematic_contract));
        vm.deal(address(attacker), 1 ether); // Fund attacker with 1 Ether
    }

    function testReentrancyAttack() public {
        uint initialBalance = address(problematic_contract).balance;
        attacker.attack{value: 1 ether}();

        uint finalBalance = address(problematic_contract).balance;
        uint attackerBalance = address(attacker).balance;

        // Checks if the attacker was able to steal Ether from the ProblematicContract
        assertLt(finalBalance, initialBalance);
        assertGt(attackerBalance, 1 ether);
    }
}
