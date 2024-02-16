import os
import sys
from eburger import settings
from eburger.utils.helpers import python_shell_source, run_command
from eburger.utils.logger import log
from eburger.utils.cli_args import args


def check_if_skip_installations_requested(missing_dependency: str):
    if args.skip_installations:
        log(
            "info",
            f"Automatic installation of dependencies was disabled, please install {missing_dependency} manually (or try again without the `skip_installations` flag) and run again.",
        )
        sys.exit(0)


def install_foundry_if_not_found():
    check_if_skip_installations_requested(missing_dependency="foundry")

    forge_binary_found = False
    try:
        run_command("forge -V")
        forge_binary_found = True
    except FileNotFoundError:
        pass

    if not forge_binary_found:
        log("info", "forge wasn't found on the system, trying to install.")
        run_command("curl -L https://foundry.paradigm.xyz | bash", shell=True)
        python_shell_source()
        run_command("foundryup")
        try:
            run_command("forge -V")
            log("info", "Successfully installed forge.")
        except:
            log(
                "error",
                "Couldn't automatically install forge, please install manually and try again.",
            )


def install_hardhat_if_not_found():
    check_if_skip_installations_requested(missing_dependency="hardhat")

    hardhat_found = False
    npm_found = False
    npx_found = False

    try:
        res, err = run_command("npx hardhat help", directory=settings.project_root)
        if err:
            raise FileNotFoundError
        hardhat_found = True
    except FileNotFoundError:
        pass
    if not hardhat_found:
        log("info", "Local hardhat not found on project, installing.")
        try:
            run_command("npm -v")
            npm_found = True
        except FileNotFoundError:
            run_command(
                "curl -L https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash",
                shell=True,
            )

            try:
                _, errs = run_command(
                    construct_sourceable_nvm_string("nvm --version"),
                    shell=True,
                    live_output=True,
                )
                if errs:
                    raise Exception
                log("info", "Successfully installed nvm.")
            except Exception as e:
                print(e)
                log(
                    "error",
                    "Couldn't automatically install nvm, please install manually and try again.",
                )

            # nodejs
            try:
                run_command(
                    construct_sourceable_nvm_string("nvm install --lts"),
                    shell=True,
                    live_output=True,
                )
                run_command(
                    construct_sourceable_nvm_string("npm -v"),
                    shell=True,
                    live_output=True,
                )
                npm_found = True
            except FileNotFoundError:
                log(
                    "error",
                    "Couldn't automatically install npm, please install manually and try again.",
                )

        if npm_found:
            try:
                run_command(
                    construct_sourceable_nvm_string("npx -v"),
                    shell=True,
                    live_output=True,
                )
                npx_found = True
            except FileNotFoundError:
                log(
                    "error",
                    "Couldn't automatically install hardhat, please install manually and try again.",
                )

            if not npx_found:
                try:
                    run_command(
                        construct_sourceable_nvm_string("npm install -g npx"),
                        shell=True,
                        live_output=True,
                    )
                    run_command(
                        construct_sourceable_nvm_string("npx -v"),
                        shell=True,
                        live_output=True,
                    )
                except FileNotFoundError:
                    log(
                        "error",
                        "Couldn't automatically install hardhat, please install manually and try again.",
                    )

            try:
                if os.path.isfile(os.path.join(settings.project_root, "yarn.lock")):
                    run_command(
                        construct_sourceable_nvm_string("npm install -g yarn"),
                        shell=True,
                        live_output=True,
                    )
                    run_command(
                        construct_sourceable_nvm_string("yarn add --dev hardhat"),
                        directory=settings.project_root,
                        shell=True,
                        live_output=True,
                    )
                else:
                    run_command(
                        construct_sourceable_nvm_string(
                            "npm install --save-dev hardhat"
                        ),
                        directory=settings.project_root,
                        shell=True,
                        live_output=True,
                    )
            except:
                log(
                    "error",
                    "Couldn't automatically install hardhat, please install manually and try again.",
                )


def set_solc_compiler_version(solc_required_version: str):
    log("info", f"Trying to set solc to version {solc_required_version}")
    solc_use_res, errors = run_command(f"solc-select use {solc_required_version}")
    if not solc_use_res or errors:
        log("info", "Trying to install missing solc version")
        _, errors = run_command(f"solc-select install {solc_required_version}")
        _, errors = run_command(f"solc-select use {solc_required_version}")
        if not solc_use_res or errors:
            log("error", "Failed to install required solc version")
    log(
        "info",
        "Successfully set solc version, trying to compile contract.",
    )


# Used to prepare inputs for run_command for the python subprocess could reach nvm and its installed binaries,
# without the user having to reload the terminal.
def construct_sourceable_nvm_string(nvm_command: str) -> str:
    source_syntax, and_sign = python_shell_source(execute_source=False)
    return f'/bin/bash -c "{source_syntax} ~/.nvm/nvm.sh {and_sign} {nvm_command}"'
