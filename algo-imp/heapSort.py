import timeit
import random

from heap import Heap
from quickSort import quickSort
from mergeSort import mergeSort


def heapSort(arr):
    heap = Heap(arr)                    # Heapify the input array
    result = []                         # Initialise array to store sorted array

    while heap.size():                  # Until heap is empty
        result.append(heap.pop())       # Pop-out the smallest element and insert in the result

    return result                       # Return the sorted array


# x = [random.randint(1, 100000) for _ in range(10000)]
# print(x)
# print(heapSort(x))

# n_turns = 1000
# print(f"Heap-Sort: {timeit.timeit('heapSort(x)', number=n_turns, globals=globals()) / n_turns: .2g} s")     # ~0.0083s
# print(f"Quick-Sort: {timeit.timeit('quickSort(x, 0, len(x)-1)', number=n_turns, globals=globals()) / n_turns: .2g} s")    # ~0.044s
# print(f"Merge-Sort: {timeit.timeit('mergeSort(x)', number=n_turns, globals=globals()) / n_turns: .2g} s")    # ~0.0012s
