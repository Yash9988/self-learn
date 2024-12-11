"""
2981. Find Longest Special Substring That Occurs Thrice I [MEDIUM]

You are given a string s that consists of lowercase English letters.

A string is called special if it is made up of only a single character. For example, the string "abc" is not special,
whereas the strings "ddd", "zz", and "f" are special.

Return the length of the longest special substring of s which occurs at least thrice, or -1 if no special substring
occurs at least thrice.

A substring is a contiguous non-empty sequence of characters within a string.


Example 1:
Input: s = "aaaa"
Output: 2

Explanation: The longest special substring which occurs thrice is "aa": substrings "aaaa", "aaaa", and "aaaa".
It can be shown that the maximum length achievable is 2.


Example 2:
Input: s = "abcdef"
Output: -1

Explanation: There exists no special substring which occurs at least thrice. Hence return -1.


Example 3:
Input: s = "abcaba"
Output: 1

Explanation: The longest special substring which occurs thrice is "a": substrings "abcaba", "abcaba", and "abcaba".
It can be shown that the maximum length achievable is 1.


Constraints:

    -> 3 <= s.length <= 50
    -> s consists of only lowercase English letters.


Concepts: Hashmap
"""
from collections import defaultdict


# Optimised Solution
def maximumLength_op(s: str) -> int:

    cnt_dict = defaultdict(list)                                    # Dict to store count-vals for special substrings
    cnt = 0                                                         # Counter to track frequency of substring
    current_c = None                                                # Track the current (continued) char
    s = s + "1"                                                     # Append a "stopper" to the string

    for c in s:                                                     # Iterate through the string
        if not current_c:                                           # Check if the first character of the string
            current_c = c                                           # Initialise the tracker

        if current_c == c:                                          # Check if character is continued for substring
            cnt += 1                                                # Increment the counter
        else:
            cnt_dict[current_c].append(cnt)                         # Append the count to the corr-substring
            current_c = c                                           # Initialise the tracker with curr-char
            cnt = 1                                                 # Reset the counter

    ans = -1                                                        # Counter to store the result
    for k, v in cnt_dict.items():                                   # Iterate through the dict-items
        v = sorted(v, reverse=True)                                 # Sort the count values for substring in reverse

        if v[0] > 2:                                                # Check if the highest value qualifies condition
            ans = max(v[0] - 2, ans)                                # Update the result counter with max-val

        if len(v) >= 2 and v[0] > 1:                                # Check if more than one counts
            ans = max(min(v[0] - 1, v[1]), ans)                     # Update the result counter with max-val

        if len(v) >= 3:                                             # Check if more than two counts
            ans = max(ans, v[2])                                    # Update the result counter with max-val

    return ans                                                      # Return the result


# Alternate Solution
def maximumLength_alt(s: str) -> int:
    mps = defaultdict(int)                                          # Dict to store (substr, count) tuple frequencies

    for i in range(len(s)):                                         # Iterate through the string
        count = 1                                                   # Initialise a counter
        mps[(s[i], count)] += 1                                     # Increment the freq for the curr-tuple

        for j in range(i, len(s)):                                  # Iterate the string starting at curr-idx
            if j + 1 < len(s) and s[j] == s[j + 1]:                 # Check if the adjacent character are equal
                count += 1                                          # Increment the count
                mps[(s[i], count)] += 1                             # Increment the tuple frequency
            else:
                break                                               # Break out of the loop, otherwise

    ans1 = 0                                                        # Initialise the result counter
    for key, value in mps.items():                                  # Iterate through the dict-items
        if value >= 3:                                              # Check if the substring frequency is greater than 3
            ans1 = max(ans1, key[1])                                # Update the counter with max-val

    return ans1 if ans1 != 0 else -1                                # Return the result
