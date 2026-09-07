import re

def parse_duration(text: str) -> int | None:
    match = re.fullmatch(r"(\d+)\s*([smhd])", text.strip().lower())
    if not match:
        return None

    value = int(match.group(1))
    unit = match.group(2)

    multipliers = {"s": 1, "m": 60, "h": 3600, "d": 86400}
    return value * multipliers[unit]
