"""
Given two strings: s and t; remove characters from 't' such that, it becomes a subsequence of 's'.

The score is calculated as: right - left + 1, where
    - 'left' is the minimum index amongst all removed characters
    - 'right' is the maximum index amongst all removed characters

Return the minimum score possible.
"""


def MinScoreSubSeq(s: str, t: str) -> int:
    ns, nt = len(s), len(t)                         # Store the size of string s and t
    k = j = nt - 1                                  # Initialise pointers at the end of string t

    dp = [-1 for _ in range(nt)]                    # Initialise the DP

    for i in range(ns - 1, -1, -1):                 # Iterate string s in reverse to index all suffixes
        if j > -1 and s[i] == t[j]:                 # If element in string s matches element in string t
            dp[k] = i                               # Store the index for element t in the DP
            j -= 1                                  # Decrement the pointers
            k -= 1

    # ans = k + 1                                   # Set the counter at the pointer k, post increment
    # if not ans:                                   # If the k is at index 0, there is no room for any prefixes
    #     return 0                                  # Hence return 0 as the minimum score

    j = 0                                           # Initialise pointer at start of string s
    ans = k - j + 1
    for i in range(ns):                             # Iterate through string to index all prefixes
        if j < nt and s[i] == t[j]:                 # If element in string s matches element in string t
            j += 1                                  # Increment pointer
            ans = min(ans, k - j + 1)               # Minimize; right - left + 1

            while k < nt and dp[k] <= i:            # Until the value is more than index i, to account for the prefix
                k += 1                              # Increment the DP pointer

    return ans                                      # Return the result


# print(MinScoreSubSeq("abacaba", "bzaa"))
# print(MinScoreSubSeq("cde", "xyz"))
# print(MinScoreSubSeq("akbclghmdenfop", "abcigjhkdef"))    # TODO: Rectify the bug (Expected: 5; Actual: 6)
