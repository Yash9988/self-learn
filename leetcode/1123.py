"""
1123. Lowest Common Ancestor of Deepest Leaves [MEDIUM]

Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

    - The node of a binary tree is a leaf if and only if it has no children
    - The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
    - The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is
      in the subtree with root A.


Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]

Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest leaf-nodes of the tree.
Note that nodes 6, 0, and 8 are also leaf nodes, but the depth of them is 2, but the depth of nodes 7 and 4 is 3.


Example 2:
Input: root = [1]
Output: [1]

Explanation: The root is the deepest node in the tree, and it's the lca of itself.


Example 3:
Input: root = [0,1,3,null,2]
Output: [2]

Explanation: The deepest leaf node in the tree is 2, the lca of one node is itself.


Constraints:

    -> The number of nodes in the tree will be in the range [1, 1000].
    -> 0 <= Node.val <= 1000
    -> The values of the nodes in the tree are unique.


Concepts: Trees, DFS
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Optimised Solution
def lcaDeepestLeaves(root: TreeNode) -> TreeNode:
    # Helper method to iterate through the tree in DFS-fashion
    def dfs(node, depth):
        if not node:                                                # Check if the node is None
            return (None, depth)                                    # Return the curr-depth

        # Recursively traverse left and right children
        left_lca, left_depth = dfs(node.left, depth + 1)
        right_lca, right_depth = dfs(node.right, depth + 1)

        if left_depth > right_depth:                                # Check if the left-subtree is deeper
            return (left_lca, left_depth)                           # Propagate its LCA and depth upward
        elif right_depth > left_depth:                              # Check if the right-subtree is deeper
            return (right_lca, right_depth)                         # Propagate its LCA and depth upward
        else:                                                       # Check if both subtrees are at the same depth
            return (node, left_depth)                               # Return the curr-node as LCA

    # Recursively traverse the tree, starting at depth 0 (root)
    lca_node, _ = dfs(root, 0)

    return lca_node                                                 # Return the result
