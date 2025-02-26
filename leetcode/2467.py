"""
2467. Most Profitable Path in a Tree [MEDIUM]

There is an undirected tree with n nodes labeled from 0 to n - 1, rooted at node 0. You are given a 2D integer array
edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

At every node i, there is a gate. You are also given an array of even integers amount, where amount[i] represents:

    - the price needed to open the gate at node i, if amount[i] is negative, or,
    - the cash reward obtained on opening the gate at node i, otherwise.

The game goes on as follows:

    - Initially, Alice is at node 0 and Bob is at node bob.
    - At every second, Alice and Bob each move to an adjacent node. Alice moves towards some leaf node, while Bob moves
      towards node 0.
    - For every node along their path, Alice and Bob either spend money to open the gate at that node, or accept the
      reward. Note that:
        - If the gate is already open, no price will be required, nor will there be any cash reward.
        - If Alice and Bob reach the node simultaneously, they share the price/reward for opening the gate there. In
          other words, if the price to open the gate is c, then both Alice and Bob pay c / 2 each. Similarly, if the
          reward at the gate is c, both of them receive c / 2 each.
    - If Alice reaches a leaf node, she stops moving. Similarly, if Bob reaches node 0, he stops moving. Note that these
      events are independent of each other.

Return the maximum net income Alice can have if she travels towards the optimal leaf node.


Example 1:
Input: edges = [[0,1],[1,2],[1,3],[3,4]], bob = 3, amount = [-2,4,2,-4,6]
Output: 6

Explanation:
The above diagram represents the given tree. The game goes as follows:
- Alice is initially on node 0, Bob on node 3. They open the gates of their respective nodes.
  Alice's net income is now -2.
- Both Alice and Bob move to node 1.
  Since they reach here simultaneously, they open the gate together and share the reward.
  Alice's net income becomes -2 + (4 / 2) = 0.
- Alice moves on to node 3. Since Bob already opened its gate, Alice's income remains unchanged.
  Bob moves on to node 0, and stops moving.
- Alice moves on to node 4 and opens the gate there. Her net income becomes 0 + 6 = 6.
Now, neither Alice nor Bob can make any further moves, and the game ends.
It is not possible for Alice to get a higher net income.


Example 2:
Input: edges = [[0,1]], bob = 1, amount = [-7280,2350]
Output: -7280

Explanation:
Alice follows the path 0->1 whereas Bob follows the path 1->0.
Thus, Alice opens the gate at node 0 only. Hence, her net income is -7280.


Constraints:

    -> 2 <= n <= 10^5
    -> edges.length == n - 1
    -> edges[i].length == 2
    -> 0 <= a_i, b_i < n
    -> a_i != b_i
    -> edges represents a valid tree.
    -> 1 <= bob < n
    -> amount.length == n
    -> amount[i] is an even integer in the range [-10^4, 10^4].


Concepts: Trees, DFS
"""
from math import inf


# Optimised Solution
def mostProfitablePath(edges: list[list[int]], bob: int, amount: list[int]) -> int:
    n = len(edges) + 1                                              # Compute the nodes in the tree
    g = [[] for _ in range(n)]                                      # Adjacency list

    # Compute the adjacent nodes
    for x, y in edges:
        g[x].append(y)
        g[y].append(x)

    bob_time = [n] * n                                              # List to track nodes visited by Bob

    # Helper method to recursively iterate the tree for Bob
    def dfs_bob(x: int, fa: int, t: int) -> bool:
        if x == 0:                                                  # Check if the curr-node is 0
            bob_time[x] = t                                         # Update the node-idx with the time-taken
            return True                                             # Return True

        for y in g[x]:                                              # Iterate through the neighbouring nodes

            # Check if Bob can get to the first node from curr-neigh, recursively
            if y != fa and dfs_bob(y, x, t + 1):
                bob_time[x] = t                                     # Update node-idx with the rec-cost
                return True                                         # Return True

        return False                                                # Return False, if no neighbour leads to first node

    dfs_bob(bob, -1, 0)                                             # Iterate the tree starting from Bob's node

    g[0].append(-1)                                                 # Add a dummy neigh to the first node
    ans = -inf                                                      # Counter to track Alice's max-income

    # Helper method to recursively iterate thr tree for Alice
    def dfs_alice(x: int, fa: int, alice_time: int, tot: int) -> None:
        if alice_time < bob_time[x]:                                # Check if Alice's time to reach node is smaller
            tot += amount[x]                                        # Increment the total with the node's amount
        elif alice_time == bob_time[x]:                             # Check if the time taken is equal
            tot += amount[x] // 2                                   # Increment the total by half the node's amount

        if len(g[x]) == 1:                                          # Check if the curr-node has only a single neighbour
            nonlocal ans                                            # Reference the non-local counter
            ans = max(ans, tot)                                     # Update the counter with the max-val
            return                                                  # Break out the rec-call

        for y in g[x]:                                              # Iterate through the neighbours
            # Check if the neighbour isn't the recently visited node
            if y != fa:
                dfs_alice(y, x, alice_time + 1, tot)                # Iterate to the neigh-node, recursively

    dfs_alice(0, -1, 0, 0)                                          # Iterate the tree starting from the first node

    return ans                                                      # Return the result
