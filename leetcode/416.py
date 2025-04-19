"""
416. Partition Equal Subset Sum [MEDIUM]

Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the
elements in both subsets is equal or false otherwise.


Example 1:
Input: nums = [1,5,11,5]
Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].


Example 2:
Input: nums = [1,2,3,5]
Output: false

Explanation: The array cannot be partitioned into equal sum subsets.


Constraints:

    -> 1 <= nums.length <= 200
    -> 1 <= nums[i] <= 100


Concepts: DP
"""


# Optimised Solution
def canPartition(nums: list[int]) -> bool:
    totalSum = sum(nums)                                            # Compute the sum of the list
    if totalSum % 2 != 0:                                           # Check if the sum is odd
        return False                                                # Return False

    targetSum = totalSum // 2                                       # Compute the split-sum
    dp = [False] * (targetSum + 1)                                  # List to track the DP-vals
    dp[0] = True                                                    # Set the base-case

    for num in nums:                                                # Iterate through the nums
        for currSum in range(targetSum, num - 1, -1):               # Iterate from target to num, in reverse
            dp[currSum] = dp[currSum] or dp[currSum - num]          # Update the DP-val at idx

    return dp[targetSum]                                            # Return the result
