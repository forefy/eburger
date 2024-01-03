class color:
    ResetAll = "\033[0m"

    Bold = "\033[1m"
    Dim = "\033[2m"
    Underlined = "\033[4m"
    Blink = "\033[5m"
    Reverse = "\033[7m"
    Hidden = "\033[8m"

    ResetBold = "\033[21m"
    ResetDim = "\033[22m"
    ResetUnderlined = "\033[24m"
    ResetBlink = "\033[25m"
    ResetReverse = "\033[27m"
    ResetHidden = "\033[28m"

    Default = "\033[39m"
    Success = "\033[38;5;79m"  # #37D2B2
    Error = "\033[38;5;204m"  # #FF5A87
    Warning = "\033[38;5;215m"  # #FFB752
    Info = "\033[38;5;69m"  # #528CFF


def log(type: str, message: str):
    match type:
        case "success":
            print(f"[{color.Success} 🍔 Success {color.Default}] {message}")
        case "error":
            print(f"[{color.Error} Error {color.Default}] {message}")
        case "warning":
            print(f"[{color.Warning} Warning {color.Default}] {message}")
        case "info":
            print(f"[{color.Info} Info {color.Default}] {message}")
