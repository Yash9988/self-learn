"""
3324. Find the Sequence of Strings Appeared on the Screen [MEDIUM]

You are given a string target.

Alice is going to type target on her computer using a special keyboard that has only two keys:

    - Key 1 appends the character "a" to the string on the screen.
    - Key 2 changes the last character of the string on the screen to its next character in the English alphabet. For
      example, "c" changes to "d" and "z" changes to "a".

Note that initially there is an empty string "" on the screen, so she can only press key 1.

Return a list of all strings that appear on the screen as Alice types target, in the order they appear, using the
minimum key presses.


Example 1:
Input: target = "abc"
Output: ["a","aa","ab","aba","abb","abc"]

Explanation:
The sequence of key presses done by Alice are:

    - Press key 1, and the string on the screen becomes "a".
    - Press key 1, and the string on the screen becomes "aa".
    - Press key 2, and the string on the screen becomes "ab".
    - Press key 1, and the string on the screen becomes "aba".
    - Press key 2, and the string on the screen becomes "abb".
    - Press key 2, and the string on the screen becomes "abc".

Example 2:
Input: target = "he"
Output: ["a","b","c","d","e","f","g","h","ha","hb","hc","hd","he"]


Constraints:

    -> 1 <= target.length <= 400
    -> target consists only of lowercase English letters.


Concepts: String Concatenation
"""


# My Solution
def stringSequence(target: str) -> list[str]:
    curr = []                                                       # List to track curr-str
    res, i = [], 0                                                  # List to store the result

    while ''.join(curr) != target:                                  # While the curr-str doesn't match the target
        curr.append('a')                                            # Append 'a' to the curr-str list
        diff = ord(target[i]) - 97                                  # Compute the diff b/w curr-char and target-char
        res.append(''.join(curr))                                   # Append the curr-string to the result list

        for _ in range(diff):                                       # Iterate through the range of diff
            curr[-1] = chr(ord(curr[-1]) + 1)                       # Modify the last char to the next char
            res.append(''.join(curr))                               # Append the modified curr-string to the list

        i += 1                                                      # Increment the pointer

    return res                                                      # Return the result


# Optimised Solution
def stringSequence_op(target: str) -> list[str]:
    s, res = '', []                                                 # List to track the result

    for ch in target:                                               # Iterate through the target string
        curr = 'a'                                                  # Start with the char 'a'
        while curr != ch:                                           # While the curr-char doesn't match the target-char
            res.append(s + curr)                                    # Extend and append the string with the curr-char
            curr = chr(ord(curr) + 1)                               # Increment the curr-char to the next in sequence

        res.append(s + curr)                                        # Append the correct sub-string to the list
        s = s + curr                                                # Modify the curr-str to include the correct char

    return res                                                      # Return the result
