"""
1310. XOR Queries of a Subarray [MEDIUM]

You are given an array arr of positive integers. You are also given the array queries where queries[i] = [left_i, right_i].

For each query i compute the XOR of elements from left_i to right_i
(that is, arr[left_i] XOR arr[left_i + 1] XOR ... XOR arr[right_i] ).

Return an array answer where answer[i] is the answer to the ith query.


Example 1:

Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
Output: [2,7,14,8]
Explanation:
The binary representation of the elements in the array are:
1 = 0001
3 = 0011
4 = 0100
8 = 1000
The XOR values for queries are:
[0,1] = 1 xor 3 = 2
[1,2] = 3 xor 4 = 7
[0,3] = 1 xor 3 xor 4 xor 8 = 14
[3,3] = 8

Example 2:

Input: arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
Output: [8,0,4,4]


Constraints:

    - 1 <= arr.length, queries.length <= 3 * 104
    - 1 <= arr[i] <= 109
    - queries[i].length == 2
    - 0 <= left_i <= right_i < arr.length

"""


# My Solution
def xorQueries(arr: list[int], queries: list[list[int]]) -> list[int]:
    dp = arr[:1]                                        # Initialise DP with the first array element
    for a in arr[1:]:                                   # Iterate from the second to last element
        dp.append(dp[-1] ^ a)                           # Perform XOR with the last element and append

    res = []                                            # Initialise an empty "result" list
    for l, r in queries:                                # Iterate through all query pairs
        ans = dp[r] ^ dp[l - 1] if l else dp[r]         # Remove the excess "XOR-sum" using the left index
        res.append(ans)                                 # Append the answer in the result array

    return res                                          # Return the result


# Optimised Solution (Smaller Space complexity with in-place operations)
def xorQueries_op(arr: list[int], queries: list[list[int]]) -> list[int]:
    for i in range(len(arr) - 1):
        arr[i + 1] ^= arr[i]

    return [arr[j] ^ arr[i - 1] if i else arr[j] for i, j in queries]
