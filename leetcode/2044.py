"""
2044. Count Number of Maximum Bitwise-OR Subsets [MEDIUM]

Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different
non-empty subsets with the maximum bitwise OR.

An array _a_ is a subset of an array _b_ if a can be obtained from b by deleting some (possibly zero) elements of b. Two
subsets are considered different if the indices of the elements chosen are different.

The bitwise OR of an array _a_ is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).


Example 1:

Input: nums = [3,1]
Output: 2

Explanation: The maximum possible bitwise OR of a subset is 3. There are 2 subsets with a bitwise OR of 3:
- [3]
- [3,1]


Example 2:

Input: nums = [2,2,2]
Output: 7

Explanation: All non-empty subsets of [2,2,2] have a bitwise OR of 2. There are 23 - 1 = 7 total subsets.


Example 3:

Input: nums = [3,2,1,5]
Output: 6

Explanation: The maximum possible bitwise OR of a subset is 7. There are 6 subsets with a bitwise OR of 7:
- [3,5]
- [3,1,5]
- [3,2,5]
- [3,2,1,5]
- [2,5]
- [2,1,5]


Constraints:

    -> 1 <= nums.length <= 16
    -> 1 <= nums[i] <= 10^5


Concepts: Subsets
"""
from collections import Counter


# My Solution
def countMaxOrSubsets(nums: list[int]) -> int:
    def getSubsets(num, i):                                 # Define a recursive helper method to find subsets
        if i == n:                                          # Check for base-case
            sums.append(num)                                # Add the OR-sum to the list
            return                                          # Terminate the loop

        getSubsets(num, i + 1)                              # Omit the element at current index
        getSubsets(num | nums[i], i + 1)                    # Include the element at current index

    sums, n = [], len(nums)                                 # Initialise a list and compute the length of input list
    getSubsets(0, 0)                                        # Obtain all subsets of the input list

    return sums.count(max(sums))                            # Return the result


# Optimised Solution
def countMaxOrSubsets_op(nums: list[int]) -> int:
    dp = Counter([0])                                       # Initialise a count-dict with zero

    for n in nums:                                          # Iterate through all elements of input list
        for k, v in list(dp.items()):                       # Iterate through all valur pairs in the count-dict
            dp[k | n] += v                                  # Update the dict with corresponding values

    return dp[max(dp)]                                      # Return the result
