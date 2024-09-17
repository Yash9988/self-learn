"""
3291. Minimum Number of Valid Strings to Form Target I [MEDIUM]

You are given an array of strings words and a string target.

A string x is called valid if x is a _prefix_ of any string in words.

Return the minimum number of valid strings that can be concatenated to form target. If it's not possible to form target,
return -1.

A prefix of a string is a substring that starts from the beginning of the string and extends to any point within it.


Example 1:

Input: words = ["abc","aaaaa","bcdef"], target = "aabcdabc"

Output: 3

Explanation:

The target string can be formed by concatenating:

    Prefix of length 2 of words[1], i.e. "aa".
    Prefix of length 3 of words[2], i.e. "bcd".
    Prefix of length 3 of words[0], i.e. "abc".


Example 2:

Input: words = ["abababab","ab"], target = "ababaababa"

Output: 2

Explanation:

The target string can be formed by concatenating:

    Prefix of length 5 of words[0], i.e. "ababa".
    Prefix of length 5 of words[0], i.e. "ababa".


Example 3:

Input: words = ["abcdef"], target = "xyz"

Output: -1


Constraints:

    -> 1 <= words.length <= 100
    -> 1 <= words[i].length <= 5 * 103
    -> The input is generated such that sum(words[i].length) <= 105.
    -> words[i] consists only of lowercase English letters.
    -> 1 <= target.length <= 5 * 103
    -> target consists only of lowercase English letters.

Concepts: DP & Trie

"""


def minValidStrings(words: list[str], target: str) -> int:
    trie = {}                                           # Initialise the 'trie' data structure
    for word in words:                                  # Iterate through all words
        node = trie                                     # Assign trie root to the current word-node
        for ch in word:                                 # Iterate through each character in word
            node = node.setdefault(ch, {})              # Recursively generate nested trie
        node["#"] = word                                # Assign the key '#' as the word at the last trie reference

    n = len(target)                                     # Obtain the length of target string
    dp = [float('inf')]*(n+1)                           # Initialise the DP
    dp[n] = 0                                           # Assign base case

    for i in range(n-1, -1, -1):                        # Iterate target in reverse to ensure selecting the best prefix
        node = trie                                     # Assign trie root to the current node at index i
        for j in range(i, n):                           # Iterate from current index to the end of target
            if target[j] in node:                       # If the character is indexed in the trie
                node = node[target[j]]                  # Navigate and assign current node, the nested trie within it
            else:
                break
            dp[i] = min(dp[i], 1 + dp[j+1])             # Compare and update the DP

    return dp[0] if dp[0] < float('inf') else -1        # Return the result


# Optimised Solution (Short Runtime)
def minValidStrings_op(words: list[str], target: str) -> int:
    dp = [0] * len(target)                              # Initialise the DP

    def search(prefix):                                 # Helper method for searching prefix in words
        for word in words:                              # Iterate through all words
            if word.startswith(prefix):                 # Check for prefix in each word
                return True
        return False

    l, r = 0, 0                                         # Initialise 2 pointers at the start of the target
    i = 0                                               # Initialise iterator
    while i < len(target):                              # Iterate through all characters in target string
        if l > r:                                       # If pointer 'l' exceeds pointer 'r'
            return -1                                   # Return -1

        strLen = r - l + 1                              # Calculate string length at current location of pointers
        if search(target[l:r + 1]):                     # If prefix is present in any of the words
            if i - strLen >= 0:                         # Update the DP
                dp[i] = dp[i - strLen] + 1
            else:
                dp[i] = 1
            r += 1                                      # Increment right pointer
        else:
            i -= 1                                      # Decrement iterator
            l += 1                                      # Increment left pointer

        i += 1                                          # Increment iterator

    return dp[-1]                                       # Return the result
