"""
2401. Longest Nice Subarray [MEDIUM]

You are given an array nums consisting of positive integers.

We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the
subarray is equal to 0.

Return the length of the longest nice subarray.

A subarray is a contiguous part of an array.

Note that subarrays of length 1 are always considered nice.


Example 1:
Input: nums = [1,3,8,48,10]
Output: 3

Explanation: The longest nice subarray is [3,8,48]. This subarray satisfies the conditions:
- 3 AND 8 = 0.
- 3 AND 48 = 0.
- 8 AND 48 = 0.
It can be proven that no longer nice subarray can be obtained, so we return 3.


Example 2:
Input: nums = [3,1,5,11,13]
Output: 1

Explanation: The length of the longest nice subarray is 1. Any subarray of length 1 can be chosen.


Constraints:

    -> 1 <= nums.length <= 10^5
    -> 1 <= nums[i] <= 10^9


Concepts: Bit Manipulation, Subarray, Sliding Window
"""


# Optimised Solution
def longestNiceSubarray(nums: list[int]) -> int:
    n = len(nums)                                                   # Obtain the list size
    max_length = 1                                                  # Counter to track max subarray length

    left = 0                                                        # Pointer to track window start
    used_bits = 0                                                   # Counter to track used bits

    for right in range(n):                                          # Iterate through the range of list
        while used_bits & nums[right] != 0:                         # Checks if curr-num shares any bits with our window
            used_bits ^= nums[left]                                 # Remove the leftmost element's bits
            left += 1                                               # Increment the left pointer

        used_bits |= nums[right]                                    # Adds the curr-ele bits to our tracking

        max_length = max(max_length, right - left + 1)              # Update the counter with max-val

    return max_length                                               # Return the result
