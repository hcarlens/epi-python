""" Search a sorted array for the first occurrence of k """

import bisect


def find_first_occurrence_naive(array, key):
    """ Naive O(n) solution) """

    for index, value in enumerate(array):
        if value == key:
            return index


def find_first_occurrence_standard_library(array, key):
    """ Standard library solution """

    return bisect.bisect_left(array, key)


def find_first_occurrence(array, key):
    """ Better solution (as per the book) """

    lo = 0
    hi = len(array) -1
    result = -1

    while lo <= hi:
        mid = (lo + hi) // 2
        if array[mid] > key:
            hi = mid - 1
        if array[mid] == key:
            result = mid
            hi = mid - 1
        else:
            lo = mid + 1

    return result