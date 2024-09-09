"""
Choose _at least_ one element from every window of size 3 such that the sum of elements for the sub-sequence is
minimized.
"""


# Top-Down Approach
def MinWindowSubSeq(arr: list, window: int) -> int:
    if (n := len(arr)) <= window:                       # Check if array is equal (or less) than the window size
        dp[n] = arr[-1]                                 # Store value of last element under DP (indexed by array size)
        return min(arr)                                 # Minimum sum is the min-element of array

    elif n not in dp:                                   # Check if solution in DP
        sub_ = [MinWindowSubSeq(arr[:-i], window) for i in range(1, window + 1)]    # Recursively obtain sub-solutions
        dp[n] = arr[-1] + min(sub_)                     # Update the DP with the min-sum for the particular array
        return min([dp[n - i] for i in range(window)])  # Return the min-result from the final array window

    return dp[n]                                        # Return the DP value for min-sum at index


# Bottom-Up Approach
def MinWindowSubSeq_(arr: list, window: int) -> int:
    if (N := len(arr)) <= window:                   # Check if array is equal (or less) than the window size
        return min(arr)                             # Minimum sum is the min-element

    for i in range(window, N):                      # Iterate from the outside of the first window
        arr[i] += min(arr[i - window: i])           # Iterative obtain the min-sum for each sub-problem

    return min(arr[-window:])                       # Return the min-result from the final array window


dp = {}
x = [3, 2, 1, 1, 2, 3, 1, 3, 2, 1]
print(MinWindowSubSeq(x, 3))
print(MinWindowSubSeq_(x, 3))
