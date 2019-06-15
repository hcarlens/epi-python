""" Test if a binary tree satisfies the BST property. """

from collections import namedtuple

def satisfies_BST_property(tree):

    tree_properties = namedtuple('TreeProperties', ['BST', 'min_value', 'max_value'])

    def get_tree_properties(tree):
        
        min_value = tree.data
        max_value = tree.data

        # base case
        if not(tree.left or tree.right):
            return tree_properties(True, tree.data, tree.data)
        if tree.left:
            left_tree_properties = get_tree_properties(tree.left)
            if not left_tree_properties.BST:
                return tree_properties(False, None, None)
            elif tree.data < left_tree_properties.max_value:
                return tree_properties(False, None, None)
            min_value = tree.left.data
        if tree.right:
            right_tree_properties = get_tree_properties(tree.right)
            if not right_tree_properties.BST:
                return tree_properties(False, None, None)
            elif tree.data > right_tree_properties.max_value:
                return tree_properties(False, None, None)
            max_value = tree.right.data
        
        return tree_properties(True, min_value, max_value)

    return get_tree_properties(tree).BST