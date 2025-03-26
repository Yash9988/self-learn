"""
1. Two Sum [EASY]

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]


Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

    -> 2 <= nums.length <= 104
    -> -109 <= nums[i] <= 109
    -> -109 <= target <= 109
    -> Only one valid answer exists.


Concepts: Hash Tables
"""


# My Solution [Time: O(N^2); Space: O(1)]
def twoSum(nums: list[int], target: int) -> list[int]:
    for i, m in enumerate(nums):                    # Iterate through all numbers
        for j, n in enumerate(nums):
            if i != j and m + n == target:          # Check if the number add upto the target value
                return [i, j]                       # Return the result


# Optimised Solution [Time: O(N); Space: O(1)]
def twoSum_op(nums: list[int], target: int) -> list[int]:
    h = {}                                          # Initialise Hash-Map
    for i, n in enumerate(nums):                    # Iterate through all numbers
        if n in h:                                  # Check if number present in hashmap
            return [h[n], i]                        # Return the current index and map-value
        else:
            h[target - n] = i                       # Store the remainder as key and current index as value
