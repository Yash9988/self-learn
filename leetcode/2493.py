"""
2493. Divide Nodes Into the Maximum Number of Groups [HARD]

You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from
1 to n.

You are also given a 2D integer array edges, where edges[i] = [a_i, b_i] indicates that there is a bidirectional edge
between nodes a_i and b_i. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

    - Each node in the graph belongs to exactly one group.
    - For every pair of nodes in the graph that are connected by an edge [a_i, b_i], if a_i belongs to the group with
    index x, and bi belongs to the group with index y, then |y - x| = 1.

Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible
to group the nodes with the given conditions.


Example 1:
Input: n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]
Output: 4

Explanation: As shown in the image we:
- Add node 5 to the first group.
- Add node 1 to the second group.
- Add nodes 2 and 4 to the third group.
- Add nodes 3 and 6 to the fourth group.
We can see that every edge is satisfied.
It can be shown that if we create a fifth group and move any node from the third or fourth group to it, at least on
of the edges will not be satisfied.


Example 2:
Input: n = 3, edges = [[1,2],[2,3],[3,1]]
Output: -1

Explanation: If we add node 1 to the first group, node 2 to the second group, and node 3 to the third group to satisfy
the first two edges, we can see that the third edge will not be satisfied.
It can be shown that no grouping is possible.


Constraints:

    -> 1 <= n <= 500
    -> 1 <= edges.length <= 10^4
    -> edges[i].length == 2
    -> 1 <= a_i, b_i <= n
    -> a_i != b_i
    -> There is at most one edge between any pair of vertices.


Concepts: Graphs, Bi-partite, Deque


Reference: https://www.youtube.com/watch?v=-vu34sct1g8
"""
from collections import deque


# Optimised Solution
def magnificentSets(n, edges):
    # Helper function to check bi-partiteness and collect component nodes
    def is_bipartite(node, c, component):
        color[node] = c                                             # Assign the node the color
        component.append(node)                                      # Append the node to the commponent

        for nbr in adj[node]:                                       # Iterate through the neighbouring nodes
            if color[nbr] == c:                                     # Check if the neigh-node is same color (odd cycle)
                return False                                        # Return False

            # Check if the neigh-node uncolored and cannot be assigned the complementary color
            if color[nbr] == -1 and not is_bipartite(nbr, 1 - c, component):
                return False                                        # Return False

        return True                                                 # Return True

    # Helper function to compute max depth (groups) for a component
    def max_groups_in_component(component):
        max_depth = 0                                               # Counter to track max-depth
        for start in component:                                     # Iterate through the components
            depth = [-1] * n                                        # List to track depth for each node
            q = deque()                                             # Deque to track unprocessed nodes
            q.append(start)                                         # Append the curr-node to the queue
            depth[start] = 0                                        # Set the depth for the curr-node to zero

            while q:                                                # While the queue is non-empty
                node = q.popleft()                                  # Pop out the first node from the queue
                for nbr in adj[node]:                               # Iterate through its neighbours
                    if depth[nbr] == -1:                            # Check if the neigh-node depth is unassigned
                        depth[nbr] = depth[node] + 1                # Update neigh-node's depth using curr-node depth
                        max_depth = max(max_depth, depth[nbr])      # Update the counter with max-val
                        q.append(nbr)                               # Append the neigh-node to the queue

        return max_depth + 1                                        # Return the result (Depth to groups conversion)

    # Initialize adjacency list and color array
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)

    color = [-1] * n                                                # List to track bi-partition colors (0/1)
    components = []                                                 # List to track the components

    # Check bi-partiteness and collect components
    for i in range(n):                                              # Iterate through the range of nodes
        if color[i] == -1:                                          # Check if the node color is unassigned
            component = []                                          # List to store the component
            if not is_bipartite(i, 0, component):                   # Check if the node cannot be assigned the color
                return -1                                           # Return -1 (Non-bipartite component)

            components.append(component)                            # Append the component to the components list

    # Calculate total groups
    total = 0
    for comp in components:
        total += max_groups_in_component(comp)

    return total                                                    # Return the result
