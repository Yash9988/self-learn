"""
1358. Number of Substrings Containing All Three Characters [MEDIUM]

Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.


Example 1:
Input: s = "abcabc"
Output: 10

Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab",
"abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).


Example 2:
Input: s = "aaacb"
Output: 3

Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb".


Example 3:
Input: s = "abc"
Output: 1


Constraints:

    -> 3 <= s.length <= 5 x 10^4
    -> s only consists of a, b or c characters.


Concepts: Substrings, Sliding window
"""


# Optimised Solution
def numberOfSubstrings(s: str) -> int:
    last_pos = [-1] * 3                                             # List to track last-idx of each character
    total = 0                                                       # Counter to track the result

    for pos in range(len(s)):                                       # Iterate through the range of string
        last_pos[ord(s[pos]) - ord('a')] = pos                      # Update the last-idx of curr-char
        total += 1 + min(last_pos)                                  # Increment the counter by the min-idx

    return total                                                    # Return the result


# Alternate Solution
def numberOfSubstrings_alt(s: str) -> int:
    count = 0                                                       # Counter to track the result
    left = 0                                                        # Set the left pointer at the beginning
    char_count = {'a': 0, 'b': 0, 'c': 0}                           # Dict to track the char-count

    for right in range(len(s)):                                     # Iterate through the string
        char_count[s[right]] += 1                                   # Increment the count for curr-char

        # Check if each character has occurred at least once
        while char_count['a'] > 0 and char_count['b'] > 0 and char_count['c'] > 0:
            count += len(s) - right                                 # Increment the counter by the diff
            char_count[s[left]] -= 1                                # Decrement the count for char at left pointer
            left += 1                                               # Increment the pointer

    return count                                                    # Return the result
