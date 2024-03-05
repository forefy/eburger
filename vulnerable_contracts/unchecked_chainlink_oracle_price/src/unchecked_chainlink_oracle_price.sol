// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

// Import the Chainlink AggregatorV3Interface
import "chainlink-brownie-contracts/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract LatestBadContract {
    AggregatorV3Interface internal priceFeed;
    int256 public minAnswer;

    /**
     * Constructor takes the address of a Chainlink Data Feed contract.
     */
    constructor(address _priceFeed, int256 _minAnswer) {
        priceFeed = AggregatorV3Interface(_priceFeed);
        minAnswer = _minAnswer; // Set the minimum acceptable answer
    }

    /**
     * Returns the latest round data from the Chainlink Data Feed.
     */
    function getLatestRoundData()
        public
        view
        returns (
            uint80 roundId,
            int256 answer,
            uint256 startedAt,
            uint256 updatedAt,
            uint80 answeredInRound
        )
    {
        (
            uint80 id,
            int256 price,
            uint256 started,
            uint256 updated,
            uint80 answeredRound
        ) = priceFeed.latestRoundData();

        // No check here! fix suggestion examples:
        // require(price >= minAnswer, "Price below minimum accepted value");
        // or
        // if (price < minAnswer) {
        //     revert("Error: Price below minimum expected value");
        // }

        return (id, price, started, updated, answeredRound);
    }
}
