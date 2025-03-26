"""
1261. Find Elements in a Contaminated Binary Tree [MEDIUM]

Given a binary tree with the following rules:

    - root.val == 0
    - For any treeNode:
        - If treeNode.val has a value x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
        - If treeNode.val has a value x and treeNode.right != null, then treeNode.right.val == 2 * x + 2

Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

Implement the FindElements class:

    - FindElements(TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
    - bool find(int target) Returns true if the target value exists in the recovered binary tree.


Example 1:
Input:
["FindElements","find","find"]
[[[-1,null,-1]],[1],[2]]
Output:
[null,false,true]

Explanation:
FindElements findElements = new FindElements([-1,null,-1]);
findElements.find(1); // return False
findElements.find(2); // return True


Example 2:
Input:
["FindElements","find","find","find"]
[[[-1,-1,-1,-1,-1]],[1],[3],[5]]
Output:
[null,true,true,false]

Explanation:
FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
findElements.find(1); // return True
findElements.find(3); // return True
findElements.find(5); // return False


Example 3:
Input:
["FindElements","find","find","find","find"]
[[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]
Output:
[null,true,false,false,true]

Explanation:
FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
findElements.find(2); // return True
findElements.find(3); // return False
findElements.find(4); // return False
findElements.find(5); // return True


Constraints:

    -> TreeNode.val == -1
    -> The height of the binary tree is less than or equal to 20
    -> The total number of nodes is between [1, 10^4]
    -> Total calls of find() is between [1, 10^4]
    -> 0 <= target <= 10^6


Concepts: Trees, DFS
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# My Solution
class FindElements:
    def __init__(self, root: TreeNode):
        # Helper method to recover the original binary tree
        def recover(node, val):
            if node is None:                                        # Check if the curr-node is None
                return                                              # Break out of the rec-call

            node.val = val                                          # Update the node-val
            recover(node.left, 2 * val + 1)                         # Iterate to the left child-node
            recover(node.right, 2 * val + 2)                        # Iterate to the right child-node

        self.root = root                                            # Store the root-node
        recover(self.root, 0)                                   # Recover the tree-vals starting from the root node

    def find(self, target: int) -> bool:
        # Helper method to iterate through the tree to find the target element, in DFS fashion
        def dfs(node):
            if node is None:                                        # Check if the curr-node is None
                return False                                        # Return False

            if node.val == target:                                  # Check if the node-val matches the target
                return True                                         # Return True

            return dfs(node.left) or dfs(node.right)                # Return the rec-result

        return dfs(self.root)                                       # Iterate through the tree and return the result


# Optimised Solution
class FindElementsOP:
    def __init__(self, root: TreeNode):
        # Helper method to iterate through the tree and store the node values
        def recover(node, val):
            if node is None:                                        # Check if the curr-node is None
                return                                              # Break out of the rec-call

            self.vals.add(val)                                      # Append the node-val to the set
            recover(node.left, 2 * val + 1)                         # Iterate to the left child-node
            recover(node.right, 2 * val + 2)                        # Iterate to the right child-node

        self.vals = set()                                           # Set to store all node values
        recover(root, 0)                                        # Iterate through the tree starting at the root

    def find(self, target: int) -> bool:
        return target in self.vals                                  # Check and return the result
