// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./SimpleRebasingToken.sol";

contract RebasingTokenSaver {
    SimpleRebasingToken public rebasingToken;

    uint256 public totalShares;
    uint256 public totalDepositedTokens;

    mapping(address => uint256) public depositorShares;

    constructor(address _rebasingTokenAddress) {
        rebasingToken = SimpleRebasingToken(_rebasingTokenAddress);
    }


    function deposit(uint256 amount) external {
        require(rebasingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        /*
            Vulnerable to rebase between this call and the previous line if not atomic
            - Calculating shares to mint based on the amount deposited vs. the current balance
            - Ensures fairness in distribution of shares proportional to the deposit amount at the time of deposit
        */
        uint256 currentBalance = rebasingToken.balanceOf(address(this));
        uint256 sharesToMint = totalShares == 0 ? amount : amount * totalShares / (currentBalance - amount);
        depositorShares[msg.sender] += sharesToMint;
        totalShares += sharesToMint;
        totalDepositedTokens = currentBalance; // Updating the last known total balance with the current balance after deposit

        // EXAMPLEE FIXED VERSION
        // uint256 sharesToMint = (totalShares == 0) ? amount : amount * totalShares / totalDepositedTokens;
        // depositorShares[msg.sender] += sharesToMint;
        // totalShares += sharesToMint;
        // totalDepositedTokens += amount; // Tracks the actual amount of tokens deposited
    }
}


