"""
1769. Minimum Number of Operations to Move All Balls to Each Box [MEDIUM]

You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and
'1' if it contains one ball.

In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1.
Note that after doing so, there may be more than one ball in some boxes.

Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to
the i-th box.

Each answer[i] is calculated considering the initial state of the boxes.


Example 1:
Input: boxes = "110"
Output: [1,1,3]

Explanation: The answer for each box is as follows:
1) First box: you will have to move one ball from the second box to the first box in one operation.
2) Second box: you will have to move one ball from the first box to the second box in one operation.
3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball
   from the second box to the third box in one operation.


Example 2:
Input: boxes = "001011"
Output: [11,8,5,4,3,4]


Constraints:

    -> n == boxes.length
    -> 1 <= n <= 2000
    -> boxes[i] is either '0' or '1'.


Concepts: Cost Minimization
"""


# My Solution
def minOperations(boxes: str) -> list[int]:
    n = len(boxes)                                                  # Compute the size of the input string
    res = [0] * n                                                   # List to track the result
    idx = [i for i in range(n) if boxes[i] == '1']                  # List to store indices of all '1's in the string

    for i in range(n):                                              # Iterate through the string range
        res[i] = sum([abs(i - x) for x in idx])                     # Update the result at index w/ the sum of diff

    return res                                                      # Return the result


# Optimised Solution
def minOperations_op(boxes: str) -> list[int]:
    answer = []                                                     # List to store the result
    pref = p = s = 0                                                # Counters to track cost, present and passed '1's
    for i, el in enumerate(boxes):                                  # Iterate through the string
        if el == '1':                                               # Check if the curr-char is '1'
            pref += i                                               # Increment the cost by curr-idx
            p += 1                                                  # Increment the present '1's counter

    for el in boxes:                                                # Iterate through the string
        answer.append(pref)                                         # Append the cost to the list
        if el == '1':                                               # Check if the curr-char is '1'
            p -= 1                                                  # Decrement the present '1's counter
            s += 1                                                  # Increment the passed '1's counter

        pref = pref - p + s                                         # Update the cost value

    return answer                                                   # Return the result


# Alternate Solution
def minOperations_alt(boxes: str) -> list[int]:
    n = len(boxes)                                                  # Obtain the size of the input string
    ans = [0] * n                                                   # List to track the result
    leftCount = leftCost = rightCount = rightCost = 0               # Counters to track respective count & costs

    for i in range(1, n):                                           # Iterate through the string range
        if boxes[i - 1] == '1':                                     # Check if prev-char was '1'
            leftCount += 1                                          # Increment the left-count

        leftCost += leftCount                                       # Increment the left-cost by the left-count value
        ans[i] = leftCost                                           # Update the result at idx

    for i in range(n - 2, -1, -1):                                  # Iterate through the list range, in reverse
        if boxes[i + 1] == '1':                                     # Check if the prev-char was '1'
            rightCount += 1                                         # Increment the right-count

        rightCost += rightCount                                     # Increment the right-cost by the right-count value
        ans[i] += rightCost                                         # Increment the result at idx by the right-cost-val

    return ans                                                      # Return the result


"""
For each index, the cost to move all boxes to it is sum of the cost `leftCost` to move all left boxes to it, and the 
cost `rightCost` to move all right boxes to it.

    - leftCost for all indexes can be calculated using a single pass from left to right.
    - rightCost for all indexes can be calculated using a single pass from right to left.

Example:

    boxes       |   11010
    leftCount   |   01223
    leftCost    |   01358
    rightCount  |   21100
    rightCost   |   42100
    ans         |   43458

"""