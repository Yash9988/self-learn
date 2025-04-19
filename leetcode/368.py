"""
368. Largest Divisible Subset [MEDIUM]

Given a set of distinct positive integers nums, return the largest subset answer such that every pair
(answer[i], answer[j]) of elements in this subset satisfies:

    - answer[i] % answer[j] == 0, or
    - answer[j] % answer[i] == 0

If there are multiple solutions, return any of them.


Example 1:
Input: nums = [1,2,3]
Output: [1,2]

Explanation: [1,3] is also accepted.


Example 2:
Input: nums = [1,2,4,8]
Output: [1,2,4,8]


Constraints:

    -> 1 <= nums.length <= 1000
    -> 1 <= nums[i] <= 2 * 10^9
    -> All the integers in nums are unique.


Concepts: DP
"""


# Optimised Solution
def largestDivisibleSubset(nums: list[int]) -> list[int]:
    n = len(nums)                                                   # Obtain the list size
    dp = [1] * n                                                    # List to track DP-vals
    parent = [-1] * n                                               # List to track the parent
    max_len, max_index = 1, 0                                       # Counter to track max-len and max-idx

    nums.sort()                                                     # Sort the list

    for i in range(n):                                              # Iterate through the list range
        for j in range(i):                                          # Iterate through the sub-range
            if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:        # Check if the condition is satisfied
                dp[i] = dp[j] + 1                                   # Update the DP-val at idx
                parent[i] = j                                       # Update the parent at idx

        if dp[i] > max_len:                                         # Check if DP-val is greater
            max_len = dp[i]                                         # Update the max-val counter
            max_index = i                                           # Update the max-idx counter

    result = []                                                     # List to store the result
    while max_index != -1:                                          # While idx-counter isn't invalid
        result.append(nums[max_index])                              # Append the idx-num to the list
        max_index = parent[max_index]                               # Update the counter with idx-parent

    return result                                                   # Return the result
