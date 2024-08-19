##
import timeit
from collections import defaultdict

# Sloppy ol' recursion. Too repetitive
def fib(n):
    if n == 0 or n == 1:
        return n

    return fib(n - 1) + fib(n - 2)


# Chad DP. Extremely Efficient
def fib_op(n):
    if n == 0 or n == 1:
        return n
    elif dp[n] == -1:
        dp[n] = fib_op(n - 1) + fib_op(n - 2)

    return dp[n]


dp = defaultdict(lambda: -1)

# print(fib(40))  # ~35.64s
# print(fib_op(40))  # ~0.0s

print(f'{timeit.timeit("fib(20)", number=100, globals=globals()) / 100: .5g}s')
print(f'{timeit.timeit("fib_op(20)", number=100, globals=globals()) / 100: .5g}s')
