"""
1718. Construct the Lexicographically Largest Valid Sequence [MEDIUM]

Given an integer n, find a sequence that satisfies all the following:

    - The integer 1 occurs once in the sequence.
    - Each integer between 2 and n occurs twice in the sequence.
    - For every integer i between 2 and n, the distance between the two occurrences of i is exactly i.

The distance between two numbers on the sequence, a[i] and a[j], is the absolute difference of their indices, |j - i|.

Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution.

A sequence a is lexicographically larger than a sequence b (of the same length) if in the first position where a and b
differ, sequence a has a number greater than the corresponding number in b. For example, [0,1,9,0] is lexicographically
larger than [0,1,5,6] because the first position they differ is at the third number, and 9 is greater than 5.


Example 1:
Input: n = 3
Output: [3,1,2,3,2]

Explanation: [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the lexicographically largest valid sequence.


Example 2:
Input: n = 5
Output: [5,3,1,4,3,5,2,4,2]


Constraints:

    -> 1 <= n <= 20


Concepts: Backtracking
"""

# Optimised Solution
def constructDistancedSequence(n: int) -> list[int]:
    # Helper method to backtrack through the sequence until a valid-seq is found
    def backtrack(i):
        if i == len_seq:                                            # Check if the sequence is completed
            return True                                             # Return True

        if seq[i]:                                                  # Check if the curr-idx is filled already
            return backtrack(i + 1)                                 # Recursively call the method with the next index

        # Iterate through the digits in reverse order for lexicographically largest seq
        for num in range(n, 0, -1):
            if num in used:                                         # Check if the digit has already been used
                continue                                            # Skip to the next iteration

            # Compute the next-idx in the sequence for the curr-digit (excluding 1)
            nxt = i + num if num > 1 else i

            if nxt >= len_seq or seq[nxt] != 0:                     # Check if the next-idx is invalid or already filled
                continue                                            # Skip to the next iteration

            seq[i] = seq[nxt] = num                                 # Update both seq-idx with the digit
            used.add(num)                                           # Append the digit to the used-set

            if backtrack(i + 1):                                    # Check if the recursive call returns a valid-seq
                return True                                         # Return True

            seq[i] = seq[nxt] = 0                                   # Reset both seq-idx
            used.remove(num)                                        # Remove the digit from used-set

        return False                                                # Return False (no digits lead to a valid-seq)

    len_seq = 2 * n - 1                                             # Compute res-len (1 occurs once, 2-n appear twice)
    seq = [0] * len_seq                                             # List to store the sequence
    used = set()                                                    # Set to track used-digits in sequence

    backtrack(0)                                                    # Begin backtracking at index 0
    return seq                                                      # Return the result