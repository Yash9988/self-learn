"""
3264. Final Array State After K Multiplication Operations I [EASY]

You are given an integer array nums, an integer k, and an integer multiplier.

You need to perform k operations on nums. In each operation:

    - Find the minimum value x in nums. If there are multiple occurrences of the minimum value, select the one that
      appears first.
    - Replace the selected minimum value x with x * multiplier.

Return an integer array denoting the final state of nums after performing all k operations.


Example 1:
Input: nums = [2,1,3,5,6], k = 5, multiplier = 2
Output: [8,4,6,5,6]

Explanation:
    Operation	        Result
After operation 1	[2, 2, 3, 5, 6]
After operation 2	[4, 2, 3, 5, 6]
After operation 3	[4, 4, 3, 5, 6]
After operation 4	[4, 4, 6, 5, 6]
After operation 5	[8, 4, 6, 5, 6]


Example 2:
Input: nums = [1,2], k = 3, multiplier = 4
Output: [16,8]

Explanation:
    Operation   	Result
After operation 1	[4, 2]
After operation 2	[4, 8]
After operation 3	[16, 8]


Constraints:

    -> 1 <= nums.length <= 100
    -> 1 <= nums[i] <= 100
    -> 1 <= k <= 10
    -> 1 <= multiplier <= 5


Concepts: Heap
"""
from heapq import heapify, heappush, heappop


# My Solution
def getFinalState(nums: list[int], k: int, multiplier: int) -> list[int]:
    heap = [(n, i) for i, n in enumerate(nums)]                     # List to store custom-tuples: (val, idx)
    heapify(heap)                                                   # Convert the list into a heap

    for _ in range(k):                                              # Iterate through the required range
        n, i = heappop(heap)                                        # Pop the smallest tuple from the heap
        heappush(heap, (n * multiplier, i))                         # Multiply the min-val and push the new tuple back

    while heap:                                                     # While the heap is non-empty
        n, i = heappop(heap)                                        # Pop the smallest tuple from the heap
        nums[i] = n                                                 # Assign value at the respective index in the list

    return nums                                                     # Return the result


# Optimised Solution
def getFinalState_op(nums: list[int], k: int, multiplier: int) -> list[int]:

    for _ in range(k):                                              # Iterate through the required range
        idx = nums.index(min(nums))                                 # Obtain the index of min-val in the list
        nums[idx] *= multiplier                                     # Multiply the element by the provided value

    return nums                                                     # Return the result
