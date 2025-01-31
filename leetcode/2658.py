"""
2658. Maximum Number of Fish in a Grid [MEDIUM]

You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:

    - A land cell if grid[r][c] = 0, or
    - A water cell containing grid[r][c] fish, if grid[r][c] > 0.

A fisher can start at any water cell (r, c) and can do the following operations any number of times:

    - Catch all the fish at cell (r, c), or
    - Move to any adjacent water cell.

Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell
exists.

An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.


Example 1:
Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
Output: 7

Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4 fish.


Example 2:
Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
Output: 1

Explanation: The fisher can start at cells (0,0) or (3,3) and collect a single fish.


Constraints:

    -> m == grid.length
    -> n == grid[i].length
    -> 1 <= m, n <= 10
    -> 0 <= grid[i][j] <= 10


Concepts: Deque, DFS
"""
from collections import deque


# My Solution
def findMaxFish(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])                                  # Obtain grid dimensions
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]                       # List of explanatory directions

    res = 0                                                         # Counter to track the result
    for i in range(m):                                              # Iterate through the range of rows
        for j in range(n):                                          # Iterate through the range of cols
            if not grid[i][j]:                                      # Check if the cell is a land-cell
                continue                                            # Skip to the next iteration

            visited = [[0 for _ in range(n)] for _ in range(m)]     # 2D list to track visited cells

            dq = deque([(i, j)])                                    # Queue to track the unprocessed cells
            temp = 0                                                # Counter to track fishes
            while dq:                                               # While the queue is non-empty
                r, c = dq.pop()                                     # Pop the last element of the queue
                temp += grid[r][c] if not visited[r][c] else 0      # Increment the counter if the cell is unvisited

                for x, y in dirs:                                   # Iterate through the directions
                    nx, ny = r + x, c + y                           # Compute the new coordinates

                    # Check if the new coordinates are valid and the cell is unvisited
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] and not visited[nx][ny]:
                        dq.append((nx, ny))                         # Append the new coordinates to the queue

                visited[r][c] = 1                                   # Mark the cell as visited

            res = max(res, temp)                                    # Update the result counter with max-val

    return res                                                      # Return the result


# Optimised Solution
def findMaxFish_op(grid: list[list[int]]) -> int:
    res = 0                                                         # Counter to track the result
    ln, wd = len(grid), len(grid[0])                                # Obtain the grid dimensions

    for y in range(ln):                                             # Iterate through the range of rows
        for x in range(wd):                                         # Iterate through the range of cols
            if grid[y][x]:                                          # Check if the cell is a water-cell
                cur_res = grid[y][x]                                # Obtain the cell value
                grid[y][x] = 0                                      # Update the cell value to zero

                dq = [(y, x)]                                       # List to store unprocessed coordinates
                while dq:                                           # While the queue is non-empty
                    y1, x1 = dq.pop()                               # Pop the last tuple from the queue

                    # Iterate through the neighbours
                    for ny, nx in [(y1 + 1, x1), (y1 - 1, x1), (y1, x1 + 1), (y1, x1 - 1)]:
                        # Check if the coordinates are valid and the cell is water
                        if 0 <= ny < ln and 0 <= nx < wd and grid[ny][nx]:
                            cur_res += grid[ny][nx]                 # Increment the counter by the cell value
                            grid[ny][nx] = 0                        # Update the cell value to zero

                            dq.append((ny, nx))                     # Append the neighbour's coordinates to the queue

                res = max(res, cur_res)                             # Update the counter with max-val

    return res                                                      # Return the result
