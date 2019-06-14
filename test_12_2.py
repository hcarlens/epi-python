from solution_12_2 import is_constructible

def test_constructible():
    assert is_constructible("abcdef", "abcdef")

def test_not_constructible():
    assert not is_constructible("abcdef", "abc")

def test_constructible_longer():
    assert is_constructible("aaabbbccabc", "abcabcabcabcabcabc")
