"""
494. Target Sum [MEDIUM]

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and
then concatenate all the integers.

    - For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the
      expression "+2-1".

Return the number of different expressions that you can build, which evaluates to target.


Example 1:
Input: nums = [1,1,1,1,1], target = 3
Output: 5

Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3


Example 2:
Input: nums = [1], target = 1
Output: 1


Constraints:

    -> 1 <= nums.length <= 20
    -> 0 <= nums[i] <= 1000
    -> 0 <= sum(nums[i]) <= 1000
    -> -1000 <= target <= 1000


Concepts: DP


Link: https://leetcode.com/problems/target-sum/solutions/455024/dp-is-easy-5-steps-to-think-through-dp-questions
"""
from collections import Counter


# Optimised Solution
def findTargetSumWays_op(nums: list[int], target: int) -> int:

    if (sum(nums) + target) % 2 != 0 or sum(nums) < abs(target):    # Check for invalid conditions
        return 0                                                    # Return 0

    subtarget = (sum(nums) + target) // 2                           # Compute the sub-target (or the "mid-point")

    dp = [0] * (subtarget + 1)                                      # List to track DP-vals
    dp[0] = 1                                                       # Initialise base case

    for num in nums:                                                # Iterate through the nums
        for i in range(subtarget, num - 1, -1):                     # Iterate from sub-target to num, in reverse
            dp[i] += dp[i - num]                                    # Update the DP-value at index

    return dp[subtarget]                                            # Return the result


# Alternate Solution
def findTargetSumWays_alt(nums: list[int], target: int) -> int:
    count = Counter({0: 1})                                         # Counter to track state instances

    for num in nums:                                                # Iterate through nums
        step = Counter()                                            # Counter to track possible sums
        for y in count:                                             # Iterate through discovered instances
            step[y + num] += count[y]                               # Increment the state count after addition
            step[y - num] += count[y]                               # Increment the state count after subtraction

        count = step                                                # Update the state dict w/ all sum-instances

    return count[target]                                            # Return the result
