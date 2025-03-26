"""
1765. Map of Highest Peak [MEDIUM]

You are given an integer matrix isWater of size m x n that represents a map of land and water cells.

    - If isWater[i][j] == 0, cell (i, j) is a land cell.
    - If isWater[i][j] == 1, cell (i, j) is a water cell.

You must assign each cell a height in a way that follows these rules:

    - The height of each cell must be non-negative.
    - If the cell is a water cell, its height must be 0.
    - Any two adjacent cells must have an absolute height difference of at most 1. A cell is adjacent to another cell if
      the former is directly north, east, south, or west of the latter (i.e., their sides are touching).

Find an assignment of heights such that the maximum height in the matrix is maximized.

Return an integer matrix height of size m x n where height[i][j] is cell (i, j)'s height. If there are multiple
solutions, return any of them.


Example 1:
Input: isWater = [[0,1],[0,0]]
Output: [[1,0],[2,1]]

Explanation: The image shows the assigned heights of each cell.
The blue cell is the water cell, and the green cells are the land cells.


Example 2:
Input: isWater = [[0,0,1],[1,0,0],[0,0,0]]
Output: [[1,1,0],[0,1,1],[1,2,2]]

Explanation: A height of 2 is the maximum possible height of any assignment.
Any height assignment that has a maximum height of 2 while still meeting the rules will also be accepted.


Constraints:

    -> m == isWater.length
    -> n == isWater[i].length
    -> 1 <= m, n <= 1000
    -> isWater[i][j] is 0 or 1.
    -> There is at least one water cell.


Concepts: Deque, BFS
"""
from collections import deque


# Optimised Solution
def highestPeak(isWater: list[list[int]]) -> list[list[int]]:
    r, c = len(isWater), len(isWater[0])                            # Obtain the grid dimensions
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]                       # List of exploratory moves
    land = [[None] * c for _ in range(r)]                           # 2D list to track land heights

    cells = deque([])                                               # Deque to track grid states
    for i in range(r):                                              # Iterate through the range of rows
        for j in range(c):                                          # Iterate through the range of cols
            if isWater[i][j] == 1:                                  # Check if the curr-cell is water
                land[i][j] = 0                                      # Update the cell value
                cells.append((i, j))                                # Append the state to the queue

    while cells:                                                    # While the queue is non-empty
        row, col = cells.popleft()                                  # Pop out the first element from the queue
        height = land[row][col] + 1                                 # Obtain and Increment the height of the cell
        for dir_r, dir_c in dirs:                                   # Iterate through the directions
            next_r, next_c = row + dir_r, col + dir_c               # Compute the new indices

            # Check if the new indices are invalid
            if next_r < 0 or next_r == r or next_c < 0 or next_c == c:
                continue                                            # Skip to the next iteration

            if land[next_r][next_c] is not None:                    # Check if the cell already has a height assigned
                continue                                            # Skip to the next iteration

            land[next_r][next_c] = height                           # Update the neighbouring cell
            cells.append((next_r, next_c))                          # Append the cell state to the queue

    return land                                                     # Return the result
