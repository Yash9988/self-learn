"""
2471. Minimum Number of Operations to Sort a Binary Tree by Level [MEDIUM]

You are given the root of a binary tree with unique values.

In one operation, you can choose any two nodes at the same level and swap their values.

Return the minimum number of operations needed to make the values at each level sorted in a strictly increasing order.

The level of a node is the number of edges along the path between it and the root node.


Example 1:
Input: root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]
Output: 3

Explanation:
- Swap 4 and 3. The 2nd level becomes [3,4].
- Swap 7 and 5. The 3rd level becomes [5,6,8,7].
- Swap 8 and 7. The 3rd level becomes [5,6,7,8].
We used 3 operations so return 3.
It can be proven that 3 is the minimum number of operations needed.


Example 2:
Input: root = [1,3,2,7,6,5,4]
Output: 3

Explanation:
- Swap 3 and 2. The 2nd level becomes [2,3].
- Swap 7 and 4. The 3rd level becomes [4,6,5,7].
- Swap 6 and 5. The 3rd level becomes [4,5,6,7].
We used 3 operations so return 3.
It can be proven that 3 is the minimum number of operations needed.


Example 3:
Input: root = [1,2,3,4,5,6]
Output: 0

Explanation: Each level is already sorted in increasing order so return 0.


Constraints:

    -> The number of nodes in the tree is in the range [1, 10^5].
    -> 1 <= Node.val <= 10^5
    -> All the values of the tree are unique.


Concept: Trees, BFS, Swap Sort/Index Sort
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Optimised Solution
def minimumOperations(root: TreeNode) -> int:
    stack, res = [root], 0                                          # Stack to track tree nodes in BFS fashion

    while stack:                                                    # While stack is non-empty
        temp = []                                                   # List to store the nodes from next level
        for node in stack:                                          # Iterate through the (parent-level) stack
            if node.left:                                           # Check if the left child-node exists
                temp.append(node.left)                              # Append the node to the list

            if node.right:                                          # Check if the right child-node exists
                temp.append(node.right)                             # Append the node to the list

        stack = temp                                                # Replace the parent-level stack with child-level
        dict_lvl = {node.val: i for i, node in enumerate(stack)}    # Dict to track indices for the level-nodes
        sort_lvl = sorted(dict_lvl.keys())                          # Sort and store the level-node values

        while dict_lvl:                                             # While the dict is non-empty
            _, i = dict_lvl.popitem()                               # Pop an item from the dict

            while sort_lvl[i] in dict_lvl:                          # While the desired/sorted item is "out of place"
                i = dict_lvl.pop(sort_lvl[i])                       # Pop that item from the dict
                res += 1                                            # Increment the swap counter

    return res                                                      # Return the result
