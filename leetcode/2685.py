"""
2685. Count the Number of Complete Components [MEDIUM]

You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a
2D-integer array edges where edges[i] = [a_i, b_i] denotes that there exists an undirected edge connecting
vertices a_i and b_i.

Return the number of complete connected components of the graph.

A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of
the subgraph shares an edge with a vertex outside the subgraph.

A connected component is said to be complete if there exists an edge between every pair of its vertices.


Example 1:
Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
Output: 3

Explanation: From the picture above, one can see that all the components of this graph are complete.


Example 2:
Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
Output: 1

Explanation: The component containing vertices 0, 1, and 2 is complete since there is an edge between every pair of two
vertices. On the other hand, the component containing vertices 3, 4, and 5 is not complete since there is no edge
between vertices 4 and 5. Thus, the number of complete components in this graph is 1.


Constraints:

    -> 1 <= n <= 50
    -> 0 <= edges.length <= n * (n - 1) / 2
    -> edges[i].length == 2
    -> 0 <= a_i, b_i <= n - 1
    -> a_i != b_i
    -> There are no repeated edges.


Concepts: Graphs, BFS
"""


# Optimised Solution
def countCompleteComponents(n: int, edges: list[list[int]]) -> int:
    G = [[] for _ in range(n)]                                      # LoL to track adjacent nodes
    for i, j in edges:                                              # Iterate through the edges
        # Update the adjacent nodes
        G[i].append(j)
        G[j].append(i)

    seen = [0] * n                                                  # List to track seen nodes
    res = 0                                                         # Counter to track result
    for i in range(n):                                              # Iterate through the nodes
        if seen[i]:                                                 # Check if node is already visited
            continue                                                # Skip to the next iteration

        bfs = [i]                                                   # List to track a component
        seen[i] = 1                                                 # Mark the node as visited
        for j in bfs:                                               # Iterate through the queue
            for k in G[j]:                                          # Iterate through the adjacent nodes
                if seen[k] == 0:                                    # Check if the node is unvisited
                    bfs.append(k)                                   # Append the node to the component list
                    seen[k] = 1                                     # Mark the node as visited

        if all(len(G[j]) == len(bfs) - 1 for j in bfs):             # Check if all component nodes have the same neighs
            res += 1                                                # Increment the result counter

    return res                                                      # Return the result
