"""
Find the #ways to reach the n-th stair when the required jumps are of length of 1 or 2
"""
import timeit


# Top-Down Approach
def jumps(n, arr):
    if not n:
        return 1                            # Return 1 if n is zero

    if dp.get(n) is None:                   # If not in DP
        dp[n] = 0                           # Initialise value with zero
        for i in arr:                       # Iterate through all step values
            if n - i < 0:                   # Ignore the negative sub-problems
                continue
            dp[n] += jumps(n - i, arr)      # Increment by all possible ways
    return dp[n]


# Bottom-Up Approach
def jumps1(n, arr):
    dp[0] = 1                               # Initialise base-case with 1

    for i in range(1, n + 1):               # Iterate through all values till n
        dp[i] = 0                           # Initialise each step with zero
        for j in arr:                       # Iterate through all step values
            if i - j < 0:                   # Ignore the negative sub-problems
                continue
            dp[i] += dp[i - j]              # Increment by all possible ways

    return dp[n]


dp = {}
# print(jumps(5, [1, 2]))
# print(jumps1(5, [1, 2]))

# n_steps = 1000
# print(f"{timeit.timeit('jumps(5, [1, 2])', number=n_steps, globals=globals()) / n_steps: .2g} s")    # ~2e-07 s
# print(f"{timeit.timeit('jumps1(5, [1, 2])', number=n_steps, globals=globals()) / n_steps: .2g} s")   # ~2.3e-06 s
