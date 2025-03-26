"""
1963. Minimum Number of Swaps to Make the String Balanced [MEDIUM]

You are given a 0-indexed string s of even length n. The string consists of exactly n / 2 opening brackets '[' and n / 2
closing brackets ']'.

A string is called balanced if and only if:

    - It is the empty string, or
    - It can be written as AB, where both A and B are balanced strings, or
    - It can be written as [C], where C is a balanced string.

You may swap the brackets at any two indices any number of times.

Return the minimum number of swaps to make s balanced.


Example 1:

Input: s = "][]["
Output: 1

Explanation: You can make the string balanced by swapping index 0 with index 3.
The resulting string is "[[]]".


Example 2:

Input: s = "]]][[["
Output: 2

Explanation: You can do the following to make the string balanced:
- Swap index 0 with index 4. s = "[]][][".
- Swap index 1 with index 5. s = "[[][]]".
The resulting string is "[[][]]".

Example 3:

Input: s = "[]"
Output: 0

Explanation: The string is already balanced.


Constraints:

    -> n == s.length
    -> 2 <= n <= 106
    -> n is even.
    -> s[i] is either '[' or ']'.
    -> The number of opening brackets '[' equals n / 2, and the number of closing brackets ']' equals n / 2.


Concepts: Matching, Single Pointer
"""


# My Solution
def minSwaps(s: str) -> int:
    dq = []                                                 # Initialise a list
    for ch in s:                                            # Iterate through string characters
        if dq and dq[-1] + ch == "[]":                      # Check for the substring '[]'
            dq.pop()                                        # Pop out the last element of the list
            continue                                        # Skip to the next iteration
        dq.append(ch)                                       # Add the character to the list

    n = len(dq) // 2                                        # Compute the length of the list

    return (n + 1) // 2 if n % 2 else n // 2                # Compute and return the result


# Optimised Solution
def minSwaps_op(s: str) -> int:
    unmatched = 0                                           # Initialise counter to track unmatched brackets
    for c in s:                                             # Iterate through all string characters
        if c == '[':                                        # Check if the curr-char is a '['
            unmatched += 1                                  # Increment the counter
        elif unmatched > 0:                                 # Check if the curr-char is a ']'
            unmatched -= 1                                  # Decrement the counter, since we found a match

    return (unmatched + 1) // 2                             # Compute and return the result
