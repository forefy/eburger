# eBurger - Visualize Solidity Smart Contracts
![eBurger](static/eburger.png?raw=true "eBurger")
eBurger is a way to quickly visualize and interact with solidity smart contracts.

## Prerequisite - The Solidity Compiler
`solc` probably exists in your system, but if not, please refer to the official documentation at https://docs.soliditylang.org/en/v0.8.9/installing-solidity.html

## How to use
- First, locate the folder at the root of all the packages, usually the project's root directory or `node_modules`.
- From that directory, run `solc` to compile the contract to a JSON formatted AST (Abstract Syntax Tree)
    ```
    solc --combined-json abi,ast,bin,bin-runtime,srcmap,srcmap-runtime,userdoc,devdoc,hashes,compact-format ../contracts/SomeContract.sol --allow-paths . > ../eburger/contract_asts/SomeContract.json
    ```
- Compile time errors can be usually solved by following error messages, fixing the code, or changing the `solc` version with `solc-select install x.x.x && solc-select use x.x.x` where x.x.x. is the required solidity version (e.g. `0.8.0`)
- Double check that you can now see the contract JSON AST under `eburger/contract_asts`
- Run `python main.py -f contract_asts/SomeContract.json`

You get two types of results from this:
- A visual Call Flow Graph under `nx.html`
- `ast_roots` variable containes pythonified representation of the AST - Bon Apetit 🍔 !

## How it looks like
Here's an example of the interactive graph
![eBurger](static/network_graph.png?raw=true "eBurger Network Graph")


## Features
- Call Flow Graph inspired by naming conventions of Solidity
- Search specific segments and highlight by parameter, function, contract etc.
- Extensive control on graph layout
- View only the code related to the contract and not all the libraries in the world
- Community and free support via [Discord](discord.gg/WaVMpBtxdB)


## What is it missing?
As you can see, the tool is still in the making - what features would you like to see? let us know!