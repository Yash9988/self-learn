"""
515. Find Largest Value in Each Tree Row [MEDIUM]

Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).


Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]


Example 2:
Input: root = [1,2,3]
Output: [1,3]


Constraints:

    -> The number of nodes in the tree will be in the range [0, 10^4].
    -> -2^31 <= Node.val <= 2^31 - 1


Concepts: Trees, DFS/BFS
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# My Solution
def largestValues(root: TreeNode) -> list[int]:
    # Method to Iterate through the tree in DFS fashion
    def dfs(node: TreeNode, lvl: int) -> None:
        if not node:                                                # Check if node doesn't exist
            return                                                  # End the recursive call

        if lvl < len(res):                                          # Check if level max-val has been initialised yet
            res[lvl] = max(res[lvl], node.val)                      # Update the corr-val with the max-val
        else:
            res.append(node.val)                                    # Append the current value, otherwise

        dfs(node.left, lvl + 1)                                     # Traverse to the left child-node
        dfs(node.right, lvl + 1)                                    # Traverse to the right child-node

    res = []                                                        # List to store the result
    dfs(root, 0)                                                    # Traverse the tree from root node in DFS fashion

    return res                                                      # Return the result
