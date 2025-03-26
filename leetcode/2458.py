"""
2458. Height of Binary Tree After Subtree Removal Queries [HARD]

You are given the root of a binary tree with n nodes. Each node is assigned a unique value from 1 to n. You are also
given an array queries of size m.

You have to perform m independent queries on the tree where in the ith query you do the following:

    - Remove the subtree rooted at the node with the value queries[i] from the tree. It is guaranteed that queries[i]
      will not be equal to the value of the root.

Return an array answer of size m where answer[i] is the height of the tree after performing the ith query.

Note:

    - The queries are independent, so the tree returns to its initial state after each query.
    - The height of a tree is the number of edges in the longest simple path from the root to some node in the tree.


Example 1:
Input: root = [1,3,4,2,null,6,5,null,null,null,null,null,7], queries = [4]
Output: [2]

Explanation: The diagram above shows the tree after removing the subtree rooted at node with value 4.
The height of the tree is 2 (The path 1 -> 3 -> 2).


Example 2:
Input: root = [5,8,9,2,1,3,7,4,6], queries = [3,2,4,8]
Output: [3,2,3,2]

Explanation: We have the following queries:
- Removing the subtree rooted at node with value 3. The height of the tree becomes 3 (The path 5 -> 8 -> 2 -> 4).
- Removing the subtree rooted at node with value 2. The height of the tree becomes 2 (The path 5 -> 8 -> 1).
- Removing the subtree rooted at node with value 4. The height of the tree becomes 3 (The path 5 -> 8 -> 2 -> 6).
- Removing the subtree rooted at node with value 8. The height of the tree becomes 2 (The path 5 -> 9 -> 3).


Constraints:

    -> The number of nodes in the tree is n.
    -> 2 <= n <= 10^5
    -> 1 <= Node.val <= n
    -> All the values in the tree are unique.
    -> m == queries.length
    -> 1 <= m <= min(n, 10^4)
    -> 1 <= queries[i] <= n
    -> queries[i] != root.val


Concepts: DFS, Trees
"""
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def treeQueries(root: TreeNode, queries: list[int]) -> list[int]:
    # Helper method to traverse tree in a DFS fashion and calculate max-depth for each node
    def dfs(node, depth):
        if not node:                                                # Check if node is None
            return -1

        Depth[node.val] = depth                                     # Assign the node with its corresponding depth
        left = dfs(node.left, depth + 1)                            # Traverse to the left node
        right = dfs(node.right, depth + 1)                          # Traverse to the right node
        cur = max(left, right) + 1                                  # Compute the maximum height
        Height[node.val] = cur                                      # Store the height at the current node
        return cur                                                  # Return the height

    Depth, Height = defaultdict(int), defaultdict(int)              # Initialise dicts to store depths & heights
    dfs(root, 0)                                                    # Traverse the tree

    cousins = defaultdict(list)                                     # Initialise dict to group nodes wrt depth, upto 2
    for val, depth in Depth.items():                                # Iterate through the depth of each node
        cousins[depth].append((-Height[val], val))                  # Append the height of nodes at same depth
        cousins[depth].sort()                                       # Sort the heights
        if len(cousins[depth]) > 2:                                 # Check if there are more than 2 nodes
            cousins[depth].pop()                                    # Remove the node with the smallest node

    ans = []                                                        # Initialise a result array
    for q in queries:                                               # Iterate through all queries
        depth = Depth[q]                                            # Obtain the depth of current node
        if len(cousins[depth]) == 1:                                # Check if node has no cousin
            ans.append(depth - 1)                                   # Append path length as depth - 1
        elif cousins[depth][0][1] == q:                             # Check if the removed node had the largest height
            ans.append(-cousins[depth][1][0] + depth)               # Append the height of the 2nd largest node.
        else:
            ans.append(-cousins[depth][0][0] + depth)               # Append the height of the largest node

    return ans                                                      # Return the result
