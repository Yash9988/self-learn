"""
5. Longest Palindromic Substring [MEDIUM]

Given a string s, return the longest _palindromic substring_ in s.


Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.


Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

    -> 1 <= s.length <= 1000
    -> s consist of only digits and English letters.


Concepts: Double Pointers, Manacher's Algorithm
"""


# Expand center using double pointers [Time: O(N^2); Space: O(1)]
def longestPalindrome(s: str) -> str:
    def expandCenter(l: int, r: int) -> str:                # Helper method to expand outwards from indexes
        while l >= 0 and r < len(s) and s[l] == s[r]:       # While characters at pointers match
            l -= 1                                          # Decrement left pointer
            r += 1                                          # Increment right pointer
        return s[l + 1: r]                                  # Return longest palindrome string

    if len(s) <= 0:                                         # Check if string is empty or a single character
        return s

    max_str = s[0]                                          # Initialise "result" with first character
    for i in range(len(s)):                                 # Iterate through the input string
        odd = expandCenter(i, i)                            # Check for odd-sized palindromes from current index
        even = expandCenter(i, i + 1)                       # Check for even-sized palindromes from current index

        if len(odd) > len(max_str):                         # Compare the lengths
            max_str = odd                                   # Assign the longest palindrome to the result variable
        if len(even) > len(max_str):                        # Compare the lengths
            max_str = even                                  # Assign the longest palindrome to the result variable

    return max_str                                          # Return the result


# Manacher's Algorithm [Time: O(N); Space: O(N)]
def longestPalindrome_op(s: str) -> str:
    if len(s) <= 1:                                             # Check if string is empty or a single character
        return s                                                # Return the string

    max_len = 1                                                 # Initialise length counter
    max_str = s[0]                                              # Assign first character as max-string
    s = '#' + '#'.join(s) + '#'                                 # Append '#' between each string character
    dp = [0 for _ in range(len(s))]                             # Initialise a DP array
    center = 0                                                  # Initialise the center pointer
    right = 0                                                   # Initialise the right pointer

    for i in range(len(s)):                                     # Iterate through the (modified) string
        if i < right:                                           # Check if iterator is less than the right pointer
            dp[i] = min(right - i, dp[2 * center - i])          # Update the DP at index with the minimum value

        while i - dp[i] - 1 >= 0 and i + dp[i] + 1 < len(s) \
                and s[i - dp[i] - 1] == s[i + dp[i] + 1]:       # Check if indexes within array range and elements match
            dp[i] += 1                                          # Increment the DP value at iterator index

        if i + dp[i] > right:                                   # Check if iterator + sub-length is > right pointer
            center = i                                          # Set the center pointer at current iterator index
            right = i + dp[i]                                   # Set the right pointer at the end of the substring

        if dp[i] > max_len:                                     # If the DP value is greater than the max-length, so far
            max_len = dp[i]                                     # Update the max-length value
            max_str = (s[i - dp[i]:i + dp[i] + 1]
                       .replace('#', ''))                       # Update the maximum substring value
    return max_str                                              # Return the result
