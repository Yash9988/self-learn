"""
1346. Check If N and Its Double Exist [EASY]

Given an array arr of integers, check if there exist two indices i and j such that:

    -> i != j
    -> 0 <= i, j < arr.length
    -> arr[i] == 2 * arr[j]


Example 1:
Input: arr = [10,2,5,3]
Output: true

Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]


Example 2:
Input: arr = [3,1,7,11]
Output: false

Explanation: There is no i and j that satisfy the conditions.


Constraints:

    -> 2 <= arr.length <= 500
    -> -10^3 <= arr[i] <= 10^3


Concepts: Sets
"""


# My Solution (Partial)
def checkIfExist(arr: list[int]) -> bool:
    seen = set([])                                                  # Initialise a set to track all the seen elements

    for a in arr:                                                   # Iterate through the array
        if 2 * a in seen or a / 2 in seen:                          # Check if half/double of curr-val exists in the set
            return True                                             # Return True
        seen.add(a)                                                 # Append the element to the set

    return False                                                    # Return False
