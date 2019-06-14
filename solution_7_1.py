""" Merge two sorted lists """

from utils import ListNode


def merge_lists(A, B):
    """
    Merge two sorted lists into one sorted list.
    """

    C_head = None
    C_tail = None
    C_next = None

    while A or B:
        if B and (A is None or A.data > B.data):
            C_next = B
            B = B.next
        else:
            C_next = A
            A = A.next

        if not C_head:
            C_head = C_next
            C_tail = C_next
        else:
            C_tail.next = C_next
            C_tail = C_tail.next

    return C_head