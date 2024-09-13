"""
1755. Closest Subsequence Sum [HARD]

You are given an integer array nums and an integer goal.

You want to choose a subsequence of nums such that the sum of its elements is the closest possible to goal. That is, if
the sum of the subsequence's elements is sum, then you want to minimize the absolute difference abs(sum - goal).

Return the minimum possible value of abs(sum - goal).

Note that a subsequence of an array is an array formed by removing some elements (possibly all or none) of the original
array.


Example 1:

Input: nums = [5,-7,3,5], goal = 6
Output: 0
Explanation: Choose the whole array as a subsequence, with a sum of 6.
This is equal to the goal, so the absolute difference is 0.

Example 2:

Input: nums = [7,-9,15,-2], goal = -5
Output: 1
Explanation: Choose the subsequence [7,-9,-2], with a sum of -4.
The absolute difference is abs(-4 - (-5)) = abs(1) = 1, which is the minimum.

Example 3:

Input: nums = [1,2,3], goal = -7
Output: 7


Constraints:

    -> 1 <= nums.length <= 40
    -> -107 <= nums[i] <= 107
    -> -109 <= goal <= 109

"""
from bisect import bisect_left


# DFS-Solution
def minAbsDifference(nums: list[int], goal: int) -> int:
    def dfs(arr: list, i: int, total: int, log: set) -> None:   # Helper-method to find all combinations of an array
        if i == len(arr):                                       # Check if pointer has reached the end of array
            log.add(total)                                      # Append the final sum value to the set
            return

        dfs(arr, i + 1, total, log)                             # Sum, exclusive of the current element
        dfs(arr, i + 1, total + arr[i], log)                    # Sum, inclusive of the current element

    sum1, sum2 = set(), set()                                   # Initialise sets for first & second half of the array

    dfs(nums[:len(nums) // 2], 0, 0, sum1)              # Find all sub-sequence sum for the first-half
    dfs(nums[len(nums) // 2:], 0, 0, sum2)              # Find all sub-sequence sum for the second-half

    s2, ans = sorted(sum2), float('inf')                        # Sort the set for second-half to apply Binary-search

    for s in sum1:                                              # Iterate through all sums from first-half
        diff = goal - s                                         # Calculate the difference from "goal"
        idx = bisect_left(s2, diff)                             # Find the closest value index in the sorted half

                                                                # Compare & store the minimum difference obtained so far
        if idx < len(s2):
            ans = min(ans, abs(diff - s2[idx]))
        if idx > 0:
            ans = min(ans, abs(diff - s2[idx - 1]))

    return ans                                                  # Return the result


# Optimised Solution (10x times faster runtime than the original)
def minAbsDifference_op(nums: list[int], goal: int) -> int:
    def sums(arr):
        sums = {0}
        for a in arr:
            sums |= {s + a for s in sums}
        return sums

    sum1 = sums(nums[1::2])
    s2 = sorted(sums(nums[::2]))

    ans = float('inf')

    for s in sum1:
        diff = goal - s
        idx = bisect_left(s2, diff)

        if idx < len(s2):
            ans = min(ans, abs(diff - s2[idx]))
        if idx > 0:
            ans = min(ans, abs(diff - s2[idx - 1]))

    return ans