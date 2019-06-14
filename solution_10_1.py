""" Merge sorted files """

from typing import List
import heapq


def merge_sorted_sequences(sequences: List):
    """ Better solution. (from the book)  """

    min_heap = []

    # initialise return list
    merged_sequence = []

    # turn each sequence into a min heap
    sorted_array_iters = [iter(x) for x in sequences]

    for i, it in enumerate(sorted_array_iters):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))
    
    while min_heap:
        smallest_entry, smallest_array_i = heapq.heappop(min_heap)
        smallest_array_iter = sorted_array_iters[smallest_array_i]
        merged_sequence.append(smallest_entry)
        next_element = next(smallest_array_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_array_i))

    return merged_sequence