"""
2641. Cousins in Binary Tree II [MEDIUM]

Given the root of a binary tree, replace the value of each node in the tree with the sum of all its cousins' values.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Return the root of the modified tree.

Note that the depth of a node is the number of edges in the path from the root node to it.


Example 1:

Input: root = [5,4,9,1,10,null,7]
Output: [0,0,0,7,7,null,11]

Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
- Node with value 5 does not have any cousins so its sum is 0.
- Node with value 4 does not have any cousins so its sum is 0.
- Node with value 9 does not have any cousins so its sum is 0.
- Node with value 1 has a cousin with value 7 so its sum is 7.
- Node with value 10 has a cousin with value 7 so its sum is 7.
- Node with value 7 has cousins with values 1 and 10 so its sum is 11.


Example 2:

Input: root = [3,1,2]
Output: [0,0,0]

Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
- Node with value 3 does not have any cousins so its sum is 0.
- Node with value 1 does not have any cousins so its sum is 0.
- Node with value 2 does not have any cousins so its sum is 0.


Constraints:

    -> The number of nodes in the tree is in the range [1, 10^5].
    -> 1 <= Node.val <= 10^4


Concepts: Tree, DFS
"""
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# My Solution
def replaceValueInTree(root: TreeNode) -> TreeNode:
    # Method to traverse tree using DFS
    def traverse(node, level=0):
        if not node:                                # Check if node is None
            return                                  # Return

        sums[level] += node.val                     # Accumulate the node value to the corresponding level-sum
        traverse(node.left, level + 1)              # Traverse to the left child-node
        traverse(node.right, level + 1)             # Traverse to the right child-node

    # Method to resolve missing child-node values
    def fix(node):
        return node.val if node else 0              # Check if node is None, else return its value

    # Method to update node values
    def update(node, total, level=0):
        if node is None:                            # Check if node is None
            return                                  # Return

        sub = fix(node.left) + fix(node.right)      # Compute the sum of the child-node values

        update(node.left, sub, level + 1)           # Traverse to the left node
        update(node.right, sub, level + 1)          # Traverse to the right node

        node.val = sums[level] - total              # Update the node value

    sums = defaultdict(int)                         # Initialise a dictionary to store level-sums
    traverse(root)                                  # Traverse through the tree
    update(root, root.val, 0)                       # Traverse and update the node values in the tree

    return root                                     # Return the result
