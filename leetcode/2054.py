"""
2054. Two Best Non-Overlapping Events [MEDIUM]

You are given a 0-indexed 2D integer array of events where events[i] = [startTime_i, endTime_i, value_i]. The i-th event
starts at startTime_i and ends at endTime_i, and if you attend this event, you will receive a value of value_i. You can
choose at most two non-overlapping events to attend such that the sum of their values is maximized.

Return this maximum sum.

Note that the start time and end time is inclusive: that is, you cannot attend two events where one of them starts and
the other ends at the same time. More specifically, if you attend an event with end time t, the next event must start at
or after t + 1.


Example 1:
Input: events = [[1,3,2],[4,5,2],[2,4,3]]
Output: 4

Explanation: Choose the green events, 0 and 1 for a sum of 2 + 2 = 4.


Example 2:
Input: events = [[1,3,2],[4,5,2],[1,5,5]]
Output: 5

Explanation: Choose event 2 for a sum of 5.

Example 3:
Input: events = [[1,5,3],[1,5,1],[6,6,5]]
Output: 8

Explanation: Choose events 0 and 2 for a sum of 3 + 5 = 8.


Constraints:

    -> 2 <= events.length <= 10^5
    -> events[i].length == 3
    -> 1 <= startTimei <= endTimei <= 10^9
    -> 1 <= valuei <= 10^6


Concepts: Binary Search, Greedy Sort
"""
from bisect import bisect_right


# Optimised Solution
def maxTwoEvents_op(events: list[list[int]]) -> int:
    max_weights = [0]                                               # List to track max-start values
    max_weight_ends = [-1]                                          # List to track end-times for max-start values

    events.sort(key=lambda x: x[1])                                 # Sort the event list by end-times

    max_two = 0                                                     # Counter to track the max-sum of 2 events

    for start, end, weight in events:                               # Iterate through the events
        index = bisect_right(max_weight_ends, start - 1) - 1        # Compute the index for end-time in max-val list

        # Check if sum b/w curr-wt and idx-wt is greater than the counter value
        if weight + max_weights[index] > max_two:
            max_two = weight + max_weights[index]                   # Update the counter value with the max-sum

        # Check if curr-wt is greater than last max-start weight
        if weight > max_weights[-1]:
            max_weights.append(weight)                              # Append the curr-wt to max-start list
            max_weight_ends.append(end)                             # Append the corresponding end-time to max-end list

    return max_two                                                  # Return the result


# Alternate Solution
def maxTwoEvents_alt(events: list[list[int]]) -> int:
    proc = []                                                       # List to store custom event tuples
    ans = m = 0                                                     # Track max-vals of started & ended events so far

    for s, e, v in events:                                          # Iterate through the events
        proc.append((s, True, v))                                   # Append event start tuple: (time, is_start, val)
        proc.append((e + 1, False, v))                              # Append event end tuple: using e+1 (inclusive)

    proc.sort()                                                     # Sort the list by time

    for time, is_start, val in proc:                                # Iterate through event tuples
        if is_start:                                                # Check if the tuple is an event-start
            ans = max(ans, m + val)                                 # Update the counter with max-sum so far
        else:
            m = max(m, val)                                         # Update the counter with max-val of an ended event

    return ans                                                      # Return the result
