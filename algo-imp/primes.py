import timeit


# Naive: O(N^2)
def naive(n: int) -> list[int]:
    def isPrime(x: int) -> bool:
        for j in range(2, int(x ** 0.5) + 1):
            if not x % j:
                return False
        return True

    res = []
    for i in range(2, n):
        if isPrime(i):
            res.append(i)

    return res


# Sieve of Eratosthenes: O(N * log(log(N)))
def SoE(n: int) -> list[int]:
    sieve = [True] * (n + 1)
    for i in range(2, n + 1):
        if sieve[i]:
            for j in range(2 * i, n + 1, i):
                sieve[j] = False

    res = []
    for i in range(2, n + 1):
        if sieve[i]:
            res.append(i)

    return res


# Sieve of Sundaram: O(N * log(N))
def SoS(n: int) -> list[int]:
    newN = (n - 1) // 2
    sieve = [True] * (newN + 1)

    for i in range(1, newN):
        j = i
        while (k := i + j + 2 * i * j) <= newN:
            sieve[k] = False
            j += 1

    res = [2]

    for i in range(1, newN + 1):
        if sieve[i]:
            res.append(2 * i + 1)

    return res


# Sieve of Atkin: O(N)/O(limit)
def SoA(n: int) -> list[int]:
    sieve = [False] * (n + 1)
    sieve[2] = sieve[3] = True

    x = 1
    while x * x <= n:
        y = 1
        while y * y <= n:
            a = (4 * x * x) + (y * y)
            if a <= n and a % 12 in {1, 5}:
                sieve[a] ^= True

            b = (3 * x * x) + (y * y)
            if b <= n and b % 12 == 7:
                sieve[b] ^= True

            c = (3 * x * x) - (y * y)
            if c <= n and y < x and c % 12 == 11:
                sieve[c] ^= True

            y += 1
        x += 1

    for i in range(5, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i * i):
                sieve[j] = False

    res = []
    for i in range(2, n + 1):
        if sieve[i]:
            res.append(i)

    return res


# print(naive(1000)); print(SoE(1000)); print(SoS(1000)); print(SoA(1000))

# limit = 10000
# n_turns = 10000
#
# print(f"Naive: {timeit.timeit('naive(limit)', number=n_turns, globals=globals()) / n_turns: .2g} s")    # 0.0066s
# print(f"SoE: {timeit.timeit('SoE(limit)', number=n_turns, globals=globals()) / n_turns: .2g} s")        # 0.0017s
# print(f"SoS: {timeit.timeit('SoS(limit)', number=n_turns, globals=globals()) / n_turns: .2g} s")        # 0.0021s
# print(f"SoA: {timeit.timeit('SoA(limit)', number=n_turns, globals=globals()) / n_turns: .2g} s")        # 0.0049s
