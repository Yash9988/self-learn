"""
2601. Prime Subtraction Operation [MEDIUM]

You are given a 0-indexed integer array nums of length n.

You can perform the following operation as many times as you want:

    - Pick an index i that you haven’t picked before, and pick a prime p strictly less than nums[i], then subtract p
      from nums[i].

Return true if you can make nums a strictly increasing array using the above operation and false otherwise.

A strictly increasing array is an array whose each element is strictly greater than its preceding element.


Example 1:
Input: nums = [4,9,6,10]
Output: true

Explanation: In the first operation: Pick i = 0 and p = 3, and then subtract 3 from nums[0], so that nums becomes [1,9,6,10].
In the second operation: i = 1, p = 7, subtract 7 from nums[1], so nums becomes equal to [1,2,6,10].
After the second operation, nums is sorted in strictly increasing order, so the answer is true.


Example 2:
Input: nums = [6,8,11,12]
Output: true

Explanation: Initially nums is sorted in strictly increasing order, so we don't need to make any operations.


Example 3:
Input: nums = [5,8,3]
Output: false

Explanation: It can be proven that there is no way to perform operations to make nums sorted in strictly increasing
order, so the answer is false.


Constraints:

    -> 1 <= nums.length <= 1000
    -> 1 <= nums[i] <= 1000
    -> nums.length == n


Concepts: Greedy Sieve of Eratosthenes/Atkin
"""
from math import sqrt
from bisect import bisect_left


# Sieve of Atkin
def primeSubOperation_op(nums: list[int]) -> bool:
    max_element = max(nums)                                         # Compute the maximum value in the list

    sieve = [1] * (max_element + 1)                                 # Initialise and store the sieve array.
    sieve[1] = 0                                                    # Initialise the base case

    for i in range(2, int(sqrt(max_element + 1)) + 1):              # Iterate through the range of primes for max-val
        if sieve[i] == 1:                                           # Check if sieve-val at curr-idx is 1
            for j in range(i * i, max_element + 1, i):              # Iterate from square of curr-idx till max-val
                sieve[j] = 0                                        # Update the sieve-vals to 0

    curr_value = 1                                                  # Initialise a counter
    i = 0                                                           # Initialise a pointer

    while i < len(nums):                                            # While pointer is smaller than list size
        difference = nums[i] - curr_value                           # Compute the diff b/w nums[i] and counter value

        if difference < 0:                                          # Check if the diff is less than 0
            return False                                            # Return False

        if sieve[difference] or difference == 0:                    # Check if the diff is prime or zero
            i += 1                                                  # Increment the pointer
            curr_value += 1                                         # Increment the counter
        else:
            curr_value += 1                                         # Increment the counter, otherwise

    return True                                                     # Return True


# Greedy Sieve of Eratosthenes
def primeSubOperation_alt(nums: list[int]) -> bool:
    valid = [True] * 1001                                           # Initialise a list
    valid[0] = valid[1] = False                                     # Initialise base conditions

    for i in range(2, len(valid)):                                  # Iterate through the list
        if valid[i]:                                                # Check if the curr-val is True
            for j in range(i * i, len(valid), i):                   # Iterate from curr-idx till the end
                valid[j] = False                                    # Update the value at idx

    primes = [i for i in range(len(valid)) if valid[i]]             # Initialise a list of primes
    prev = 0                                                        # Initialise a counter

    for num in nums:                                                # Iterate through nums
        if num <= prev:                                             # Check if curr-val is smaller than counter value
            return False                                            # Return False

        if i := bisect_left(primes, num - prev):                    # Check if the diff is prime
            num -= primes[i - 1]                                    # Decrement the curr-val

        prev = num                                                  # Update the counter

    return True                                                     # Return True
