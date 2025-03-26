"""
2696. Minimum String Length After Removing Substrings [EASY]

You are given a string s consisting only of uppercase English letters.

You can apply some operations to this string where, in one operation, you can remove any occurrence of one of the
substrings "AB" or "CD" from s.

Return the minimum possible length of the resulting string that you can obtain.

Note that the string concatenates after removing the substring and could produce new "AB" or "CD" substrings.


Example 1:

Input: s = "ABFCACDB"
Output: 2

Explanation: We can do the following operations:
- Remove the substring "ABFCACDB", so s = "FCACDB".
- Remove the substring "FCACDB", so s = "FCAB".
- Remove the substring "FCAB", so s = "FC".
So the resulting length of the string is 2.
It can be shown that it is the minimum length that we can obtain.


Example 2:

Input: s = "ACBBD"
Output: 5

Explanation: We cannot do any operations on the string so the length remains the same.


Constraints:

    -> 1 <= s.length <= 100
    -> s consists only of uppercase English letters.


Concepts: Deque/Stack, Substrings
"""
from collections import deque


# My Solution
def minLength(s: str) -> int:
        dq = deque()                                        # Initialise a stack DS
        for ch in s:                                        # Iterate through the string characters
            if dq and dq[-1] == 'A' and ch == 'B':          # Check for substring 'AB'
                dq.pop()                                    # Pop the last element ('A') from the stack
                continue                                    # Skip to next character

            if dq and dq[-1] == 'C' and ch == 'D':          # Check for substring 'CD'
                dq.pop()                                    # Pop the last element ('C') from the stack
                continue                                    # Skip to next character

            dq.append(ch)                                   # Add the current character to stack

        return len(dq)                                      # Return the length of the remaining string


# Optimised Solution
def minLength_op(s: str) -> int:
    while ('AB' in s) or ('CD' in s):                       # While substring 'AB' and 'CD' present in string
        if 'AB' in s:                                       # Check for substring 'AB'
            s = s.replace('AB', '')                         # Replace the substring with empty space
        if 'CD' in s:                                       # Check for substring 'CD'
            s = s.replace('CD', '')                         # Replace the substring with empty space

    return len(s)                                           # Return the length of the remaining string
