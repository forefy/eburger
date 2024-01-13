# eBurger - Template Based Smart Contracts Static Analysis

<img src="static/eburger.png?raw=true" alt="eBurger" width="600"/>

eBurger is a way to quickly interact with solidity smart contracts.

Running scanners won't win you competitions. spin up custom templates tailored to specific projects in minutes ([Wiki](https://github.com/forefy/eburger/wiki)).

- [Comparison table](#comparison-table)
- [How it looks like 👀](#how-it-looks-like)
- [How to install](#how-to-install)
- [How to run](#how-to-run)
    - [How to run - simple](#simple-examples)
    - [How to run - advanced](#advanced-usage)
- [Adding templates](#adding-templates)
- [What is missing](#what-is-missing)


## Comparison table
| Active Static Analyzer                                 | Language        | Visualization Graph    | 2 Minutes to write a custom template with ChatGPT    | Many findings that are already found before the contest began | Would want to eat |
|--------------------------------------------------------|-----------------|------------------------|-------------------------------------------------------|---------------------------------------------------------------|-------------------|
| [eBurger](https://github.com/forefy/eburger)           | Python          | ✅                     | ✅                                                    |                                                               | ✅                |
| [Slither](https://github.com/crytic/slither)           | Python          | ✅                     |                                                       | ✅                                                            |                   |
| [4naly3er](https://github.com/Picodes/4naly3er)        | TypeScript 🤮   |                        |                                                       | ✅                                                            |                   |
| [mythril](https://github.com/Consensys/mythril)        | Python          |                        |                                                       | ✅                                                            |                   |

Forgot one? open an issue :)

## How it looks like

Here's a demo video

https://github.com/forefy/eburger/assets/152717707/68f8a41c-1dfd-42d2-82ab-38c7a167e030

Above example will also generate an AST, pythonified AST and a visual call flow graph under the folder `.eburger`.

Here's an example of an interactive graph
![eBurger](static/network_graph.png?raw=true "eBurger Network Graph")

## How to install
These 4 commands will make `eburger` available globally:
```
git clone https://github.com/forefy/eburger.git
cd eburger
pip3 install .
eburger -h
```

## How to run

### Simple examples
Simplest:
```bash
cd MyProject/
eburger
cat eburger-results.json
```
..

This will run a focused scan on one file and it's dependencies:
```
eburger -f ../ProjectToScan/src/SomeContract.sol
```
..


### Advanced usage
Refer to the [Wiki](https://github.com/forefy/eburger/wiki/Advanced-usage).


## Adding templates
Templates can be added by adding new YAML files under the `templates/` directory.

If you are using eburger as a python package (installed with pip install), the templates location can be found with running `pip3 show eburger` or by running the tool on a contract and seeing the templates path printed to the console.

For documentation refer to the [Wiki](https://github.com/forefy/eburger/wiki/Templates).


## Features
- YAML template support to query contract structure and raise insights for any matches
- Fast learning curve for adding templates, ability to customize templates to the current ongoing audit project
- Foundry and Hardhat support ❣️
- Call Flow Graph inspired by naming conventions of Solidity
- Search specific segments and highlight by parameter, function, contract etc
- Extensive control on graph layout
- View only the code related to the contract and not all the libraries in the world
- Community and free support via [Discord](discord.gg/WaVMpBtxdB)


## What is missing
As you can see, the tool is still in the making - what features would you like to see? let us know!
