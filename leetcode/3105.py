"""
3105. Longest Strictly Increasing or Strictly Decreasing Subarray [EASY]

You are given an array of integers nums. Return the length of the longest _subarray_ of nums which is either
strictly increasing or strictly decreasing.


Example 1:
Input: nums = [1,4,3,3,2]
Output: 2

Explanation:
The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].

The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].

Hence, we return 2.


Example 2:
Input: nums = [3,3,3,3]
Output: 1

Explanation:
The strictly increasing subarrays of nums are [3], [3], [3], and [3].

The strictly decreasing subarrays of nums are [3], [3], [3], and [3].

Hence, we return 1.


Example 3:
Input: nums = [3,2,1]
Output: 3

Explanation:
The strictly increasing subarrays of nums are [3], [2], and [1].

The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and [3,2,1].

Hence, we return 3.


Constraints:

    -> 1 <= nums.length <= 50
    -> 1 <= nums[i] <= 50


Concepts: Subarray
"""

# My Solution
def longestMonotonicSubarray(nums: list[int]) -> int:
    l = r = 0                                                       # Pointers to track starting points for inc & dec
    prev = nums[0]                                                  # Counter to track the last element
    res = 1                                                         # Counter to track the result

    for i in range(1, len(nums)):                                   # Iterate through the list range
        n = nums[i]                                                 # Obtain the element at curr-idx
        if n > prev:                                                # Check if the curr-ele is greater than the prev
            res = max(res, i - l + 1)                               # Update the result with max-val
            r = i                                                   # Reset the dec-pointer to the curr-idx
        elif n < prev:                                              # Check else if the curr-ele is smaller
            res = max(res, i - r + 1)                               # Update the result with max-val
            l = i                                                   # Reset the inc-pointer to the curr-idx
        else:
            l = r = i                                               # Set both pointers to the curr-idx, otherwise

        prev = n                                                    # Update the counter with curr-ele

    return res                                                      # Return the result

# Optimised Solution
def longestMonotonicSubarray_op(nums: list[int]) -> int:
    n, ans, inc, dec = len(nums), 1, 1, 1                           # Counters to track subarray sizes and result

    for i in range(1, n):                                           # Iterate through the list range
        A = nums[i] > nums[i - 1]                                   # Check if curr-ele is greater than the prev
        B = nums[i] < nums[i - 1]                                   # Check if curr-ele is smaller than the prev

        inc = A * inc + 1                                           # Increment the inc-counter, accordingly
        dec = B * dec + 1                                           # Increment the dec-counter, accordingly
        ans = max(ans, dec, inc)                                    # Update the result counter with max-val

    return ans                                                      # Return the result
