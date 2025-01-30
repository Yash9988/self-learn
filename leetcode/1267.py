"""
1267. Count Servers that Communicate [MEDIUM]

You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell
there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or
on the same column.

Return the number of servers that communicate with any other server.


Example 1:
Input: grid = [[1,0],[0,1]]
Output: 0

Explanation: No servers can communicate with others.


Example 2:
Input: grid = [[1,0],[1,1]]
Output: 3

Explanation: All three servers can communicate with at least one other server.


Example 3:
Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4

Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can
communicate with each other. The server at right bottom corner can't communicate with any other server.


Constraints:

    -> m == grid.length
    -> n == grid[i].length
    -> 1 <= m <= 250
    -> 1 <= n <= 250
    -> grid[i][j] == 0 or 1


Concepts: Counting
"""


# My Solution
def countServers(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])                                  # Obtain the grid dimensions
    r, c = [0] * m, [0] * n                                         # List to track servers for each row/col

    for i in range(m):                                              # Iterate through the range of rows
        for j in range(n):                                          # Iterate through the range of cols
            if grid[i][j]:                                          # Check if server is present at curr-cell
                r[i] += 1                                           # Increment the corr-row
                c[j] += 1                                           # Increment the corr-col

    counted = [[False] * n for _ in range(m)]                       # 2D list to track counted servers
    res = 0                                                         # Counter to track the result

    for i in range(m):                                              # Iterate through the range of rows
        if r[i] > 1:                                                # Check if the row contains more than 1 server
            for j in range(n):                                      # Iterate through the range of cols
                if grid[i][j] and not counted[i][j]:                # Check if the server has not been counted
                    res += 1                                        # Increment the result counter
                    counted[i][j] = True                            # Mark the server counted

    for j in range(n):                                              # Iterate through the range of cols
        if c[j] > 1:                                                # Check if the col contains more than 1 server
            for i in range(m):                                      # Iterate through the range of rows
                if grid[i][j] and not counted[i][j]:                # Check if the server has not been counted
                    res += 1                                        # Increment the result counter
                    counted[i][j] = True                            # Mark the server counted

    return res                                                      # Return the result


# Optimised Solution
def countServers_op(grid: list[list[int]]) -> int:
    count = 0                                                       # Counter to track the result
    for r in range(len(grid)):                                      # Iterate through the range of rows
        s = sum(grid[r])                                            # Compute the sum of all servers in the curr-row
        if s > 1:                                                   # Check if the sum is higher than one
            count += s                                              # Increment the counter by the sum-val
        elif s == 1:                                                # Check if there's only one server in the curr-row
            c = grid[r].index(1)                                    # Obtain the col-idx for the server

            # Check if sum of servers in the col is greater than one
            if sum(grid[r][c] for r in range(len(grid))) > 1:
                count += 1                                          # Increment the result counter

    return count                                                    # Return the result
