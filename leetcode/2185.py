"""
2185. Counting Words With a Given Prefix [EASY]

You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s.


Example 1:
Input: words = ["pay","attention","practice","attend"], pref = "at"
Output: 2

Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".


Example 2:
Input: words = ["leetcode","win","loops","success"], pref = "code"
Output: 0

Explanation: There are no strings that contain "code" as a prefix.


Constraints:

    -> 1 <= words.length <= 100
    -> 1 <= words[i].length, pref.length <= 100
    -> words[i] and pref consist of lowercase English letters.


Concepts: Prefix
"""


# My Solution
def prefixCount(words: list[str], pref: str) -> int:
    return sum(word.startswith(pref) for word in words)             # Check for prefix in words and return the sum
