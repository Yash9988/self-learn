"""
1957. Delete Characters to Make Fancy String [EASY]

A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.


Example 1:
Input: s = "leeetcode"
Output: "leetcode"

Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".


Example 2:
Input: s = "aaabaaaa"
Output: "aabaa"

Explanation:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".


Example 3:
Input: s = "aab"
Output: "aab"

Explanation: No three consecutive characters are equal, so return "aab".


Constraints:

    -> 1 <= s.length <= 10^5
    -> s consists only of lowercase English letters.


Concepts: Stacks
"""


# My Solution
def makeFancyString(s: str) -> str:
    stack, cnt = [], 0                                          # Initialise a stack and counter
    for ch in s:                                                # Iterate through the string
        if not stack:                                           # Check if stack is empty
            stack.append(ch)                                    # Append the character to stack
            cnt = 1                                             # Set the counter
        elif ch == stack[-1] and cnt < 2:                       # Check if curr-char equals last-char and counter < 2
            stack.append(ch)                                    # Append the character to stack
            cnt += 1                                            # Increment the counter
        elif ch == stack[-1] and cnt == 2:                      # Check if curr-char equals last-char and counter > 2
            continue                                            # Skip the iteration
        else:
            stack.append(ch)                                    # Append the character to stack
            cnt = 1                                             # Set the counter

    return ''.join(stack)                                       # Return the result


# Alternate Solution
def makeFancyString_alt(s: str) -> str:
    stack = []                                                  # Initialise a stack
    for ch in s:                                                # Iterate through the string
        if len(stack) > 1 and stack[-2] == stack[-1] == ch:     # Check if curr-char equals last 2 chars in stack
            stack.pop()                                         # Pop-out the last element from stack
        stack.append(ch)                                        # Append the curr-char to stack

    return ''.join(stack)                                       # Return the result
