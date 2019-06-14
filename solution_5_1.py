""" The Dutch national flag problem """


def naive_dnf_partition(A, i):
    """
    Like the pivot step of a quicksort,
    but with 3 partitions instead of 2.
    This solution requires O(n) extra memory. 
    """

    lower_elements = []
    higher_elements = []
    equal_elements = []

    for element in A:
        if element > A[i]:
            higher_elements.append(element)
        elif element < A[i]:
            lower_elements.append(element)
        else:
            equal_elements.append(element)

    partitioned_list = lower_elements + equal_elements + higher_elements

    return partitioned_list


def dnf_partition(A, i):
    """
    Slightly more intelligent solution, which partitions in-place. 
    O(1) extra memory required.
    Keeps a list of smaller elements starting from index 0, 
        larger elements starting from the end of the list, 
        and a list of elements equal to the pivot somewhere in the middle,
        possibly padded by unclassified elements on either side. 
    """

    num_equal_elements = 1
    start_equal_index = i
    end_lower_index = 0
    start_higher_index = len(A)

    def shift_equals_right():
        """
        swap the first element equal to A[i] with the first
        element that succeeds the equals partition
        """

        A[start_equal_index], A[start_equal_index + num_equal_elements] = \
            A[start_equal_index + num_equal_elements], A[start_equal_index]

    while start_higher_index - end_lower_index > num_equal_elements:

        # make some space between the partitions if we need to
        if start_equal_index == end_lower_index:
            shift_equals_right()
            start_equal_index += 1

        if A[end_lower_index] < A[start_equal_index]:
            end_lower_index += 1

        elif A[end_lower_index] > A[start_equal_index]:
            A[end_lower_index], A[start_higher_index -
                                  1] = A[start_higher_index -
                                         1], A[end_lower_index]
            start_higher_index -= 1

        else:
            if start_equal_index + num_equal_elements == start_higher_index:
                # insert on the left of the equals partition
                A[end_lower_index], A[start_equal_index - 1] = \
                    A[start_equal_index -1 ], A[end_lower_index]
                num_equal_elements += 1
                start_equal_index -= 1

            else:
                # insert on the right of the equals partition
                A[end_lower_index], A[start_equal_index + num_equal_elements] = \
                    A[start_equal_index + num_equal_elements], A[end_lower_index]
                num_equal_elements += 1

    return A