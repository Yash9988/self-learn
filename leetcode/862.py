"""
862. Shortest Subarray with Sum at Least K [HARD]

Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of
at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.


Example 1:

Input: nums = [1], k = 1
Output: 1


Example 2:

Input: nums = [1,2], k = 4
Output: -1


Example 3:

Input: nums = [2,-1,2], k = 3
Output: 3


Constraints:

    -> 1 <= nums.length <= 10^5
    -> -10^5 <= nums[i] <= 10^5
    -> 1 <= k <= 10^9


Concepts: Shortest subarray, deque
"""
from collections import deque


def shortestSubarray(nums: list[int], k: int) -> int:
    shortest = float('inf')                                 # Track the shortest valid subarray length
    queue = deque([])                                       # Initialise a deque to store (sum, length) pairs
    total = currLen = 0                                     # Initialise counters to track current sum and length

    for i, n in enumerate(nums):                            # Iterate through the list elements
        if n < 0:                                           # Check if the element is negative
            if total + n <= 0:                              # Check if the sum will be <= 0
                queue = deque([])                           # Reset the queue
                total = currLen = 0                         # Reset the counters
                continue                                    # Skip to next iteration
            else:
                removed, removeLen = queue.pop()            # Pop the tuple from the end of the queue
                curr = n + removed                          # Add and store the removed element value to the curr-ele
                stackLength = 1 + removeLen                 # Increment and store the removed length

                while queue and curr < 0:                   # While curr-val is less than zero
                    removed, removeLen = queue.pop()        # Pop the tuple from the end of the queue
                    curr += removed                         # Add the removed value to the current element
                    stackLength += removeLen                # Add the removed length

                total += n                                  # Increment the total counter by the current element value
                queue.append((curr, stackLength))           # Push the tuple at the end of the queue
                currLen += 1                                # Increment the counter
        else:
            queue.append((n, 1))                            # Append the tuple into the queue
            total += n                                      # Increment the counter by element value
            currLen += 1                                    # Increment the length counter

        while queue and total >= k:                         # While the curr-window sum exceeds k
            shortest = min(shortest, currLen)               # Compute and store the min-val
            removed, removeLen = queue.popleft()            # Pop the tuple from the start of the queue
            total -= removed                                # Decrement the total counter by the removed ele-val
            currLen -= removeLen                            # Decrement the length counter by the removed len-val

    return shortest if shortest <= len(nums) else -1        # Return the result
