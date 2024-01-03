// SPDX-License-Identifier: MIT
pragma solidity 0.8.20;
contract VulnerableContract {
    address payable owner;
    constructor() {
        owner = payable(msg.sender);
    }

    // Function to send Ether using call, without checking return value
    function unsafeSend(address payable receiver, uint amount) public {
        require(msg.sender == owner, "Caller is not the owner");

        // This is an unchecked call as the return value is not verified
        receiver.call{value: amount}("");
    }

    // Function to allow the contract to receive Ether
    receive() external payable {}
}
