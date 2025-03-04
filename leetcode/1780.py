"""
1780. Check if Number is a Sum of Powers of Three [MEDIUM]

Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise,
return false.

An integer y is a power of three if there exists an integer x such that y == 3x.


Example 1:
Input: n = 12
Output: true

Explanation: 12 = 31 + 32


Example 2:
Input: n = 91
Output: true

Explanation: 91 = 30 + 32 + 34


Example 3:
Input: n = 21
Output: false


Constraints:

    1 <= n <= 10^7


Concepts: Mathematical Intuition


Link: https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/solutions/6492524/simple-math-python-c-java-c-js
"""


# Optimised Solution
def checkPowersOfThree(n: int) -> bool:
    while n > 0:                                                    # While the num is greater than zero
        if n % 3 == 2:                                              # Check if the mod remainder is two
            return False                                            # Return False

        n //= 3                                                     # Divide the num by 3

    return True                                                     # Return True
