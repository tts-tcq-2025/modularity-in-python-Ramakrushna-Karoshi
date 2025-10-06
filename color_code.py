from typing import Tuple
from color_validate import ColorValidation


class ColorCode(ColorValidation):
    @classmethod
    def color_pair_to_string(cls, major: str, minor: str) -> str:
        cls.validate(major, minor)
        return f"{major} {minor}"

    @classmethod
    def get_color_from_pair_number(cls, pair_number: int) -> Tuple[str, str]:
        total = cls.total_pairs()
        if not 1 <= pair_number <= total:
            raise ValueError(f"Pair number must be between 1 and {total}.")
        zero_based = pair_number - 1
        major_index = zero_based // len(cls.MINOR_COLORS)
        minor_index = zero_based % len(cls.MINOR_COLORS)
        return cls.MAJOR_COLORS[major_index], cls.MINOR_COLORS[minor_index]

    @classmethod
    def get_pair_number_from_color(cls, major: str, minor: str) -> int:
        cls.validate(major, minor)
        return cls.MAJOR_COLORS.index(major) * len(cls.MINOR_COLORS) + \
               cls.MINOR_COLORS.index(minor) + 1

    @classmethod
    def total_pairs(cls) -> int:
        return len(cls.MAJOR_COLORS) * len(cls.MINOR_COLORS)
