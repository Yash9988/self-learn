"""
1930. Unique Length-3 Palindromic Subsequences [MEDIUM]

Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted
without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".


Example 1:
Input: s = "aabca"
Output: 3

Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")


Example 2:
Input: s = "adc"
Output: 0

Explanation: There are no palindromic subsequences of length 3 in "adc".


Example 3:
Input: s = "bbcbaba"
Output: 4

Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")


Constraints:

    -> 3 <= s.length <= 10^5
    -> s consists of only lowercase English letters.


Concepts: Last Occurrence
"""
from math import inf


# Alternate Solution (Easier to understand)
def countPalindromicSubsequence_alt(s: str) -> int:
    fc, lc = [inf] * 26, [-inf] * 26                                # Lists to track first & last char-occurrence

    for i, ch in enumerate(s):                                      # Iterate through the string
        idx = ord(ch) - ord('a')                                    # Compute the char-idx

        fc[idx] = min(fc[idx], i)                                   # Update the first occurrence index
        lc[idx] = max(lc[idx], i)                                   # Update the last occurrence index

    res = 0                                                         # Counter to track result
    for i in range(26):                                             # Iterate through the alphabet range
        if fc[i] == inf or lc[i] == -inf:                           # Check if the char only appears once
            continue                                                # Skip to the next iteration

        unique = set([])                                            # Set to store the unique chars in the range
        for j in range(fc[i] + 1, lc[i]):                           # Iterate through the window range
            unique.add(s[j])                                        # Add the curr-char to the set

        res += len(unique)                                          # Increment the counter by the length of the set

    return res                                                      # Return the result


# Optimised Solution
def countPalindromicSubsequence_op(s: str) -> int:
    res = 0                                                         # Counter to track the result

    for ch in range(26):                                            # Iterate through the alphabet range
        c = chr(ord('a') + ch)                                      # Compute the char-idx
        leftIdx, rightIdx = s.find(c), s.rfind(c)                   # Obtain the first occurrence-idx from left & right

        if leftIdx != rightIdx:                                     # Check if the indices are different
            res += len(set(s[leftIdx + 1:rightIdx]))                # Increment counter by unique chars in the window

    return res                                                      # Return the result
