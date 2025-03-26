"""
684. Redundant Connection [MEDIUM]

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added
edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented
as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the
graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers,
return the answer that occurs last in the input.


Example 1:
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]


Example 2:
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]


Constraints:

    -> n == edges.length
    -> 3 <= n <= 1000
    -> edges[i].length == 2
    -> 1 <= a_i < b_i <= edges.length
    -> a_i != b_i
    -> There are no repeated edges.
    -> The given graph is connected.


Concepts: Graph, Union Find
"""


# Optimised Solution
class UnionFind:
    def __init__(self, n: int):
        self.parent = [*range(n)]                                   # List of nodes
        self.rank = [1] * n                                         # List to track node ranks

    def find(self, x: int) -> int:
        if self.parent[x] != x:                                     # Check if the element is not its own parent
            self.parent[x] = self.find(self.parent[x])              # Recursively find such element
        return self.parent[x]                                       # Return the element

    def union(self, x: int, y: int) -> None:
        x, y = self.find(x), self.find(y)                           # Find the parent for both elements
        if x == y:                                                  # Check if the parents are same
            return True                                             # Return True

        if self.rank[x] < self.rank[y]:                             # Check if the first element rank is smaller
            self.parent[x] = y                                      # Assign the second element as first's parent
        else:
            self.parent[y] = x                                      # Assign the first element as second's parent
            if self.rank[x] == self.rank[y]:                        # Check if the ranks of both elements are equal
                self.rank[x] += 1                                   # Increment the rank of the first element
        return False                                                # Return False


class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        uf = UnionFind(len(edges) + 1)                              # UnionFind object for the graph nodes
        for u, v in edges:                                          # Iterate through the edges
            if uf.union(u, v):                                      # Perform union on the nodes
                return [u, v]                                       # Return the result
