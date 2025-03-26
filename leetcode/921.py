"""
921. Minimum Add to Make Parentheses Valid [MEDIUM]

A parentheses string is valid if and only if:

    - It is the empty string,
    - It can be written as AB (A concatenated with B), where A and B are valid strings, or
    - It can be written as (A), where A is a valid string.

You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".

Return the minimum number of moves required to make s valid.


Example 1:

Input: s = "())"
Output: 1


Example 2:

Input: s = "((("
Output: 3


Constraints:

    -> 1 <= s.length <= 1000
    -> s[i] is either '(' or ')'.


Concepts: Deque, Counting
"""


# My Solution
def minAddToMakeValid(s: str) -> int:
    dq = []                                     # Initialise a list
    for ch in s:                                # Iterate through all string characters
        if dq and dq[-1] + ch == "()":          # Check for the substring '()' b/w last element of deque & curr-char
            dq.pop()                            # Remove the last element from the deque
            continue                            # Skip to the next iteration
        dq.append(ch)                           # Add the current character to the list

    return len(dq)                              # Compute and return the length of the resulting list
