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
