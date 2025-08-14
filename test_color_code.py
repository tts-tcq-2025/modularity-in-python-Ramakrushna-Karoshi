from color_code import ColorCode

def test_number_to_pair(pair_number: int, expected_major_color: str, expected_minor_color: str) -> None:
    """
    Tests if a pair number correctly translates to the expected colors.
    Raises AssertionError if the test fails.
    """
    major_color, minor_color = ColorCode.get_color_from_pair_number(pair_number)
    assert major_color == expected_major_color, f"Expected major color: {expected_major_color}, Got: {major_color}"
    assert minor_color == expected_minor_color, f"Expected minor color: {expected_minor_color}, Got: {minor_color}"

def test_pair_to_number(major_color: str, minor_color: str, expected_pair_number: int) -> None:
    """
    Tests if a color pair correctly translates to the expected number.
    Raises AssertionError if the test fails.
    """
    pair_number = ColorCode.get_pair_number_from_color(major_color, minor_color)
    assert pair_number == expected_pair_number, f"Expected pair number: {expected_pair_number}, Got: {pair_number}"

def run_all_tests() -> None:
    """
    Runs all test cases for the color code logic.
    Extend this function as new colors or logic are added.
    """
    # Number to pair tests
    test_number_to_pair(4, 'White', 'Brown')
    test_number_to_pair(5, 'White', 'Slate')
    # Pair to number tests
    test_pair_to_number('Black', 'Orange', 12)
    test_pair_to_number('Violet', 'Slate', 25)
    test_pair_to_number('Red', 'Orange', 7)
    # Future-proof: Add more tests here as color lists grow

if __name__ == '__main__':
    run_all_tests()
    print('All tests passed! ✅')
