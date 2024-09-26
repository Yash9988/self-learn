"""
3298. Count Substrings That Can Be Rearranged to Contain a String II [HARD]

You are given two strings word1 and word2.

A string x is called valid if x can be rearranged to have word2 as a _prefix_.

Return the total number of valid _substrings_ of word1.

Note that the memory limits in this problem are smaller than usual, so you must implement a solution with a linear
runtime complexity.


Example 1:

Input: word1 = "bcca", word2 = "abc"
Output: 1

Explanation:

The only valid substring is "bcca" which can be rearranged to "abcc" having "abc" as a prefix.


Example 2:

Input: word1 = "abcabc", word2 = "abc"
Output: 10

Explanation:

All the substrings except substrings of size 1 and size 2 are valid.


Example 3:

Input: word1 = "abcabc", word2 = "aaabc"
Output: 0


Constraints:

    -> 1 <= word1.length <= 106
    -> 1 <= word2.length <= 104
    -> word1 and word2 consist only of lowercase English letters.


Concepts: Double Pointers, Substrings
"""
from collections import defaultdict


# Optimised Solution
def validSubstringCount(word1: str, word2: str) -> int:
    # c = Counter(word2)                # Obtain frequency of all character in prefix (Manual counting is ~2x faster)
    if len(word1) < len(word2):         # Check if the length of prefix is greater
        return 0                        # Return 0

    c = defaultdict(int)                # Initialise a default-dict to store character frequencies for prefix word
    for ch in word2:                    # Iterate through all characters in the prefix
        c[ch] += 1                      # Increment the respective character count

    l, m, res = 0, len(c), 0            # Initialise counters for left-pointer, matches, and result
    for ch in word1:                    # Iterate through all characters in word1 string
        c[ch] -= 1                      # Decrement the frequency of the current character
        if c[ch] == 0:                  # Check if the frequency is zero
            m -= 1                      # Reduce the match counter, denoting the satisfaction of requirement in prefix

        while m == 0:                   # While the match counter is zero
            lch = word1[l]              # Acquire the character at left-pointer
            if c[lch] == 0:             # Check if the frequency of the said character is zero
                m += 1                  # Increment the match counter, denoting reversion of prefix requirement
            c[lch] += 1                 # Increment the frequency of the current character
            l += 1                      # Increment the left pointer

        res += l                        # Add the index of left-pointer to the result, after each iteration
    return res                          # Return the result
