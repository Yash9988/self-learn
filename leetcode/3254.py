"""
3254. Find the Power of K-Size Subarrays I [MEDIUM]

You are given an array of integers nums of length n and a positive integer k.

The power of an array is defined as:
Its maximum element if all of its elements are consecutive and sorted in ascending order. -1 otherwise.

You need to find the power of all _subarrays_ of nums of size k.

Return an integer array results of size n - k + 1, where results[i] is the power of nums[i...(i + k - 1)].


Example 1:
Input: nums = [1,2,3,4,3,2,5], k = 3
Output: [3,4,-1,-1,-1]

Explanation:
There are 5 subarrays of nums of size 3:

    [1, 2, 3] with the maximum element 3.
    [2, 3, 4] with the maximum element 4.
    [3, 4, 3] whose elements are not consecutive.
    [4, 3, 2] whose elements are not sorted.
    [3, 2, 5] whose elements are not consecutive.


Example 2:
Input: nums = [2,2,2,2,2], k = 4
Output: [-1,-1]


Example 3:
Input: nums = [3,2,3,2,3,2], k = 2
Output: [-1,3,-1,3,-1]


Constraints:

    -> 1 <= n == nums.length <= 500
    -> 1 <= nums[i] <= 10^5
    -> 1 <= k <= n


Concepts: Subarray Window
"""


# Optimised Solution
def resultsArray(nums: list[int], k: int) -> list[int]:
    if k == 1:                                          # Check if windows size is 1
        return nums                                     # Return the original list

    result = []                                         # Initialise the result list
    curStreak = 1                                       # Initialise a counter to track streak

    for i in range(1, len(nums)):                       # Iterate through the list, starting at index 1
        if nums[i] == nums[i - 1] + 1:                  # Check if the elements are consecutive & sorted
            curStreak += 1                              # Increment the streak counter
        else:
            curStreak = 1                               # Reset the counter

        if curStreak >= k:                              # Check if streak value >= window size
            result.append(nums[i])                      # Append the curr-ele to the result list
        else:
            result.append(-1)                           # Append -1 to the list, otherwise

    return result[k - 2:]                               # Return the result
