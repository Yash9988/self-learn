"""
440. K-th Smallest in Lexicographical Order [HARD]

Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].


Example 1:

Input: n = 13, k = 2
Output: 10
Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9],
             so the second-smallest number is 10.


Example 2:

Input: n = 1, k = 1
Output: 1


Constraints:
    -> 1 <= k <= n <= 109


Concepts: Denary Tree
"""


def findKthNumber(n: int, k: int) -> int:
    def count_steps(prefix1, prefix2):                  # Helper method to count numbers between prefix1 and prefix2
        steps = 0                                       # Initialise counter
        while prefix1 <= n:                             # Check if prefix1 is smaller than the limit
            steps += min(n + 1, prefix2) - prefix1      # Increment steps with the difference between prefixes
            prefix1 *= 10                               # Increment the prefix1 by a level of 10
            prefix2 *= 10                               # Increment the prefix2 by a level of 10
        return steps                                    # Return the result

    curr = 1                                            # Initialise pointer
    k -= 1                                              # Decrement the index pointer

    while k > 0:                                        # While the pointer is non-zero
        step = count_steps(curr, curr + 1)              # Get the steps between consecutive numbers
        if step <= k:                                   # If the steps are <= k, we skip this prefix's subtree
            curr += 1                                   # Increment the pointer to next prefix
            k -= step                                   # Decrement the index-pointer by the number of steps skipped
        else:
            curr *= 10                                  # Increment the pointer by level of 10
            k -= 1                                      # Decrement the index-pointer

    return curr                                         # Return the pointer value
