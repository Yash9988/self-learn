import timeit
import numpy as np


def partition(arr: list, low: int, high: int):

    pivot = arr[high]                           # Set last element of array as the pivot
    i = low                                     # Initialise pointer at start (low) of array

    for j in range(low, high):                  # Iterate from low to high
        if arr[j] <= pivot:                     # Check if current element is smaller than pivot
            arr[i], arr[j] = arr[j], arr[i]     # Swap element at current index with element at initial pointer
            i += 1                              # Increment the initial pointer

    arr[i], arr[high] = arr[high], arr[i]       # Finally, swap the pivot with initial pointer index
    return i                                    # Return the pointer as new pivot point


def quickSort(arr: list, low: int, high: int) -> None:
    if low < high:                              # Check if low index is smaller than high
        pivot = partition(arr, low, high)       # Get the pivot point in array

        quickSort(arr, low, pivot - 1)          # Split the array to the left of pivot
        quickSort(arr, pivot + 1, high)         # Split the array to the right of pivot

    return

# x = np.random.randint(100000, size=500).tolist()
# quickSort(x, 0, len(x) - 1)

# n_iters = 1000
# print(f"Quick Sort: {timeit.timeit('quickSort(x, 0, len(x)-1)', number=n_iters, globals=globals()): .2g} seconds") # ~7.9s
# print(f"List Sort(): {timeit.timeit('x.sort()', number=n_iters, globals=globals()): .2g} seconds")      # ~0.0012s
# print(f"Sorted(): {timeit.timeit('sorted(x)', number=n_iters, globals=globals()): .2g} seconds")        # ~0.0018s
