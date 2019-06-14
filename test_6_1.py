from solution_6_1 import string_to_int, int_to_string

def test_string_to_int():
    assert string_to_int("1") == 1
    assert string_to_int("135462") == 135462
    assert string_to_int("0") == 0
    assert string_to_int("-1") == -1
    assert string_to_int("-20") == -20
    assert string_to_int("-0") == 0
    assert string_to_int("--30") == 30


def test_int_to_string():
    assert int_to_string(1) == "1"
    assert int_to_string(135462) == "135462"
    assert int_to_string(0) == "0"
    assert int_to_string(-1) == "-1"
    assert int_to_string(-20) == "-20"