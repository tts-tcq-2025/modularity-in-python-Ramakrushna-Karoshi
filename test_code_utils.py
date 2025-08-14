from color_utils import get_all_pairs, add_major_color, add_minor_color
from color_code import ColorCode

def test_get_all_pairs_count():
    assert len(get_all_pairs()) == ColorCode.total_pairs(), "Pair count mismatch"

def test_add_major_color():
    initial = ColorCode.total_pairs()
    add_major_color('Orange')
    assert 'Orange' in ColorCode.MAJOR_COLORS
    assert ColorCode.total_pairs() == initial + len(ColorCode.MINOR_COLORS)

def test_add_minor_color():
    initial = ColorCode.total_pairs()
    add_minor_color('Pink')
    assert 'Pink' in ColorCode.MINOR_COLORS
    assert ColorCode.total_pairs() == initial + len(ColorCode.MAJOR_COLORS)

def run_utils_tests():
    test_get_all_pairs_count()
    test_add_major_color()
    test_add_minor_color()
    print('Utility tests passed! ✅')

if __name__ == '__main__':
    run_utils_tests()
