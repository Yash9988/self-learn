"""
386. Lexicographical Numbers [MEDIUM]

Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space.


Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]


Example 2:

Input: n = 2
Output: [1,2]


Constraints:
    -> 1 <= n <= 5 * 104


Concepts: Custom Sorting
"""
from functools import cmp_to_key


# My Solution
def lexicalOrder(n: int) -> list[int]:
    def compare(a: int, b: int) -> int:                             # Helper function for custom comparison
        return -1 if str(a) < str(b) else 1

    return sorted(list(range(1, n + 1)), key=cmp_to_key(compare))   # Return sorted list with custom function


# Optimised Solution
def lexicalOrder_op(n: int) -> list[int]:
    res, num = [], 1                                                # Initialise "result" list and counter

    for _ in range(n):                                              # Iterate through the entire range
        res.append(num)                                             # Append counter to the list
        if num * 10 <= n:                                           # Check if num * 10 within limit
            num *= 10                                               # Update the value of counter
        else:
            while num % 10 == 9 or num + 1 > n:                     # While counter less than limit or doesn't include 9
                num //= 10                                          # Divide the counter by 10
            num += 1                                                # Increment the counter

    return res                                                      # Return the resulting list
