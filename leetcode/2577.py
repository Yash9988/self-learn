"""
2577. Minimum Time to Visit a Cell In a Grid [HARD]

You are given a m x n matrix grid consisting of non-negative integers where grid[row][col] represents the minimum time
required to be able to visit the cell (row, col), which means you can visit the cell (row, col) only when the time you
visit it is greater than or equal to grid[row][col].

You are standing in the top-left cell of the matrix in the 0th second, and you must move to any adjacent cell in the
four directions: up, down, left, and right. Each move you make takes 1 second.

Return the minimum time required in which you can visit the bottom-right cell of the matrix. If you cannot visit the
bottom-right cell, then return -1.


Example 1:
Input: grid = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]
Output: 7

Explanation: One of the paths that we can take is the following:
- at t = 0, we are on the cell (0,0).
- at t = 1, we move to the cell (0,1). It is possible because grid[0][1] <= 1.
- at t = 2, we move to the cell (1,1). It is possible because grid[1][1] <= 2.
- at t = 3, we move to the cell (1,2). It is possible because grid[1][2] <= 3.
- at t = 4, we move to the cell (1,1). It is possible because grid[1][1] <= 4.
- at t = 5, we move to the cell (1,2). It is possible because grid[1][2] <= 5.
- at t = 6, we move to the cell (1,3). It is possible because grid[1][3] <= 6.
- at t = 7, we move to the cell (2,3). It is possible because grid[2][3] <= 7.
The final time is 7. It can be shown that it is the minimum time possible.


Example 2:
Input: grid = [[0,2,4],[3,2,1],[1,0,4]]
Output: -1

Explanation: There is no path from the top left to the bottom-right cell.


Constraints:

    -> m == grid.length
    -> n == grid[i].length
    -> 2 <= m, n <= 1000
    -> 4 <= m * n <= 10^5
    -> 0 <= grid[i][j] <= 10^5
    -> grid[0][0] == 0


Concepts: Queue, BFS
"""
from heapq import heappush, heappop


# Optimised Solution
def minimumTime(grid: list[list[int]]) -> int:
    DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))                        # Initialise a list of all possible moves
    if grid[0][1] > 1 and grid[1][0] > 1:                           # Check if starting-adjacent values are greater than 1
        return -1                                                   # It is impossible to traverse the grid further

    n, m = len(grid), len(grid[0])                                  # Compute the dimensions of the grid
    q = [(0, 0, 0)]                                                 # Initialise a queue with the form: (time, x, y)
    visit = [[False] * m for _ in range(n)]                         # Initialise a 2D list to track visited cells
    visit[0][0] = True                                              # Set the first cell as visited

    while q:                                                        # While the queue is non-empty
        t, x, y = heappop(q)                                        # Pop out the smallest tuple from the heap
        for dx, dy in DIR:                                          # Iterate through the valid move-set
            nx, ny = x + dx, y + dy                                 # Compute the offset indices

            # Check if the new indices are outside the grid dimensions or curr-cell is already visited
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visit[nx][ny]:
                continue                                            # Skip to the next iteration

            nt = t + 1                                              # Increment the time
            if grid[nx][ny] > nt:                                   # Check if the cell value is greater than curr-time
                nt += (grid[nx][ny] - t) // 2 * 2                   # Add the time-diff to make the move possible

            if nx == n - 1 and ny == m - 1:                         # Check if the curr-cell is the bottom-right of grid
                return nt                                           # Return curr-time

            visit[nx][ny] = True                                    # Mark the curr-cell as visited
            heappush(q, (nt, nx, ny))                               # Push the new tuple into the heap

    return -1                                                       # It is impossible to reach the bottom-right cell
