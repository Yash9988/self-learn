"""
2762. Continuous Subarrays [MEDIUM]

You are given a 0-indexed integer array nums. A subarray of nums is called continuous if:

    - Let i, i + 1, ..., j be the indices in the subarray. Then, for each pair of indices i <= i1, i2 <= j,
      0 <= |nums[i1] - nums[i2]| <= 2.

Return the total number of continuous subarrays.

A subarray is a contiguous non-empty sequence of elements within an array.


Example 1:
Input: nums = [5,4,2,4]
Output: 8

Explanation:
Continuous subarray of size 1: [5], [4], [2], [4].
Continuous subarray of size 2: [5,4], [4,2], [2,4].
Continuous subarray of size 3: [4,2,4].
Thereare no subarrys of size 4.
Total continuous subarrays = 4 + 3 + 1 = 8.
It can be shown that there are no more continuous subarrays.


Example 2:
Input: nums = [1,2,3]
Output: 6

Explanation:
Continuous subarray of size 1: [1], [2], [3].
Continuous subarray of size 2: [1,2], [2,3].
Continuous subarray of size 3: [1,2,3].
Total continuous subarrays = 3 + 2 + 1 = 6.


Constraints:

    -> 1 <= nums.length <= 10^5
    -> 1 <= nums[i] <= 10^9


Concepts: Subarray, Deque
"""
from collections import deque


# Optimised Solution
def continuousSubarrays(nums: list[int]) -> int:
    n = len(nums)                                                   # Obtain the size of the list
    l = res = 0                                                     # Initialise left pointer and a result counter
    max_, min_ = deque(), deque()                                   # Deques to track the subarray elements within range

    for r in range(n):                                              # Iterate through the list range
        while min_ and nums[r] < min_[-1]:                          # While the curr-ele is smaller than last min-deque
            min_.pop()                                              # Pop the last element of min-deque
        min_.append(nums[r])                                        # Append the curr-ele to the min-deque

        while max_ and nums[r] > max_[-1]:                          # While the curr-ele is greater than last max-deque
            max_.pop()                                              # Pop the last element of max-deque
        max_.append(nums[r])                                        # Append the curr-ele to the max-deque

        while max_[0] - min_[0] > 2:                                # While the diff b/w first-ele of deque is `>` 2

            # Check if element at left pointer equals first element of min-deque
            if nums[l] == min_[0]:
                min_.popleft()                                      # Pop the first element of the deque

            # Check if element at left pointer equals first element of max-deque
            if nums[l] == max_[0]:
                max_.popleft()                                      # Pop the first element of the deque

            l += 1                                                  # Increment the pointer

        res += r - l + 1                                            # Increment the result counter by the pointer diff

    return res                                                      # Return the result
