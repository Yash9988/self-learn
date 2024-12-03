"""
3097. Shortest Subarray With OR at Least K II [MEDIUM]

You are given an array nums of non-negative integers and an integer k.

An array is called special if the bitwise OR of all of its elements is at least k.

Return the length of the shortest special non-empty _subarray_ of nums, or return -1 if no special subarray exists.


Example 1:
Input: nums = [1,2,3], k = 2
Output: 1

Explanation: The subarray [3] has OR value of 3. Hence, we return 1.


Example 2:
Input: nums = [2,1,8], k = 10
Output: 3

Explanation: The subarray [2,1,8] has OR value of 11. Hence, we return 3.


Example 3:
Input: nums = [1,2], k = 0
Output: 1

Explanation: The subarray [1] has OR value of 1. Hence, we return 1.


Constraints:

    -> 1 <= nums.length <= 2 * 10^5
    -> 0 <= nums[i] <= 10^9
    -> 0 <= k <= 10^9


Concepts: Subarrays
"""
from math import inf


def minimumSubarrayLength(nums: list[int], k: int) -> int:
    res = inf                                               # Initialise a counter to track the result value
    d = dict()                                              # Initialise a dictionary to store all possible OR values

    for i, x in enumerate(nums):                            # Iterate through the numbers
        d = {or_ | x: left for or_, left in d.items()}      # Update the dictionary with new values and their indices
        d[x] = i                                            # Append the curr-ele to the dictionary
        for or_, left in d.items():                         # Iterate through the dictionary items
            if or_ >= k:                                    # Check if the value is greater than `k`
                res = min(res, i - left + 1)                # Update the result counter with the smallest subarray size

    return res if res < inf else -1                         # Return the result
