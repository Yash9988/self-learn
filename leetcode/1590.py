"""
1590. Make Sum Divisible by P [MEDIUM]

Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the
remaining elements is divisible by p. It is not allowed to remove the whole array.

Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

A subarray is defined as a contiguous block of elements in the array.


Example 1:

Input: nums = [3,1,4,2], p = 6
Output: 1
Explanation: The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the
sum of the remaining elements is 6, which is divisible by 6.


Example 2:

Input: nums = [6,3,5,2], p = 9
Output: 2
Explanation: We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2],
leaving us with [6,3] with sum 9.


Example 3:

Input: nums = [1,2,3], p = 3
Output: 0
Explanation: Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.


Constraints:

    -> 1 <= nums.length <= 105
    -> 1 <= nums[i] <= 109
    -> 1 <= p <= 109


Concepts: Prefix-Sum
"""


def minSubarray(nums: list[int], p: int) -> int:
    target = sum(nums) % p                          # Calculate and store the mod of sum of the input array

    if target == 0:                                 # Check if the target is zero
        return 0                                    # Return zero

    presum = {0: -1}                                # Initialise a hashmap to store prefix-sum of array at each index
    total = 0                                       # Initialise a total-counter
    res = len(nums)                                 # Initialise the result counter to be the length of array
    for i in range(len(nums)):                      # Iterate through the input array
        total += nums[i]                            # Add the current element value to the total-counter
        mod = (total - target) % p                  # Calculate the mod for the difference between total and target
        if mod in presum:                           # Check if calculated mod is present in the hashmap
            res = min(res, i - presum[mod])         # Compare and update the result with the minimum value
        presum[total % p] = i                       # Insert mod of total as key with the current index as its value

    return res if res != len(nums) else -1          # Return the result
