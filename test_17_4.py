from solution_17_4 import three_sum


def test_three_sum_true():
    assert three_sum([11, 2, 5, 7, 3], 21)


def test_three_sum_false():
    assert not three_sum([11, 2, 5, 7, 3], 22)