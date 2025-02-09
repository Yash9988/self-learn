"""
2364. Count Number of Bad Pairs [MEDIUM]

You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if:
    i < j and j - i != nums[j] - nums[i].

Return the total number of bad pairs in nums.


Example 1:
Input: nums = [4,1,3,3]
Output: 5

Explanation: The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
There are a total of 5 bad pairs, so we return 5.


Example 2:
Input: nums = [1,2,3,4,5]
Output: 0

Explanation: There are no bad pairs.


Constraints:

    -> 1 <= nums.length <= 10^5
    -> 1 <= nums[i] <= 10^9


Concepts: Hashmap, Mathematical Intuition


Link: https://leetcode.com/problems/count-number-of-bad-pairs/solutions/6395666/beats-100-hashmap-math-approach-easiest-solution-ever-algorithm-explained
"""
from collections import Counter


# Optimised Solution
def countBadPairs(nums: list[int]) -> int:
    length = len(nums)                                              # Obtain the list size
    nums_new = [num - index for index, num in enumerate(nums)]      # Compute the diff b/w num and its corr-idx

    count = Counter(nums_new)                                       # Compute a freq-map of the diff

    total_pairs = length * (length - 1) / 2                         # Compute total #pairs

    for key, val in count.items():                                  # Iterate through the freq-items
        if val > 1:                                                 # Check if the freq is greater than one
            total_pairs -= val * (val - 1) / 2                      # Decrement the possible good-pairs

    return int(total_pairs)                                         # Return the result
