"""
N friends can go to the birthday party. The methods are as follow:

    1. Go alone
    2. Go in a pair

Find the total #ways in which they can go to a party
"""


# Top-Down Approach
def nPairing(n: int) -> int:
    if n in {0, 1, 2}:                                      # Check for base cases
        return n

    dp[n] = nPairing(n - 1) + (n - 1) * nPairing(n - 2)     # Find result and store in a DP
            # Going alone   +   nCr ways of Pairing up
    return dp[n]                                            # Return the result


# Bottom-Up Approach
def nPairing_(n: int) -> int:

    # O(n) Space
    # a = [1, 2]
    # for i in range(3, n + 1):
    #     a.append(a[-1] + (i - 1) * a[-2])
    #
    # return a[-1]

    # O(1) Space
    if n in {1, 2}:                     # Base cases
        return n

    a, b = 1, 2
    i = 2                               # Initialise iterator
    while (i := i + 1) <= n:            # Increment and iterate to N
        a, b = b, b + (i - 1) * a       # Update for relevant indexes
    return b                            # Return the result


dp = {}
# print(nPairing(4))
# print(nPairing_(4))
