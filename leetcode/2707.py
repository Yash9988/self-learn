"""
2707. Extra Characters in a String [MEDIUM]

You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more
non-overlapping substrings such that each substring is present in dictionary. There may be some extra characters in s
which are not present in any of the substrings.

Return the minimum number of extra characters left over if you break up s optimally.


Example 1:

Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
Output: 1
Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. There is only 1
unused character (at index 4), so we return 1.


Example 2:

Input: s = "sayhelloworld", dictionary = ["hello","world"]
Output: 3
Explanation: We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12. The characters
at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.


Constraints:

    -> 1 <= s.length <= 50
    -> 1 <= dictionary.length <= 50
    -> 1 <= dictionary[i].length <= 50
    -> dictionary[i] and s consists of only lowercase English letters
    -> dictionary contains distinct words


Concepts: DP, Trie
"""


# Bottom-Up Approach [Time: O(N^2); Space: O(N)]
def minExtraChar(s: str, dictionary: list[str]) -> int:
    max_val = len(s) + 1                                # Select an arbitrary large value to denote unchecked index
    dp = [max_val] * max_val                            # Initialise a DP with the selected value
    dp[0] = 0                                           # Set the first DP value to 0, indicating extra-chars at index
    words = set(dictionary)                             # Convert list of dictionary into a set for inexpensive look-up

    for i in range(1, max_val):                         # Iterate through the input string (i + 1)
        dp[i] = dp[i - 1] + 1                           # Update the DP value at current index with worst-case scenario
        for l in range(1, i + 1):                       # Iterate in reverse to the string head, looking for matches
            if s[i - l:i] in words:                     # Check if substring is in dictionary
                dp[i] = min(dp[i], dp[i - l])           # Update the DP value at index with the minimum

    return dp[-1]                                       # Return the final DP value, indicating the minimum extra-chars


# Trie Approach
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


def buildTrie(words):                                           # Helper function to initialise a Trie from a list
    root = TrieNode()                                           # Initialise the root of Trie
    for word in words:                                          # Iterate though all the words
        node = root                                             # Assign a copy of the root
        for ch in word:                                         # Iterate through each character of the word
            if ch not in node.children:                         # Check if Trie contains child reference to the char
                node.children[ch] = TrieNode()                  # Assign a new Trie-node as the value to the char
            node = node.children[ch]                            # Iterate to the reference child Trie-node
        node.is_word = True                                     # Update the attribute at the end of word iteration
    return root                                                 # Return the root node


def minExtraChar_op(s: str, dictionary: list[str]) -> int:

    n = len(s)                                                  # Store the length of the string
    root = buildTrie(dictionary)                                # Create a Trie for the dictionary of words
    dp = [float('inf')] * (n + 1)                               # Initialise a DP
    dp[-1] = 0                                                  # Assign the last value as zero, for extra-characters

    for i in reversed(range(n)):                                # Iterate through the string in reverse
        dp[i] = dp[i + 1] + 1                                   # Update the DP value at index with worst-case scenario
        node = root                                             # Assign a copy of the root Trie node
        for j in range(i, n):                                   # Iterate from the current index to the end of string
            if s[j] not in node.children:                       # Check if the character is a child of current trie
                break                                           # Break the loop if there is no child-reference
            node = node.children[s[j]]                          # Iterate to the nested trie node within the child-ref
            if node.is_word:                                    # Check if character denotes the completion of a word
                dp[i] = min(dp[i], dp[j + 1])                   # Update the DP value at current iterator index

    return dp[0]                                                # Return the minimum DP value for extra-char present
