"""
3133. Minimum Array End [MEDIUM]

You are given two integers n and x. You have to construct an array of positive integers nums of size n where for every
0 <= i < n - 1, nums[i + 1] is greater than nums[i], and the result of the bitwise AND operation between all elements of
nums is x.

Return the minimum possible value of nums[n - 1].


Example 1:
Input: n = 3, x = 4
Output: 6

Explanation: nums can be [4,5,6] and its last element is 6.


Example 2:
Input: n = 2, x = 7
Output: 15

Explanation: nums can be [7,15] and its last element is 15.


Constraints:

    -> 1 <= n, x <= 10^8


Concepts: Bit-Manipulation
"""


# My Approach (Incomplete)  TODO: Figure out the problem
def minEnd(n: int, x: int) -> int:
    skips = 1 << (len(bin(x)) - x.bit_count() - 2)
    shifts, extra = max(0, n // skips - 1), max(0, n % skips - 1)

    val = int('1' * shifts + bin(x)[2:], 2)
    return val + extra


# Optimised Solution
def minEnd_op(n: int, x: int) -> int:
    bx, bn = 1, 1                           # Initialise binary counters
    while bn < n:                           # While second pointer is < n
        if (bx & x) == 0:                   # Check if curr-bit in x is empty
            if bn & (n - 1):                # Check if curr-bit in (n - 1) is empty
                x += bx                     # Transfer bit-val from (n - 1) to x
            bn <<= 1                        # Shift the n-counter
        bx <<= 1                            # Shift the x-counter
    return x                                # Return the result


"""
Intuition: the smallest element equals x, and all elements look like x with some additional bits.

I think it's best to use an example. Let x be 100110 (38).

The elements, smallest to largest, will look like:

    100110
    100111
    101110
    101111
    110110
    .. and so on

As you see, we incrementing it from zero to n - 1, and interweave it around the existing bits in x.

What is the largest element? Let n be 37, so we need 36 additional elements.

36 in binary is 100100, and we need to interweave that into x without disturbing existing bits.

That is, we place bits from n - 1 into zero bits of x, going right-to-left:

10011`0` |   10`0`110 |   1`1`0110 |   `0`110110 |  `0`0110110  | `1`00110110
      ^         ^           ^           ^            ^             ^
10010`0` | 1001`0`0   | 100`1`00   | 10`0`100    | 1`0`0100     | `1`00100

So, the result is 310 (100110110).
"""
