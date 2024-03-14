// SPDX-License-Identifier: MIT
pragma solidity 0.8.20;

contract BadCode {
    function hashCollision1(string memory input1, string memory input2) public pure returns (bytes32) {
        return keccak256(abi.encodePacked(input1, input2));
    }

    function hashCollision2(bytes memory input1, uint256[] memory input2) public pure returns (bytes32) {
        return keccak256(abi.encodePacked(input1, input2));
    }

    function noHashCollision(string memory input1, string memory input2) public pure returns (bytes32) {
        return keccak256(abi.encode(input1, input2));
    }
}