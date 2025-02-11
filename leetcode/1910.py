"""
1910. Remove All Occurrences of a Substring [MEDIUM]

Given two strings s and part, perform the following operation on s until all occurrences of the substring part are
removed:

- Find the leftmost occurrence of the substring part and remove it from s.

Return s after removing all occurrences of part.

A substring is a contiguous sequence of characters in a string.


Example 1:
Input: s = "daabcbaabcbc", part = "abc"
Output: "dab"

Explanation: The following operations are done:
- s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
- s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".
- s = "dababc", remove "abc" starting at index 3, so s = "dab".
Now s has no occurrences of "abc".


Example 2:
Input: s = "axxxxyyyyb", part = "xy"
Output: "ab"

Explanation: The following operations are done:
- s = "axxxxyyyyb", remove "xy" starting at index 4 so s = "axxxyyyb".
- s = "axxxyyyb", remove "xy" starting at index 3 so s = "axxyyb".
- s = "axxyyb", remove "xy" starting at index 2 so s = "axyb".
- s = "axyb", remove "xy" starting at index 1 so s = "ab".
Now s has no occurrences of "xy".


Constraints:

    -> 1 <= s.length <= 1000
    -> 1 <= part.length <= 1000
    -> s and part consists of lowercase English letters.


Concepts: Substrings, Postfix
"""


# Optimised Solution
def removeOccurrences(s: str, part: str) -> str:
    while part in s:                                                # While the sub-string is present in the string
        s = s.replace(part, "", 1)                                  # Remove the substring, once

    return s                                                        # Return the result


# Alternate Solution
def removeOccurrences_alt(s: str, part: str) -> str:
    res = ''                                                        # String to store the result
    i, m = 0, len(part)                                             # Obtain the substring length and set a pointer

    for ch in s:                                                    # Iterate through the string
        res += ch                                                   # Append curr-char to the res-str
        i += 1                                                      # Increment the pointer

        if i >= m and res.endswith(part):                           # Check if the res-str ends with the sub-string
            i -= m                                                  # Decrement the pointer by substring length
            res = res[:i]                                           # Slice the res-str till the pointer

    return res                                                      # Return the result
