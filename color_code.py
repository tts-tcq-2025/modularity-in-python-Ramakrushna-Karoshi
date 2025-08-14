from typing import Tuple, List, ClassVar

class ColorCode:
    MAJOR_COLORS: ClassVar[List[str]] = ['White', 'Red', 'Black', 'Yellow', 'Violet']
    MINOR_COLORS: ClassVar[List[str]] = ["Blue", "Orange", "Green", "Brown", "Slate"]

    @classmethod
    def color_pair_to_string(cls, major_color: str, minor_color: str) -> str:
        cls._validate_color(major_color, minor_color)
        return f'{major_color} {minor_color}'

    @classmethod
    def get_color_from_pair_number(cls, pair_number: int) -> Tuple[str, str]:
        if not 1 <= pair_number <= cls.total_pairs():
            raise ValueError(f"Pair number must be between 1 and {cls.total_pairs()}.")
        zero_based = pair_number - 1
        major_index = zero_based // len(cls.MINOR_COLORS)
        minor_index = zero_based % len(cls.MINOR_COLORS)
        return cls.MAJOR_COLORS[major_index], cls.MINOR_COLORS[minor_index]

    @classmethod
    def get_pair_number_from_color(cls, major_color: str, minor_color: str) -> int:
        cls._validate_color(major_color, minor_color)
        major_index = cls.MAJOR_COLORS.index(major_color)
        minor_index = cls.MINOR_COLORS.index(minor_color)
        return major_index * len(cls.MINOR_COLORS) + minor_index + 1

    @classmethod
    def total_pairs(cls) -> int:
        return len(cls.MAJOR_COLORS) * len(cls.MINOR_COLORS)

    @classmethod
    def _validate_color(cls, major_color: str, minor_color: str) -> None:
        if major_color not in cls.MAJOR_COLORS:
            raise ValueError(f"Invalid major color: {major_color}")
        if minor_color not in cls.MINOR_COLORS:
            raise ValueError(f"Invalid minor color: {minor_color}")
