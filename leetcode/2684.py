"""
2684. Maximum Number of Moves in a Grid [Medium]

You are given a 0-indexed m x n matrix grid consisting of positive integers.

You can start at any cell in the first column of the matrix, and traverse the grid in the following way:

    - From a cell (row, col), you can move to any of the cells: (row - 1, col + 1), (row, col + 1) and (row + 1, col + 1)
      such that the value of the cell you move to, should be strictly bigger than the value of the current cell.

Return the maximum number of moves that you can perform.


Example 1:
Input: grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
Output: 3

Explanation: We can start at the cell (0, 0) and make the following moves:
- (0, 0) -> (0, 1).
- (0, 1) -> (1, 2).
- (1, 2) -> (2, 3).
It can be shown that it is the maximum number of moves that can be made.


Example 2:
Input: grid = [[3,2,4],[2,1,9],[1,1,7]]
Output: 0

Explanation: Starting from any cell in the first column we cannot perform any moves.


Constraints:

    -> m == grid.length
    -> n == grid[i].length
    -> 2 <= m, n <= 1000
    -> 4 <= m * n <= 10^5
    -> 1 <= grid[i][j] <= 10^6


Concepts: DP
"""
from functools import cache


# Optimised Solution
def maxMoves(grid: list[list[int]]) -> int:
    # Helper method to traverse through a sub-grid
    @cache
    def dp(i, j):
        ans = 0                                                         # Initialise a result counter
        for x, y in dirs:                                               # Iterate through the valid moves
            ni, nj = i + x, j + y                                       # Compute the reference point from curr-pos
            if 0 <= ni < m and nj < n and grid[i][j] < grid[ni][nj]:    # Check for the validity conditions
                ans = max(ans, 1 + dp(ni, nj))                          # Update the counter with the max-val
        return ans                                                      # Return the result

    m, n, dirs = len(grid), len(grid[0]), [(0, 1), (1, 1), (-1, 1)]     # Initialise the dimensions and valid move-set

    return max(dp(i, 0) for i in range(m))                              # Iterate through all rows in the first column


# Alternate Solution
def maxMoves_alt(grid: list[list[int]]) -> int:
    dp = [[0] * len(grid[0]) for _ in range(len(grid))]                 # Initialise a DP grid
    res, n = 0, len(grid)                                               # Initialise result counter and grid size

    for i in range(n):                                                  # Iterate through the rows
        for j in range(1, len(grid[0])):                                # Iterate through the cols, starting at index 1
            for k in range(-1, 2):                                      # Iterate through the valid directions
                if -1 < i - k < n and grid[i - k][j - 1] < grid[i][j]:  # Check for the validity conditions
                    if j > 1 and not dp[i - k][j - 1]:                  # Check if prev-col value is zero
                        continue                                        # Skip this iteration
                    dp[i][j] = max(dp[i][j], dp[i - k][j - 1] + 1)      # Update the DP at position with max-val
                    res = max(res, dp[i][j])                            # Update the result counter with max-val

    return res                                                          # Return the result
