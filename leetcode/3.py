"""
3. Longest Substring Without Repeating Characters [MEDIUM]

Given a string s, find the length of the longest _substring_ without repeating characters.


Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.


Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.


Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

    -> 0 <= s.length <= 5 * 104
    -> s consists of English letters, digits, symbols and spaces.


Concepts: Double Pointers
"""


# My Solution
def lengthOfLongestSubstring(s: str) -> int:
    if s == "":                                 # Check if the string is empty
        return 0                                # Return length zero

    seen, res = set(), 0                        # Initialise a set and result-counter
    l = r = 0                                   # Initialise the pointer

    for r, c in enumerate(s):                   # Iterate through all characters in the input string
        if c in seen:                           # Check if current character has been seen before
            res = max(res, r - l)               # Compare and store the maximum length, so far
            while s[l] != c:                    # Until the repeated character is observed
                seen.remove(s[l])               # Remove the current character from substring at pointer index
                l += 1                          # Increment the pointer
            l += 1                              # Increment the pointer, once more
        else:
            seen.add(c)                         # Add the current character in the set

    return max(res, r - l + 1)                  # Compare and return the maximum result
