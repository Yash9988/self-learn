"""
866. Prime Palindrome [MEDIUM]

Given an integer n, return the smallest prime palindrome greater than or equal to n.

An integer is prime if it has exactly two divisors: 1 and itself. Note that 1 is not a prime number.

    For example, 2, 3, 5, 7, 11, and 13 are all primes.

An integer is a palindrome if it reads the same from left to right as it does from right to left.

    For example, 101 and 12321 are palindromes.

The test cases are generated so that the answer always exists and is in the range [2, 2 * 108].


Example 1:
Input: n = 6
Output: 7

Example 2:
Input: n = 8
Output: 11

Example 3:
Input: n = 13
Output: 101


Constraints:    1 <= n <= 108
"""


class Solution:
    def primePalindrome(self, n: int) -> int:
        if 8 <= n <= 11:                                        # Only prime for even palindromes
            return 11

        for i in range(10 ** (len(str(n)) // 2), 10 ** 5):      # Iterate from the closest power of 10 to 99999
            j = int(str(i) + str(i)[-2::-1])                    # Create and only check (odd) palindromes
            if j >= n and self.isPrime(j):                      # If greater than or equal to n AND prime
                return j

    def isPrime(self, n: int) -> bool:
        if n < 2 or n % 2 == 0:                                 # Check for 1 and (accidental) evens
            return n == 2                                       # True if 2, False otherwise
        for i in range(3, int(n ** 0.5) + 1, 2):                # Iterate explicitly over odds
            if n % i == 0:
                return False
        return True


"""
-> Intuition

Write some example, you find all even length palindromes are divisible by 11.
So we need to search only palindrome with odd length.

We can prove as follow:
11 % 11 = 0
1111 % 11 = 0
111111 % 11 = 0
11111111 % 11 = 0

So:
1001 % 11 = (1111 - 11 * 10) % 11 = 0
100001 % 11 = (111111 - 1111 * 10) % 11 = 0
10000001 % 11 = (11111111 - 111111 * 10) % 11 = 0

For any palindrome with even length:
abcddcba % 11
= (a * 10000001 + b * 100001 * 10 + c * 1001 * 100 + d * 11 * 1000) % 11
= 0

All palindrome with even length is multiple of 11.
So among them, 11 is the only one prime
if (8 <= N <= 11) return 11

For other cases, we consider only palindrome with odd dights.

-> More Generally

A number is divisible by 11 if sum(even digits) - sum(odd digits) is divisible by 11.
Base case: 0
Inductive step:
If there is no carry when we add 11 to a number, both sums +1.
Whenever carry happens, one sum -10 and the other +1.
The invariant holds in both cases.

-> Time Complexity

O(10000) to check all numbers 1 - 10000.
isPrime function is O(sqrt(x)) in worst case.
But only sqrt(N) worst cases for 1 <= x <= N
In general it's O(logx)
"""