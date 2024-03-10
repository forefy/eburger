// SPDX-License-Identifier: MIT
pragma solidity 0.8.20;
contract BuggieContract {
    address public owner;
    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        // Incorrect: Just checks the condition but doesn't enforce it
        owner == msg.sender;
        _;
    }

    function changeOwner(address _newOwner) public onlyOwner {
        // This function is intended to be restricted to the current owner
        // However, due to the flawed modifier, any address can call this function
        owner = _newOwner;
    }
}
