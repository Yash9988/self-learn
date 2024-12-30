"""
689. Maximum Sum of 3 Non-Overlapping Subarrays [HARD]

Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and
return them.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are
multiple answers, return the lexicographically smallest one.


Example 1:
Input: nums = [1,2,1,2,6,7,5,1], k = 2
Output: [0,3,5]

Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.


Example 2:

Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
Output: [0,2,4]


Constraints:

    -> 1 <= nums.length <= 2 * 10^4
    -> 1 <= nums[i] < 2^16
    -> 1 <= k <= floor(nums.length / 3)


Concepts: Subarray
"""


# Optimised Solution
def maxSumOfThreeSubarrays(nums: list[int], k: int) -> list[int]:
    n = len(nums)                                                   # Obtain the list size
    maxsum = 0                                                      # Counter to track max-sum
    sum = [0]                                                       # List to track the running-sum
    posLeft = [0] * n                                               # List to track left-max-sum interval
    posRight = [n - k] * n                                          # List to track right-max-sum interval
    ans = [0, 0, 0]                                                 # List to store the final result

    for i in nums:                                                  # Iterate through the nums
        sum.append(sum[-1] + i)                                     # Append the running sum to the list

    # DP for starting index of the left max sum interval
    tot = sum[k] - sum[0]                                           # Compute the diff b/w the start-window edge values
    for i in range(k, n):                                           # Iterate the range: k to n
        if sum[i + 1] - sum[i + 1 - k] > tot:                       # Check if the curr-window diff is higher
            posLeft[i] = i + 1 - k                                  # Update the list at idx with window-end
            tot = sum[i + 1] - sum[i + 1 - k]                       # Update the counter with the new diff
        else:
            posLeft[i] = posLeft[i - 1]                             # Carry forward the prev-idx-val, otherwise

    # DP for starting index of the right max sum interval
    tot = sum[n] - sum[n - k]                                       # Compute the diff b/w the end-window edge values
    for i in range(n - k - 1, -1, -1):                              # Iterate the range: 0 to n - k, in reverse
        if sum[i + k] - sum[i] >= tot:                              # Check if the curr-window diff is higher or equal
            posRight[i] = i                                         # Update the list at idx with window-start
            tot = sum[i + k] - sum[i]                               # Update the counter with the new diff
        else:
            posRight[i] = posRight[i + 1]                           # Carry back the prev-idx-val, otherwise

    # test all possible middle interval
    for i in range(k, n - 2 * k + 1):                               # Iterate the range: k to n - 2k
        l = posLeft[i - 1]                                          # Update the left pointer with idx from left-max
        r = posRight[i + k]                                         # Update the right pointer with idx from right-max

        # Compute the sum for each subarray window wrt the pointers
        tot = (sum[i + k] - sum[i]) + (sum[l + k] - sum[l]) + (sum[r + k] - sum[r])

        if tot > maxsum:                                            # Check if the curr-sum is higher than max-sum
            maxsum = tot                                            # Update the counter with max-val
            ans = [l, i, r]                                         # Update the result list with current pointer values

    return ans                                                      # Return the result
