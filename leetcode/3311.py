"""
3311. Construct 2D Grid Matching Graph Layout [HARD]

You are given a 2D integer array edges representing an undirected graph having n nodes, where edges[i] = [ui, vi]
denotes an edge between nodes ui and vi.

Construct a 2D grid that satisfies these conditions:

    - The grid contains all nodes from 0 to n - 1 in its cells, with each node appearing exactly once.
    - Two nodes should be in adjacent grid cells (horizontally or vertically) if and only if there is an edge between
      them in edges.

It is guaranteed that edges can form a 2D grid that satisfies the conditions.

Return a 2D integer array satisfying the conditions above. If there are multiple solutions, return any of them.


Example 1:

Input: n = 4, edges = [[0,1],[0,2],[1,3],[2,3]]

Output: [[3,1],[2,0]]


Example 2:

Input: n = 5, edges = [[0,1],[1,3],[2,3],[2,4]]

Output: [[4,2,3,1,0]]


Example 3:

Input: n = 9, edges = [[0,1],[0,4],[0,5],[1,7],[2,3],[2,4],[2,5],[3,6],[4,6],[4,7],[6,8],[7,8]]

Output: [[8,6,3],[7,4,2],[1,0,5]]


Constraints:

    -> 2 <= n <= 5 * 10^4
    -> 1 <= edges.length <= 10^5
    -> edges[i] = [ui, vi]
    -> 0 <= ui < vi < n
    -> All the edges are distinct.
    -> The input is generated such that edges can form a 2D grid that satisfies the conditions.


Concepts: Graphs
"""


def constructGridLayout(n: int, edges: list[list[int]]) -> list[list[int]]:
    adj = [[] for _ in range(n)]                                    # Initialise an empty adjacency list
    for u, v in edges:                                              # Iterate through the edges
        adj[u].append(v)                                            # Update the adjacency list of root node
        adj[v].append(u)                                            # Update the adjacency list of destination node

    deg = [len(row) for row in adj]                                 # Compute the degree of each node in the graph
    root = deg.index(min(deg))                                      # Compute the node with the smallest degree
    path = [root]                                                   # Initialise path list with root
    seen = [0] * n                                                  # Initialise a seen-list
    seen[root] = 1                                                  # Set the flag for root node
    for node in path:                                               # Iterate through the path list
        if len(path) >= 2 and deg[path[-1]] == deg[root]:           # Check if degree of curr-node equals root-node's
            break                                                   # Break out of the loop
        adj[node].sort(key=deg.__getitem__)                         # Sort the adj-list of curr-node based upon node-deg
        for nei in adj[node]:                                       # Iterate through the adjacent nodes
            if not seen[nei] and deg[nei] <= deg[root] + 1:         # Check if adj-node is unseen and degree > root's
                path.append(nei)                                    # Add the adj-node to the path
                seen[nei] = 1                                       # Set the flag for the adj-node
                break                                               # Break out of the loop

    C = len(path)                                                   # Compute the number of columns of the grid
    R = n // C                                                      # Compute the number of rows of the grid
    ans = [[0] * C for _ in range(R)]                               # Initialise a 2D table
    ans[0] = path                                                   # Assign the first row as the computed path-list
    for r in range(1, R):                                           # Iterate through the remaining rows
        for c in range(C):                                          # Iterate through the columns
            for nei in adj[ans[r - 1][c]]:                          # Iterate through adj-nodes for the node above
                if not seen[nei]:                                   # Check if the adj-node is unseen
                    ans[r][c] = nei                                 # Update the table cell with the corresponding node
                    seen[nei] = 1                                   # Set the flag of the node
                    break                                           # Break out of the adj-nodes loop

    return ans                                                      # Return the result
