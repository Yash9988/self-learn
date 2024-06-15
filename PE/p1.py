##
# https://projecteuler.net/problem=1

sum([i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0])  # 233168


##
# https://projecteuler.net/problem=2

def fib_sum(a=1, b=2, sum_=2):
    if (c := a + b) > 4e6:
        return sum_

    sum_ += c if c % 2 == 0 else 0

    return fib_sum(b, c, sum_)


print(fib_sum())  # 4613732

##
# https://projecteuler.net/problem=3

num, n = 600851475143, 2

while n ** 2 <= num:
    if num % n == 0:
        num //= n
    else:
        n += 1

print(num)
