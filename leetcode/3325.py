"""
3325. Count Substrings With K-Frequency Characters I [MEDIUM]

Given a string s and an integer k, return the total number of _substrings_ of s where at least one character appears at
least k times.


Example 1:
Input: s = "abacb", k = 2
Output: 4

Explanation:
The valid substrings are:

    "aba" (character 'a' appears 2 times).
    "abac" (character 'a' appears 2 times).
    "abacb" (character 'a' appears 2 times).
    "bacb" (character 'b' appears 2 times).


Example 2:
Input: s = "abcde", k = 1
Output: 15

Explanation:
All substrings are valid because every character appears at least once.


Constraints:

    -> 1 <= s.length <= 3000
    -> 1 <= k <= s.length
    -> s consists only of lowercase English letters.


Concepts: Substring count, Sliding window
"""
from collections import defaultdict


# Optimised Solution
def numberOfSubstrings(s: str, k: int) -> int:
    l, cnt = 0, defaultdict(int)                                    # Dict to track count of characters
    res = 0                                                         # Counter to store the result

    for ch in s:                                                    # Iterate through the string
        cnt[ch] += 1                                                # Increment the char-count
        while cnt[ch] == k:                                         # While the count is equal to `k`
            cnt[s[l]] -= 1                                          # Decrement the count for char at left pointer
            l += 1                                                  # Increment the pointer

        res += l                                                    # Increment the result counter by pointer index

    return res                                                      # Return the result
