""" Test if a binary tree is height-balanced """

def is_balanced(binary_tree):
    """
    Returns (is_balanced, height) so we can
    use this function recursively. 
    Height is only defined if is_balanced == True
    """
    if not binary_tree:
        return True, -1

    # recursive postorder traversal
    left_is_balanced, left_height = is_balanced(binary_tree.left)
    
    if not left_is_balanced:
        return False, None
    
    right_is_balanced, right_height = is_balanced(binary_tree.right)
    
    if not right_is_balanced:
        return False, None
    
    if abs(right_height - left_height) > 1:
        return False, None

    return True, max(left_height, right_height) + 1
