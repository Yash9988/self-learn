"""
1415. The k-th Lexicographical String of All Happy Strings of Length n [MEDIUM]

A happy string is a string that:

    - consists only of letters of the set ['a', 'b', 'c'].
    - s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).

For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are
not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n.


Example 1:
Input: n = 1, k = 3
Output: "c"

Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".


Example 2:
Input: n = 1, k = 4
Output: ""

Explanation: There are only 3 happy strings of length 1.


Example 3:
Input: n = 3, k = 9
Output: "cab"

Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb",
 "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"


Constraints:

    -> 1 <= n <= 10
    -> 1 <= k <= 100


Concepts: Backtracking, Mathematical Intuition
"""


# Optimised Solution
def getHappyString(n: int, k: int) -> str:
    totalHappy = 3 * (2 ** (n - 1))                                 # Compute all possible "happy-strings"

    if k > totalHappy:                                              # Check if `k` is greater than total happy-strings
        return ""                                                   # Return an empty string

    res = ""                                                        # Empty string to store the result
    choices = "abc"                                                 # String of char-choices
    low, high = 1, totalHappy                                       # Pointers for tracking low and high

    for i in range(n):                                              # Iterate through the range all happy-strings
        partition_size = (high - low + 1) // len(choices)           # Computer the partition size

        cur = low                                                   # Create a copy of the low pointer
        for c in choices:                                           # Iterate through the choices
            if k in range(cur, cur + partition_size):               # Check if `k` lies in the current low-high range
                res += c                                            # Append the curr-char to the result string
                low = cur                                           # Set the low-pointer at the curr-pointer
                high = cur + partition_size - 1                     # Set the high-pointer at the end of the partition
                choices = "abc".replace(c, "")                      # Remove the used char from the choices
                break                                               # Break out of the loop
            cur += partition_size                                   # Increment the curr-pointer by the partition size

    return res                                                      # Return the result


# Alternate Solution
def getHappyString_alt(n: int, k: int) -> str:
    # Helper method to backtrack through the result string
    def backtrack(i, happy_str):
        nonlocal count                                              # Reference the non-local variable

        if i == n:                                                  # Check if curr-idx is equal to string length
            count += 1                                              # Increment the counter (finished a string)
            if count == k:                                          # Check if the counter value equals `k`
                return happy_str                                    # Return the result (found k string)
            return None                                             # Return None (wasn't k string)

        for char in "abc":                                          # Iterate through the choices (ensures lex-order)
            if happy_str and happy_str[-1] == char:                 # Check if curr-char equals prev-char
                continue                                            # Skip to the next iteration

            res = backtrack(i + 1, happy_str + char)                # Rec-call the method with modified string
            if res:                                                 # Check if the string is the k-th happy string
                return res                                          # Return the k-th happy-string

        return None                                                 # Return None (never found k-th string)

    count = 0                                                       # Counter to track the i-th happy-string

    return backtrack(0, "") or ""                       # Return the result
