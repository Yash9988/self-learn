"""
889. Construct Binary Tree from Preorder and Postorder Traversal [MEDIUM]

Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct
values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.


Example 1:
Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]


Example 2:
Input: preorder = [1], postorder = [1]
Output: [1]


Constraints:

    -> 1 <= preorder.length <= 30
    -> 1 <= preorder[i] <= preorder.length
    -> All the values of preorder are unique.
    -> postorder.length == preorder.length
    -> 1 <= postorder[i] <= postorder.length
    -> All the values of postorder are unique.
    -> It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same
       binary tree.


Concepts: Trees, DFS
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Optimised Solution
def constructFromPrePost(preorder: list[int], postorder: list[int]) -> TreeNode:
    # preorder = root, left, right
    # postorder = left, right, root

    # Helper method to create a tree-node
    def makeTree():
        node = TreeNode(postorder.pop())                            # Take the root from postorder; post = [left, right]

        # Check if postorder node isn't right leaf; post = [left, right], pre = [root, left, right]
        if node.val != preorder[-1]:
            node.right = makeTree()                                 # Build right subtree

        # Check if postorder node isn't left leaf; post = [left], pre = [root, left]
        if node.val != preorder[-1]:
            node.left = makeTree()                                  # Build left subtree

        preorder.pop()                                              # Root already used; post = [], pre = [root]

        return node

    return makeTree()                                               # Return the result
