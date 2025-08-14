from color_code import ColorCode
from color_utils import get_all_pairs
from color_format import format_pair, format_manual_header, format_manual_footer
from test_color_code import run_all_tests
from test_color_utils import run_utils_tests

def print_color_code_manual() -> None:
    print(format_manual_header())
    for pair_number, major, minor in get_all_pairs():
        print(format_pair(pair_number, major, minor))
    print(format_manual_footer())

if __name__ == '__main__':
    run_all_tests()
    run_utils_tests()
    print_color_code_manual()
    print('Program execution complete. ✨')
