// SPDX-License-Identifier: MIT
pragma solidity 0.8.20;

contract FaultyContract {
    uint256[] public largeArray;
    uint256 public lastSum;  // State variable to store the last calculated sum

    function addToLargeArray(uint256 element) public {
        largeArray.push(element);
    }

    // Vulnerable function with an unbounded loop.
    function updateSum() public {
        uint256 sum = 0;
        for (uint256 i = 0; i < largeArray.length; i++) {
            sum += largeArray[i]; // reading from a state variable can cost significannt amount of gas
        }
    }
}
