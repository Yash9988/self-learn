"""
2257. Count Unguarded Cells in the Grid [MEDIUM]

You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards
and walls where guards[i] = [row_i, col_i] and walls[j] = [row_j, col_j] represent the positions of the i-th guard and
j-th wall respectively.

A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position
 unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.

Return the number of unoccupied cells that are not guarded.


Example 1:
Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
Output: 7

Explanation: The guarded and unguarded cells are shown in red and green respectively in the above diagram.
There are a total of 7 unguarded cells, so we return 7.


Example 2:
Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
Output: 4

Explanation: The unguarded cells are shown in green in the above diagram.
There are a total of 4 unguarded cells, so we return 4.


Constraints:

    -> 1 <= m, n <= 10^5
    -> 2 <= m * n <= 10^5
    -> 1 <= guards.length, walls.length <= 5 * 10^4
    -> 2 <= guards.length + walls.length <= m * n
    -> guards[i].length == walls[j].length == 2
    -> 0 <= row_i, row_j < m
    -> 0 <= col_i, col_j < n
    -> All the positions in guards and walls are unique.


Concepts: Action Set
"""

# Optimised Solution
def countUnguarded(m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
    grid = [[0] * n for _ in range(m)]                                      # Initialize grid with zeros
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]                         # Process guards' vision

    for x, y in guards + walls:                                             # Iterate through guard & wall positions
        grid[x][y] = 2                                                      # Mark obstacles

    for gx, gy in guards:                                                   # Iterate through all guards
        for dx, dy in directions:                                           # Iterate through all movement directions
            x, y = gx, gy                                                   # Store the guard's initial position

            while (0 <= x + dx < m and 0 <= y + dy < n
                   and grid[x + dx][y + dy] != 2):                          # Check cells in curr-dir until obstacle
                x += dx                                                     # Update the x-offset
                y += dy                                                     # Update the y-offset
                grid[x][y] = 1                                              # Mark the grid as guarded

    return sum(row.count(0) for row in grid)                                # Count unguarded cells and return the result
