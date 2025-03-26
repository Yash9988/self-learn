"""
951. Flip Equivalent Binary Trees [MEDIUM]

For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise.


Example 1:
Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true

Explanation: We flipped at nodes with values 1, 3, and 5.


Example 2:
Input: root1 = [], root2 = []
Output: true


Example 3:
Input: root1 = [], root2 = [1]
Output: false


Constraints:

    -> The number of nodes in each tree is in the range [0, 100].
    -> Each tree will have unique node values in the range [0, 99].


Concepts: Trees, DFS
"""
from collections import defaultdict, deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# My Solution
def flipEquiv(root1: TreeNode, root2: TreeNode) -> bool:
    # Method to traverse through the tree in DFS
    def traverse(node, parent, s, level=0):
        if not node:                                                # Check if node is None
            return                                                  # Return

        s[level].update([parent.val, node.val])                     # Add the node and its parent to corresponding-level
        traverse(node.left, node, s, level + 1)                     # Traverse to the left child-node
        traverse(node.right, node, s, level + 1)                    # Traverse to the right child-node

    n1, n2 = defaultdict(set), defaultdict(set)                     # Initialise 2 dictionaries to store level-nodes
    traverse(root1, root1, n1)                                      # Traverse first tree
    traverse(root2, root2, n2)                                      # Traverse second tree

    return n1 == n2                                                 # Compare the dictionaries and return the result


# Optimised Solution
def flipEquiv_op(r1: TreeNode, r2: TreeNode) -> bool:
    if not r1 or not r2: return r1 == r2 == None
    return r1.val == r2.val and (flipEquiv_op(r1.left, r2.left) and flipEquiv_op(r1.right, r2.right)
                                 or flipEquiv_op(r1.left, r2.right) and flipEquiv_op(r1.right, r2.left))


# Alternate Solution (BFS)
def flipEquiv_alt1(r1: TreeNode, r2: TreeNode) -> bool:
    dq1, dq2 = map(deque, ([r1], [r2]))
    while dq1 and dq2:
        node1, node2 = dq1.popleft(), dq2.popleft()
        if node1 == node2 == None: continue
        elif not node1 or not node2 or node1.val != node2.val: return False

        if node1.left == node2.left == None or node1.left and node2.left and node1.left.val == node2.left.val:
            dq1.extend([node1.left, node1.right])
        else:
            dq1.extend([node1.right, node1.left])
        dq2.extend([node2.left, node2.right])
    return not dq1 and not dq2


# Alternate Solution (DFS)
def flipEquiv_alt2(r1: TreeNode, r2: TreeNode) -> bool:
    stk1, stk2 = [r1], [r2]
    while stk1 and stk2:
        node1, node2 = stk1.pop(), stk2.pop()
        if node1 == node2 == None:
            continue
        elif not node1 or not node2 or node1.val != node2.val:
            return False

        if node1.left == node2.left == None or node1.left and node2.left and node1.left.val == node2.left.val:
            stk1.extend([node1.left, node1.right])
        else:
            stk1.extend([node1.right, node1.left])
        stk2.extend([node2.left, node2.right])
    return not stk1 and not stk2
