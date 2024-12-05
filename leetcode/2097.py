"""
2097. Valid Arrangement of Pairs [HARD]

You are given a 0-indexed 2D integer array pairs where pairs[i] = [start_i, end_i]. An arrangement of pairs is valid if
for every index i where 1 <= i < pairs.length, we have end_i-1 == start_i.

Return any valid arrangement of pairs.

Note: The inputs will be generated such that there exists a valid arrangement of pairs.


Example 1:
Input: pairs = [[5,1],[4,5],[11,9],[9,4]]
Output: [[11,9],[9,4],[4,5],[5,1]]

Explanation:
This is a valid arrangement since end_i-1 always equals start_i.
end_0 = 9 == 9 = start_1
end_1 = 4 == 4 = start_2
end_2 = 5 == 5 = start_3


Example 2:
Input: pairs = [[1,3],[3,2],[2,1]]
Output: [[1,3],[3,2],[2,1]]

Explanation:
This is a valid arrangement since end_i-1 always equals start_i.
end_0 = 3 == 3 = start_1
end_1 = 2 == 2 = start_2
The arrangements [[2,1],[1,3],[3,2]] and [[3,2],[2,1],[1,3]] are also valid.


Example 3:
Input: pairs = [[1,2],[1,3],[2,1]]
Output: [[1,2],[2,1],[1,3]]

Explanation:
This is a valid arrangement since end_i-1 always equals start_i.
end_0 = 2 == 2 = start_1
end_1 = 1 == 1 = start_2


Constraints:

    -> 1 <= pairs.length <= 10^5
    -> pairs[i].length == 2
    -> 0 <= start_i, end_i <= 10^9
    -> start_i != end_i
    -> No two pairs are exactly the same.
    -> There exists a valid arrangement of pairs.


Concepts: Queue, Graphs, DFS, Hierholzer's algorithm
"""
from collections import defaultdict, deque


# Optimised Solution
def validArrangement_op(pairs: list[list[int]]) -> list[list[int]]:
    # Helper method to perform DFS traversal on the graph
    def dfs(curr):
        while graph[curr]:                                          # While the curr-node has adj-nodes
            nextNode = graph[curr].pop()                            # Pop an adj-node
            dfs(nextNode)                                           # Recursively call the method on the adj-node
            path.append((curr, nextNode))                           # Append the node tuple to the result list

    graph = defaultdict(list)                                       # Dict to represent adj-list
    inOutDeg = defaultdict(int)                                     # Dict to track in/out degree difference

    # Build graph and calculate in/out degrees
    for start, end in pairs:                                        # Iterate through the pairs
        graph[start].append(end)                                    # Append the end node to the start node adj-list
        inOutDeg[start] += 1                                        # Increment the (out-)degree for start node
        inOutDeg[end] -= 1                                          # Decrement the (in-)degree for end node

    # Find starting node (node with out-degree > in-degree)
    startNode = pairs[0][0]                                         # Initialise with the default start
    for node in inOutDeg:                                           # Iterate through the degrees
        if inOutDeg[node] == 1:                                     # Check if the node-degree is 1
            startNode = node                                        # Assign the curr-node as start
            break                                                   # Break out of the iteration

    path = []                                                       # Initialise an empty result list
    dfs(startNode)                                                  # Use the helper method to traverse graph from node

    return path[::-1]                                               # Reverse the list and return the result
