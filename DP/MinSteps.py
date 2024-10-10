"""
Find the minimum #steps required to reach 1 using only one of the three operations;
Divide by 2, Divide by 3 or Reduce by 1.
"""
import timeit


# Top-Down approach (Recursive)
def reduce(n):
    if n == 1:
        return 0

    if dp.get(n, -1) == -1:

        s1 = 1 + reduce(n / 2) if n % 2 == 0 else float('inf')  # Divide by 2
        s2 = 1 + reduce(n / 3) if n % 3 == 0 else float('inf')  # Divide by 3
        s3 = 1 + reduce(n - 1)                                  # Reduce by 1

        dp[n] = min(s1, s2, s3)                                 # Find min

    return dp[n]


# Bottom-Up approach (Iterative)
def reduce_iter(n):
    dp[1], i = 0, 2

    while i <= n:
        s1 = dp[i / 2] if i % 2 == 0 else float('inf')  # Divide by 2
        s2 = dp[i / 3] if i % 3 == 0 else float('inf')  # Divide by 3
        s3 = dp[i - 1]                                  # Reduce by 1

        dp[i] = 1 + min(s1, s2, s3)                     # Find min

        i += 1
    return dp[n]


dp = {}

# n_steps = 1000
# print(f"{timeit.timeit('reduce(1000)', number=n_steps, globals=globals()) / n_steps: .2g}s")  # 1.2e-06 s
# print(f"{timeit.timeit('reduce_iter(1000)', number=n_steps, globals=globals()) / n_steps: .2g}s")  # 6.3e-04 s
