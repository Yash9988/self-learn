"""
2206. Divide Array Into Equal Pairs [EASY]

You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

    - Each element belongs to exactly one pair.
    - The elements present in a pair are equal.

Return true if nums can be divided into n pairs, otherwise return false.


Example 1:
Input: nums = [3,2,3,2,2,2]
Output: true

Explanation:
There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.


Example 2:
Input: nums = [1,2,3,4]
Output: false

Explanation:
There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.


Constraints:

    -> nums.length == 2 * n
    -> 1 <= n <= 500
    -> 1 <= nums[i] <= 500


Concepts: Hashmap
"""
from collections import Counter


# My Solution
def divideArray(nums: list[int]) -> bool:
    seen = set()                                                    # Set to track seen elements
    for num in nums:                                                # Iterate through the numbers
        if num in seen:                                             # Check if num is present in set
            seen.remove(num)                                        # Remove num from the set
        else:
            seen.add(num)                                           # Add num to the set, otherwise

    return False if len(seen) else True                             # Compare and return the result


# Optimised Solution
def divideArray_op(nums: list[int]) -> bool:
    counter = Counter(nums)                                         # Compute the freq-dict for the input list

    for count in counter.values():                                  # Iterate thought the frequencies
        if count % 2:                                               # Check if the freq is odd
            return False                                            # Return False

    return True                                                     # Return True
