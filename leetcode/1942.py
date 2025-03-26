"""
1942. The Number of the Smallest Unoccupied Chair [MEDIUM]

There is a party where n friends numbered from 0 to n - 1 are attending. There is an infinite number of chairs in this
party that are numbered from 0 to infinity. When a friend arrives at the party, they sit on the unoccupied chair with
the smallest number.

For example, if chairs 0, 1, and 5 are occupied when a friend comes, they will sit on chair number 2.

When a friend leaves the party, their chair becomes unoccupied at the moment they leave. If another friend arrives at
that same moment, they can sit in that chair.

You are given a 0-indexed 2D integer array times, where times[i] = [arrival_i, leaving_i], indicating the arrival and
leaving times of the i-th friend respectively, and an integer targetFriend. All arrival times are distinct.

Return the chair number that the friend numbered targetFriend will sit on.


Example 1:

Input: times = [[1,4],[2,3],[4,6]], targetFriend = 1
Output: 1

Explanation:
- Friend 0 arrives at time 1 and sits on chair 0.
- Friend 1 arrives at time 2 and sits on chair 1.
- Friend 1 leaves at time 3 and chair 1 becomes empty.
- Friend 0 leaves at time 4 and chair 0 becomes empty.
- Friend 2 arrives at time 4 and sits on chair 0.
Since friend 1 sat on chair 1, we return 1.


Example 2:

Input: times = [[3,10],[1,5],[2,6]], targetFriend = 0
Output: 2

Explanation:
- Friend 1 arrives at time 1 and sits on chair 0.
- Friend 2 arrives at time 2 and sits on chair 1.
- Friend 0 arrives at time 3 and sits on chair 2.
- Friend 1 leaves at time 5 and chair 0 becomes empty.
- Friend 2 leaves at time 6 and chair 1 becomes empty.
- Friend 0 leaves at time 10 and chair 2 becomes empty.
Since friend 0 sat on chair 2, we return 2.


Constraints:

    -> n == times.length
    -> 2 <= n <= 10^4
    -> times[i].length == 2
    -> 1 <= arrivali < leavingi <= 10^5
    -> 0 <= targetFriend <= n - 1
    -> Each arrivali time is distinct.


Concepts: Heaps
"""
from heapq import *


# My Solution
def smallestChair(times: list[list[int]], targetFriend: int) -> int:
    taken, avail = [], []                                       # Initialise 2 heaps
    curr = 0                                                    # Initialise seat counter

    times = [(i, time[0], time[1])
             for i, time in enumerate(times)]                   # Modify list to include resp-index w/ each time-tuple
    times.sort(key=lambda x: x[1])                              # Sort the list of tuples by their arrival times

    for time in times:                                          # Iterate through all time tuples
        while taken and taken[0][0] <= time[1]:                 # Check if the occupied seats can be emptied
            heappush(avail, heappop(taken)[1])                  # Pop those seats and append to the available heap

        if time[0] == targetFriend:                             # Check if the index of curr-friend is the required one
            break                                               # Break out of the iteration loop

        if avail:                                               # Check if there are any available seats to allocate
            heappush(taken, (time[2], heappop(avail)))          # Obtain the available seat index and assign as taken
        else:
            heappush(taken, (time[2], curr))                    # Assign the seat index using counter
            curr += 1                                           # Increment the counter

    return heappop(avail) if avail else curr                    # Return the available seat index or curr-counter value


# Alternate Solution
def smallestChair_alt(times: list[list[int]], targetFriend: int) -> int:
    vals = []                                                   # Initialise a list for modified time tuples
    for i, (arrival, leaving) in enumerate(times):              # Iterate through all the time tuples
        vals.append((leaving, 0, i))                            # Append departure times w/ resp-ind (equal comes first)
        vals.append((arrival, 1, i))                            # Append arrival times w/ resp-ind (equal comes second)

    k = 0                                                       # Initialise seat counter
    pq = []                                                     # Initialise a heap for available seats
    mp = {}                                                     # Initialise a dict for player-to-seat mapping
    for _, arrival, i in sorted(vals):                          # Iterate through the sorted list of modified tuples
        if arrival:                                             # Check if it's an arrival-tuple
            if pq:                                              # Check if there are any available seats
                s = heappop(pq)                                 # Pop and obtain the seat index from the heap
            else:
                s = k                                           # Obtain the counter value as seat index, otherwise
                k += 1                                          # Increment the counter
            if i == targetFriend:                               # Check if curr-ind is the required target value
                return s                                        # Return the current seat index
            mp[i] = s                                           # Map the current seat index to the respective friend
        else:
            heappush(pq, mp[i])                                 # Push the mapped seat-index for the curr-friend, else
