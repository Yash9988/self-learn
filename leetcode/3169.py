"""
3169. Count Days Without Meetings [MEDIUM]

You are given a positive integer days representing the total number of days an employee is available for work
(starting from day 1). You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents
the starting and ending days of meeting i (inclusive).

Return the count of days when the employee is available for work but no meetings are scheduled.

Note: The meetings may overlap.


Example 1:
Input: days = 10, meetings = [[5,7],[1,3],[9,10]]
Output: 2

Explanation:
There is no meeting scheduled on the 4th and 8th days.


Example 2:
Input: days = 5, meetings = [[2,4],[1,3]]
Output: 1

Explanation:
There is no meeting scheduled on the 5th day.


Example 3:
Input: days = 6, meetings = [[1,6]]
Output: 0

Explanation:
Meetings are scheduled for all working days.


Constraints:

    -> 1 <= days <= 10^9
    -> 1 <= meetings.length <= 10^5
    -> meetings[i].length == 2
    -> 1 <= meetings[i][0] <= meetings[i][1] <= days


Concepts: Sorting, Counting
"""


# Optimised Solution
def countDays(days: int, meetings: list[list[int]]) -> int:
    meetings.sort()                                                 # Sort the input list

    meeting_days_count = 0                                          # Counter to track total meeting days
    current_start = current_end = -1                                # Pointers to track start and end of a period

    for start, end in meetings:                                     # Iterate through the meetings
        if start > current_end:                                     # Check if the start is greater than the end pointer
            if current_end != -1:                                   # Check if the end pointer is initialised
                # Compute and increment the meeting days in the current period
                meeting_days_count += current_end - current_start + 1

            current_start, current_end = start, end                 # Update the pointers for the current period
        else:
            current_end = max(current_end, end)                     # Extend the period end pointer to max-val

    if current_end != -1:                                           # Check if the end pointer is initialised
        meeting_days_count += current_end - current_start + 1       # Compute and increment the counter with the diff

    return days - meeting_days_count                                # Compute and return the result
