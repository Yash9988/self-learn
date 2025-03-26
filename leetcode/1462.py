"""
1462. Course Schedule IV [MEDIUM]

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array
prerequisites where prerequisites[i] = [a_i, b_i] indicates that you must take course a_i first if you want to take
course b_i.

    - For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.

Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course
c, then course a is a prerequisite of course c.

You are also given an array queries where queries[j] = [u_j, v_j]. For the j-th query, you should answer whether course
u_j is a prerequisite of course v_j or not.

Return a boolean array answer, where answer[j] is the answer to the j-th query.


Example 1:
Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
Output: [false,true]

Explanation: The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
Course 0 is not a prerequisite of course 1, but the opposite is true.


Example 2:
Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
Output: [false,false]

Explanation: There are no prerequisites, and each course is independent.


Example 3:
Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
Output: [true,true]


Constraints:

    -> 2 <= numCourses <= 100
    -> 0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2)
    -> prerequisites[i].length == 2
    -> 0 <= a_i, b_i <= numCourses - 1
    -> a_i != b_i
    -> All the pairs [a_i, b_i] are unique.
    -> The prerequisites graph has no cycles.
    -> 1 <= queries.length <= 10^4
    -> 0 <= u_i, v_i <= numCourses - 1
    -> u_i != v_i


Concepts: Hashset, DFS, Topological Sort
"""
from collections import defaultdict


# Optimised Solution
def checkIfPrerequisite(numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
    # Method to explore the course pre-reqs in a DFS fashion
    def dfs(course):
        for postreq in graph[course]:                               # Iterate through the post-reqs of the course
            if postreq not in postreq_set[course]:                  # Check if post-req is absent in the corr-set
                postreq_set[course].add(postreq)                    # Append the post-req to the set
                postreq_set[course].update(dfs(postreq))            # Recursively add the "indirects" to the set

        return postreq_set[course]                                  # Return the set of courses


    graph = defaultdict(list)                                       # Dict to track all the post-reqs for each course
    for prereq, postreq in prerequisites:                           # Iterate through the pre-reqs
        graph[prereq].append(postreq)                               # Append the post-req course to the corr-pre-req

    postreq_set = [set() for _ in range(numCourses)]                # List of sets to store post-reqs for each course

    for i in range(numCourses):                                     # Iterate through the range of courses
        dfs(i)                                                      # Explore its post-reqs

    res = []                                                        # List to store the results
    for prereq, postreq in queries:                                 # Iterate through the queries
        if postreq not in postreq_set[prereq]:                      # Check if the course is not in the corr-set
            res.append(False)                                       # Append False to the list
        else:
            res.append(True)                                        # Append True to the list, otherwise

    return res                                                      # Return the result
