// SPDX-License-Identifier: MIT
pragma solidity 0.8.20;

import "../lib/openzeppelin-contracts/contracts/token/ERC20/IERC20.sol";
import "../lib/openzeppelin-contracts/contracts/token/ERC20/utils/SafeERC20.sol";

contract InsecureTokenTransfer {
    using SafeERC20 for IERC20;

    IERC20 private _token;

    constructor(IERC20 tokenAddress) {
        _token = tokenAddress;
    }

    function insecureTransfer(address sender, address recipient, uint256 value) public {
        _token.transferFrom(sender, recipient, value);
    }

    // Methods below are intended to show secure use cases
    function secureTransferTo(address recipient, uint256 value) public {
        // transferring from the function caller can give more control over the from address
        _token.transferFrom(msg.sender, recipient, value);
    }

}
