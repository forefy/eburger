# eBurger - Template Based Smart Contracts Static Analysis

<img src="static/eburger.png?raw=true" alt="eBurger" width="600"/>

eBurger is a static analysis tool that provides a way to quickly query and analyze solidity smart contracts.

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
Comparison of actively maintained / popular solidity smart contract static analyzers

| Static Analyzer                                        | Language        | 2 Minutes to write a custom template with ChatGPT    | Many findings that are already found before the contest began | Would want to eat |
|--------------------------------------------------------|-----------------|-------------------------------------------------------|---------------------------------------------------------------|-------------------|
| [eBurger](https://github.com/forefy/eburger)           | Python          | ✅                                                    |                                                               | ✅                |
| [Slither](https://github.com/crytic/slither)           | Python          |                                                       | ✅                                                            |                   |
| [4naly3er](https://github.com/Picodes/4naly3er)        | TypeScript 🤮   |                                                       | ✅                                                            |                   |
| [mythril](https://github.com/Consensys/mythril)        | Python          |                                                       |                                                               |                   |
| [aderyn](https://github.com/Cyfrin/aderyn)             | Rust            |                                                       |                                                               |                   |


Forgot one or made a mistake? open a pull request or an issue :)

## How it looks like

Here's a demo video

https://github.com/forefy/eburger/assets/152717707/65bf6a6d-adbc-4664-84d4-73ac641a8307

Besides `eburger-output.json`, above example will also generate extended info under the folder `.eburger`.


## How to install

### From PyPi
```
pip3 install eburger
eburger -h
```

### From source
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
cat eburger-output.json
```
..

A focused scan of one file and it's dependencies:
```
eburger -f ../ProjectToScan/src/SomeContract.sol
```
..


### Advanced usage
Refer to the [Wiki](https://github.com/forefy/eburger/wiki/Advanced-usage).


## Adding templates
Templates can be added by creating new YAML files and either load them with `eburger -t mytemplate.yaml .` or by placing them under the `templates/` directory.

If you are using eburger as a python package (installed via pip install), the templates location can be found with running `pip3 show eburger` or by running the tool on a contract and seeing the templates path printed to the console.

For documentation refer to the [Wiki](https://github.com/forefy/eburger/wiki/Templates).


## Features
- YAML template support to query contract structure and raise insights for any matches
- Fast learning curve for adding templates, ability to customize templates to the current ongoing audit project
- Foundry and Hardhat support ❣️
- View only the code related to the contract and not all the libraries in the world
- Community and free support via [Discord](https://discord.gg/WaVMpBtxdB)


## What is missing
What features would you like to see? let us know!

[Discord](https://discord.gg/WaVMpBtxdB) | [Discussions](https://github.com/forefy/eburger/discussions) | [Feature requests](https://github.com/forefy/eburger/issues/new?assignees=forefy&labels=&projects=&template=feature_request.md&title=) | [Wiki](https://github.com/forefy/eburger/wiki) | [Twitter DM](https://twitter.com/messages/compose?recipient_id=1469398978185809922)