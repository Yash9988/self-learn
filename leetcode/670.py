"""
670. Maximum Swap [MEDIUM]

You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.


Example 1:

Input: num = 2736
Output: 7236

Explanation: Swap the number 2 and the number 7.


Example 2:

Input: num = 9973
Output: 9973

Explanation: No swap.


Constraints:

    -> 0 <= num <= 108


Concepts: Swapping, Pointers
"""


# Optimal Solution
def maximumSwap(num: int) -> int:
    A = list(map(int, str(num)))                            # Initialise a list of (string) digits
    last = {x: i for i, x in enumerate(A)}                  # Initialise a dict to store each digit's last occurrence

    for i, x in enumerate(A):                               # Iterate through the digits of the number
        for d in range(9, x, -1):                           # Iterate through all digits from 9 to 0
            if last.get(d, -1) > i:                         # Check if any larger digit has a higher index than current
                A[i], A[last[d]] = A[last[d]], A[i]         # Swap the digits at the respective indexes
                return int("".join(map(str, A)))            # Return the combined list of strings as a number

    return num                                              # Return the original number


# Alternate Solution
def maximumSwap_alt(num: int) -> int:
    n = len(str(num))                                       # Compute the digits in the number
    num = list(map(int, str(num)))                          # Initialise a list of string digits

    max_idx = n - 1                                         # Set the max index pointer at the last digit
    x = y = 0                                               # Initialise 2 pointers

    for i in range(n)[::-1]:                                # Iterate through the number digits in reverse
        if num[i] > num[max_idx]:                           # Check if digit at curr-idx is larger than max-idx digit
            max_idx = i                                     # Update the max-idx pointer
        elif num[i] < num[max_idx]:                         # Check if the digit is smaller, otherwise
            x, y = i, max_idx                               # Update the pointers at corresponding indexes

    num[x], num[y] = num[y], num[x]                         # Swap the elements at pointer-indexes

    return int(''.join(map(str, num)))                      # Return the result
