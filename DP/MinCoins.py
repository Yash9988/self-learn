"""
Given a set of coins = {1, 4, 5} and a target sum, return the minimum #coins that forms the sum
"""
import timeit


# Top-Down Approach
def change(n, coins):
    if n == 0:
        return n

    if dp.get(n) is None:
        ans = float('inf')                          # Set answer to max-value

        for coin in coins:                          # Iterate through all coins available
            sub = n - coin                          # Obtain new "sub-problem"
            if sub < 0:                             # Skip if value goes below zero
                continue
            ans = min(ans, 1 + change(sub, coins))  # Replace answer with the minimum acquired so far

        dp[n] = ans                                 # Store the final answer in the DP
    return dp[n]


# Bottom-up Approach
def change1(n, coins):
    dp[0] = 0                       # Set the base-case value

    for i in range(1, n + 1):       # Iterate till n
        ans = float('inf')          # Set answer to max-value

        for coin in coins:          # Iterate through all coins available
            if i - coin < 0:        # Skip if value goes below zero
                continue

            sub = 1 + dp[i - coin]  # Add a step
            ans = min(sub, ans)     # Replace with min so far

        dp[i] = ans                 # Store the final answer in DP

    return dp[n]


dp = {}

# n_steps = 1000
# print(f"{timeit.timeit('change(30, [1, 4, 5])', number=n_steps, globals=globals()) / n_steps: .2g}s")   # ~2.1e-07 s
# print(f"{timeit.timeit('change1(30, [1, 4, 5])', number=n_steps, globals=globals()) / n_steps: .2g}s")  # ~1.9e-05 s
