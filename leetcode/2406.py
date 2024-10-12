"""
2406. Divide Intervals Into Minimum Number of Groups [MEDIUM]

You are given a 2D integer array intervals where intervals[i] = [left_i, right_i] represents the inclusive interval
[left_i, right_i].

You have to divide the intervals into one or more groups such that each interval is in exactly one group, and no two
intervals that are in the same group intersect each other.

Return the minimum number of groups you need to make.

Two intervals intersect if there is at least one common number between them. For example, the intervals [1, 5] and
[5, 8] intersect.


Example 1:

Input: intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
Output: 3

Explanation: We can divide the intervals into the following groups:
- Group 1: [1, 5], [6, 8].
- Group 2: [2, 3], [5, 10].
- Group 3: [1, 10].
It can be proven that it is not possible to divide the intervals into fewer than 3 groups.


Example 2:

Input: intervals = [[1,3],[5,6],[8,10],[11,13]]
Output: 1

Explanation: None of the intervals overlap, so we can put all of them in one group.


Constraints:

    -> 1 <= intervals.length <= 10^5
    -> intervals[i].length == 2
    -> 1 <= left_i <= right_i <= 10^6


Concepts: Heap, Line Sweep, Binary Search
"""
from heapq import *


# Optimised Solution
def minGroups_op(intervals: list[list[int]]) -> int:
    pq = []                                             # Initialise a heap
    for left, right in sorted(intervals):               # Iterate through the sorted list of intervals
        if pq and pq[0] < left:                         # Check if the min-heap value is smaller than start of interval
            heappop(pq)                                 # Pop out the "expired" interval from the heap
        heappush(pq, right)                             # Push in the end value of current interval into the heap
    return len(pq)                                      # Return the length of the heap


# Alternate Solution
def minGroups_alt(intervals: list[list[int]]) -> int:
    A = []                                              # Initialise a list
    for a, b in intervals:                              # Iterate through all the intervals
        A.append([a, 1])                                # Append the start of the interval with an "occupied" flag
        A.append([b + 1, -1])                           # Append the end of the interval with a "released" flag

    res = cur = 0                                       # Initialise result and current counter
    for a, diff in sorted(A):                           # Sort and iterate through the list we created
        cur += diff                                     # Accumulate the difference in the current counter
        res = max(res, cur)                             # Update the result counter to hold the maximum value so far
    return res                                          # Return the result


# My Solution (TODO: Figure out why it doesn't work, even tho it should :3)
# def minGroups(intervals: list[list[int]]) -> int:
#     groups = []
#     for l, r in intervals:
#         flag = True
#         for group in groups:
#             il, ir = bisect_right(group, l), bisect_right(group, r)
#             if il == ir and not il % 2:
#                 group[il:ir] = [l, r]
#                 flag = False
#                 break
#
#         if flag:
#             groups.append([l, r])
#
#     print(groups)
#     return len(groups)
