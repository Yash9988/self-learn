"""
2563. Count the Number of Fair Pairs [MEDIUM]

Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

A pair (i, j) is fair if:

    - 0 <= i < j < n, and
    - lower <= nums[i] + nums[j] <= upper


Example 1:
Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).


Example 2:
Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).


Constraints:

    -> 1 <= nums.length <= 10^5
    -> nums.length == n
    -> -10^9 <= nums[i] <= 10^9
    -> -10^9 <= lower <= upper <= 10^9


Concepts: Double Pointers,
"""


# Optimised Solution
def countFairPairs_op(nums: list[int], lower: int, upper: int) -> int:
    # Helper method to calculate the number of pairs with sum less than `value`.
    def lower_bound(value: int) -> int:
        left, right = 0, len(nums) - 1                          # Initialise 2 pointers
        result = 0                                              # Initialise a result counter

        while left < right:                                     # While the left pointer is smaller than the right one
            sum_ = nums[left] + nums[right]                     # Compute the sum of element values at the pointers

            if sum_ < value:                                    # Check if the sum is smaller than the value
                result += right - left                          # Add the window size to the result counter
                left += 1                                       # Increment the left pointer
            else:
                right -= 1                                      # Decrement the right pointer, until valid window

        return result                                           # Return the result

    nums.sort()                                                 # Sort the input list
    return lower_bound(upper + 1) - lower_bound(lower)          # Compute the diff and return the result


# Alternate Solution
def countFairPairs_alt(nums: list[int], lower: int, upper: int) -> int:
    # Helper method to calculate the number of pairs with sum less than `value`
    def countLess(val: int) -> int:
        res, j = 0, len(nums) - 1                               # Initialise a result counter and a pointer

        for i in range(len(nums)):                              # Iterate through nums
            while i < j and nums[i] + nums[j] > val:            # While `curr-idx < pointer` and `sum > val`
                j -= 1                                          # Decrement the pointer

            res += max(0, j - i)                                # Add the window size to the result counter

        return res                                              # Return the result

    nums.sort()                                                 # Sort the input list
    return countLess(upper) - countLess(lower - 1)              # Compute the diff and return the result
