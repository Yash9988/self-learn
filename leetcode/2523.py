"""
2523. Closest Prime Numbers in Range [MEDIUM]

Given two positive integers left and right, find the two integers num1 and num2 such that:

    - left <= num1 < num2 <= right.
    - Both num1 and num2 are prime numbers.
    - `num2 - num1` is the minimum amongst all other pairs satisfying the above conditions.

Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return
the one with the smallest num1 value. If no such numbers exist, return [-1, -1].


Example 1:
Input: left = 10, right = 19
Output: [11,13]

Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.


Example 2:
Input: left = 4, right = 6
Output: [-1,-1]

Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.


Constraints:

    1 <= left <= right <= 10^6


Concepts: Sieve of Atkins
"""


# My Solution
def closestPrimes(left: int, right: int) -> list[int]:
    # Helper method to obtain the primes numbers between a given range
    def getPrimes():
        atkins = [True] * (right + 1)                               # List to track prime number candidates
        primes = []                                                 # List to store the prime numbers within range

        for i in range(2, right + 1):                               # Iterate through the candidate range
            if atkins[i]:                                           # Check if curr-ele is a prime candidate
                # Mark all the curr-ele's multiples as non-candidates
                for j in range(2 * i, right + 1, i):
                    atkins[j] = False

        for i in range(2, right + 1):                               # Iterate through the candidate range
            if atkins[i] and i >= left:                             # Check if curr-ele is a candidate and within range
                primes.append(i)                                    # Append the element to the list

        return primes                                               # Return the list of primes

    res = [-1, -1]                                                  # List to store the result
    min_diff = float('inf')                                         # Counter to track min-diff
    primes = getPrimes()                                            # Obtain the list of primes within desired range

    for i, j in zip(primes, primes[1:]):                            # Iterate through the prime pairs
        if j - i < min_diff:                                        # Check if the pair-diff is smaller than counter
            res = [i, j]                                            # Update the result list
            min_diff = j - i                                        # Update the counter with min-val

    return res                                                      # Return the result


# Optimised Solution
def closestPrimes_op(left: int, right: int) -> list[int]:
    sieve = [True] * (right + 1)                                    # List to track prime number candidates
    sieve[0] = sieve[1] = False                                     # Unmark the invalid candidates

    for i in range(2, int(right ** 0.5) + 1):                       # Iterate through the candidate range
        if sieve[i]:                                                # Check if the curr-ele is a valid candidate
            # Mark all the curr-ele's multiples as non-candidates
            for j in range(i * i, right + 1, i):
                sieve[j] = False

    primes = [i for i in range(left, right + 1) if sieve[i]]        # Obtain the list of primes within desired range

    if len(primes) < 2:                                             # Check if there are less than 2 primes in the list
        return [-1, -1]                                             # Return the result

    min_gap = float('inf')                                          # Counter to track min-diff
    result = [-1, -1]                                               # List to store the result

    for i in range(1, len(primes)):                                 # Iterate through the primes
        gap = primes[i] - primes[i - 1]                             # Compute the diff b/w prev and curr prime
        if gap < min_gap:                                           # Check if the diff is smaller than counter
            min_gap = gap                                           # Update the counter with min-val
            result = [primes[i - 1], primes[i]]                     # Update the result with the prime pair

    return result                                                   # Return the result
