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
            stdout=None,
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
