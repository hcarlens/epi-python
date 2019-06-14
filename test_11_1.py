from solution_11_1 import find_first_occurrence

def test_array_search():
    array = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    assert find_first_occurrence(array, 108) == 3

def test_array_search_2():
    array = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    assert find_first_occurrence(array, 285) == 6

def test_array_search_identical_elements():
    array = [1, 1, 1, 1, 1, 1, 1]
    assert find_first_occurrence(array, 1) == 0