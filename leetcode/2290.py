"""
2290. Minimum Obstacle Removal to Reach Corner [HARD]

You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one of two values:

    - 0 represents an empty cell,
    - 1 represents an obstacle that may be removed.

You can move up, down, left, or right from and to an empty cell.

Return the minimum number of obstacles to remove so you can move from the upper left corner (0, 0) to the lower right
corner (m - 1, n - 1).


Example 1:
Input: grid = [[0,1,1],[1,1,0],[1,1,0]]
Output: 2

Explanation: We can remove the obstacles at (0, 1) and (0, 2) to create a path from (0, 0) to (2, 2).
It can be shown that we need to remove at least 2 obstacles, so we return 2.
Note that there may be other ways to remove 2 obstacles to create a path.


Example 2:
Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
Output: 0

Explanation: We can move from (0, 0) to (2, 4) without removing any obstacles, so we return 0.


Constraints:

    -> m == grid.length
    -> n == grid[i].length
    -> 1 <= m, n <= 105
    -> 2 <= m * n <= 105
    -> grid[i][j] is either 0 or 1.
    -> grid[0][0] == grid[m - 1][n - 1] == 0


Concepts: Deque, BFS, Action Set
"""
from collections import deque


# Optimised Solution
def minimumObstacles(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])                                  # Initialise the grid dimensions
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]                 # Initialise the valid directions

    # Deque for 0-1 BFS: (x, y, obstacles_removed)
    deque_ = deque([(0, 0, 0)])                                     # Start at (0, 0) with 0 obstacles removed
    visited = [[False] * n for _ in range(m)]                       # Initialise a 2D list to track visited cells
    visited[0][0] = True                                            # Mark the first cell visited

    while deque_:                                                   # While the queue is non-empty
        x, y, obstacles_removed = deque_.popleft()                  # Pop the leftmost tuple from the queue

        if x == m - 1 and y == n - 1:                               # Check if we reach the bottom-right corner
            return obstacles_removed                                # Return the result

        for dx, dy in directions:                                   # Iterate through the move-set
            nx, ny = x + dx, y + dy                                 # Compute the offset indices

            # Check if the new indices are within the grid and the cell hasn't been visited before
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True                              # Mark the cell visited

                if grid[nx][ny] == 0:                               # Check if the curr-cell is empty
                    deque_.appendleft((nx, ny, obstacles_removed))  # No obstacle to remove
                else:
                    deque_.append((nx, ny, obstacles_removed + 1))  # Remove the obstacle

    return -1                                                       # If no path exists
