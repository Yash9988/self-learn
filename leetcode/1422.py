"""
1422. Maximum Score After Splitting a String [EASY]

Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings
(i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right
substring.


Example 1:
Input: s = "011101"
Output: 5

Explanation:
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5
left = "01" and right = "1101", score = 1 + 3 = 4
left = "011" and right = "101", score = 1 + 2 = 3
left = "0111" and right = "01", score = 1 + 1 = 2
left = "01110" and right = "1", score = 2 + 1 = 3


Example 2:
Input: s = "00111"
Output: 5

Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5


Example 3:
Input: s = "1111"
Output: 3


Constraints:

    -> 2 <= s.length <= 500
    -> The string s consists of characters '0' and '1' only.


Concepts: Substring
"""


# My Solution
def maxScore(s: str) -> int:
    n, res = len(s), 0                                              # Obtain the string length
    for i in range(1, n):                                           # Iterate through the range: 1 to n
        l = r = 0                                                   # Counters to track left & right substring values
        for j in range(i):                                          # Iterate till i
            l += 1 if s[j] == '0' else 0                            # Increment counter if character is `0`

        for j in range(i, n):                                       # Iterate from i to n
            r += 1 if s[j] == '1' else 0                            # Increment counter if character is '1'

        res = max(res, l + r)                                       # Update the result with the max-val

    return res                                                      # Return the result


# Optimised Solution
def maxScore_op(s: str) -> int:
    z = o = 0                                                       # Counters to track char-freq
    max_ = float('-inf')                                            # Counter to track max-val for left substring

    for i, c in enumerate(s):                                       # Iterate through the string
        z += 1 if c == '0' else 0                                   # Increment counter if curr-char is `0`
        o += 1 if c == '1' else 0                                   # Increment counter if curr-char is `1`

        if i != len(s) - 1:                                         # Check if end of string isn't reached
            max_ = max(max_, z - o)                                 # Update the counter with the max-diff

    return max_ + o                                                 # Compute and return the result
