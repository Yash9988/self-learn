"""
2501. Longest Square Streak in an Array [Medium]

You are given an integer array nums. A subsequence of nums is called a square streak if:

    - The length of the subsequence is at least 2, and
    - after sorting the subsequence, each element (except the first element) is the square of the previous number.

Return the length of the longest square streak in nums, or return -1 if there is no square streak.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the
order of the remaining elements.


Example 1:
Input: nums = [4,3,6,16,8,2]
Output: 3

Explanation: Choose the subsequence [4,16,2]. After sorting it, it becomes [2,4,16].
- 4 = 2 * 2.
- 16 = 4 * 4.
Therefore, [4,16,2] is a square streak.
It can be shown that every subsequence of length 4 is not a square streak.


Example 2:
Input: nums = [2,3,5,6,7]
Output: -1

Explanation: There is no square streak in nums so return -1.


Constraints:

    -> 2 <= nums.length <= 10^5
    -> 2 <= nums[i] <= 10^5


Concepts:
"""
from math import isqrt


# My Solution
def longestSquareStreak(nums: list[int]) -> int:
    res = -1                                        # Initialise the result counter
    nums = set(nums)                                # Initialise a set of the input list
    for n in nums:                                  # Iterate through the numbers
        ans = 1                                     # Initialise a counter
        t = n                                       # Create a copy of the curr-val
        while n != 1 and t ** 2 in nums:            # While the square of the curr-val exists in the set
            t **= 2                                 # Update the copy by squaring its value
            ans += 1                                # Increment the counter
            res = max(res, ans)                     # Update the result with the max-val

    return res                                      # Return the result


# Optimised Solution
def longestSquareStreak_op(nums):
    mp = {}                                         # Initialise a dict
    nums.sort()                                     # Sort the list of numbers
    res = -1                                        # Initialise a result counter

    for num in nums:                                # Iterate through the numbers
        sqrt = isqrt(num)                           # Compute the square root of the number

        if sqrt * sqrt == num and sqrt in mp:       # Check if sqrt is valid and in dict
            mp[num] = mp[sqrt] + 1                  # Increment the "streak" for the number
            res = max(res, mp[num])                 # Update the result counter with the max "streak" value
        else:
            mp[num] = 1                             # Initialise the streak for the number, otherwise

    return res                                      # Return the result
