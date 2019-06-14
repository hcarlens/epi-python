from solution_9_1 import is_balanced
from utils import BinaryTreeNode


def test_is_balanced_yes_simple():

    tree = BinaryTreeNode(left=BinaryTreeNode(), right=BinaryTreeNode())
    assert is_balanced(tree)[0] == True


def test_is_balanced_yes_single_subnode():

    tree = BinaryTreeNode(left=BinaryTreeNode())
    assert is_balanced(tree)[0] == True


def test_is_balanced_no_simple():

    tree = BinaryTreeNode(left=None, right=BinaryTreeNode(left=BinaryTreeNode()))
    assert is_balanced(tree)[0] == False


def test_is_balanced_no_deeper():

    tree = BinaryTreeNode(left=BinaryTreeNode(left=BinaryTreeNode(),
                                              right=BinaryTreeNode(right=BinaryTreeNode())),
                          right=BinaryTreeNode())
    assert is_balanced(tree)[0] == False