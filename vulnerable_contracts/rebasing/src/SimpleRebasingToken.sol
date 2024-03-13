// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "openzeppelin-contracts/contracts/token/ERC20/ERC20.sol";

contract SimpleRebasingToken is ERC20 {
    constructor() ERC20("SimpleRebasingToken", "SRT") {
        _mint(msg.sender, 1000000 * 10**18);
    }

    function rebase(int256 supplyDelta) external {
        if (supplyDelta < 0) {
            _burn(address(this), uint256(-supplyDelta));
        } else {
            _mint(address(this), uint256(supplyDelta));
        }
    }
}