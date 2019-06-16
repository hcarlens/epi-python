""" The 3-sum problem """


def three_sum_naive(A, t):
    """
    Naive approach: O(n^2)
    Calculate all potential two_sums, 
    then check compatibility with individual numbers.
    """

    two_sums = set(m + n for m in A for n in A)

    for m in A:
        if (t - m) in two_sums:
            return True

    return False


def three_sum(A, t):
    """
    Smarter approach.
    Time complexity O(n*n), space complexity O(1)
    """

    A.sort() # O(nlogn)

    return any(two_sum(A, t - a) for a in A)


def two_sum(A, t):
    """ Assume A is sorted. """
    i, j = 0, len(A) - 1

    while i <= j:
        if A[i] + A[j] == t:
            return True
        elif A[i] + A[j] < t:
            i += 1
        else:  # A[i] + A[j] > t.
            j -= 1

    return False
