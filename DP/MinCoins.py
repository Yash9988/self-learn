"""
Given a set of coins = {1, 4, 5} and a target sum, return the minimum #coins that forms the sum
"""


# Top-Down Approach
def change(n):
    if n == 0:
        return n

    if dp.get(n, -1) == -1:
        s1 = 1 + change(n - 5) if n - 5 >= 0 else float('inf')  # Reduce by 5
        s2 = 1 + change(n - 4) if n - 4 >= 0 else float('inf')  # Reduce by 4
        s3 = 1 + change(n - 1) if n - 1 >= 0 else float('inf')  # Reduce by 1

        dp[n] = min(s1, s2, s3)                                 # Find min

    return dp[n]


# Bottom-up Approach
def change1(n):
    dp[0] = 0

    for i in range(1, n + 1):
        s1 = dp[i - 5] if i - 5 >= 0 else float('inf')  # Reduce by 5
        s2 = dp[i - 4] if i - 5 >= 0 else float('inf')  # Reduce by 4
        s3 = dp[i - 1] if i - 5 >= 0 else float('inf')  # Reduce by 1

        dp[i] = 1 + min(s1, s2, s3)                     # Find min

    return dp[n]


dp = {}
print(change(150))
print(change1(1500))