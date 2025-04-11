"""
2818. Apply Operations to Maximize Score [HARD]

You are given an array nums of n positive integers and an integer k.

Initially, you start with a score of 1. You have to maximize your score by applying the following operation at most k times:

    - Choose any non-empty subarray nums[l, ..., r] that you haven't chosen previously.
    - Choose an element x of nums[l, ..., r] with the highest prime score. If multiple such elements exist, choose the
      one with the smallest index.
    - Multiply your score by x.

Here, nums[l, ..., r] denotes the subarray of nums starting at index l and ending at the index r, both ends being inclusive.

The prime score of an integer x is equal to the number of distinct prime factors of x. For example, the prime score of
300 is 3 since 300 = 2 * 2 * 3 * 5 * 5.

Return the maximum possible score after applying at most k operations.

Since the answer may be large, return it modulo 10^9 + 7.


Example 1:
Input: nums = [8,3,9,3,8], k = 2
Output: 81

Explanation: To get a score of 81, we can apply the following operations:
- Choose subarray nums[2, ..., 2]. nums[2] is the only element in this subarray. Hence, we multiply the score by nums[2].
  The score becomes 1 * 9 = 9.
- Choose subarray nums[2, ..., 3]. Both nums[2] and nums[3] have a prime score of 1, but nums[2] has the smaller index.
  Hence, we multiply the score by nums[2]. The score becomes 9 * 9 = 81.
It can be proven that 81 is the highest score one can obtain.


Example 2:
Input: nums = [19,12,14,6,10,18], k = 3
Output: 4788

Explanation: To get a score of 4788, we can apply the following operations:
- Choose subarray nums[0, ..., 0]. nums[0] is the only element in this subarray. Hence, we multiply the score by nums[0].
  The score becomes 1 * 19 = 19.
- Choose subarray nums[5, ..., 5]. nums[5] is the only element in this subarray. Hence, we multiply the score by nums[5].
  The score becomes 19 * 18 = 342.
- Choose subarray nums[2, ..., 3]. Both nums[2] and nums[3] have a prime score of 2, but nums[2] has the smaller index.
  Hence, we multipy the score by nums[2]. The score becomes 342 * 14 = 4788.
It can be proven that 4788 is the highest score one can obtain.


Constraints:

    -> 1 <= nums.length == n <= 10^5
    -> 1 <= nums[i] <= 10^5
    -> 1 <= k <= min(n * (n + 1) / 2, 10^9)


Concepts: Prime Factors, Double pointers, Sieve, Subarray
"""


# Optimised Solution

# Compute the number of prime factors for each number in the given range
MOD = 10 ** 9 + 7
MX = 10 ** 5 + 1
omega = [0] * MX

for i in range(2, MX):
    if omega[i] == 0:
        for j in range(i, MX, i):
            omega[j] += 1


def maximumScore(nums: list[int], k: int) -> int:
    n = len(nums)                                                   # Obtain the size of the list
    left = [-1] * n                                                 # Track num-idx with greater prime-score to the left
    right = [n] * n                                                 # Track num-idx with greater prime-score to the right
    st = []                                                         # List to track processed indices

    for i, v in enumerate(nums):                                    # Iterate through the nums
        while st and omega[nums[st[-1]]] < omega[v]:                # While curr-ele prime score is greater
            right[st.pop()] = i                                     # Pop the stack-idx and update it's corr-val

        if st:                                                      # Check if the stack is non-empty
            left[i] = st[-1]                                        # Update the corr-val

        st.append(i)                                                # Append the curr-idx to the list

    ans = 1                                                         # Counter to track the score

    # Iterate though the range of list
    for i, v, l, r in sorted(zip(range(n), nums, left, right), key=lambda x: -x[1]):
        tot = (i - l) * (r - i)                                     # Compute freq of highest prime score element

        if tot >= k:                                                # Check if the freq is greater/equal to `k`
            ans *= pow(v, k, MOD) % MOD                             # Update the result counter
            break                                                   # Break out of the loop

        ans *= pow(v, tot, MOD) % MOD                               # Update the result counter
        k -= tot                                                    # Decrement the counter

    return ans                                                      # Return the result
