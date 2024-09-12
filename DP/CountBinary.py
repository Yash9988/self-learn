"""
Given a string length N, how many unique strings can be created using the digits 0 and 1,
without two consecutive 1s.

General pattern shows the trend f(n) = f(n - 1) + f(n - 2)
"""


# Top-Down Approach
def CountBinary(n: int) -> int:
    if n in {1, 2}:                                         # Check for base-cases
        return n + 1
    elif n not in dp:                                       # Check if value not in DP
        dp[n] = CountBinary(n - 1) + CountBinary(n - 2)     # Recursively obtain and store the solution

    return dp[n]                                            # Return the result


# Bottom-Up Approach
def CountBinary_(n: int) -> int:
    if n in {1, 2}:                                         # Check for base-cases
        return n + 1

    a, b = 2, 3                                             # Initialise base cases
    i = 2                                                   # Initialise iterator
    while (i := i + 1) <= n:                                # Iterate to N
        a, b = b, a + b                                     # Iteratively obtain solution

    return b                                                # Return the result


dp = {}
# print(CountBinary(4))
# print(CountBinary_(4))
