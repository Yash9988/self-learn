"""
2554. Maximum Number of Integers to Choose From a Range I [MEDIUM]

You are given an integer array banned and two integers n and maxSum. You are choosing some number of integers following
the below rules:

    - The chosen integers have to be in the range [1, n].
    - Each integer can be chosen at most once.
    - The chosen integers should not be in the array banned.
    - The sum of the chosen integers should not exceed maxSum.

Return the maximum number of integers you can choose following the mentioned rules.


Example 1:
Input: banned = [1,6,5], n = 5, maxSum = 6
Output: 2

Explanation: You can choose the integers 2 and 4.
2 and 4 are from the range [1, 5], both did not appear in banned, and their sum is 6, which did not exceed maxSum.


Example 2:
Input: banned = [1,2,3,4,5,6,7], n = 8, maxSum = 1
Output: 0

Explanation: You cannot choose any integer while following the mentioned conditions.


Example 3:
Input: banned = [11], n = 7, maxSum = 50
Output: 7

Explanation: You can choose the integers 1, 2, 3, 4, 5, 6, and 7.
They are from the range [1, 7], all did not appear in banned, and their sum is 28, which did not exceed maxSum.


Constraints:

    -> 1 <= banned.length <= 10^4
    -> 1 <= banned[i], n <= 10^4
    -> 1 <= maxSum <= 10^9


Concepts: Set
"""


# My Solution
def maxCount(banned: list[int], n: int, maxSum: int) -> int:
    banned = set(banned)                                            # Obtain a set of all banned integers
    res = 0                                                         # Initialise a result counter

    for i in range(1, n + 1):                                       # Iterate through the given range
        if i not in banned:                                         # Check if the curr-int is not banned from use
            if maxSum - i >= 0:                                     # Check if the diff b/w is non-negative
                maxSum -= i                                         # Decrement the maxSum by the curr-int value
                res += 1                                            # Increment the result counter
            else:
                break                                               # Break out of the loop, otherwise

    return res                                                      # Return the result
