"""
2583. Kth Largest Sum in a Binary Tree [MEDIUM]

You are given the root of a binary tree and a positive integer k.

The level sum in the tree is the sum of the values of the nodes that are on the same level.

Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree,
return -1.

Note that two nodes are on the same level if they have the same distance from the root.


Example 1:

Input: root = [5,8,9,2,1,3,7,4,6], k = 2
Output: 13

Explanation: The level sums are the following:
- Level 1: 5.
- Level 2: 8 + 9 = 17.
- Level 3: 2 + 1 + 3 + 7 = 13.
- Level 4: 4 + 6 = 10.
The 2nd largest level sum is 13.


Example 2:

Input: root = [1,2,null,3], k = 1
Output: 3

Explanation: The largest level sum is 3.


Constraints:

    The number of nodes in the tree is n.
    2 <= n <= 105
    1 <= Node.val <= 106
    1 <= k <= n


Concepts: Tree, Heap, DFS
"""
from heapq import *
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# My Solution
def kthLargestLevelSum(root: TreeNode, k: int) -> int:
    def traverse(node: TreeNode, level: int) -> None:       # Helper method to DFS the tree
        if node is None:                                    # Check if the node is None
            return                                          # Return
        sums[level] += node.val                             # Sum the node value to the corresponding level
        traverse(node.left, level + 1)                      # Traverse left node
        traverse(node.right, level + 1)                     # Traverse right node

    sums = defaultdict(int)                                 # Initialise a dict to track sum at each tree-level
    traverse(root, 1)                                       # Traverse through the tree in DFS fashion

    if k > max(sums):                                       # Check if required level is higher than max-key in sum-dict
        return -1                                           # Return -1

    pq = []                                                 # Initialise a priority queue
    [heappush(pq, -val) for val in sums.values()]           # Push all level sums into the heap

    while k := k - 1:                                       # While the counter is non-zero
        heappop(pq)                                         # Pop element from the heap

    return -heappop(pq)                                     # Return the result
