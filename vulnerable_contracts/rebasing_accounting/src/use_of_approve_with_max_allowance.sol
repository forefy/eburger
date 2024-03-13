// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

contract VulnerableApproval {
    // Function to approve an infinite allowance to a given spender
    function approveInfinite(address token, address spender) external {
        IERC20(token).approve(spender, type(uint256).max);
    }


    function transferWithApproval(address token, address from, address to, uint256 amount) external {
        IERC20 tokenContract = IERC20(token);
        require(tokenContract.transferFrom(from, to, amount), "Transfer failed");
    }
}
