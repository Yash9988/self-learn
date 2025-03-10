"""
2379. Minimum Recolors to Get K Consecutive Black Blocks [EASY]

You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the
i-th block. The characters 'W' and 'B' denote the colors white and black, respectively.

You are also given an integer k, which is the desired number of consecutive black blocks.

In one operation, you can recolor a white block such that it becomes a black block.

Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.


Example 1:
Input: blocks = "WBBWWBBWBW", k = 7
Output: 3

Explanation:
One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
so that blocks = "BBBBBBBWBW".
It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
Therefore, we return 3.


Example 2:
Input: blocks = "WBWBBBW", k = 2
Output: 0

Explanation:
No changes need to be made, since 2 consecutive black blocks already exist.
Therefore, we return 0.


Constraints:

    -> n == blocks.length
    -> 1 <= n <= 100
    -> blocks[i] is either 'W' or 'B'.
    -> 1 <= k <= n


Concepts: Sliding Window
"""


# Optimised Solution
def minimumRecolors(blocks: str, k: int) -> int:
    c = 0                                                           # Counter to track count of white within curr-window
    for i in range(k):                                              # Iterate through the window range
        if blocks[i] == 'W':                                        # Check if the curr-block is white
            c += 1                                                  # Increment the counter

    a, l = c, 0                                                     # Counter & pointer to track result and window-start
    for i in range(k, len(blocks)):                                 # Iterate through the blocks outside the window
        if blocks[l] == 'W':                                        # Check if the block at pointer is white
            c -= 1                                                  # Decrement the counter

        l += 1                                                      # Increment the pointer
        if blocks[i] == 'W':                                        # Check if block at curr-idx is white
            c += 1                                                  # Increment the counter

        a = min(a, c)                                               # Update the counter with min-val

    return a                                                        # Return the result


# Alternate Solution
def minimumRecolors_alt(blocks: str, k: int) -> int:
    black_count = 0                                                 # Counter to track black blocks
    ans = float("inf")                                              # Counter to track the result

    for i in range(len(blocks)):                                    # Iterate through the blocks
        if i - k >= 0 and blocks[i - k] == 'B':                     # Check if block is black and idx is outside window
            black_count -= 1                                        # Decrement the counter

        if blocks[i] == 'B':                                        # Check if the curr-block is black
            black_count += 1                                        # Increment the counter

        ans = min(ans, k - black_count)                             # Update the result with min-val

    return ans                                                      # Return the result
