"""
2127. Maximum Employees to Be Invited to a Meeting [HARD]

A company is organizing a meeting and has a list of n employees, waiting to be invited. They have arranged for a large
circular table, capable of seating any number of employees.

The employees are numbered from 0 to n - 1. Each employee has a favorite person, and they will attend the meeting only
if they can sit next to their favorite person at the table. The favorite person of an employee is not themself.

Given a 0-indexed integer array favorite, where favorite[i] denotes the favorite person of the ith employee, return the
maximum number of employees that can be invited to the meeting.


Example 1:
Input: favorite = [2,2,1,2]
Output: 3

Explanation:
The above figure shows how the company can invite employees 0, 1, and 2, and seat them at the round table.
All employees cannot be invited because employee 2 cannot sit beside employees 0, 1, and 3, simultaneously.
Note that the company can also invite employees 1, 2, and 3, and give them their desired seats.
The maximum number of employees that can be invited to the meeting is 3.


Example 2:
Input: favorite = [1,2,0]
Output: 3

Explanation:
Each employee is the favorite person of at least one other employee, and the only way the company can invite them is if
they invite every employee. The seating arrangement will be the same as that in the figure given in example 1:
- Employee 0 will sit between employees 2 and 1.
- Employee 1 will sit between employees 0 and 2.
- Employee 2 will sit between employees 1 and 0.
The maximum number of employees that can be invited to the meeting is 3.


Example 3:
Input: favorite = [3,0,1,4,1]
Output: 4

Explanation:
The above figure shows how the company will invite employees 0, 1, 3, and 4, and seat them at the round table.
Employee 2 cannot be invited because the two spots next to their favorite employee 1 are taken.
So the company leaves them out of the meeting.
The maximum number of employees that can be invited to the meeting is 4.


Constraints:

    -> n == favorite.length
    -> 2 <= n <= 10^5
    -> 0 <= favorite[i] <= n - 1
    -> favorite[i] != i


Concepts: Deque, BFS, Topological Sorting, Cycle Detection


Link: https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/solutions/6329874/scenario-analysis-topological-sorting-cycle-detection-with-example
"""
from collections import deque


# Optimised Solution
def maximumInvitations(favorite: list[int]) -> int:
    n = len(favorite)                                               # Obtain the size of the list
    levels = [1] * n                                                # List to track the levels
    indegree = [0] * n                                              # List to track node in-degree

    for i in range(n):                                              # Iterate through the range of the list
        indegree[favorite[i]] += 1                                  # Increment the in-degree for the favorite node

    queue = deque()                                                 # Queue to process employees in BFS fashion

    # Iterate and append the nodes with zero in-degree into the queue
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)

    while queue:                                                    # While the queue is non-empty
        node = queue.popleft()                                      # Pop the first element of the queue
        neighbor = favorite[node]                                   # Obtain the corr-favorite node
        indegree[neighbor] -= 1                                     # Decrement the in-degree of the favorite
        levels[neighbor] = levels[node] + 1                         # Increment the level of the favorite
        if indegree[neighbor] == 0:                                 # Check if the favorite's in-degree is zero
            queue.append(neighbor)                                  # Append the node to the queue

    longest_path = max_perimeter = 0                                # Counters to track the length
    for i in range(n):                                              # Iterate through the range of list
        if indegree[i] != 0:                                        # Check if the node's in-degree is non-zero
            circle_start = circle_node = i                          # Set pointers at curr-idx
            indegree[circle_node] -= 1                              # Decrement the node's in-degree
            circle_perimeter = 1                                    # Set the perimeter to 1

            while favorite[circle_node] != circle_start:            # While the favorite node isn't the circle start
                circle_node = favorite[circle_node]                 # Replace the node with its favorite
                indegree[circle_node] -= 1                          # Decrement the node's in-degree
                circle_perimeter += 1                               # Increment the perimeter counter

            if circle_perimeter == 2:                               # Check if the perimeter only includes 2 nodes
                # Increment the counter with each node's levels
                longest_path += levels[circle_start] + levels[circle_node]
            else:
                # Update the counter with the max-val
                max_perimeter = max(max_perimeter, circle_perimeter)

    return max(max_perimeter, longest_path)                         # Return the result
