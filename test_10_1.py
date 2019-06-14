from solution_10_1 import merge_sorted_sequences

def test_merge_two_sequences():
    merged_sequence = merge_sorted_sequences([[1, 4, 7], [2, 5]])
    assert merged_sequence == [1, 2, 4, 5, 7]


def test_merge_three_sequences():
    merged_sequence = merge_sorted_sequences([[1, 4, 7, 30], [2, 5], [10, 50, 100]])
    assert merged_sequence == [1, 2, 4, 5, 7, 10, 30, 50, 100]

    
def test_merge_three_sequences_from_book():
    merged_sequence = merge_sorted_sequences([[3, 5, 7], [0, 6], [0, 6, 28]])
    assert merged_sequence == [0, 0, 3, 5, 6, 6, 7, 28]