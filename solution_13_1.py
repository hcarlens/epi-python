""" Compute the intersection of two sorted arrays """

import bisect

def intersect_two_sorted_arrays_binary_search(A, B):
    """
    Iterate through the first array, search the second.
    O(mlogn)
    """

    def is_present(k):
        i = bisect.bisect_left(B, k)
        return i< len(B) and B[i] == k
    
    return [
        a for i, a in enumerate(A)
        if (i == 0 or a != A[i - 1]) and is_present(a)
    ]

def intersect_two_sorted_arrays_equal_length(A, B):
    """
    O(m + n)
    """
    i, j, intersection_A_B = 0, 0, []
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i - 1]:
                intersection_A_B.append(A[i])
            i, j = i + 1, j + 1
        elif A[i] < B[j]:
            i += 1
        else: # A[i] > B[j]
            j += 1
    return intersection_A_B


def intersect_two_sorted_arrays_standard_library(A, B):
    """ Implementation using standard libraries """
    return sorted(list(set(A).intersection(B)))

