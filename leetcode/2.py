"""
2. Add Two Numbers [MEDIUM]

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.


Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]


Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

    -> The number of nodes in each linked list is in the range [1, 100].
    -> 0 <= Node.val <= 9
    -> It is guaranteed that the list represents a number that does not have leading zeros.


Concepts: Linked Lists
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    h = curr = None                                         # Initialise LL-pointers
    c = 0                                                   # Initialise "carry" counter

    while l1 or l2:                                         # Iterate to the end of both LLs
        a = l1.val if l1 else 0                             # Obtain the node value from the first LL
        b = l2.val if l2 else 0                             # Obtain the node value from the second LL
        t = a + b + c                                       # Calculate the sum
        c = t // 10                                         # Calculate the remainder/"carry"

        n = ListNode(t % 10, None)                          # Create a new LL-node with the new total as its value
        if h is None:                                       # Check if head pointer is assigned
            h = curr = n                                    # Assign pointer at the start of the new LL
        else:
            curr.next = n                                   # Update the "next" of previous LL-node to current node
            curr = curr.next                                # Move the pointer to the latest node in LL

        l1 = l1.next if l1 else None                        # Increment the first LL pointer
        l2 = l2.next if l2 else None                        # Increment the second LL pointer

    if c:                                                   # Check if there is any pending "carry" to account for
        curr.next = ListNode(c, None)                       # Create and attach a new node at the end of the LL

    return h                                                # Return the pointer at the head/start of the LL
