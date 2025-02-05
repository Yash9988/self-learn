"""
827. Making A Large Island [HARD]

You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.


Example 1:
Input: grid = [[1,0],[0,1]]
Output: 3

Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.


Example 2:
Input: grid = [[1,1],[1,0]]
Output: 4

Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.


Example 3:
Input: grid = [[1,1],[1,1]]
Output: 4

Explanation: Can't change any 0 to 1, only one island with area = 4.


Constraints:

    -> n == grid.length
    -> n == grid[i].length
    -> 1 <= n <= 500
    -> grid[i][j] is either 0 or 1.


Concepts: DFS
"""
from collections import defaultdict


def largestIsland(grid: list[list[int]]) -> int:
    # Helper function to explore the largest island area given a starting cell
    def explore_land(start):
        queue = [start]                                             # Queue to track land cells to explore
        water = set()                                               # Set to track all water cells connected to land
        area = 1                                                    # Counter to track total area of island

        while queue:                                                # While the queue is non-empty
            i, j = queue.pop()                                      # Pop the last element from the queue
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:       # Iterate through the neighbouring directions
                ni, nj = i + di, j + dj                             # Compute the land adjacent cell index
                if 0 <= ni < m and 0 <= nj < n:                     # Check if the index is within valid bounds
                    if grid[ni][nj] == 1:                           # Check if the neigh-cell is land
                        grid[ni][nj] = -1                           # Mark the cell visited
                        queue.append((ni, nj))                      # Append the cell index to the queue
                        area += 1                                   # Increment the counter
                    elif grid[ni][nj] == 0:                         # Check if the neigh-cell is water
                        water.add((ni, nj))                         # Append the cell index to the set

        for cell in water:                                          # Iterate through the water cells
            water_area[cell] += area                                # Increment water cells' value by island area

    m, n = len(grid), len(grid[0])                                  # Obtain the grid dimensions
    water_area = defaultdict(int)                                   # Dict to store area for each water cell

    for i in range(m):                                              # Iterate through the row-range
        for j in range(n):                                          # Iterate through the col-range
            if grid[i][j] == 1:                                     # Check if the cell is a land (unvisited)
                grid[i][j] = -1                                     # Mark the land visited
                explore_land((i, j))                                # Traverse the grid starting from the curr-cell

    if water_area:                                                  # Check if the dict is non-empty
        return 1 + max(water_area.values())                         # Return the max-land connected to water

    # Edge cases for if all cells are water or land
    return 1 if grid[0][0] == 0 else m * n                          # Return the result
