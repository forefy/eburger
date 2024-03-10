// SPDX-License-Identifier: MIT
pragma solidity 0.8.20;

contract WrongContract {
    address public recipient;

    function setRecipient(address _recipient) public {
        // _recipient could be address(0x0), as nothing validates it.
        recipient = _recipient;
    }
}