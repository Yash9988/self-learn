"""
1671. Minimum Number of Removals to Make Mountain Array [HARD]

You may recall that an array arr is a mountain array if and only if:

    - arr.length >= 3
    - There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
        -- arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        -- arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Given an integer array nums, return the minimum number of elements to remove to make nums a mountain array.


Example 1:
Input: nums = [1,3,1]
Output: 0
Explanation: The array itself is a mountain array so we do not need to remove any elements.


Example 2:
Input: nums = [2,1,1,5,6,2,3,1]
Output: 3
Explanation: One solution is to remove the elements at indices 0, 1, and 5, making the array nums = [1,5,6,3,1].


Constraints:

    -> 3 <= nums.length <= 1000
    -> 1 <= nums[i] <= 10^9
    -> It is guaranteed that you can make a mountain array out of nums.


Concepts: LIS, DP
"""
from bisect import bisect_left


# Optimised Solution
def minimumMountainRemovals(nums: list[int]) -> int:
    # Helper method to find the longest increasing subsequence
    def LIS(nums):
        dp = [10**10] * (len(nums) + 1)                         # Initialise a DP for input list
        lens = [0]*len(nums)                                    # Initialise a list to store lengths
        for i, elem in enumerate(nums):                         # Iterate through the numbers
            lens[i] = bisect_left(dp, elem) + 1                 # Update the len-list at index, with corr-pos in dp
            dp[lens[i] - 1] = elem                              # Update the DP at correct index with element
        return lens                                             # Return the len-list

    l1, l2 = LIS(nums), LIS(nums[::-1])[::-1]                   # Compute the len-list and reversed for input list
    ans, n = 0, len(nums)                                       # Initialise result counter and compute list length
    for i in range(n):                                          # Iterate through the nums
        if l1[i] >= 2 and l2[i] >= 2:                           # Check for valid conditions
            ans = max(ans, l1[i] + l2[i] - 1)                   # Update the result counter with max-val

    return n - ans                                              # Compute and return the result


# Alternate Solution
def minimumMountainRemovals_alt(nums: list[int]) -> int:
    n = len(nums)                                               # Compute the length of the input list
    dp1, dp2 = [1] * n, [1] * n                                 # Initialise 2 DPs
    for i in range(1, n):                                       # Iterate through the nums, starting at index 1
        for j in range(i):                                      # Iterate to the curr-idx
            if nums[j] < nums[i]:                               # Check if prev-num is smaller than curr-num
                dp1[i] = max(dp1[i], 1 + dp1[j])                # Update DP1 with max-val

            if nums[j] > nums[i]:                               # Check if pre-num is greater than curr-num
                if dp1[j] > 1:                                  # Check if prev-num is greater than one
                    dp2[i] = max(dp2[i], 1 + dp1[j])            # Update DP2 with max-val w/ DP1

                if dp2[j] > 1:                                  # Check if prev-num is smaller than one
                    dp2[i] = max(dp2[i], 1 + dp2[j])            # Update the DP2 with max-val

    return n - max(dp2)                                         # Compute and return the result
