"""
1976. Number of Ways to Arrive at Destination [MEDIUM]

You are in a city that consists of n intersections numbered from 0 to n - 1 with bidirectional roads between some
intersections. The inputs are generated such that you can reach any intersection from any other intersection and that
there is at most one road between any two intersections.

You are given an integer n and a 2D integer array roads where roads[i] = [u_i, v_i, time_i] means that there is a road
between intersections u_i and v_i that takes time_i minutes to travel. You want to know in how many ways you can travel
from intersection 0 to intersection n - 1 in the shortest amount of time.

Return the number of ways you can arrive at your destination in the shortest amount of time. Since the answer may be
large, return it modulo 109 + 7.


Example 1:
Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
Output: 4

Explanation: The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes.
The four ways to get there in 7 minutes are:
- 0 ➝ 6
- 0 ➝ 4 ➝ 6
- 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
- 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6


Example 2:
Input: n = 2, roads = [[1,0,10]]
Output: 1

Explanation: There is only one way to go from intersection 0 to intersection 1, and it takes 10 minutes.


Constraints:

    -> 1 <= n <= 200
    -> n - 1 <= roads.length <= n * (n - 1) / 2
    -> roads[i].length == 3
    -> 0 <= u_i, v_i <= n - 1
    -> 1 <= time_i <= 109
    -> u_i != v_i
    -> There is at most one road connecting any two intersections.
    -> You can reach any intersection from any other intersection.


Concepts: Graphs, Heap, DP, Dijkstra's Algorithm
"""
import heapq


# Optimised Solution
def countPaths(n: int, roads: list[list[int]]) -> int:
    graph = [[] for _ in range(n)]                                  # LoL to track adjacent nodes
    # Compute the adjacency list
    for u, v, time in roads:
        graph[u].append((v, time))
        graph[v].append((u, time))

    dist = [float('inf')] * n                                       # List to track min-dist for each node
    ways = [0] * n                                                  # DP to track all possible ways b/w intersections

    # Initialise the DP base-case
    dist[0] = 0
    ways[0] = 1

    pq = [(0, 0)]                                                   # Priority queue to track unprocessed states

    MOD = 10 ** 9 + 7                                               # Mod-val to avoid integer overflow

    # Dijkstra's algorithm
    while pq:                                                       # While the queue is non-empty
        d, node = heapq.heappop(pq)                                 # Pop the smallest tuple from heap

        if d > dist[node]:                                          # Check if the curr-dist is smaller than node-dist
            continue                                                # Skip to the next iteration

        for neighbor, time in graph[node]:                          # Iterate through the adjacent nodes
            if dist[node] + time < dist[neighbor]:                  # Check if the node-dist is smaller than neigh-dist
                dist[neighbor] = dist[node] + time                  # Update the neigh-dist
                ways[neighbor] = ways[node]                         # Update the neigh-ways

                # Push the neigh-state to the heap
                heapq.heappush(pq, (dist[neighbor], neighbor))

            elif dist[node] + time == dist[neighbor]:               # Check if the distances are equal
                # Update the neigh-ways with the sum
                ways[neighbor] = (ways[neighbor] + ways[node]) % MOD

    return ways[n - 1]                                              # Return the result
