"""
2529. Maximum Count of Positive Integer and Negative Integer [EASY]

Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the
number of negative integers.

    - In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then
      return the maximum of pos and neg.

Note that 0 is neither positive nor negative.


Example 1:
Input: nums = [-2,-1,-1,1,2,3]
Output: 3

Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.


Example 2:
Input: nums = [-3,-2,-1,0,0,1,2]
Output: 3

Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.


Example 3:
Input: nums = [5,20,66,1314]
Output: 4
Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.


Constraints:

    -> 1 <= nums.length <= 2000
    -> -2000 <= nums[i] <= 2000
    -> nums is sorted in a non-decreasing order.


Follow up: Can you solve the problem in O(log(n)) time complexity?


Concepts: Binary Search
"""
from bisect import bisect_left


# My Solution
def maximumCount(nums: list[int]) -> int:
    pos = neg = 0                                                   # Counters to track pos & neg integers
    for num in nums:                                                # Iterate through the list
        pos += num > 0                                              # Increment the counter if num is pos
        neg += num < 0                                              # Increment the counter if num is neg

    return max(pos, neg)                                            # Return the result


# Optimised Solution
def maximumCount_op(nums: list[int]) -> int:
    first_non_negative = bisect_left(nums, 0)                       # Obtain the index for the first zero
    first_positive = bisect_left(nums, 1)                           # Obtain the index for the first pos-int

    neg = first_non_negative                                        # Count the number of negative numbers
    pos = len(nums) - first_positive                                # Count the number of positive numbers

    return max(neg, pos)                                            # Return the result
