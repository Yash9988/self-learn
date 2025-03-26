"""
2342. Max Sum of a Pair With Equal Sum of Digits [MEDIUM]

You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j,
such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the
conditions.


Example 1:
Input: nums = [18,43,36,13,7]
Output: 54

Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.


Example 2:
Input: nums = [10,12,19,14]
Output: -1

Explanation: There are no two numbers that satisfy the conditions, so we return -1.


Constraints:

    -> 1 <= nums.length <= 10^5
    -> 1 <= nums[i] <= 10^9


Concepts: Max Pairing
"""
from collections import defaultdict


# My Solution
def maximumSum(nums: list[int]) -> int:
    sums = defaultdict(list)                                        # Dict to track similar-summed numbers
    for num in nums:                                                # Iterate through the numbers
        key = sum(map(int, list(str(num))))                         # Compute the sum of its digits
        sums[key].append(num)                                       # Append the num to the corr-sum-key

    res = -1                                                        # Counter to track the result
    for val in sums.values():                                       # Iterate through the dict-vals
        if len(val) > 1:                                            # Check if there's more than 2 elements in the list
            temp = sum(sorted(val)[-2:])                            # Sort and compute the sum of the largest 2 elements
            res = max(res, temp)                                    # Update the counter with max-val

    return res                                                      # Return the result


# Optimised Solution
def maximumSum_op(nums: list[int]) -> int:
    d, mx = dict(), -1                                              # Dict to track similar pairs and counter for result

    for num in nums:                                                # Iterate through the numbers
        # Compute the sum of the num-digits
        sm, n = 0, num
        while n:
            sm += n % 10
            n //= 10

        if sm in d:                                                 # Check if sum-key already present in the dict
            if d[sm][0] <= num:                                     # Check if num is greater than the first element
                d[sm][1] = d[sm][0]                                 # Shift the smaller element to the second index
                d[sm][0] = num                                      # Substitute the num at the first index
            elif d[sm][1] < num:                                    # Check if num is smaller than the second element
                d[sm][1] = num                                      # Substitute the num at the second index
        else:
            d[sm] = [num, -1]                                       # Initialise key with [num, -1] pair

    for k in d:                                                     # Iterate through the dict-keys
        if d[k][1] != -1:                                           # Check if the second element is not -1
            sm = d[k][0] + d[k][1]                                  # Compute the pair-sum
            if sm > mx:                                             # Check if the sum is greater than counter value
                mx = sm                                             # Update the counter with max-val

    return mx                                                       # Return the result
