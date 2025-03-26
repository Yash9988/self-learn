"""
2530. Maximal Score After Applying K Operations [MEDIUM]

You are given a 0-indexed integer array nums and an integer k. You have a starting score of 0.

In one operation:

    - choose an index i such that 0 <= i < nums.length,
    - increase your score by nums[i], and
    - replace nums[i] with ceil(nums[i] / 3).

Return the maximum possible score you can attain after applying exactly k operations.

The ceiling function ceil(val) is the least integer greater than or equal to val.


Example 1:

Input: nums = [10,10,10,10,10], k = 5
Output: 50

Explanation: Apply the operation to each array element exactly once. The final score is 10 + 10 + 10 + 10 + 10 = 50.

Example 2:

Input: nums = [1,10,3,3,3], k = 3
Output: 17

Explanation: You can do the following operations:
Operation 1: Select i = 1, so nums becomes [1,4,3,3,3]. Your score increases by 10.
Operation 2: Select i = 1, so nums becomes [1,2,3,3,3]. Your score increases by 4.
Operation 3: Select i = 2, so nums becomes [1,1,1,3,3]. Your score increases by 3.
The final score is 10 + 4 + 3 = 17.


Constraints:

    -> 1 <= nums.length, k <= 10^5
    -> 1 <= nums[i] <= 10^9


Concepts: Heap
"""
import math
from heapq import *


# My Solution
def maxKelements(nums: list[int], k: int) -> int:
    nums = [-x for x in nums]                           # Modify the input list to store negatives of all numbers
    heapify(nums)                                       # Convert the list into a heap

    res = 0                                             # Initialise a result counter
    while k:                                            # While the #operations are non-zero
        x = -heappop(nums)                              # Pop-out the minimum element from heap and negate it
        res += x                                        # Increment the result counter by the max-val obtained
        heappush(nums, -math.ceil(x / 3))               # Push the reduced value back into the heap (negated)
        k -= 1                                          # Decrement the operation counter

    return res                                          # Return the result


# Optimised Solution
def maxKelements_op(nums: list[int], k: int) -> int:
    pq = [-x for x in nums]                             # Modify the input list to store negatives of all numbers
    heapify(pq)                                         # Convert the list into a heap

    score = 0                                           # Initialise the result counter
    for _ in range(k):                                  # Iterate for 'k' operations
        score -= heappushpop(pq, pq[0] // 3)            # Obtain max-val from heap and increment the result counter
        # score -= heapreplace(pq, pq[0] // 3)          # Alternate method to obtain the same result

    return score                                        # Return the result
