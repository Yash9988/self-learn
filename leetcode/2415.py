"""
2415. Reverse Odd Levels of Binary Tree [MEDIUM]

Given the root of a perfect binary tree, reverse the node values at each odd level of the tree.

For example, suppose the node values at level 3 are [2,1,3,4,7,11,29,18], then it should become [18,29,11,7,4,3,1,2].

Return the root of the reversed tree.

A binary tree is perfect if all parent nodes have two children and all leaves are on the same level.

The level of a node is the number of edges along the path between it and the root node.


Example 1:
Input: root = [2,3,5,8,13,21,34]
Output: [2,5,3,8,13,21,34]

Explanation:
The tree has only one odd level.
The nodes at level 1 are 3, 5 respectively, which are reversed and become 5, 3.


Example 2:
Input: root = [7,13,11]
Output: [7,11,13]

Explanation:
The nodes at level 1 are 13, 11, which are reversed and become 11, 13.


Example 3:
Input: root = [0,1,2,0,0,0,0,1,1,1,1,2,2,2,2]
Output: [0,2,1,0,0,0,0,2,2,2,2,1,1,1,1]

Explanation:
The odd levels have non-zero values.
The nodes at level 1 were 1, 2, and are 2, 1 after the reversal.
The nodes at level 3 were 1, 1, 1, 1, 2, 2, 2, 2, and are 2, 2, 2, 2, 1, 1, 1, 1 after the reversal.


Constraints:

    -> The number of nodes in the tree is in the range [1, 2^14].
    -> 0 <= Node.val <= 10^5
    -> root is a perfect binary tree.


Concepts: Trees, DFS
"""
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# My Solution
def reverseOddLevels(root: TreeNode) -> TreeNode:
    # Helper method to traverse (and update) a tree in DFS fashion
    def dfs(node: TreeNode, level: int, update: bool) -> None:
        if not node:                                                # Check if node is None
            return                                                  # Exit the call

        if update and level % 2:                                    # Check if update flag is set and level is odd
            node.val = vals[level].pop()                            # Update the node value from the list

        if not update and level % 2:                                # Check if update flag is unset and level is odd
            vals[level].append(node.val)                            # Append the node value to the corr. level key

        dfs(node.left, level + 1, update)                           # Traverse to the left child-node
        dfs(node.right, level + 1, update)                          # Traverse to the right child-node

    vals = defaultdict(list)                                        # Dict of lists to store node values at each level
    dfs(root, 0, False)                                             # Store node values at each level in sequence
    dfs(root, 0, True)                                              # Update node values at odd levels in reverse

    return root                                                     # Return the root node


# Optimised Solution
def reverseOddLevels_op(root: TreeNode) -> TreeNode:
    # Helper method to reverse node values at odd levels by swapping
    def reverse(n1: TreeNode, n2: TreeNode, level: int) -> None:
        if not n1 or not n2:                                        # Check if either node is None
            return                                                  # Exit the call

        if level % 2:                                               # Check if the curr-level is odd
            n1.val, n2.val = n2.val, n1.val                         # Swap the node values

        reverse(n1.left, n2.right, level + 1)                       # Traverse to the outer child nodes
        reverse(n1.right, n2.left, level + 1)                       # Traverse to the inner child nodes

    reverse(root.left, root.right, 1)                               # Update node values at odd levels

    return root                                                     # Return the root node
