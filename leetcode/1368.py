"""
1368. Minimum Cost to Make at Least One Valid Path in a Grid [HARD]

Given an m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in
this cell. The sign of grid[i][j] can be:

    - 1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
    - 2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
    - 3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
    - 4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])

Notice that there could be some signs on the cells of the grid that point outside the grid.

You will initially start at the upper left cell (0, 0). A valid path in the grid is a path that starts from the upper
left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid path does
not have to be the shortest.

You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.

Return the minimum cost to make the grid have at least one valid path.


Example 1:
Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
Output: 3

Explanation: You will start at point (0, 0).
The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) change the arrow to down with cost = 1 -->
(1, 3) --> (1, 2) --> (1, 1) --> (1, 0) change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2, 2) -->
(2, 3) change the arrow to down with cost = 1 --> (3, 3)
The total cost = 3.


Example 2:
Input: grid = [[1,1,3],[3,2,2],[1,1,4]]
Output: 0

Explanation: You can follow the path from (0, 0) to (2, 2).


Example 3:
Input: grid = [[1,2],[4,3]]
Output: 1


Constraints:

    -> m == grid.length
    -> n == grid[i].length
    -> 1 <= m, n <= 100
    -> 1 <= grid[i][j] <= 4


Concepts: Deque
"""
from collections import deque


# Optimised Solution
def minCost(grid: list[list[int]]) -> int:
    # Method to traverse the grid in a DFS fashion
    def dfs(i: int, j: int, cost: int) -> None:
        if i < 0 or i == m or j < 0 or j == n:                      # Check for invalid indices
            return                                                  # Break out of the method call

        if dp[i][j] != -1:                                          # Check if the DP-val at index has been initialised
            return                                                  # Break out of the method call

        dp[i][j] = cost                                             # Update the DP-val at index with cost
        q.append((i, j))                                            # Append the 2D-index to the queue
        dx, dy = dirs[grid[i][j] - 1]                               # Obtain the move-dir from the list
        dfs(i + dx, j + dy, cost)                                   # Recursively call the method with the new index


    m, n = len(grid), len(grid[0])                                  # Obtain the grid dimensions
    dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))                       # List to track all possible moves
    dp = [[-1] * n for _ in range(m)]                               # 2D list to track the DP values
    q = deque()                                                     # Deque to track the states

    dfs(0, 0, 0)                                                    # Traverse the grid starting from the first cell

    cost = 0                                                        # Counter to track the cost
    while q:                                                        # While the queue is non-empty
        cost += 1                                                   # Increment the cost
        for _ in range(len(q)):                                     # Iterate through the range of states in queue
            i, j = q.popleft()                                      # Pop the left-most state from the queue
            for dx, dy in dirs:                                     # Iterate through the move-set
                    dfs(i + dx, j + dy, cost)                       # Traverse the grid in the curr-dir

    return dp[-1][-1]                                               # Return the result


# Alternate Solution
def minCost_alt(grid: list[list[int]]) -> int:
    # Check if coordinates are within grid bounds
    def _is_valid(row: int, col: int, num_rows: int, num_cols: int) -> bool:
        return 0 <= row < num_rows and 0 <= col < num_cols


    num_rows, num_cols = len(grid), len(grid[0])                    # Obtain the grid dimensions

    # Direction vectors: right, left, down, up (matching grid values 1,2,3,4)
    _dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Track minimum cost to reach each cell
    min_cost = [[float("inf")] * num_cols for _ in range(num_rows)]
    min_cost[0][0] = 0                                              # Set the first cell cost to zero

    # Use deque for 0-1 BFS - add zero cost moves to front, cost=1 to back
    dq = deque([(0, 0)])

    while dq:                                                       # While the queue is non-empty
        row, col = dq.popleft()                                     # Pop out the pair of indices from the queue

        # Try all four directions
        for dir_idx, (dx, dy) in enumerate(_dirs):
            new_row, new_col = row + dx, col + dy                   # Compute the new cell index
            cost = 0 if grid[row][col] == dir_idx + 1 else 1        # Update cost counter

            # If position is valid and we found a better path
            if (
                _is_valid(new_row, new_col, num_rows, num_cols)
                and min_cost[row][col] + cost < min_cost[new_row][new_col]
            ):

                min_cost[new_row][new_col] = min_cost[row][col] + cost

                # Add to back if cost=1, front if cost=0
                if cost == 1:
                    dq.append((new_row, new_col))
                else:
                    dq.appendleft((new_row, new_col))

    return min_cost[num_rows - 1][num_cols - 1]                     # Return the result
