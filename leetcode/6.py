"""
6. Zigzag Conversion [MEDIUM]

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display
this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows.


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"


Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"

Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"


Constraints:

    -> 1 <= s.length <= 1000
    -> s consists of English letters (lower-case and upper-case), ',' and '.'.
    -> 1 <= numRows <= 1000


Concepts: Custom Iteration
"""


# My Solution
def convert(s: str, numRows: int) -> str:
    if numRows == 1:                                    # Check if numRows is 1
        return s                                        # Return the input string, unmodified

    steps = list(range(2 * (numRows - 1), 1, -2))       # Create a list of steps based upon the numRows
    steps += steps[:1]                                  # Add the first element to make the list "balanced"

    n, res = len(steps), ""                             # Initialise the empty result string
    for i in range(n):                                  # Iterate through all steps
        j = i                                           # Assign a pointer at current index
        x, y = steps[i], steps[n - i - 1]               # Store the pair of swapping step values (zig/zag)
        while j < len(s):                               # While the pointer index is within the string
            res += s[j]                                 # Add the character at pointer index to result string
            j += x                                      # Increment the pointer by the step value
            x, y = y, x                                 # Swap the value of steps with its counterpart

    return res                                          # Return the result


# Alternate solution
def convert_op(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):               # Check if numRows is 1 or greater than input-string length
        return s                                        # Return the string, unmodified

    L = [''] * numRows                                  # Initialise a list of empty string, for each row
    index, step = 0, 1                                  # Initialise indexer and step-direction for rows

    for x in s:                                         # Iterate through the input string
        L[index] += x                                   # Add the character at current index to the pointed row string
        if index == 0:                                  # Check if row-index is 0
            step = 1                                    # Switch the step-direction to positive
        elif index == numRows - 1:                      # Check if row-index is numRows-1
            step = -1                                   # Switch the step-direction to negative
        index += step                                   # Increment the row-index in the step-direction

    return ''.join(L)                                   # Join all row-strings and return the result
