"""
2593. Find Score of an Array After Marking All Elements [MEDIUM]

You are given an array nums consisting of positive integers.

Starting with score = 0, apply the following algorithm:

    - Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest
      index.
    - Add the value of the chosen integer to score.
    - Mark the chosen element and its two adjacent elements if they exist.
    - Repeat until all the array elements are marked.

Return the score you get after applying the above algorithm.


Example 1:
Input: nums = [2,1,3,4,5,2]
Output: 7

Explanation: We mark the elements as follows:
- 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2,1,3,4,5,2].
- 2 is the smallest unmarked element, so we mark it and its left adjacent element: [2,1,3,4,5,2].
- 4 is the only remaining unmarked element, so we mark it: [2,1,3,4,5,2].
Our score is 1 + 2 + 4 = 7.


Example 2:
Input: nums = [2,3,5,1,3,2]
Output: 5

Explanation: We mark the elements as follows:
- 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2,3,5,1,3,2].
- 2 is the smallest unmarked element, since there are two of them, we choose the left-most one, so we mark the one at
  index 0 and its right adjacent element: [2,3,5,1,3,2].
- 2 is the only remaining unmarked element, so we mark it: [2,3,5,1,3,2].
Our score is 1 + 2 + 2 = 5.


Constraints:

    -> 1 <= nums.length <= 10^5
    -> 1 <= nums[i] <= 10^6


Concepts: Heap, Deque
"""
from heapq import heapify, heappop
from collections import deque


# My Solution
def findScore(nums: list[int]) -> int:
    n = len(nums)                                                   # Obtain the size of the list
    marked = set([])                                                # Set to store the marked indices
    heap = [(nums[i], i) for i in range(n)]                         # Initialise a tuple list of form: (value, index)
    heapify(heap)                                                   # Transform the list into heap

    res = 0                                                         # Counter to track the value sum
    while len(marked) < n:                                          # While the size of the set is smaller than the list
        while heap[0][1] in marked:                                 # While the min-ele idx is present in the set
            heappop(heap)                                           # Pop out the tuple from the heap

        val, idx = heappop(heap)                                    # Pop out the smallest unmarked tuple from heap

        res += val                                                  # Increment the counter by the ele-val
        marked.update([max(0, idx - 1), idx, min(n - 1, idx + 1)])  # Append the current & adj-indices to the set

    return res                                                      # Return the result


# Optimised Solution
def findScore_op(nums: list[int]) -> int:
    n = len(nums)                                                   # Obtain the size of the list
    q = deque()                                                     # Queue to store values
    score = 0                                                       # Counter to track the score

    for i in range(n):                                              # Iterate through the list range
        if q and nums[i] >= q[-1]:                                  # Check if curr-ele `>=` to the last queue element
            skip = False                                            # Unset the skip-flag

            while q:                                                # While the queue is non-empty
                add = q.pop()                                       # Pop the last element from the queue
                if not skip:                                        # Check if the flag is unset
                    score += add                                    # Increment the score counter

                skip = not skip                                     # Flip the skip-flag

            continue                                                # Skip to the next iteration

        q.append(nums[i])                                           # Append the curr-val to the queue

    skip = False                                                    # Unset the skip-flag
    while q:                                                        # While the queue is non-empty
        add = q.pop()                                               # Pop the last element from the queue
        if not skip:                                                # Check if the flag is unset
            score += add                                            # Increment the score counter

        skip = not skip                                             # Flip the skip-flag

    return score                                                    # Return the result
