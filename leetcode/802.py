"""
802. Find Eventual Safe States [MEDIUM]

There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D
integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i
to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from
that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.


Example 1:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]

Explanation: The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.


Example 2:
Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
Output: [4]

Explanation:
Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.


Constraints:

    -> n == graph.length
    -> 1 <= n <= 10^4
    -> 0 <= graph[i].length <= n
    -> 0 <= graph[i][j] <= n - 1
    -> graph[i] is sorted in a strictly increasing order.
    -> The graph may contain self-loops.
    -> The number of edges in the graph will be in the range [1, 4 * 10^4].


Concepts: Deque
"""
from collections import deque


# Optimised Solution
def eventualSafeNodes(graph: list[list[int]]) -> list[int]:
    # Method to traverse the graph in a DFS fashion
    def dfs(node: int) -> bool:
        if visited[node]:                                           # Check if the node is already visited
            return not inPath[node]                                 # If inPath is True, it means there's a cycle.

        visited[node] = True                                        # Set the node as visited
        inPath[node] = True                                         # Set the node to be inPath

        for neighbor in graph[node]:                                # Iterate through the neighbours
            if not dfs(neighbor):                                   # Check if a cycle is detected
                return False                                        # Return False

        inPath[node] = False                                        # Unset the node to be inPath
        safe[node] = True                                           # Set the node to be safe

        return True                                                 # Return True

    n = len(graph)                                                  # Obtain the number of nodes in the graph
    safe = [False] * n                                              # List to track safe nodes
    visited = [False] * n                                           # List to track visited nodes
    inPath = [False] * n                                            # List to track inPath nodes

    for i in range(n):                                              # Iterate through the nodes
        if not visited[i]:                                          # Check if node is unvisited
            dfs(i)                                                  # Iterate the graph from that node

    return [i for i in range(n) if safe[i]]                         # Return the result


# Alternate Solution
def eventualSafeNodes_alt(graph: list[list[int]]) -> list[int]:
    n = len(graph)                                                  # Obtain the number of nodes in the graph
    indegree = [0] * n                                              # List to track in-degrees of each node
    adj = [[] for _ in range(n)]                                    # Adjacency list

    for i in range(n):                                              # Iterate through the nodes
        for node in graph[i]:                                       # Iterate through its neighbours
            adj[node].append(i)                                     # Update the adjacency list
            indegree[i] += 1                                        # Increment the node's in-degree

    q = deque()                                                     # Queue to track unprocessed nodes

    # Push all the nodes with in-degree zero in the queue.
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    safe = [False] * n                                              # List to track safe nodes
    while q:                                                        # While the queue is non-empty
        node = q.popleft()                                          # Pop the first element of the queue
        safe[node] = True                                           # Set the node to be safe

        for neighbor in adj[node]:                                  # Iterate through its neighbours
            indegree[neighbor] -= 1                                 # Delete the edge "node -> neighbor".
            if indegree[neighbor] == 0:                             # Check if the neighbour's in-degree is zero
                q.append(neighbor)                                  # Append the neighbour to the queue

    safeNodes = []                                                  # List to store the results

    # Add all the safe nodes into the result list
    for i in range(n):
        if safe[i]:
            safeNodes.append(i)

    return safeNodes                                                # Return the result
