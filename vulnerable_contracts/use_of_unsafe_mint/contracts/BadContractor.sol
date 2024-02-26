// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
contract BadNFT is ERC721Enumerable {
    constructor() ERC721("BadNFT", "BNFT") {}

    function mint(address to, uint256 tokenId) public {
        _mint(to, tokenId);
    }
}