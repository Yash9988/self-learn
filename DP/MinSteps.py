"""
Find the minimum #steps required to reach 1 using only one of the three operations;
Divide by 2, Divide by 3 or Reduce by 1.
"""
import timeit


def reduce(n):
    if n == 1:
        return 0

    if dp.get(n, -1) == -1:

        s1 = s2 = float('inf')

        if n % 2 == 0:
            s1 = 1 + reduce(n / 2)
        if n % 3 == 0:
            s2 = 1 + reduce(n / 3)

        s3 = 1 + reduce(n - 1)

        dp[n] = min(s1, s2, s3)

    return dp[n]


def reduce_iter(n):
    dp[1], i = 0, 2

    while i <= n:
        dp[i] = 1 + min(dp[i - 1], dp[i / 2] if i % 2 == 0 else float('inf'), dp[i / 3] if i % 3 == 0 else float('inf'))
        i += 1
    return dp[n]


dp = {}

# n_steps = 1000
# print(f"{timeit.timeit('reduce(1000)', number=n_steps, globals=globals()) / n_steps: .2g}s")  # 1.2e-06 s
# print(f"{timeit.timeit('reduce_iter(1000)', number=n_steps, globals=globals()) / n_steps: .2g}s")  # 6.3e-04 s
