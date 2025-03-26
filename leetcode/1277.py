"""
1277. Count Square Submatrices with All Ones [Medium]

Given a m * n matrix of ones and zeros, return how many square sub-matrices have all ones.


Example 1:
Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15

Explanation:
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.


Example 2:
Input: matrix =
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7

Explanation:
There are 6 squares of side 1.
There is 1 square of side 2.
Total number of squares = 6 + 1 = 7.


Constraints:

    -> 1 <= arr.length <= 300
    -> 1 <= arr[0].length <= 300
    -> 0 <= arr[i][j] <= 1


Concepts: DP
"""


def countSquares(matrix: list[list[int]]) -> int:
    for i in range(1, len(matrix)):                             # Iterate through the rows, starting at index 1
        for j in range(1, len(matrix[0])):                      # Iterate through the columns, starting at index 1
            matrix[i][j] *= min(matrix[i - 1][j],
                                matrix[i][j - 1],
                                matrix[i - 1][j - 1]) + 1       # Compute the min-val from previous window and multiply
    return sum(map(sum, matrix))                                # Return the sum
