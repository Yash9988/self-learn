"""
2516. Take K of Each Character From Left and Right [Medium]

You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you
may take either the leftmost character of s, or the rightmost character of s.

Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not
possible to take k of each character.


Example 1:
Input: s = "aabaaaacaabc", k = 2
Output: 8

Explanation:
Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
A total of 3 + 5 = 8 minutes is needed.
It can be proven that 8 is the minimum number of minutes needed.


Example 2:
Input: s = "a", k = 1
Output: -1

Explanation: It is not possible to take one 'b' or 'c' so return -1.


Constraints:

    -> 1 <= s.length <= 10^5
    -> s consists of only the letters 'a', 'b', and 'c'.
    -> 0 <= k <= s.length


Concepts:
"""


# Optimised Solution
def takeCharacters(s: str, k: int) -> int:
    freq = [0] * 3                                          # Initialise a list to track the frequencies of each char
    size = len(s)                                           # Compute the length of the string

    for char in s:                                          # Iterate through the string
        freq[ord(char) - ord('a')] += 1                     # Increment the count of respective character

    left = right = 0                                        # Initialise 2 pointers

    if freq[0] < k or freq[1] < k or freq[2] < k:           # Check if insufficient characters to satisfy requirement
        return -1                                           # Return -1

    for right in range(size):                               # Iterate through the string
        freq[ord(s[right]) - ord('a')] -= 1                 # Decrement the count of respective character

        if freq[0] < k or freq[1] < k or freq[2] < k:       # Check if any character count is less than required value
            freq[ord(s[left]) - ord('a')] += 1              # Increment back the count of the curr-char
            left += 1                                       # Increment the pointer

    return size - (right - left + 1)                        # Compute and return the result