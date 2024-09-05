"""
Given an N x M grid of a brick wall and a tile of shape 1xM.

Find all the # unique orientations of placing the tile in the grid.
"""


# Top-Down Approach (n = #rows in the grid)
def nTiling(n: int) -> int:
    if n < M:                                   # If rows are less than the vertical height of the tile
        return 1                                # Only 1 way of orienting the tiles (horizontally)
    elif n == M:                                # If the available rows equals the vertical height of the tile
        return 2                                # 2 unique ways of orienting the tiles (H&V)

    dp[n] = nTiling(n - 1) + nTiling(n - M)     # Recursively obtain and sum all possible orientations

    return dp[n]                                # Return the result


# Bottom-Up Approach (n = #rows in the grid)
def nTiling_(n: int) -> int:
    a = [1 for _ in range(M)]
    a.append(2)

    for i in range(M + 1, n + 1):
        a.append(a[i - 1] + a[i - M])

    return a[n]


dp, M = {}, 5                                   # Defining 'M' as a global constant to reduce method signature
# print(nTiling(6))
# print(nTiling_(6))
