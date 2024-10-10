##
import timeit
from collections import defaultdict


# Sloppy ol' recursion. Too repetitive
def fib(n):
    if n == 0 or n == 1:
        return n

    return fib(n - 1) + fib(n - 2)


# Chad DP (with memoization). Time efficient
def fib_op(n):
    if n == 0 or n == 1:
        return n
    elif dp.get(n, -1) == -1:
        dp[n] = fib_op(n - 1) + fib_op(n - 2)

    return dp[n]


# Chad iterative DP. Space & Time Efficient
def fib_op2(n):
    a, b = 0, 1
    i = 1

    while i < n:
        a, b = b, a + b
        i += 1

    return b


dp = {}

# timeit python fib.py
# print(fib(40))  # ~35.64s
# print(fib_op(40))  # ~0.0s
# print(fib_op2(40))  # ~0.0s

# n = 100
# print(f'{timeit.timeit("fib(20)", number=n, globals=globals()) / n: .5g}s')
# print(f'{timeit.timeit("fib_op(20)", number=n, globals=globals()) / n: .5g}s')
