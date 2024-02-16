# Template Based Smart Contracts Static Analyzer

<p align="center">
<img src="https://github.com/forefy/eburger/raw/main/static/eburger.png" alt="eBurger" title="eBurger" width="450"/>
</p>

<p align="center">
<a href="https://github.com/forefy/eburger/releases/"><img alt="eBurger releases" src="https://img.shields.io/github/release/forefy/eburger">
<img alt="eBurger GitHub repo size" title="eBurger GitHub repo size" src="https://img.shields.io/github/repo-size/forefy/eburger">
<img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/forefy/eburger/.github/workflows/pip-audit.yml">
<img alt="eBurger GitHub commit activity" src="https://img.shields.io/github/commit-activity/m/forefy/eburger">
<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/forefy/eburger">
<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dw/eburger">
<a href="https://github.com/forefy/eburger/issues"><img alt="Issues" src="https://img.shields.io/github/issues-raw/forefy/eburger">
<a href="https://discord.gg/WaVMpBtxdB"><img alt="Forefy Discord" src="https://img.shields.io/discord/1174395390494257152.svg?logo=discord"></a>
<a href="https://twitter.com/forefy"><img alt="Forefy Twitter" src="https://img.shields.io/twitter/follow/forefy.svg?logo=twitter"></a>
</p>

<p align="center">
<a href="https://discord.gg/WaVMpBtxdB" title="eBurger Discord">Discord</a>
| <a href="https://github.com/forefy/eburger/discussions" title="eBurger Discussions">Discussions</a>
| <a href="https://github.com/forefy/eburger/issues/new?assignees=forefy&labels=&projects=&template=feature_request.md&title=" title="eBurger Feature request">Feature request</a>
| <a href="https://github.com/forefy/eburger/wiki" title="eBurger Wiki">Wiki</a>
| <a href="https://twitter.com/messages/compose?recipient_id=1469398978185809922" title="Forefy Twitter DM">Twitter DM</a>
</p>

## What is eBurger
eBurger is a static analysis tool that provides a way to quickly query and analyze solidity smart contracts.

Running static analyzers won't win you competitions. 
What we provide instead with eBurger is the ability to spin up custom templates tailored to your current audited project in minutes ([Wiki](https://github.com/forefy/eburger/wiki)) allowing you to orchestrate unique lookups through the codebase to empower your audits.

- [How to install](#how-to-install)
- [How to run](#how-to-run)
    - [How to run - simple](#simple-examples)
    - [How to run - advanced](#advanced-usage)
- [How it looks like 👀](#how-it-looks-like)
- [SARIF support](#sarif-support)
- [GitHub Action](#github-action)
- [Contributing templates](#contributing-templates)
- [Comparison table](#comparison-table)
- [Features](#features)
- [What is missing](#what-is-missing)


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
Simplest
```bash
cd MyProject/
eburger
cat eburger-output.json
```

<br>

SARIF output
```bash
eburger -f MyProject/ -o sarif
```

<br>

Markdown output (running from the project's directory)
```bash
eburger -o markdown
```

<br>

Focused scan of a single file and its dependencies
```bash
eburger -f ../ProjectToScan/src/SomeContract.sol
```

<br>

Only print nsloc count
```bash
eburger -f MyProject/ --nsloc
```

<br>

Run custom YAML templates
```bash
eburger -t MyCustomYAMLs/ -f MyProject/
```

### Advanced usage
Refer to the [Wiki](https://github.com/forefy/eburger/wiki/Advanced-usage).


## How it looks like

Here's a demo video

https://github.com/forefy/eburger/assets/152717707/65bf6a6d-adbc-4664-84d4-73ac641a8307

Besides `eburger-output.json`, above example will also generate extended info under the folder `.eburger`.


## SARIF support
SARIF (Static Analysis Results Interchange Format) is a standard format for static analysis tool results.

To have an interactive GUI open up in VSCode that can organinze and interact with the results found, follow these steps:
- Install Microsoft's [SARIF Viewer VSCode extenstion](marketplace.visualstudio.com/items?itemname=ms-sarifvscode.sarif-viewer)
- Run `eburger --output sarif`
- From within VSCode, click the resulted `eburger-output.sarif` file placed in the working directory

This will open an interactive vscode menu with the issues, description, navigation of vulnerable code lines, etc.
![eburger SARIF view](https://github.com/forefy/eburger/raw/main/static/SARIF.png "eburger SARIF view")


## GitHub Action
CI pipelines are supported via the [eburger-action](https://github.com/forefy/eburger-action) GitHub Action, it helps continuously assessing your code and viewing the raised insights on your repo's security pane.

![eburger-action](https://github.com/forefy/eburger/raw/main/static/eburger-action1.png "eburger-action security view")

![eburger-action](https://github.com/forefy/eburger/raw/main/static/eburger-action2.png "eburger-action issue view")

Visit the action's page for more information.



## Contributing templates
Templates can be added by creating new YAML files and either load them with `eburger -t mytemplate.yaml .` or by placing them under the `templates/` directory.

If you are using eburger as a python package (installed via pip install), the templates location can be found with running `pip3 show eburger` or by running the tool on a contract and seeing the templates path printed to the console.

For template writing and documentation refer to the [Wiki](https://github.com/forefy/eburger/wiki/Templates).


## Comparison table
Comparison of actively maintained / popular solidity smart contract static analyzers

| Static Analyzer                                        | Language        | 2 Minutes to write a custom template with ChatGPT     | GitHub Action | Many findings that are already found before the contest began | Would want to eat |
|--------------------------------------------------------|-----------------|-------------------------------------------------------|---------------|---------------------------------------------------------------|-------------------|
| [eBurger](https://github.com/forefy/eburger)           | Python          | ✅                                                    | ✅            |                                                               | ✅                |
| [Slither](https://github.com/crytic/slither)           | Python          |                                                       | ✅            | ✅                                                            |                   |
| [4naly3er](https://github.com/Picodes/4naly3er)        | TypeScript 🤮   |                                                       |               | ✅                                                            |                   |
| [mythril](https://github.com/Consensys/mythril)        | Python          |                                                       |               |                                                               |                   |
| [aderyn](https://github.com/Cyfrin/aderyn)             | Rust            |                                                       |               |                                                               |                   |


Forgot one or made a mistake? open a pull request or an issue :)

## Features
- YAML template support to query contract structure and raise insights for any matches
- Fast learning curve for creating templates, ability to customize templates to the current ongoing audit project
- Foundry and Hardhat support ❣️
- SARIF support & VSCode GUI integration
- GitHub Actions integration through [eburger-action](https://github.com/forefy/eburger-action)
- Markdown report
- Community and free support via [Discord](https://discord.gg/WaVMpBtxdB)


## What is missing
What features would you like to see? [let us know](https://github.com/forefy/eburger/issues/new?assignees=forefy&labels=&projects=&template=feature_request.md&title=)!