"""
3319. K-th Largest Perfect Subtree Size in Binary Tree [MEDIUM]

You are given the root of a binary tree and an integer k.

Return an integer denoting the size of the kth largest perfect binary _subtree_, or -1 if it doesn't exist.

A perfect binary tree is a tree where all leaves are on the same level, and every parent has two children.


Example 1:

Input: root = [5,3,6,5,2,5,7,1,8,null,null,6,8], k = 2
Output: 3

Explanation:
The roots of the perfect binary subtrees are highlighted in black. Their sizes, in non-increasing order are
[3, 3, 1, 1, 1, 1, 1, 1]. The 2nd largest size is 3.


Example 2:

Input: root = [1,2,3,4,5,6,7], k = 1
Output: 7

Explanation:
The sizes of the perfect binary subtrees in non-increasing order are [7, 3, 3, 1, 1, 1, 1]. The size of the largest
perfect binary subtree is 7.


Example 3:

Input: root = [1,2,3,null,4], k = 3
Output: -1

Explanation:
The sizes of the perfect binary subtrees in non-increasing order are [1, 1]. There are fewer than 3 perfect binary subtrees.


Constraints:

    -> The number of nodes in the tree is in the range [1, 2000].
    -> 1 <= Node.val <= 2000
    -> 1 <= k <= 1024


Concepts: Binary Tree, DFS
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# My Solution
def kthLargestPerfectSubtree(root: TreeNode, k: int) -> int:
    # Method to traverse through the tree using DFS
    def dfs(node: TreeNode) -> int:
        if not node:                                        # Check if not is None
            return 1                                        # Return 1

        l, r = dfs(node.left), dfs(node.right)              # Traverse and compute leaf-depth for the child-nodes

        if l > 0 and l == r:                                # Check if the depths are equal
            res.append(2 ** l - 1)                          # Compute and append the tree size to the result list

        return l + 1 if l == r else -1                      # Check and return the appropriate value

    res = []                                                # Initialise a result list
    dfs(root)                                               # Traverse through the tree

    return sorted(res)[-k] if k <= len(res) else -1         # Return the result
