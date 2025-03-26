"""
2948. Make Lexicographically Smallest Array by Swapping Elements [MEDIUM]

You are given a 0-indexed array of positive integers nums and a positive integer limit.

In one operation, you can choose any two indices i and j and swap nums[i] and nums[j] if |nums[i] - nums[j]| <= limit.

Return the lexicographically smallest array that can be obtained by performing the operation any number of times.

An array a is lexicographically smaller than an array b if in the first position where a and b differ, array a has an
element that is less than the corresponding element in b. For example, the array [2,10,3] is lexicographically smaller
than the array [10,2,3] because they differ at index 0 and 2 < 10.


Example 1:
Input: nums = [1,5,3,9,8], limit = 2
Output: [1,3,5,8,9]

Explanation: Apply the operation 2 times:
- Swap nums[1] with nums[2]. The array becomes [1,3,5,9,8]
- Swap nums[3] with nums[4]. The array becomes [1,3,5,8,9]
We cannot obtain a lexicographically smaller array by applying any more operations.
Note that it may be possible to get the same result by doing different operations.


Example 2:
Input: nums = [1,7,6,18,2,1], limit = 3
Output: [1,6,7,18,1,2]

Explanation: Apply the operation 3 times:
- Swap nums[1] with nums[2]. The array becomes [1,6,7,18,2,1]
- Swap nums[0] with nums[4]. The array becomes [2,6,7,18,1,1]
- Swap nums[0] with nums[5]. The array becomes [1,6,7,18,1,2]
We cannot obtain a lexicographically smaller array by applying any more operations.


Example 3:
Input: nums = [1,7,28,19,10], limit = 3
Output: [1,7,28,19,10]

Explanation: [1,7,28,19,10] is the lexicographically smallest array we can obtain because we cannot apply the operation
on any two indices.


Constraints:

    -> 1 <= nums.length <= 10^5
    -> 1 <= nums[i] <= 10^9
    -> 1 <= limit <= 10^9


Concepts: Custom Sorting
"""


# Optimised Solution
def lexicographicallySmallestArray(nums: list[int], limit: int) -> list[int]:
    ordered_nums = sorted(nums)                                     # Sort the input list for reference
    prev = ordered_nums[0]                                          # Set a pointer at the first sorted element
    num_to_group = {}                                               # Dict to group numbers
    current_group = 0                                               # Counter to track curr-group
    group_start = [0]                                               # List to track group starts

    for i, x in enumerate(ordered_nums):                            # Iterate through the sorted list
        # Check if diff b/w curr & prev is greater than the limit
        if x - prev > limit:
            current_group += 1                                      # Increment the counter
            group_start.append(i)                                   # Append the curr-idx to the list

        num_to_group[x] = current_group                             # Assign the curr-group to the element
        prev = x                                                    # Update the pointer to the curr-ele

    result = []                                                     # List to store the result
    for x in nums:                                                  # Iterate through the input list
        group = num_to_group[x]                                     # Obtain the group for the curr-ele
        result.append(ordered_nums[group_start[group]])             # Append the element to the result list
        group_start[group] += 1                                     # Increment the group start idx

    return result                                                   # Return the result
