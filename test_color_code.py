from color_code import ColorCode

def test_number_to_pair(pair_number: int, expected_major: str, expected_minor: str) -> None:
    major, minor = ColorCode.get_color_from_pair_number(pair_number)
    assert major == expected_major, f"Expected {expected_major}, got {major}"
    assert minor == expected_minor, f"Expected {expected_minor}, got {minor}"

def test_pair_to_number(major: str, minor: str, expected_number: int) -> None:
    number = ColorCode.get_pair_number_from_color(major, minor)
    assert number == expected_number, f"Expected {expected_number}, got {number}"

def run_all_tests() -> None:
    test_number_to_pair(4, 'White', 'Brown')
    test_number_to_pair(5, 'White', 'Slate')
    test_pair_to_number('Black', 'Orange', 12)
    test_pair_to_number('Violet', 'Slate', 25)
    test_pair_to_number('Red', 'Orange', 7)
    print('All tests passed! ✅')

if __name__ == '__main__':
    run_all_tests()
