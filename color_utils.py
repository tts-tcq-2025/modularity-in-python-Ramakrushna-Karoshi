from typing import List, Tuple
from color_code import ColorCode


def get_all_pairs() -> List[Tuple[int, str, str]]:
    return [(i, *ColorCode.get_color_from_pair_number(i))
            for i in range(1, ColorCode.total_pairs() + 1)]


def add_major_color(color: str) -> None:
    if color not in ColorCode.MAJOR_COLORS:
        ColorCode.MAJOR_COLORS.append(color)


def add_minor_color(color: str) -> None:
    if color not in ColorCode.MINOR_COLORS:
        ColorCode.MINOR_COLORS.append(color)
