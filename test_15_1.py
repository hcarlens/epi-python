from solution_15_1 import transfer_tower

def test_transfer_1_ring():
    steps = transfer_tower(n_rings=1)
    assert steps == [(0, 1)]


def test_transfer_2_rings():
    steps = transfer_tower(n_rings=2)
    assert steps == [(0, 2), (0, 1), (2, 1)]

def test_transfer_3_rings():
    steps = transfer_tower(n_rings=3)
    assert steps == [(0, 1), (0, 2), (1, 2), (0, 1), (2, 0), (2, 1), (0, 1)]