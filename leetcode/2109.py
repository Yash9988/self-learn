"""
2109. Adding Spaces to a String [MEDIUM]

You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices in the original
string where spaces will be added. Each space should be inserted before the character at the given index.

    - For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces before 'Y' and 'C', which are at
      indices 5 and 9 respectively. Thus, we obtain "Enjoy Your Coffee".

Return the modified string after the spaces have been added.


Example 1:
Input: s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]
Output: "Leetcode Helps Me Learn"

Explanation:
The indices 8, 13, and 15 correspond to the underlined characters in "LeetcodeHelpsMeLearn".
We then place spaces before those characters.


Example 2:
Input: s = "icodeinpython", spaces = [1,5,7,9]
Output: "i code in py thon"

Explanation:
The indices 1, 5, 7, and 9 correspond to the underlined characters in "icodeinpython".
We then place spaces before those characters.


Example 3:
Input: s = "spacing", spaces = [0,1,2,3,4,5,6]
Output: " s p a c i n g"

Explanation:
We are also able to place spaces before the first character of the string.


Constraints:

    -> 1 <= s.length <= 3 * 10^5
    -> s consists only of lowercase and uppercase English letters.
    -> 1 <= spaces.length <= 3 * 10^5
    -> 0 <= spaces[i] <= s.length - 1
    -> All the values of spaces are strictly increasing.


Concepts: Strings
"""


# My Solution
def addSpaces(s: str, spaces: list[int]) -> str:
    j = 0                                                           # Pointer for tracking space-indexes
    m, n = len(spaces), len(s)                                      # Obtain the size of both lists
    res = ""                                                        # Initialise an empty string to store the result

    for i in range(n):                                              # Iterate through the string
        if j < m and i == spaces[j]:                                # Check if curr-idx matches the value at pointer
            res += " "                                              # Append a space in the result string
            j += 1                                                  # Increment the pointer
        res += s[i]                                                 # Append the character at curr-idx to the result

    return res                                                      # Return the result


# Optimised Solution
def addSpaces_op(s: str, spaces: list[int]) -> str:
    index, result = 0, []                                           # Initialise a counter and a list

    for space in spaces:                                            # Iterate through the space-indexes
        result.append(s[index: space])                              # Slice and append the string from idx to space-idx
        index = space                                               # Update the counter to value to space-idx

    result.append(s[index:])                                        # Append the last slice to the list

    return " ".join(result)                                         # Join w/ spaces and return the result
