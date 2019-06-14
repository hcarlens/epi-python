""" Shared components """

class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right