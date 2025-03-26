"""
1800. Maximum Ascending Subarray Sum [EASY]

Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.

A subarray [nums_l, nums_l+1, ..., nums_r-1, nums_r] is ascending if for all i where l <= i < r, nums_i  < nums_i+1.
Note that a subarray of size 1 is ascending.


Example 1:
Input: nums = [10,20,30,5,10,50]
Output: 65

Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.


Example 2:
Input: nums = [10,20,30,40,50]
Output: 150

Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.


Example 3:
Input: nums = [12,17,15,13,10,11,12]
Output: 33

Explanation: [10,11,12] is the ascending subarray with the maximum sum of 33.


Constraints:

    -> 1 <= nums.length <= 100
    -> 1 <= nums[i] <= 100


Concepts: Subarray
"""


# My Solution
def maxAscendingSum(nums: list[int]) -> int:
    res = 0                                                         # Counter to track the result
    t = nums[0]                                                     # Counter to track asc-sum

    for i in range(1, len(nums)):                                   # Iterate through teh list range
        if nums[i] <= nums[i - 1]:                                  # Check if the curr-ele is smaller than the prev
            res = max(res, t)                                       # Update the result counter with max-val
            t = 0                                                   # Reset the asc-sum counter

        t += nums[i]                                                # Increment the counter with ele-val

    return max(res, t)                                              # Compute and return the result
