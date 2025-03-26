"""
1790. Check if One String Swap Can Make Strings Equal [EASY]

You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a
string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the
strings. Otherwise, return false.


Example 1:
Input: s1 = "bank", s2 = "kanb"
Output: true

Explanation: For example, swap the first character with the last character of s2 to make "bank".


Example 2:
Input: s1 = "attack", s2 = "defend"
Output: false

Explanation: It is impossible to make them equal with one string swap.


Example 3:
Input: s1 = "kelb", s2 = "kelb"
Output: true

Explanation: The two strings are already equal, so no string swap operation is required.


Constraints:

    -> 1 <= s1.length, s2.length <= 100
    -> s1.length == s2.length
    -> s1 and s2 consist of only lowercase English letters.


Concepts:
"""


# Optimised Solution
def areAlmostEqual(s1: str, s2: str) -> bool:
    if s1 == s2:                                                    # Check if both strings are equal
        return True                                                 # Return True

    cnt = 0                                                         # Counter to track the character mismatch
    x = y = -1                                                      # Pointers to track the char-mismatch indices

    for i in range(len(s1)):                                        # Iterate through the range of strings
        if s1[i] != s2[i]:                                          # Check if the characters mismatch at curr-idx
            cnt += 1                                                # Increment the counter
            if x == -1:                                             # Check if the first pointer is unassigned
                x = i                                               # Set the pointer at curr-idx
            elif y == -1:                                           # Else, check if the second pointer is unassigned
                y = i                                               # Set the pointer at curr-idx

        if cnt > 2:                                                 # Check if the count is higher than 2
            return False                                            # Return False

    return cnt == 2 and s1[x] == s2[y] and s1[y] == s2[x]           # Compute and return the result
