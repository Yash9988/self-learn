"""
1497. Check If Array Pairs Are Divisible by k [MEDIUM]

Given an array of integers arr of even length n and an integer k.

We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.

Return true If you can find a way to do that or false otherwise.


Example 1:

Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
Output: true

Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).


Example 2:

Input: arr = [1,2,3,4,5,6], k = 7
Output: true

Explanation: Pairs are (1,6),(2,5) and(3,4).


Example 3:

Input: arr = [1,2,3,4,5,6], k = 10
Output: false

Explanation: You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum
             divisible by 10.


Constraints:

    -> arr.length == n
    -> 1 <= n <= 105
    -> n is even.
    -> -109 <= arr[i] <= 109
    -> 1 <= k <= 105


Concepts: Double Pointers, Pairing
"""


# My Solution
def canArrange(arr: list[int], k: int) -> bool:
    counts = [0 for _ in range(k)]                              # Initialise a count-array of length k
    for a in arr:                                               # Iterate through the input array
        counts[a % k] += 1                                      # Increment the count at respective index

    if counts[0] % 2 or (k % 2 == 0 and counts[k // 2] % 2):    # Check if value at start or middle is odd
        return False                                            # Return False

    i, j = 1, k - 1                                             # Initialise 2 pointers at the start and end
    while i < j:                                                # While left pointer is less than the right pointer
        if counts[i] != counts[j]:                              # Check if the value at pointer indexes don't match
            return False                                        # Return False
        i, j = i + 1, j - 1                                     # Update the pointers in respective direction

    return True                                                 # Return True


# Alternate (Cleaner) Solution
def canArrange_alt(arr: list[int], k: int) -> bool:

    if sum(arr) % k != 0:                                       # Check if sum of all elements isn't divisible by k
        return False                                            # Return False

    remainder_count = [0] * k                                   # Initialise a count-array of length k
    for num in arr:                                             # Iterate through the input array
        remainder_count[num % k] += 1                           # Increment the count at respective index

    for i in range(1, (k // 2) + 1):                            # Iterate through half the count-array
        if remainder_count[i] != remainder_count[k - i]:        # Check if the value at either end of index don't match
            return False                                        # Return False

    return remainder_count[0] % 2 == 0                          # Check and return if the first element of count is even
