"""
962. Maximum Width Ramp [MEDIUM]

A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j].
The width of such a ramp is j - i.

Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.


Example 1:

Input: nums = [6,0,8,2,1,5]
Output: 4

Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.


Example 2:

Input: nums = [9,8,1,0,1,9,4,0,4,1]
Output: 7

Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.


Constraints:

    -> 2 <= nums.length <= 5 * 10^4
    -> 0 <= nums[i] <= 5 * 10^4


Concepts: Stack
"""


def maxWidthRamp(nums: list[int]) -> int:
    s, n = [], len(nums)                                # Initialise a stack
    res = 0                                             # Initialise result counter
    for i, num in enumerate(nums):                      # Iterate through the input-array
        if not s or nums[s[-1]] > num:                  # Check if stack is empty OR last-ele of stack > curr-ele
            s.append(i)                                 # Append the element to the stack

    for j in range(n)[::-1]:                            # Iterate through the input-array in reverse
        while s and nums[s[-1]] <= nums[j]:             # Check if stack is not empty AND last-ele <= curr-ele
            res = max(res, j - s.pop())                 # Compute the diff b/w the indexes and pop element from stack

    return res                                          # Return the result
