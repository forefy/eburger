// SPDX-License-Identifier: MIT
pragma solidity 0.8.20;

contract UngoodContract {
    function transferEther(address payable recipient, uint256 amount) public {
        // Vulnerable: using .transfer() for sending Ether
        recipient.transfer(amount);
    }

    function sendEther(address payable recipient, uint256 amount) public {
        // Vulnerable: using .send() for sending Ether
        bool sent = recipient.send(amount);
        require(sent, "Failed to send Ether");
    }
}