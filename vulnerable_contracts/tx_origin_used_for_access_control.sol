// SPDX-License-Identifier: MIT
pragma solidity 0.8.20;
contract BadContract {
    address payable owner;

    constructor() public {
        owner = payable(msg.sender);
    }

    function sendTo(address payable receiver, uint amount) public {
        require(tx.origin == owner, "Caller is not the owner");
        receiver.transfer(amount);
    }
}