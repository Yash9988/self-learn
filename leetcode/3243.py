"""
3243. Shortest Distance After Road Addition Queries I [MEDIUM]

You are given an integer n and a 2D integer array queries.

There are n cities numbered from 0 to n - 1. Initially, there is a unidirectional road from city i to city i + 1 for all
0 <= i < n - 1.

queries[i] = [ui, vi] represents the addition of a new unidirectional road from city ui to city vi. After each query,
you need to find the length of the shortest path from city 0 to city n - 1.

Return an array answer where for each i in the range [0, queries.length - 1], answer[i] is the length of the shortest
path from city 0 to city n - 1 after processing the first i + 1 queries.


Example 1:
Input: n = 5, queries = [[2,4],[0,2],[0,4]]
Output: [3,2,1]

Explanation:
After the addition of the road from 2 to 4, the length of the shortest path from 0 to 4 is 3.

After the addition of the road from 0 to 2, the length of the shortest path from 0 to 4 is 2.

After the addition of the road from 0 to 4, the length of the shortest path from 0 to 4 is 1.


Example 2:
Input: n = 4, queries = [[0,3],[0,2]]
Output: [1,1]

Explanation:
After the addition of the road from 0 to 3, the length of the shortest path from 0 to 3 is 1.

After the addition of the road from 0 to 2, the length of the shortest path remains 1.


Constraints:

    -> 3 <= n <= 500
    -> 1 <= queries.length <= 500
    -> queries[i].length == 2
    -> 0 <= queries[i][0] < queries[i][1] < n
    -> 1 < queries[i][1] - queries[i][0]
    -> There are no repeated roads among the queries.


Concepts: Graphs
"""


# Optimised Solution
def shortestDistanceAfterQueries(n: int, queries: list[list[int]]) -> list[int]:
    # Helper method to update the distances b/w the nodes, given a new connection
    def updateDistances(graph, current, distances):
        newDist = distances[current] + 1                            # Compute the new distance

        for neighbor in graph[current]:                             # Iterate through the neighbours of curr-node
            if distances[neighbor] <= newDist:                      # Check if the neigh-dist is smaller than new-dist
                continue                                            # Skip the iteration

            distances[neighbor] = newDist                           # Update the neigh-dist with the new distance
            updateDistances(graph, neighbor, distances)             # Update the distances in the graph wrt curr-node


    distances = [n - 1 - i for i in range(n)]                       # Initialise a list of distances b/w the nodes

    graph = [[] for _ in range(n)]                                  # Initialise an empty LoLs to represent the graph
    for i in range(n - 1):                                          # Iterate through the nodes
        graph[i + 1].append(i)                                      # Append the source node to the target node

    answer = []                                                     # Initialise an empty list to store the result

    for source, target in queries:                                  # Iterate through the queries
        graph[target].append(source)                                # Append the source node to target node

        # Update the distance for the source node with the min-dist
        distances[source] = min(distances[source], distances[target] + 1)
        updateDistances(graph, source, distances)                   # Update the distances in the graph wrt curr-node

        answer.append(distances[0])                                 # Append the shortest distance to the result list

    return answer                                                   # Return the result
