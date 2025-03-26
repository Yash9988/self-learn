"""
3309. Maximum Possible Number by Binary Concatenation [MEDIUM]

You are given an array of integers nums of size 3.

Return the maximum possible number whose binary representation can be formed by concatenating the binary representation
of all elements in nums in some order.

Note that the binary representation of any number does not contain leading zeros.


Example 1:

Input: nums = [1,2,3]
Output: 30

Explanation:
Concatenate the numbers in the order [3, 1, 2] to get the result "11110", which is the binary representation of 30.


Example 2:

Input: nums = [2,8,16]
Output: 1296

Explanation:
Concatenate the numbers in the order [2, 8, 16] to get the result "10100010000", which is the binary representation of 1296.


Constraints:

    -> nums.length == 3
    -> 1 <= nums[i] <= 127


Concepts: Custom Sorting
"""
from functools import cmp_to_key


def maxGoodNumber(nums: list[int]) -> int:
    def cmp(a, b):                                  # Define a custom comparison method
        return 1 if a + b < b + a else -1

    nums = [bin(x)[2:] for x in nums]               # Modify the input-list to contain binary-repr of the elements
    nums.sort(key=cmp_to_key(cmp))                  # Sort the modified list using the custom comparator

    return int(''.join(nums), 2)                    # Return the integer-repr of all the sorted binaries combined
