"""
3203. Find Minimum Diameter After Merging Two Trees [HARD]

There exist two undirected trees with n and m nodes, numbered from 0 to n - 1 and from 0 to m - 1, respectively. You are
given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [a_i, b_i]
indicates that there is an edge between nodes a_i and b_i in the first tree and edges2[i] = [u_i, v_i] indicates that
there is an edge between nodes u_i and v_i in the second tree.

You must connect one node from the first tree with another node from the second tree with an edge.

Return the minimum possible diameter of the resulting tree.

The diameter of a tree is the length of the longest path between any two nodes in the tree.


Example 1:
Input: edges1 = [[0,1],[0,2],[0,3]], edges2 = [[0,1]]
Output: 3

Explanation:
We can obtain a tree of diameter 3 by connecting node 0 from the first tree with any node from the second tree.


Example 2:
Input: edges1 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], edges2 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]
Output: 5

Explanation:
We can obtain a tree of diameter 5 by connecting node 0 from the first tree with node 0 from the second tree.


Constraints:

    -> 1 <= n, m <= 10^5
    -> edges1.length == n - 1
    -> edges2.length == m - 1
    -> edges1[i].length == edges2[i].length == 2
    -> edges1[i] = [a_i, b_i]
    -> 0 <= a_i, b_i < n
    -> edges2[i] = [u_i, v_i]
    -> 0 <= u_i, v_i < m
    -> The input is generated such that edges1 and edges2 represent valid trees.


Concepts: Graphs, BFS
"""


# Optimised Solution
def minimumDiameterAfterMerge(edges1: list[list[int]], edges2: list[list[int]]) -> int:
    # Method to compute the furthest node and the respective distance from a node
    def farthest(G, i):
        n = len(G)                                                  # Obtain the number of nodes in the graph
        bfs = [i]                                                   # List to track node traversal in BFS fashion
        seen = [0] * n                                              # List to track the visited nodes
        seen[i] = 1                                                 # Set the current node flag
        res = maxd = -1                                             # Counters to track furthest node and distance

        for i in bfs:                                               # Iterate through the bfs list
            for j in G[i]:                                          # Iterate through its adjacent nodes
                if not seen[j]:                                     # Check if the node hasn't been visited already
                    seen[j] = seen[i] + 1                           # Update the node flag with the corr-distance
                    bfs.append(j)                                   # Add the node to the bfs node
                    if seen[j] > maxd:                              # Check if the distance of curr-node is higher
                        res = j                                     # Set the current node as the furthest
                        maxd = seen[j]                              # Update the counter w/ curr-node's distance

        return res, maxd - 1                                        # Return the furthest node and its distance

    # Method to compute the diameter of a graph, given its edges
    def diameter(edges):
        if not edges:                                               # Check if graph has no edges
            return 0                                                # Return 0

        n = len(edges) + 1                                          # Compute the nodes in the graph
        G = [[] for _ in range(n)]                                  # LoL to store adjacent nodes

        for u, v in edges:                                          # Iterate through the edges
            G[u].append(v), G[v].append(u)                          # Update the nodes w/ respective adjacent nodes

        v1, _ = farthest(G, 0)                                      # Compute the furthest node from "first" node
        _, d = farthest(G, v1)                                      # Compute the max-distance from the furthest node

        return d                                                    # Return the graph diameter

    d1, d2 = diameter(edges1), diameter(edges2)                     # Compute the diameter for each graph

    return max(d1, d2, (d1 + 1) // 2 + (d2 + 1) // 2 + 1)           # Compute and return the result
