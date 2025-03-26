"""
1079. Letter Tile Possibilities [MEDIUM]

You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.


Example 1:
Input: tiles = "AAB"
Output: 8

Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".


Example 2:
Input: tiles = "AAABBC"
Output: 188


Example 3:
Input: tiles = "V"
Output: 1


Constraints:

    -> 1 <= tiles.length <= 7
    -> tiles consists of uppercase English letters.


Concepts: Backtracking, Substrings, Mathematical Intuition
"""
from math import factorial
from collections import Counter


# Optimised Solution
def numTilePossibilities(tiles: str) -> int:
    # Helper method to recursively backtrack and compute the valid permutations
    def backtrack(i):
        nonlocal ans                                                # Reference the global variable within local scope
        permutations = 1                                            # Counter to track the permutations
        for x in res:                                               # Iterate through the rem-list
            if x > 0:                                               # Check if the character has been used
                permutations *= factorial(x)                        # Update the perm-counter by the freq-factorial

        ans += factorial(sum(res)) // permutations                  # Increment the res-counter

        for j in range(i, len(remaining)):                          # Iterate through the remaining range
            if remaining[j] > 0:                                    # Check if char-freq is non-zero
                res[j] += 1                                         # Increment the used-freq for char
                remaining[j] -= 1                                   # Decrement the char-freq

                backtrack(j)                                        # Backtrack from the curr-idx

                res[j] -= 1                                         # Decrement the used-freq for char
                remaining[j] += 1                                   # Increment the char-freq

    remaining = list(Counter(tiles).values())                       # List of char-freq in the string
    res = [0] * len(remaining)                                      # List to track the used characters
    ans = 0                                                         # Counter to track the result

    backtrack(0)                                                    # Backtrack the string from index 0
    return ans - 1                                                  # Return the result

# Alternate Solution
def numTilePossibilities_alt(tiles: str) -> int:
    # Helper method to recursively backtrack and compute the valid permutations
    def rec(t, u):
        count = 0                                                   # Counter to track the non-empty seqs
        for i in range(n):                                          # Iterate through the string range

            # Check if idx-char is used or is duplicate and the prev-char is already accounted for
            if u[i] or (i > 0 and t[i] == t[i - 1] and not used[i - 1]):
                continue                                            # Skip to the next iteration

            u[i] = True                                             # Mark the curr-char as used
            count += 1 + rec(t, u)                                  # Rec-call with updated list and update the counter
            u[i] = False                                            # Mark the curr-char as not used

        return count                                                # Return the result

    n = len(tiles)                                                  # Compute the string size
    tiles = sorted(tiles)                                           # Sort the input string
    used = [False] * n                                              # List to track used characters

    return rec(tiles, used)                                         # Recursively call the method and return the result
