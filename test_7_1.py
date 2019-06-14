from utils import ListNode
from solution_7_1 import merge_lists

def test_merge_odd_even_short_lists():
    A = ListNode(data=0, next_node=ListNode(data=2))
    B = ListNode(data=1, next_node=ListNode(data=3))
    C = merge_lists(A, B)
    assert C.data == 0
    assert C.next.data == 1
    assert C.next.next.data == 2
    assert C.next.next.next.data == 3
    assert C.next.next.next.next == None
