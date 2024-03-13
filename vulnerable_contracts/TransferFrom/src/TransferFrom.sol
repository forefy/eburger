// SPDX-License-Identifier: MIT
pragma solidity 0.8.20;

import "../lib/openzeppelin-contracts/contracts/token/ERC20/IERC20.sol";
import "../lib/openzeppelin-contracts/contracts/token/ERC20/utils/SafeERC20.sol";

contract SecureTokenTransfer {
    using SafeERC20 for IERC20;

    IERC20 private _token;

    constructor(IERC20 tokenAddress) {
        _token = tokenAddress;
    }

    function insecureTransfer(address sender, address recipient, uint256 value) public {
        _token.transferFrom(sender, recipient, value);
    }

    function insecureSafeTransfer(address sender, address recipient, uint256 value) public {
        _token.safeTransferFrom(sender, recipient, value);
    }

    // Methods below are intended to show secure use cases
    function secureTransferTo(address recipient, uint256 value) public {
        // Always transferring from the function caller ensures control over the from address
        _token.transferFrom(msg.sender, recipient, value);
    }

    function secureSafeTransferTo(address recipient, uint256 value) public {
        // Using SafeERC20 to securely transfer tokens
        _token.safeTransferFrom(msg.sender, recipient, value);
    }

    function secureContractTransfer(address recipient, uint256 value) public {
        // Securely transferring from the contract itself, assuming the contract holds tokens
        _token.safeTransferFrom(address(this), recipient, value);
    }

    // Demonstrates the transfer of tokens from the contract to a recipient
    // Assumes the contract is trusted and holds tokens
    function secureContractToRecipient(address recipient, uint256 value) public {
        _token.safeTransferFrom(address(this), recipient, value);
    }

    // Safely transfers tokens from the caller to the recipient using SafeERC20
    function callerToRecipientSafeTransfer(address recipient, uint256 value) public {
        SafeERC20.safeTransferFrom(_token, msg.sender, recipient, value);
    }

    // ArbitraryTransferFromDetector has a false positive here
    function falsePositive(address to, uint256 am) public {
        address from_msgsender = msg.sender;
        _token.transferFrom(from_msgsender, to, am);
    }

}
