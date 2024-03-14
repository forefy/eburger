// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract ProblematicContract {
    mapping(address => uint) public balances;

    function deposit() public payable {
        require(msg.value > 0, "Deposit amount must be greater than 0");
        balances[msg.sender] += msg.value;
    }

    function withdraw() public {
        uint balance = balances[msg.sender];
        require(balance > 0, "Insufficient funds");
        
        /*
            When a contract uses .call(), execution control is temporarily transferred to msg.sender.
            msg.sender can then execute any code within its fallback/receive function, including interacting with other contracts.
            If msg.sender is a malicious contract, it may call withraw() in this contract (reentrancy)
            Upon getting to the msg.sender.call line again, this chain of events will occur repeatedly until ProblematicContract runs out of funds.
        */
        (bool sent, ) = msg.sender.call{value: balance}("");
        require(sent, "Failed to send Ether");

        // violation of the check-effect-interaction pattern
        balances[msg.sender] = 0;
    }
}