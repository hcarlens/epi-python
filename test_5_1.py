from solution_5_1 import dnf_partition
import random

def test_simple():
    p = dnf_partition([1], 0)
    assert p == [1]

def test_three_elements_higher():
    p = dnf_partition([2, 3, 1], 1)
    assert p == [2, 1, 3] or p == [1, 2, 3]

def test_three_elements_middle():
    p = dnf_partition([2, 3, 1], 0)
    assert p == [1, 2, 3]

def test_three_elements_lower():
    p = dnf_partition([2, 3, 1], 2)
    assert p == [1, 2, 3] or p == [1, 3, 2]

def test_four_elements_middle():
    p = dnf_partition([2, 3, 2, 1], 0)
    assert p == [1, 2, 2, 3]

def test_large_random_array():
    random.seed(0)

    random_list = [random.randint(1, 10) for i in range(100)]
    print(random_list)

    partition_element_value = random_list[0]
    print(partition_element_value)

    p = dnf_partition(random_list, 0)
    print(p)

    end_lower_partition = 0
    start_higher_partition = len(p)

    for index, item in enumerate(p):
        if item < partition_element_value:
            end_lower_partition = index
        if item > partition_element_value:
            start_higher_partition = min(start_higher_partition, index)

    assert end_lower_partition < start_higher_partition - 1
