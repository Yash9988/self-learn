"""
1028. Recover a Tree From Preorder Traversal [HARD]

We run a preorder depth-first search (DFS) on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this
node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

If a node has only one child, that child is guaranteed to be the left child.

Given the output traversal of this traversal, recover the tree and return its root.


Example 1:
Input: traversal = "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]


Example 2:
Input: traversal = "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]


Example 3:
Input: traversal = "1-401--349---90--88"
Output: [1,401,null,349,88,90]


Constraints:

    -> The number of nodes in the original tree is in the range [1, 1000].
    -> 1 <= Node.val <= 10^9


Concepts: Trees, DFS
"""
import re


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# My Solution
def recoverFromPreorder(traversal: str) -> TreeNode:
    # Helper method to iterate through the tree in DFS-fashion
    def dfs(node, lvl):
        # Reference to non-local variables
        nonlocal depth
        nonlocal traversal

        if depth == lvl:                                            # Check if the num-depth matches the curr-lvl
            curr = ''                                               # String to store the node-val
            while traversal and traversal[0].isdigit():             # While the first-char is a digit
                curr += traversal.pop(0)                            # Append the char to the string

            node.val = int(curr)                                    # Convert and assign the num as node-val
            depth = 0                                               # Reset the num-depth

            while traversal and traversal[0] == '-':                # While the first-char is a '-'
                depth += 1                                          # Increment the depth counter
                traversal.pop(0)                                    # Pop the element from the list

        if depth > lvl:                                             # Check if the num-depth is greater than curr-lvl
            node.left = TreeNode()                                  # Create a left child-node
            dfs(node.left, lvl + 1)                                 # Iterate to the left child-node

        if depth > lvl:                                             # Check if the num-depth is greater than curr-lvl
            node.right = TreeNode()                                 # Create a right child-node
            dfs(node.right, lvl + 1)                                # Iterate to the right child-node


    root = TreeNode()                                               # Initialise the root node
    traversal = list(traversal)                                     # Convert the string to a list of chars
    depth = 0                                                       # Counter to track the num-depth

    dfs(root, 0)                                                # Iterate through the tree starting from root node

    return root                                                     # Return the result


# Optimised Solution
def recoverFromPreorder_op(traversal: str) -> TreeNode:
    tree_map = {}                                                   # Dict to track nodes at each level
    num = ''                                                        # String to store the first-num

    for ch in traversal:                                            # Iterate through the string
        if ch == '-':                                               # Check if the curr-char is '-'
            break                                                   # Break out of the loop
        num += ch                                                   # Append the curr-char to the num-string

    tree_map[0] = TreeNode(int(num))                                # Create a new node and store it at the root-lvl

    nodes = re.findall(r'(-+)(\d+)', traversal)                     # Obtain all the (dashes, digits) tuples
    for dash, val in nodes:                                         # Iterate through the tuples
        depth = len(dash)                                           # Compute the depth of the node
        num = int(val)                                              # Convert the value of the node from string to int

        parent = tree_map[depth - 1]                                # Obtain node's parent using its depth
        node = TreeNode(num)                                        # Create a new node with the corr-val

        if parent.left is None:                                     # Check if left child-node is absent
            parent.left = node                                      # Assign the node as parent's left child
        else:
            parent.right = node                                     # Assign the node as parent's right child, otherwise

        tree_map[depth] = node                                      # Store the node in the depth at its corr-depth

    return tree_map[0]                                              # Return the result
