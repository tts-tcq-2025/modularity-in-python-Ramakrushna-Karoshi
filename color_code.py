from typing import Tuple, List, ClassVar

class ColorCode:
    """
    Encapsulates logic for the 25-pair color code standard.
    Designed for extensibility and future-proofing.
    """

    MAJOR_COLORS: ClassVar[List[str]] = ['White', 'Red', 'Black', 'Yellow', 'Violet']
    MINOR_COLORS: ClassVar[List[str]] = ["Blue", "Orange", "Green", "Brown", "Slate"]

    @classmethod
    def color_pair_to_string(cls, major_color: str, minor_color: str) -> str:
        """
        Returns a formatted string for a color pair.
        """
        cls._validate_color(major_color, minor_color)
        return f'{major_color} {minor_color}'

    @classmethod
    def get_color_from_pair_number(cls, pair_number: int) -> Tuple[str, str]:
        """
        Converts a pair number to its corresponding major and minor colors.
        Raises ValueError if the pair number is out of range.
        """
        if not 1 <= pair_number <= cls.total_pairs():
            raise ValueError(f"Pair number must be between 1 and {cls.total_pairs()}.")
        zero_based_pair_number = pair_number - 1
        major_index = zero_based_pair_number // len(cls.MINOR_COLORS)
        minor_index = zero_based_pair_number % len(cls.MINOR_COLORS)
        return cls.MAJOR_COLORS[major_index], cls.MINOR_COLORS[minor_index]

    @classmethod
    def get_pair_number_from_color(cls, major_color: str, minor_color: str) -> int:
        """
        Converts a major and minor color pair to its corresponding pair number.
        Raises ValueError if colors are invalid.
        """
        cls._validate_color(major_color, minor_color)
        major_index = cls.MAJOR_COLORS.index(major_color)
        minor_index = cls.MINOR_COLORS.index(minor_color)
        return major_index * len(cls.MINOR_COLORS) + minor_index + 1

    @classmethod
    def total_pairs(cls) -> int:
        """
        Returns the total number of color pairs.
        """
        return len(cls.MAJOR_COLORS) * len(cls.MINOR_COLORS)

    @classmethod
    def add_major_color(cls, color: str) -> None:
        """
        Adds a new major color to the color code system.
        """
        if color not in cls.MAJOR_COLORS:
            cls.MAJOR_COLORS.append(color)

    @classmethod
    def add_minor_color(cls, color: str) -> None:
        """
        Adds a new minor color to the color code system.
        """
        if color not in cls.MINOR_COLORS:
            cls.MINOR_COLORS.append(color)

    @classmethod
    def _validate_color(cls, major_color: str, minor_color: str) -> None:
        """
        Validates that the provided colors exist in the color code system.
        Raises ValueError if invalid.
        """
        if major_color not in cls.MAJOR_COLORS:
            raise ValueError(f"Invalid major color provided: {major_color}")
        if minor_color not in cls.MINOR_COLORS:
            raise ValueError(f"Invalid minor color provided: {minor_color}")

    @classmethod
    def get_all_pairs(cls) -> List[Tuple[int, str, str]]:
        """
        Returns a list of all color pairs as (pair_number, major_color, minor_color).
        """
        pairs = []
        for pair_number in range(1, cls.total_pairs() + 1):
            major_color, minor_color = cls.get_color_from_pair_number(pair_number)
            pairs.append((pair_number, major_color, minor_color))
        return pairs
