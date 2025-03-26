"""
3174. Clear Digits [EASY]

You are given a string s.

Your task is to remove all digits by doing this operation repeatedly:

    - Delete the first digit and the closest non-digit character to its left.

Return the resulting string after removing all digits.


Example 1:
Input: s = "abc"
Output: "abc"

Explanation:
There is no digit in the string.


Example 2:
Input: s = "cb34"
Output: ""

Explanation:
First, we apply the operation on s[2], and s becomes "c4".

Then we apply the operation on s[1], and s becomes "".


Constraints:

    -> 1 <= s.length <= 100
    -> s consists only of lowercase English letters and digits.
    -> The input is generated such that it is possible to delete all digits.


Concepts: Stack
"""


# My Solution (Optimised)
def clearDigits(s: str) -> str:
    res = []                                                        # List to store the filtered characters
    for ch in s:                                                    # Iterate through the characters
        if ch.isalpha():                                            # Check if curr-char is an alphabet
            res.append(ch)                                          # Append the char to the list
        else:
            res.pop()                                               # Pop out last-char from the list, otherwise

    return ''.join(res)                                             # Join the filtered-chars and return the result
