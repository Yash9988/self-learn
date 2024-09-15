"""
3290. Maximum Multiplication Score [MEDIUM]

You are given an integer array 'a' of size 4 and another integer array 'b' of size at least 4.

You need to choose 4 indices i0, i1, i2, and i3 from the array b such that i0 < i1 < i2 < i3. Your score will be equal
to the value a[0] * b[i0] + a[1] * b[i1] + a[2] * b[i2] + a[3] * b[i3].

Return the maximum score you can achieve.


Example 1:

Input: a = [3,2,5,6], b = [2,-6,4,-5,-3,2,-7]

Output: 26

Explanation:
We can choose the indices 0, 1, 2, and 5. The score will be 3 * 2 + 2 * (-6) + 5 * 4 + 6 * 2 = 26.


Example 2:

Input: a = [-1,4,5,-2], b = [-5,-1,-3,-2,-4]

Output: -1

Explanation:
We can choose the indices 0, 1, 3, and 4. The score will be (-1) * (-5) + 4 * (-1) + 5 * (-2) + (-2) * (-4) = -1.


Constraints:
    -> a.length == 4
    -> 4 <= b.length <= 105
    -> -105 <= a[i], b[i] <= 105

"""


# Top-Down Approach (Time: O(N))
def Score(a: list[int], b: list[int], ia: int, ib: int, dp: list[list]):

    if ia == len(a):                                                    # Check for base-cases
        return 0
    if ib == len(b):
        return float('-inf')

    if dp[ia][ib] == float('-inf'):                                     # If no solution in DP
        pick = a[ia] * b[ib] + Score(a, b, ia + 1, ib + 1, dp)          # Selecting the element at index 'ib'
        npick = Score(a, b, ia, ib + 1, dp)                             # Skipping the element at index 'ib'

        dp[ia][ib] = max(pick, npick)                                   # Pick and store the maximum value

    return dp[ia][ib]                                                   # Return the result


def maxScore(a: list[int], b: list[int]) -> int:
    dp = [[float('-inf')] * len(b) for _ in range(len(a))]              # Initialise the DP
    return Score(a, b, 0, 0, dp)


# Bottom-Up Approach
def maxScore_(a: list[int], b: list[int]):
    n = len(b)                                                          # Get the length for array 'b'
    dp = [[float('-inf')] * (n + 1) for _ in range(5)]                  # Initialise the DP

    for j in range(n + 1):                                              # Set the value for base-cases
        dp[0][j] = 0

    for i in range(1, 5):                                               # Iterate through all indexes of array 'a'
        for j in range(1, n + 1):                                       # Iterate through all indexed of array 'b'
            pick = a[i - 1] * b[j - 1] + dp[i - 1][j - 1]               # Selecting the elements at current indexes
            npick = dp[i][j - 1]                                        # Skipping the elements at current indexes

            dp[i][j] = max(pick, npick)                                 # Compare and store the maximum value

    return dp[4][n]                                                     # Return the result
