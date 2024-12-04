"""
1574. Shortest Subarray to be Removed to Make Array Sorted [MEDIUM]

Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are
non-decreasing.

Return the length of the shortest subarray to remove.

A subarray is a contiguous subsequence of the array.


Example 1:
Input: arr = [1,2,3,10,4,2,3,5]
Output: 3

Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be
[1,2,3,3,5] which are sorted. Another correct solution is to remove the subarray [3,10,4].


Example 2:
Input: arr = [5,4,3,2,1]
Output: 4

Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a
subarray of length 4, either [5,4,3,2] or [4,3,2,1].


Example 3:
Input: arr = [1,2,3]
Output: 0

Explanation: The array is already non-decreasing. We do not need to remove any elements.


Constraints:

    -> 1 <= arr.length <= 10^5
    -> 0 <= arr[i] <= 10^9


Concepts: Subarray, Double Pointers
"""


def findLengthOfShortestSubarray(arr: list[int]) -> int:
    n = len(arr)                                            # Compute the list size

    # 1. Find the rightmost point where array becomes non-ascending
    right = n - 1                                           # Initialise the right pointer
    while right > 0 and arr[right - 1] <= arr[right]:       # While array is non-ascending
        right -= 1                                          # Decrement the pointer

    # 2. If array is already sorted in ascending order
    if right == 0:                                          # Check if pointer at the start
        return 0                                            # Return 0

    # 3. Initial minimum length is from start to right pointer
    min_length = right                                      # Initialise a length counter

    # 4. Check each element from left side
    for left in range(n):                                   # Iterate through the array
        # 4.1 Break if left sequence becomes non-ascending
        if left > 0 and arr[left - 1] > arr[left]:          # Check if array is non-ascending
            break

        # 4.2 Find the first element from right that's >= arr[left]
        while right < n and arr[left] > arr[right]:         # While ele-val at left pointer is greater than right
            right += 1                                      # Increment the right pointer

        # 4.3 Update minimum length of subarray to be removed
        current_length = right - left - 1                   # Compute the subarray length
        min_length = min(min_length, current_length)        # Update the length counter with min-val

    return min_length                                       # Return the result
