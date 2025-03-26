"""
1975. Maximum Matrix Sum [MEDIUM]

You are given an n x n integer matrix. You can do the following operation any number of times:

    - Choose any two adjacent elements of matrix and multiply each of them by -1.

Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using
the operation mentioned above.


Example 1:
Input: matrix = [[1,-1],[-1,1]]
Output: 4

Explanation: We can follow the following steps to reach sum equals 4:
- Multiply the 2 elements in the first row by -1.
- Multiply the 2 elements in the first column by -1.


Example 2:
Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
Output: 16

Explanation: We can follow the following step to reach sum equals 16:
- Multiply the 2 last elements in the second row by -1.


Constraints:

    -> n == matrix.length == matrix[i].length
    -> 2 <= n <= 250
    -> -10^5 <= matrix[i][j] <= 10^5


Concepts:
"""
from math import inf


# Optimised Solution
def maxMatrixSum(matrix: list[list[int]]) -> int:
    total_sum = negative_count = 0                  # Initialise sum and frequency counters
    min_el = inf                                    # Initialise min-ele counter

    for i in matrix:                                # Iterate through the rows
        for j in i:                                 # Iterate through the cols
            if j < 0:                               # Check if the value is negative
                j = -j                              # Update to positive value
                negative_count += 1                 # Increment the frequency counter

            total_sum += j                          # Increment the sum counter by the value

            if j < min_el:                          # Check if the value is smaller than the min-ele counter value
                min_el = j                          # Update the min-ele counter

    if negative_count % 2 == 0:                     # Check if the freq counter value is even
        return total_sum                            # Return the sum
    else:
        return total_sum - 2 * min_el               # Return the sum after removing the min-ele, otherwise
