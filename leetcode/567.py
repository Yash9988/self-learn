"""
567. Permutation in String [MEDIUM]

Given two strings s1 and s2, return true if s2 contains a _permutation_ of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.


Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").


Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false


Constraints:

    -> 1 <= s1.length, s2.length <= 104
    -> s1 and s2 consist of lowercase English letters.


Concepts: Sliding Window
"""
from collections import Counter


def checkInclusion(s1: str, s2: str) -> bool:
    n1, m = len(s1), 0                              # Initialise match-counter
    cnt = Counter(s1)                               # Compute the frequency of each character

    for i, ch2 in enumerate(s2):                    # Iterate through the string
        if ch2 in cnt:                              # Check if character is present in the dict
            m -= cnt[ch2] == 0                      # Decrement match-counter if character count already zero
            cnt[ch2] -= 1                           # Decrement character count
            m += cnt[ch2] == 0                      # Increment match-counter if character count is zero now

        idx = i - n1                                # Compute the index outside the window size
        if i >= n1 and s2[idx] in cnt:              # If the character at pointer is in the dict
            m -= cnt[s2[idx]] == 0                  # Decrement match-counter if character count already zero
            cnt[s2[idx]] += 1                       # Decrement character count
            m += cnt[s2[idx]] == 0                  # Increment match-counter if character count is zero now

        if m == len(cnt):                           # Check if the match-counter matches the characters in string
            return True                             # Return True

    return False                                    # Return False
