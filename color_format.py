from color_code import ColorCode

def format_pair(pair_number: int, major: str, minor: str) -> str:
    return f"Pair {pair_number:2}: {ColorCode.color_pair_to_string(major, minor)}"

def format_manual_header() -> str:
    return f"{ColorCode.total_pairs()}-Pair Color Code Manual\n" + "-" * 32

def format_manual_footer() -> str:
    return "-" * 32
