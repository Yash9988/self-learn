"""
3152. Special Array II [MEDIUM]

An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

You are given an array of integer nums and a 2D integer matrix queries, where for queries[i] = [from_i, to_i] your task
is to check that _subarray_ nums[from_i...to_i] is special or not.

Return an array of booleans answer such that answer[i] is true if nums[from_i...to_i] is special.


Example 1:
Input: nums = [3,4,1,2,6], queries = [[0,4]]
Output: [false]

Explanation: The subarray is [3,4,1,2,6]. 2 and 6 are both even.


Example 2:
Input: nums = [4,3,1,6], queries = [[0,2],[2,3]]
Output: [false,true]

Explanation:

    - The subarray is [4,3,1]. 3 and 1 are both odd. So the answer to this query is false.
    - The subarray is [1,6]. There is only one pair: (1,6) and it contains numbers with different parity. So the answer to
      this query is true.


Constraints:

    -> 1 <= nums.length <= 10^5
    -> 1 <= nums[i] <= 10^5
    -> 1 <= queries.length <= 10^5
    -> queries[i].length == 2
    -> 0 <= queries[i][0] <= queries[i][1] <= nums.length - 1


Concepts: Prefix Sum
"""
from itertools import accumulate


# My Solution (TLE)
def isArraySpecial(nums: list[int], queries: list[list[int]]) -> list[bool]:

    res = []                                                        # List to store the result
    for s, e in queries:                                            # Iterate through the queries
        p, f = nums[s] % 2, True                                    # Compute the initial parity and initialise a flag
        for i in range(s, e + 1, 2):                                # Iterate through the odd indices
            if p != nums[i] % 2:                                    # Check if the parity doesn't match
                f = False                                           # Unset the flag

            if not f:                                               # Check if the flag is unset
                break                                               # Break out of the loop

        for i in range(s + 1, e + 1, 2):                            # Iterate through the even indices
            if p == nums[i] % 2:                                    # Check if the parity matches
                f = False                                           # Unset the flag

            if not f:                                               # Check if the flag is unset
                break                                               # Break out of the loop

        res.append(f)                                               # Append the flag state in the list

    return res                                                      # Return the result


# Optimised Solution
def isArraySpecial_op(nums: list[int], queries: list[list[int]]) -> list[bool]:

    runningSum = 0                                                  # Counter to track running sum
    partialSum = []                                                 # List to store partial sums
    oddEven = None                                                  # Counter to track parity

    for num in nums:                                                # Iterate through the nums
        if num % 2 == oddEven:                                      # Check if the parity matches the prev-num
            runningSum += 1                                         # Increment the counter

        oddEven = num % 2                                           # Compute the parity of curr-num
        partialSum.append(runningSum)                               # Append the counter to the list

    out = []                                                        # List to store the result

    for start, end in queries:                                      # Iterate through the queries

        # Compare the prefix-sum at the indexes for equality and append the result to the list
        out.append(partialSum[start] == partialSum[end])

    return out                                                      # Return the result


# Shortest Solution
def isArraySpecial_sh(nums: list[int], queries: list[list[int]]) -> list[bool]:
    ps = list(accumulate([(a ^ b) & 1 == 0 for a, b in zip(nums, nums[1:])], initial=0))
    return [ps[f] == ps[t] for f, t in queries]
