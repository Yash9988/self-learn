"""
Given a brick wall of dimension 4 x N and a tile of dimension 1x4/4x1
Find the total # unique orientations to arrange tiles on the wall
"""


# Top-Down Approach (n = #columns in the wall)
def Tiling(n: int) -> int:
    if n in {1, 2, 3}:                      # If the available #columns are between 1 and 3
        return 1                            # Only one way (vertical) to place the tile
    elif n == 4:                            # If the available #columns are 4
        return 2                            # There are two ways of placing the tile (H&V)

    dp[n] = Tiling(n - 1) + Tiling(n - 4)   # Recursively obtain and sum all possible ways

    return dp[n]                            # Return the result


# Bottom-Up Approach (n = #columns in the wall)
def Tiling_(n: int) -> int:
    a = [0, 1, 1, 1, 2]                     # Initialise base cases

    for i in range(5, n + 1):               # Iterate till N
        a.append(a[i - 1] + a[i - 4])       # Iteratively obtain and sum of all possible ways

    return a[n]                             # Return the result


dp = {}
# print(Tiling(8))
# print(Tiling_(8))
