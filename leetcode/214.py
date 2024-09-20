"""
214. Shortest Palindrome [HARD]

You are given a string s. You can convert s to a palindrome by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.


Example 1:

Input: s = "aacecaaa"
Output: "aaacecaaa"


Example 2:

Input: s = "abcd"
Output: "dcbabcd"


Constraints:

    -> 0 <= s.length <= 5 * 104
    -> s consists of lowercase English letters only.


Concepts: KMP-Algorithm
"""


def shortestPalindrome(s: str) -> str:
    g = s + "|" + s[::-1]                               # Append the reverse at the end of original string, divided by |
    lps = [-1] + [0] * len(g)                           # Initialise a KMP table
    l, r = -1, 0                                        # Initialise 2 pointers
    while r < len(g):                                   # While pointer is less than the length of modified string
        while l >= 0 and g[l] != g[r]:                  # If the character at pointer indexed don't match
            l = lps[l]                                  # Move the other pointer using the KMP table
        l, r = l + 1, r + 1                             # Increment the pointers
        lps[r] = l                                      # Update the table with respective indexes at pointers

    return s[lps[-1]:][::-1] + s                        # Return the result


def shortestPalindrome_op(s: str) -> str:
    r = s[::-1]                                         # Reverse the original string
    for i in range(len(s) + 1):                         # Iterate through the modified string
        if s.startswith(r[i:]):                         # Check for prefixes in original with substrings from modified
            return r[:i] + s                            # Return the result


"""
-> EXPLANATION

Example: s = dedcba. Then r = abcded and I try these overlays (the part in (...) is the prefix I cut off, I just include
it in the display for better understanding):

  s          dedcba
  r[0:]      abcded    Nope...
  r[1:]   (a)bcded     Nope...
  r[2:]  (ab)cded      Nope...
  r[3:] (abc)ded       Yes! Return abc + dedcba

"""