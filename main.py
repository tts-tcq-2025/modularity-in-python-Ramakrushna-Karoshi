from color_code import ColorCode
from test_color_code import run_all_tests

def print_color_code_manual() -> None:
    """
    Generates and prints a formatted manual of the color code pairs.
    Automatically adapts to any number of pairs.
    """
    print(f"{ColorCode.total_pairs()}-Pair Color Code Manual\n" + "-" * 32)
    for pair_number, major_color, minor_color in ColorCode.get_all_pairs():
        print(f"Pair {pair_number:2}: {ColorCode.color_pair_to_string(major_color, minor_color)}")
    print("-" * 32)

if __name__ == '__main__':
    # Run all tests (future-proof: will always run all defined tests)
    run_all_tests()

    # Generate and print the manual (future-proof: adapts to color list changes)
    print_color_code_manual()
    print('Program execution complete. ✨')
