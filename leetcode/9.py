"""
9. Palindrome Number [EASY]

Given an integer x, return true if x is a _palindrome_, and false otherwise.


Example 1:

Input: x = 121
Output: true

Explanation: 121 reads as 121 from left to right and from right to left.


Example 2:

Input: x = -121
Output: false

Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.


Example 3:

Input: x = 10
Output: false

Explanation: Reads 01 from right to left. Therefore, it is not a palindrome.


Constraints:

    -> -231 <= x <= 231 - 1


Concepts: Integer Operations


Follow up: Could you solve it without converting the integer to a string?
"""


# My Solution
def isPalindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]           # Convert integer to string and compare with its reverse


# Alternate Solution (without converting to string)
def isPalindrome_alt(x: int) -> bool:
    if x < 0:                               # Check if integer is negative
        return False                        # Return False

    o, r = x, 0                             # Copy the original integer value and initialise a counter
    while x:                                # While input-integer is non-zero
        r = r * 10 + x % 10                 # Sum the remainder of the input into the counter
        x //= 10                            # Reduce the input-integer by 10 folds

    return o == r                           # Compare the final value with original input and return the result
