"""
179. Largest Number [MEDIUM]

Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.


Example 1:

Input: nums = [10,2]
Output: "210"

Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"


Constraints:

    -> 1 <= nums.length <= 100
    -> 0 <= nums[i] <= 109


Concepts: Custom Sort

"""
from functools import cmp_to_key


def largestNumber(nums: list[int]) -> str:
    def compare(n1: str, n2: str) -> int:                               # Helper method for custom sort-technique
        return -1 if n1 + n2 > n2 + n1 else \
            (1 if n1 + n2 < n2 + n1 else 0)                             # Check which ordering will procure higher value

    if not any(nums):                                                   # If the numbers are all zeros
        return "0"

    return "".join(sorted(map(str, nums), key=cmp_to_key(compare)))     # Sort and combine the list for the highest val
