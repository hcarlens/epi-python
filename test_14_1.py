from solution_14_1 import satisfies_BST_property
from utils import BinaryTreeNode

def test_true_simple():
    test_tree = BinaryTreeNode(data=2, left=BinaryTreeNode(data=1), right=BinaryTreeNode(3))
    assert satisfies_BST_property(test_tree)

def test_false_simple():
    test_tree = BinaryTreeNode(data=5, left=BinaryTreeNode(data=1), right=BinaryTreeNode(3))
    assert not satisfies_BST_property(test_tree)

def test_true_nested():
    test_tree = BinaryTreeNode(data=5, left=BinaryTreeNode(data=3, left=BinaryTreeNode(data=2), right=BinaryTreeNode(data=4)), right=BinaryTreeNode(7))
    assert satisfies_BST_property(test_tree)
    
def test_false_nested():
    test_tree = BinaryTreeNode(data=5, left=BinaryTreeNode(data=3, left=BinaryTreeNode(data=8), right=BinaryTreeNode(data=4)), right=BinaryTreeNode(7))
    assert not satisfies_BST_property(test_tree)