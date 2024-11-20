"""
2461. Maximum Sum of Distinct Subarrays With Length K [MEDIUM]

You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that
meet the following conditions:

    - The length of the subarray is k, and
    - All the elements of the subarray are distinct.

Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.


Example 1:
Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15

Explanation: The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions


Example 2:
Input: nums = [4,4,4], k = 3
Output: 0

Explanation: The subarrays of nums with length 3 are:
- [4,4,4] which does not meet the requirements because the element 4 is repeated.
We return 0 because no subarrays meet the conditions.


Constraints:

    -> 1 <= k <= nums.length <= 10^5
    -> 1 <= nums[i] <= 10^5


Concepts: Double Pointers
"""


# Optimal Solution
def maximumSubarraySum_op(nums: list[int], k: int) -> int:
    n = len(nums)                                               # Compute the length of the list
    elements = set()                                            # Initialise a set for storing unique elements
    current_sum = 0                                             # Initialise a counter to track the window-sum
    max_sum = 0                                                 # Initialise a counter to track the max-sum
    begin = 0                                                   # Initialise a pointer to track the window beginning

    for end in range(n):                                        # Iterate through the list
        if nums[end] not in elements:                           # Check if the curr-ele isn't present in the set
            current_sum += nums[end]                            # Increment the counter with the element value
            elements.add(nums[end])                             # Add the element to the set

            if end - begin + 1 == k:                            # Check of the window is of desired length
                if current_sum > max_sum:                       # Check if the curr-sum is greater than max-sum
                    max_sum = current_sum                       # Update the max-sum value

                current_sum -= nums[begin]                      # Decrement the counter with ele-val at window start
                elements.remove(nums[begin])                    # Remove the element at window start from the set
                begin += 1                                      # Increment the pointer

        else:
            while nums[begin] != nums[end]:                     # While elements at window start and end are different
                current_sum -= nums[begin]                      # Decrement the counter with ele-val at window start
                elements.remove(nums[begin])                    # Remove the element at window start from the set
                begin += 1                                      # Increment the pointer

            begin += 1                                          # Increment the pointer

    return max_sum                                              # Return the result


# Alternate Solution
def maximumSubarraySum_alt(nums: list[int], k: int) -> int:
    res = 0                                                     # Initialise a counter to track the max-sum
    prev_idx = {}                                               # Initialise a dict to track prev index of a num
    cur_sum = 0                                                 # Initialise a counter to track window sum

    l = 0                                                       # Initialise window start pointer

    for r in range(len(nums)):                                  # Iterate through the list
        cur_sum += nums[r]                                      # Increment the counter with element value

        i = prev_idx.get(nums[r], -1)                           # Obtain the previous index of the element

        while l <= i or r - l + 1 > k:                          # Check if pointer `<=` prev-idx or window `>` desired length
            cur_sum -= nums[l]                                  # Decrement the counter by element value at window start
            l += 1                                              # Increment the pointer

        if r - l + 1 == k:                                      # Check if the window is of desired length
            res = max(res, cur_sum)                             # Update the counter with max-val

        prev_idx[nums[r]] = r                                   # Update the prev-idx of the element

    return res                                                  # Return the result