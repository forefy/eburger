import json


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
        case "insights":
            # json_printable = json.dumps(message, indent=4)
            # print(json_printable)
            for item in message:
                try:
                    item.get("results")[0]["file"]
                except Exception:
                    log("warning", f"Bad results for {item.get('name')}, skipping.")
                    continue
                first_result = item.get("results")[0]
                location = first_result.get("file")
                lines = first_result.get("lines")
                lines = lines.replace("Line ", "::").replace(" Columns ", "::")
                location += lines
                name = item.get("name")
                severity = item.get("severity")
                match severity:
                    case "High":
                        severity = f"[{color.Error} ❗️High {color.Default}]"
                    case "Medium":
                        severity = f"[{color.Warning} ❗️Medium {color.Default}]"
                    case "Low":
                        severity = f"[{color.Info} ❗️Low {color.Default}]"

                print(f"{severity} {name} at {location}")
