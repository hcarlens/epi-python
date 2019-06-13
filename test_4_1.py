from solution_4_1 import parity

def test_parity_4():
    assert parity(4) == 1

def test_parity_1():
    assert parity(1) == 1

def test_parity_2():
    assert parity(2) == 1

def test_parity_6():
    assert parity(6) == 0

def test_parity_7():
    assert parity(7) == 1

def test_parity_100():
    assert parity(100) == 1