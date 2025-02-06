"""
1726. Tuple with Same Product [MEDIUM]

Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d
where a, b, c, and d are elements of nums, and a != b != c != d.


Example 1:
Input: nums = [2,3,4,6]
Output: 8

Explanation: There are 8 valid tuples:
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)


Example 2:
Input: nums = [1,2,4,5,10]
Output: 16

Explanation: There are 16 valid tuples:
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)


Constraints:

    -> 1 <= nums.length <= 1000
    -> 1 <= nums[i] <= 10^4
    -> All elements in nums are distinct.


Concepts: Mathematical Intuition, Combinations
"""
from collections import defaultdict


# My Solution (Optimised)
def tupleSameProduct(nums: list[int]) -> int:
    n = len(nums)                                                   # Obtain the list size
    grps = defaultdict(int)                                         # Dict to track the products

    for i in range(n):                                              # Iterate through the list range
        for j in range(i + 1, n):                                   # Iterate through the remaining range
            grps[nums[i] * nums[j]] += 1                            # Increment the freq of the product obtained

    res = 0                                                         # Counter to track the result
    for v in grps.values():                                         # Iterate through the product frequencies
        if v > 1:                                                   # Check if the freq is greater than 1
            res += 4 * v * (v - 1)                                  # Compute and Increment the counter, accordingly

    return res                                                      # Return the result
