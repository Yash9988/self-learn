"""
2661. First Completely Painted Row or Column [MEDIUM]

You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers
in the range [1, m * n].

Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].

Return the smallest index i at which either a row or a column will be completely painted in mat.


Example 1:
Input: arr = [1,3,4,2], mat = [[1,4],[2,3]]
Output: 2

Explanation: The moves are shown in order, and both the first row and second column of the matrix become fully painted
at arr[2].


Example 2:
Input: arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]
Output: 3

Explanation: The second column becomes fully painted at arr[3].


Constraints:

    -> m == mat.length
    -> n = mat[i].length
    -> arr.length == m * n
    -> 1 <= m, n <= 10^5
    -> 1 <= m * n <= 10^5
    -> 1 <= arr[i], mat[r][c] <= m * n
    -> All the integers of arr are unique.
    -> All the integers of mat are unique.


Concepts: Hashmap
"""


# My Solution
def firstCompleteIndex(arr: list[int], mat: list[list[int]]) -> int:
    n = len(arr)                                                    # Obtain the list size
    r, c = len(mat), len(mat[0])                                    # Obtain the dimensions of the grid
    idx = {}                                                        # Dictionary to map values to their corr-indices

    for i in range(r):                                              # Iterate through the range of rows
        for j in range(c):                                          # Iterate through the range of cols
            idx[mat[i][j]] = (i, j)                                 # Update the dict with value and its index

    x, y = [0] * r, [0] * c                                         # Lists to track the painted rows and cols
    for i in range(n):                                              # Iterate through the range of list
        a, b = idx[arr[i]]                                          # Obtain the index of the curr-val
        x[a] += 1                                                   # Increment the corr-idx in row-list
        y[b] += 1                                                   # Increment the corr-idx in col-list

        if x[a] == c or y[b] == r:                                  # Check if either a row or col is completely painted
            return i                                                # Return the result

# Optimised Solution
def firstCompleteIndex_op(arr: list[int], mat: list[list[int]]) -> int:

    # Obtain the grid dimensions
    m, n = len(mat), len(mat[0])
    # rows[i] := the number of painted grid in the i-th row
    rows = [0] * m
    # cols[j] := the number of painted grid in the j-th column
    cols = [0] * n
    # numToRow[num] := the i-th row of `num` in `mat`
    numToRow = [0] * (m * n + 1)
    # numToCol[num] := the j-th column of `num` in `mat`
    numToCol = [0] * (m * n + 1)

    # Update the lists with corresponding indices for each element
    for i, row in enumerate(mat):
        for j, num in enumerate(row):
            numToRow[num] = i
            numToCol[num] = j

    # Iterate through the list and "paint" the corr-cells until a row or column is complete
    for i, a in enumerate(arr):
        rows[numToRow[a]] += 1
        if rows[numToRow[a]] == n:
            return i
        cols[numToCol[a]] += 1
        if cols[numToCol[a]] == m:
            return i
