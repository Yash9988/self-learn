"""
2429. Minimize XOR [MEDIUM]

Given two positive integers num1 and num2, find the positive integer x such that:

    - x has the same number of set bits as num2, and
    - The value x XOR num1 is minimal.

Note that XOR is the bitwise XOR operation.

Return the integer x. The test cases are generated such that x is uniquely determined.

The number of set bits of an integer is the number of 1's in its binary representation.


Example 1:
Input: num1 = 3, num2 = 5
Output: 3

Explanation:
The binary representations of num1 and num2 are 0011 and 0101, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 3 = 0 is minimal.


Example 2:
Input: num1 = 1, num2 = 12
Output: 3

Explanation:
The binary representations of num1 and num2 are 0001 and 1100, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 1 = 2 is minimal.


Constraints:

    -> 1 <= num1, num2 <= 10^9


Concepts: Bit Manipulation
"""


# My Solution
def minimizeXor(num1: int, num2: int) -> int:

    need = num2.bit_count() - num1.bit_count()                      # Compute the bit-difference

    if not need:                                                    # Check if the diff is zero
        return num1                                                 # Return num1 as result, as is

    res = list(bin(num1)[2:])                                       # List to store binary-repr for num1
    n = len(res)                                                    # Obtain the list size

    for i in range(n)[::-1]:                                        # Iterate through the list range, in reverse
        # Check if we need to add more bits and the curr-bit is unset
        if need > 0 and res[i] == '0':
            res[i] = '1'                                            # Set the curr-bit
            need -= 1                                               # Decrement the counter
        # Check if we need to reduce bits and the curr-bit is set
        elif need < 0 and res[i] == '1':
            res[i] = '0'                                            # Unset the curr-bit
            need += 1                                               # Increment the counter

    if need:                                                        # Check if we still need to add more bits
        res = ['1'] * need + res                                    # Append the result with a list of remaining bits

    return int(''.join(res), 2)                                     # Return the result


# Alternate Solution
def minimizeXor_alt(num1: int, num2: int) -> int:

    need = num2.bit_count() - num1.bit_count()                      # Compute the bit-difference

    if not need:                                                    # Check if the diff is zero
        return num1                                                 # Return num1 as result, as is

    curr = 1                                                        # Initialise bit-pointer

    while need:                                                     # While the required bits are non-zero
        # Check if we need to add more bits and the curr-bit is unset
        if need > 0 and not num1 & curr:
            num1 |= curr                                            # Set the curr-but
            need -= 1                                               # Decrement the counter
        # Check if we need to reduce bits and the curr-bit is set
        elif need < 0 and num1 & curr:
            num1 ^= curr                                            # Unset the curr-bit
            need += 1                                               # Increment the counter

        curr <<= 1                                                  # Shift the pointer to the left by one-bit

    return num1                                                     # Return the result

