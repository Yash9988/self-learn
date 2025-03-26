"""
3312. Sorted GCD Pair Queries [HARD]

You are given an integer array nums of length n and an integer array queries.

Let gcdPairs denote an array obtained by calculating the _GCD_ of all possible pairs (nums[i], nums[j]), where
0 <= i < j < n, and then sorting these values in ascending order.

For each query queries[i], you need to find the element at index queries[i] in gcdPairs.

Return an integer array answer, where answer[i] is the value at gcdPairs[queries[i]] for each query.

The term gcd(a, b) denotes the greatest common divisor of a and b.


Example 1:

Input: nums = [2,3,4], queries = [0,2,2]
Output: [1,2,2]

Explanation:
gcdPairs = [gcd(nums[0], nums[1]), gcd(nums[0], nums[2]), gcd(nums[1], nums[2])] = [1, 2, 1].

After sorting in ascending order, gcdPairs = [1, 1, 2].

So, the answer is [gcdPairs[queries[0]], gcdPairs[queries[1]], gcdPairs[queries[2]]] = [1, 2, 2].


Example 2:

Input: nums = [4,4,2,1], queries = [5,3,1,0]
Output: [4,2,1,1]

Explanation:
gcdPairs sorted in ascending order is [1, 1, 1, 2, 2, 4].


Example 3:

Input: nums = [2,2], queries = [0,0]
Output: [2,2]

Explanation:
gcdPairs = [2].


Constraints:

    -> 2 <= n == nums.length <= 10^5
    -> 1 <= nums[i] <= 5 * 10^4
    -> 1 <= queries.length <= 10^5
    -> 0 <= queries[i] < n * (n - 1) / 2


Concepts: Counting, Binary Search
Solution: https://leetcode.com/problems/sorted-gcd-pair-queries/solutions/5883785/actual-explanations-and-dry-run-of-what-we-do-and-why-we-do-it-this-way
"""
from bisect import bisect_right
from collections import defaultdict


def gcdValues(nums: list[int], queries: list[int]) -> list[int]:
    max_gcd = max(nums)                             # Compute the max-val in the list
    counter = defaultdict(int)                      # Initialise a count dict
    for n in nums:                                  # Iterate through all numbers
        counter[n] += 1                             # Increment the count of corresponding value

    gcd = [0] * (max_gcd + 1)                       # Initialise a list for storing GCD

    for i in range(max_gcd, 0, -1):                 # Iterate till zero from the max-gcd value
        count = 0                                   # Initialise counter to track instances & multiples of `i`
        for j in range(i, max_gcd + 1, i):          # Iterate in steps of `i` to obtain all multiples
            count += counter[j]                     # Increment the counter by the frequency of element

        gcd[i] = count * (count - 1) // 2           # Compute the total possible pairs, given the counter value

        for j in range(2 * i, max_gcd + 1, i):      # Iterate from the 2nd multiple of `i` till the max-gcd value
            gcd[i] -= gcd[j]                        # Use exclusion to remove double counted pairs

    prefix = [0] * (max_gcd + 1)                    # Initialise a list to store prefix sum of GCDs
    curr = 0                                        # Initialise a curr-counter
    for i in range(1, max_gcd + 1):                 # Iterate through the GCD list
        curr += gcd[i]                              # Add the gcd value at the current index
        prefix[i] += curr                           # Update the prefix list with the curr-counter value

    res = []                                        # Initialise a result list
    for q in queries:                               # Iterate through the queries
        res.append(bisect_right(prefix, q))         # Use binary search to find the required GCD value

    return res                                      # Return the result
