"""
2425. Bitwise XOR of All Pairings [MEDIUM]

You are given two 0-indexed arrays, nums1 and nums2, consisting of non-negative integers. There exists another array,
nums3, which contains the bitwise XOR of all pairings of integers between nums1 and nums2 (every integer in nums1 is
paired with every integer in nums2 exactly once).

Return the bitwise XOR of all integers in nums3.


Example 1:
Input: nums1 = [2,1,3], nums2 = [10,2,5,0]
Output: 13

Explanation:
A possible nums3 array is [8,0,7,2,11,3,4,1,9,1,6,3].
The bitwise XOR of all these numbers is 13, so we return 13.


Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 0

Explanation:
All possible pairs of bitwise XORs are nums1[0] ^ nums2[0], nums1[0] ^ nums2[1], nums1[1] ^ nums2[0],
and nums1[1] ^ nums2[1].
Thus, one possible nums3 array is [2,5,1,6].
2 ^ 5 ^ 1 ^ 6 = 0, so we return 0.


Constraints:

    -> 1 <= nums1.length, nums2.length <= 10^5
    -> 0 <= nums1[i], nums2[j] <= 10^9


Concepts: Bit Manipulation, Mathematical Intuition


Link: https://leetcode.com/problems/bitwise-xor-of-all-pairings/solutions/6225157/bitwise-xor-of-all-pairings
"""


# Optimised Solution
def xorAllNums(nums1: list[int], nums2: list[int]) -> int:
    n1, n2 = len(nums1), len(nums2)                                 # Obtain the sizes of both lists
    res = 0                                                         # Counter to track the result

    # Check if elements will be repeated odd number of times when paired
    if n2 % 2:
        for n in nums1:                                             # Iterate through the first list
            res ^= n                                                # Update the counter value

    # Check if elements will be repeated odd number of times when paired
    if n1 % 2:
        for n in nums2:                                             # Iterate through the second list
            res ^= n                                                # Update the counter value

    return res                                                      # Return the result

