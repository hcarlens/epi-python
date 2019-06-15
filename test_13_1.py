from solution_13_1 import intersect_two_sorted_arrays_binary_search, \
    intersect_two_sorted_arrays_equal_length, \
    intersect_two_sorted_arrays_standard_library


def test_standard_library_solution():
    A = [2, 3, 3, 5, 5, 6, 7, 7, 8, 12]
    B = [5, 5, 6, 8, 8, 9, 10, 10]

    computed_intersection = intersect_two_sorted_arrays_standard_library(A, B)

    assert computed_intersection == [5, 6, 8]


def test_binary_search_solution():
    A = [2, 3, 3, 5, 5, 6, 7, 7, 8, 12]
    B = [5, 5, 6, 8, 8, 9, 10, 10]

    computed_intersection = intersect_two_sorted_arrays_binary_search(A, B)

    assert computed_intersection == [5, 6, 8]


def test_equal_length_solution():
    A = [2, 3, 3, 5, 5, 6, 7, 7, 8, 12]
    B = [5, 5, 6, 8, 8, 9, 10, 10]

    computed_intersection = intersect_two_sorted_arrays_equal_length(A, B)

    assert computed_intersection == [5, 6, 8]