"""
7. Reverse Integer [MEDIUM]

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the
signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


Example 1:

Input: x = 123
Output: 321


Example 2:

Input: x = -123
Output: -321


Example 3:

Input: x = 120
Output: 21


Constraints:

    -> -231 <= x <= 231 - 1


Concepts: Explicit Type-Conversion
"""


# My Solution
def reverse(x: int) -> int:
    limit = 2 ** 31                                         # Assign the 32-bit integer limit
    res = -int(str(abs(x))[::-1]) if x < 0 \
        else int(str(x)[::-1])                              # Reverse the integer using integer <-> string conversion

    return res if -limit <= res <= limit - 1 else 0         # Return the result, based upon the limit range
