"""
632. Smallest Range Covering Elements from K Lists [HARD]

You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number
from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.


Example 1:

Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]

Explanation:
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].


Example 2:

Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]


Constraints:

    -> nums.length == k
    -> 1 <= k <= 3500
    -> 1 <= nums[i].length <= 50
    -> -10^5 <= nums[i][j] <= 10^5
    -> nums[i] is sorted in non-decreasing order.


Concepts: Heap
"""
from heapq import *


def smallestRange(nums: list[list[int]]) -> list[int]:
    pq = [(row[0], i, 0) for i, row in enumerate(nums)]     # Initialise a list of min-elements from all 'k' lists
    heapify(pq)                                             # Convert the list into a heap

    ans = -1e9, 1e9                                         # Initialise the largest range
    right = max(row[0] for row in nums)                     # Obtain the max of all min-elements in the 'k' lists

    while pq:                                               # While the heap is not empty
        left, i, j = heappop(pq)                            # Obtain the smallest element from the heap
        if right - left < ans[1] - ans[0]:                  # Check if the range w/ curr-ele is smaller than previous
            ans = left, right                               # Update the range

        if j + 1 == len(nums[i]):                           # Check if we have reached the end of one of the 'k' lists
            break                                           # Break out of the loop

        v = nums[i][j + 1]                                  # Obtain the next element from the "current" list
        right = max(right, v)                               # Compute the maximum b/w the new-ele and curr-right extreme
        heappush(pq, (v, i, j + 1))                         # Append the new-ele into the heap with corresponding indexes

    return list(ans)                                        # Return the result
