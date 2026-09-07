import re

def parse_duration(duration_str: str):
    if not duration_str:
        return None
    match = re.match(r"^(\d+)([smhd])$", duration_str.lower().strip())
    if not match:
        return None
    value, unit = int(match.group(1)), match.group(2)
    units = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}
    return value * units[unit]