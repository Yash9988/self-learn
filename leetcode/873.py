"""
873. Length of Longest Fibonacci Subsequence [MEDIUM]

A sequence x1, x2, ..., xn is Fibonacci-like if:

    - n >= 3
    - x_i + x_i+1 == x_i+2 for all i + 2 <= n

Given a strictly increasing array arr of positive integers forming a sequence, return the length of the longest
Fibonacci-like subsequence of arr. If one does not exist, return 0.

A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr, without
changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].


Example 1:
Input: arr = [1,2,3,4,5,6,7,8]
Output: 5

Explanation: The longest subsequence that is fibonacci-like: [1,2,3,5,8].


Example 2:
Input: arr = [1,3,7,11,12,14,18]
Output: 3

Explanation: The longest subsequence that is fibonacci-like: [1,11,12], [3,11,14] or [7,11,18].


Constraints:

    -> 3 <= arr.length <= 1000
    -> 1 <= arr[i] < arr[i + 1] <= 10^9


Concepts: DP, Combinations
"""


# Optimised Solution
def lenLongestFibSubseq(arr: list[int]) -> int:
    n = len(arr)                                                    # Obtain the list size

    # dp[prev][curr] stores length of Fibonacci sequence ending at indexes prev,curr
    dp = [[0] * n for _ in range(n)]
    max_len = 0                                                     # Counter to track max-length of subseq

    # Find all possible pairs that sum to arr[curr]
    for curr in range(2, n):
        # Use two pointers to find pairs that sum to arr[curr]
        start = 0
        end = curr - 1

        while start < end:                                          # While the left pointer is smaller than right
            pair_sum = arr[start] + arr[end]                        # Compute the sum

            if pair_sum > arr[curr]:                                # Check if sum is greater than curr-ele
                end -= 1                                            # Decrement the right pointer
            elif pair_sum < arr[curr]:                              # Check if sum is lesser than curr-ele
                start += 1                                          # Increment the left pointer
            else:
                # Found a valid pair, update dp
                dp[end][curr] = dp[start][end] + 1

                max_len = max(dp[end][curr], max_len)               # Update the counter with max-val
                end -= 1                                            # Decrement the right pointer
                start += 1                                          # Increment the left pointer

    # Add 2 to include first two numbers, or return 0 if no sequence found
    return max_len + 2 if max_len else 0