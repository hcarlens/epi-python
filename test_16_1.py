from solution_16_1 import count_number_of_combinations


def test_number_of_combinations_score_12():
    n = count_number_of_combinations(12)
    assert n == 4


def test_number_of_combinations_score_2():
    n = count_number_of_combinations(2)
    assert n == 1


def test_number_of_combinations_score_3():
    n = count_number_of_combinations(3)
    assert n == 1


def test_number_of_combinations_score_7():
    n = count_number_of_combinations(7)
    assert n == 2  # 7 or 2 + 2 + 3



def test_number_of_combinations_score_9():
    n = count_number_of_combinations(9)
    assert n == 3