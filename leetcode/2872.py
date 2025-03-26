"""
2872. Maximum Number of K-Divisible Components [HARD]

There is an undirected tree with n nodes labeled from 0 to n - 1. You are given the integer n and a 2D integer array
edges of length n - 1, where edges[i] = [a_i, b_i] indicates that there is an edge between nodes a_i and b_i in the tree.

You are also given a 0-indexed integer array values of length n, where values[i] is the value associated with the i-th
node, and an integer k.

A valid split of the tree is obtained by removing any set of edges, possibly empty, from the tree such that the
resulting components all have values that are divisible by k, where the value of a connected component is the sum of the
values of its nodes.

Return the maximum number of components in any valid split.


Example 1:
Input: n = 5, edges = [[0,2],[1,2],[1,3],[2,4]], values = [1,8,1,4,4], k = 6
Output: 2

Explanation: We remove the edge connecting node 1 with 2. The resulting split is valid because:
- The value of the component containing nodes 1 and 3 is values[1] + values[3] = 12.
- The value of the component containing nodes 0, 2, and 4 is values[0] + values[2] + values[4] = 6.
It can be shown that no other valid split has more than 2 connected components.


Example 2:
Input: n = 7, edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], values = [3,0,6,1,5,2,1], k = 3
Output: 3

Explanation: We remove the edge connecting node 0 with 2, and the edge connecting node 0 with 1. The resulting split is
valid because:
- The value of the component containing node 0 is values[0] = 3.
- The value of the component containing nodes 2, 5, and 6 is values[2] + values[5] + values[6] = 9.
- The value of the component containing nodes 1, 3, and 4 is values[1] + values[3] + values[4] = 6.
It can be shown that no other valid split has more than 3 connected components.


Constraints:

    -> 1 <= n <= 3 * 10^4
    -> edges.length == n - 1
    -> edges[i].length == 2
    -> 0 <= a_i, b_i < n
    -> values.length == n
    -> 0 <= values[i] <= 10^9
    -> 1 <= k <= 10^9
    -> Sum of values is divisible by k.
    -> The input is generated such that edges represents a valid tree.


Concepts: Graphs, Prefix Sum
"""
from collections import deque, defaultdict


# Optimised Solution
def maxKDivisibleComponents(n: int, edges: list[list[int]], values: list[int], k: int) -> int:
    if n == 1:                                                      # Check if graph consists of a single node
        return 1                                                    # Return 1

    adj = defaultdict(set)                                          # Dict to track adjacent nodes in the graph
    for u, v in edges:                                              # Iterate through all edges
        adj[u].add(v), adj[v].add(u)                                # Append nodes as adjacent to each other in the dict

    # Queue to track all leaf nodes in the graph
    leaf = deque(node for node, adjs in adj.items() if len(adjs) == 1)

    res = 0                                                         # Counter to track the components
    while leaf:                                                     # While the queue is non-empty
        for _ in range(len(leaf)):                                  # Iterate through the range of queue
            node = leaf.popleft()                                   # Pop the first element from the queue
            parent = adj[node].pop() if adj[node] else -1           # Obtain the node's parent, if present

            if parent >= 0:                                         # Check if node has a parent
                adj[parent].remove(node)                            # Remove the node as parent's adjacent

            if values[node] % k:                                    # Check if node value is non-divisible by `k`
                values[parent] += values[node]                      # Add the node's value to its parent's node
            else:
                res += 1                                            # Split the node and increment counter, otherwise

            if parent >= 0 and len(adj[parent]) == 1:               # Check if the parent node is now a (new) leaf node
                leaf.append(parent)                                 # Append the parent node to the queue

    return res                                                      # Return the result
