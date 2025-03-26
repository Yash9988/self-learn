"""
2337. Move Pieces to Obtain a String [MEDIUM]

You are given two strings start and target, both of length n. Each string consists only of the characters 'L', 'R', and
'_' where:

    - The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space
      directly to its left, and a piece 'R' can move to the right only if there is a blank space directly to its right.
    - The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.

Return true if it is possible to obtain the string target by moving the pieces of the string start any number of times.
Otherwise, return false.


Example 1:
Input: start = "_L__R__R_", target = "L______RR"
Output: true

Explanation: We can obtain the string target from start by doing the following moves:
- Move the first piece one step to the left, start becomes equal to "L___R__R_".
- Move the last piece one step to the right, start becomes equal to "L___R___R".
- Move the second piece three steps to the right, start becomes equal to "L______RR".
Since it is possible to get the string target from start, we return true.


Example 2:
Input: start = "R_L_", target = "__LR"
Output: false

Explanation: The 'R' piece in the string start can move one step to the right to obtain "_RL_".
After that, no pieces can move anymore, so it is impossible to obtain the string target from start.


Example 3:
Input: start = "_R", target = "R_"
Output: false

Explanation: The piece in the string start can move only to the right, so it is impossible to obtain the string target
from start.


Constraints:

    -> n == start.length == target.length
    -> 1 <= n <= 10^5
    -> start and target consist of the characters 'L', 'R', and '_'.


Concepts: Strings, Double Pointers
"""


# Optimised Solution
def canChange(s: str, t: str) -> bool:
    n = len(s)                                                      # Obtain string length
    s += '@'                                                        # Append `@` to the source string
    t += '@'                                                        # Append `@` to the target string
    i, j = 0, 0                                                     # Initialise 2 pointers

    while i < n or j < n:                                           # While either pointer is smaller than string length
        while i < n and s[i] == '_':                                # While the source string has black spaces in a row
            i += 1                                                  # Increment the first pointer

        while j < n and t[j] == '_':                                # While the target string has black spaces in a row
            j += 1                                                  # Increment the second pointer

        c = s[i]                                                    # Acquire the character at first pointer

        if c != t[j]:                                               # Check if character at both pointers don't match
            return False                                            # Return False

        if c == 'L' and i < j:                                      # Check if char is `L` and first pointer is smaller
            return False                                            # Return False

        if c == 'R' and i > j:                                      # Check if char is `R` and first pointer is greater
            return False                                            # Return False

        i += 1                                                      # Increment the first pointer
        j += 1                                                      # Increment the second pointer

    return True                                                     # Return True
