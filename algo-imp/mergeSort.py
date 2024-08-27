import timeit
import numpy as np


def mergeSort(arr: list) -> list:
    if (n := len(arr)) <= 1:                                        # Check for single element array
        return arr

    left, right = mergeSort(arr[:n // 2]), mergeSort(arr[n // 2:])  # Split array in (almost) two equal parts

    sorted_ = []                                                    # Create an empty list (can also be done in-place)
    i = j = 0                                                       # Initialise pointers for each half of array

    while i < len(left) and j < len(right):                         # Iterate through each array until one reaches end
        if left[i] <= right[j]:                                     # Compare values between arrays
            sorted_.append(left[i])                                 # Append left value to result if smaller
            i += 1                                                  # Increment left pointer
        else:
            sorted_.append(right[j])                                # Append right value to result if smaller
            j += 1                                                  # Increment right pointer

    if i == len(left):                                              # If left pointer reached end first
        sorted_.extend(right[j:])                                   # Append the remaining right array to result
    else:
        sorted_.extend(left[i:])                                    # Append the remaining left array to result, else

    return sorted_                                                  # Return the sorted (sub)array


# x = np.random.randint(100000, size=10000).tolist()
# print(x)
# print(mergeSort(x))

# n_iters = 100
# print(f"Merge Sort: {timeit.timeit('mergeSort(x)', number=n_iters, globals=globals()): .2g} seconds")   # ~2.8s
# print(f"List Sort(): {timeit.timeit('x.sort()', number=n_iters, globals=globals()): .2g} seconds")      # ~0.006s
# print(f"Sorted(): {timeit.timeit('sorted(x)', number=n_iters, globals=globals()): .2g} seconds")        # ~0.0083s
