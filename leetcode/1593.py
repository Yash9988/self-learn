"""
1593. Split a String Into the Max Number of Unique Substrings [MEDIUM]

Given a string s, return the maximum number of unique substrings that the given string can be split into.

You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the
original string. However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.


Example 1:

Input: s = "ababccc"
Output: 5

Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc']
is not valid as you have 'a' and 'b' multiple times.


Example 2:

Input: s = "aba"
Output: 2

Explanation: One way to split maximally is ['a', 'ba'].


Example 3:

Input: s = "aa"
Output: 1

Explanation: It is impossible to split the string any further.


Constraints:

    -> 1 <= s.length <= 16
    -> s contains only lower case English letters.


Concepts: Substrings, DFS
"""


def maxUniqueSplit(s: str) -> int:
    def dfs(s: str) -> int:
        if not s:                                               # Check for empty string
            return 0                                            # Return 0

        res = 0                                                 # Initialise result counter
        for i in range(1, len(s) + 1):                          # Iterate through the length of input-string
            if s[:i] not in seen and len(s) - i + 1 > res:      # Check if substring is unseen
                seen.add(s[:i])                                 # Add substring to the set
                res = max(res, 1 + dfs(s[i:]))                  # Recursively solve for the max-val of remaining string
                seen.remove(s[:i])                              # Remove the substring from the set

        return res                                              # Return the result counter

    seen = set([])                                              # Initialise a set to store all substrings
    return dfs(s)                                               # Return the result
