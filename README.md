# eBurger - Template Based Smart Contracts Static Analysis
<img src="static/eburger.png?raw=true" alt="eBurger" width="500"/>


eBurger is a way to quickly interact with solidity smart contracts.

Running scanners won't win you competitions, spin up custom templates tailored to specific projects in minutes ( [Wiki](https://github.com/forefy/eburger/wiki) ).

* [Comparison Table](#comparison-table)
* [How to install](#how-to-install)
    * [Prerequisite - The Solidity Compiler](#prerequisite---the-solidity-compiler)
    * [Clone](#Clone)
* [How to run simply](#how-to-run-simply)
* [How to run - advanced](#how-to-run---advanced)
* [Adding templates](#adding-templates)
* [What is missing](what-is-missing)



## Comparison Table
| Active Static Analyzer                                 | Language        | Visualization Graph    | 2 Minutes to write a custom template with Chat GPT    | Many findings that are already found before the contest began | Would want to eat |
|--------------------------------------------------------|-----------------|------------------------|-------------------------------------------------------|---------------------------------------------------------------|-------------------|
| [eBurger](https://github.com/forefy/eburger)           | Python          | ✅                     | ✅                                                    |                                                               | ✅                |
| [Slither](https://github.com/crytic/slither)           | Python          | ✅                     |                                                       | ✅                                                            |                   |
| [4naly3er](https://github.com/Picodes/4naly3er)        | TypeScript 🤮   |                        |                                                       | ✅                                                            |                   |
| [mythril](https://github.com/Consensys/mythril)        | Python          |                        |                                                       | ✅                                                            |                   |

Forgot one? open an issue :)

## How to install
### Prerequisite - The Solidity Compiler
`solc` probably exists in your system, but if not, please refer to the official documentation at https://docs.soliditylang.org/en/v0.8.9/installing-solidity.html

`poetry` - preferred python package manager. You can get it `curl -sSL https://install.python-poetry.org | python3 -`

### Clone
```
git clone https://github.com/forefy/eburger.git
cd eburger
poetry shell
```

## How to run simply
```
python main.py -file ../ProjectToScan/src/SomeContract.sol
```
This will run a focused scan on one file and it's dependencies.


```
python main.py -folder ../ProjectToScan/src/ -r @openzeppelin/=../ProjectToScan/lib/openzeppelin-contracts/
```
In above example we are compiling the solidity folder ProjectToScan, as well as specifying remappings configured in the project.


## How to run - advanced
Refer to the [Wiki](https://github.com/forefy/eburger/wiki/Advanced-usage).

## Adding templates
Templates can be added by adding new YAML files under the `templates/` directory
For documentation refer to the [Wiki](https://github.com/forefy/eburger/wiki/Templates).

## How it looks like
Here's an example of the interactive graph
![eBurger](static/network_graph.png?raw=true "eBurger Network Graph")

## Features
- YAML template support to query contract structure and raise insights for any matches
- Call Flow Graph inspired by naming conventions of Solidity
- Search specific segments and highlight by parameter, function, contract etc.
- Extensive control on graph layout
- View only the code related to the contract and not all the libraries in the world
- Community and free support via [Discord](discord.gg/WaVMpBtxdB)


## What is missing
As you can see, the tool is still in the making - what features would you like to see? let us know!