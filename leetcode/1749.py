"""
1749. Maximum Absolute Sum of Any Subarray [MEDIUM]

You are given an integer array nums. The absolute sum of a subarray [nums_l, nums_l+1, ..., nums_r-1, nums_r] is
abs(nums_l + nums_l+1 + ... + nums_r-1 + nums_r).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:

    - If x is a negative integer, then abs(x) = -x.
    - If x is a non-negative integer, then abs(x) = x.


Example 1:
Input: nums = [1,-3,2,3,-4]
Output: 5

Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.


Example 2:
Input: nums = [2,-5,1,-4,3,-2]
Output: 8

Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.


Constraints:

    -> 1 <= nums.length <= 10^5
    -> -10^4 <= nums[i] <= 10^4


Concepts: Prefix-Sum
"""
from itertools import accumulate


# Optimised Solution
def maxAbsoluteSum(nums: list[int]) -> int:
    s = list(accumulate(nums, initial=0))                           # Compute the prefix-sum for the input list
    return max(s) - min(s)                                          # Compute and return the result
