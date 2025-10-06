from typing import ClassVar, List


class ColorValidation:
    MAJOR_COLORS: ClassVar[List[str]] = ['White', 'Red', 'Black', 'Yellow', 'Violet']
    MINOR_COLORS: ClassVar[List[str]] = ["Blue", "Orange", "Green", "Brown", "Slate"]

    @classmethod
    def validate(cls, major: str, minor: str) -> None:
        if major not in cls.MAJOR_COLORS:
            raise ValueError(f"Invalid major color: {major}")
        if minor not in cls.MINOR_COLORS:
            raise ValueError(f"Invalid minor color: {minor}")
