"""
3208. Alternating Groups II [MEDIUM]

There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i
is represented by colors[i]:

    - colors[i] == 0 means that tile i is red.
    - colors[i] == 1 means that tile i is blue.

An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except
the first and last one has a different color from its left and right tiles).

Return the number of alternating groups.

Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.


Example 1:
Input: colors = [0,1,0,1,0], k = 3
Output: 3


Example 2:
Input: colors = [0,1,0,0,1,0,1], k = 6
Output: 2


Example 3:
Input: colors = [1,1,0,1], k = 4
Output: 0


Constraints:

    -> 3 <= colors.length <= 10^5
    -> 0 <= colors[i] <= 1
    -> 3 <= k <= colors.length


Concepts:
"""


# Optimised Solution
def numberOfAlternatingGroups(colors: list[int], k: int) -> int:
    l = []                                                          # List to track repeating color index
    n = len(colors)                                                 # Obtain the list size
    for i in range(n - 1):                                          # Iterate through the list of colors
        if colors[i] == colors[i + 1]:                              # Check for repeating colors
            l.append(i)                                             # Append the index to the list

    if colors[n - 1] == colors[0]:                                  # Check for the cyclic repeat-case
        l.append(n - 1)                                             # Append the index to the list

    if len(l) == 0:                                                 # Check if the list is empty
        return n                                                    # Return the size of the list

    l.append(l[0] + n)                                              # Increment and append the first index by list size

    res = 0                                                         # Counter to track the result
    for i in range(len(l) - 1):                                     # Iterate through the list of indexes
        res += max(0, l[i + 1] - l[i] - k + 1)                      # Increment the counter by max-val

    return res                                                      # Return the result
