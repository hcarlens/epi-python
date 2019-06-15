""" The Towers of Hanoi """

def transfer_tower(n_rings, from_peg=0, to_peg=1, intermediate_peg=2):
    """
    Transfer a tower of n rings from one peg to another, 
    using a third peg as intermediate. 
    """

    result = []

    if n_rings == 1:
        result.append((from_peg, to_peg))
    else:
        result += transfer_tower(n_rings - 1, from_peg, intermediate_peg, to_peg)
        result.append((from_peg, to_peg))
        result += transfer_tower(n_rings - 1, intermediate_peg, to_peg, from_peg)
    
    return result