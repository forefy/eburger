import os
from eburger import settings
from eburger.main import run_command
from eburger.utils.logger import log


def install_foundry_if_not_found():
    forge_binary_found = False
    try:
        run_command("forge -V")
        forge_binary_found = True
    except FileNotFoundError:
        pass

    if not forge_binary_found:
        log("info", "forge wasn't found on the system, trying to install.")
        run_command(
            "curl -L https://foundry.paradigm.xyz | bash",
            shell=True,
        )
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
    hardhat_found = False
    npm_found = False
    npx_found = False

    try:
        res = run_command("npx hardhat", directory=settings.project_root)
        if res[0].startswith("Error"):
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
            log(
                "error",
                "Can't automatically install hardhat without npm being installed manually first, please install npm and run again.",
            )

        if npm_found:
            try:
                run_command("npm install -g npx")
                res = run_command("npx -v")
                npx_found = True
            except FileNotFoundError:
                log(
                    "error",
                    "Couldn't automatically install hardhat, please install manually and try again.",
                )

            if npx_found:
                try:
                    if os.path.isfile(os.path.join(settings.project_root, "yarn.lock")):
                        run_command(
                            "yarn add --dev hardhat",
                            directory=settings.project_root,
                        )
                    else:
                        run_command(
                            "npm install --save-dev hardhat",
                            directory=settings.project_root,
                        )
                except:
                    log(
                        "error",
                        "Couldn't automatically install hardhat, please install manually and try again.",
                    )


def set_solc_compiler_version(solc_required_version):
    log("info", f"Trying to set solc to version {solc_required_version}")
    solc_use_res = run_command(f"solc-select use {solc_required_version}")
    if not solc_use_res:
        log("error", "Error switching solc version, trying to install")
        run_command(f"solc-select install {solc_required_version}")
        solc_use_res = run_command(f"solc-select use {solc_required_version}")
        if not solc_use_res:
            log("error", "Failed to install required solc version")
    log(
        "info",
        "Successfully set solc version, trying to compile contract.",
    )
