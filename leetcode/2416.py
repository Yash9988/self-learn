"""
2416. Sum of Prefix Scores of Strings [HARD]

You are given an array words of size n consisting of non-empty strings.

We define the score of a string word as the number of strings words[i] such that word is a prefix of words[i].

For example, if words = ["a", "ab", "abc", "cab"], then the score of "ab" is 2, since "ab" is a prefix of both "ab" and
"abc".

Return an array answer of size n where answer[i] is the sum of scores of every non-empty prefix of words[i].

Note that a string is considered as a prefix of itself.


Example 1:

Input: words = ["abc","ab","bc","b"]
Output: [5,4,3,2]

Explanation: The answer for each string is the following:
- "abc" has 3 prefixes: "a", "ab", and "abc".

- There are 2 strings with the prefix "a", 2 strings with the prefix "ab", and 1 string with the prefix "abc".
The total is answer[0] = 2 + 2 + 1 = 5.

- "ab" has 2 prefixes: "a" and "ab".

- There are 2 strings with the prefix "a", and 2 strings with the prefix "ab".
The total is answer[1] = 2 + 2 = 4.

- "bc" has 2 prefixes: "b" and "bc".

- There are 2 strings with the prefix "b", and 1 string with the prefix "bc".
The total is answer[2] = 2 + 1 = 3.

- "b" has 1 prefix: "b".

- There are 2 strings with the prefix "b".
The total is answer[3] = 2.


Example 2:

Input: words = ["abcd"]
Output: [4]

Explanation:
"abcd" has 4 prefixes: "a", "ab", "abc", and "abcd".
Each prefix has a score of one, so the total is answer[0] = 1 + 1 + 1 + 1 = 4.


Constraints:

    -> 1 <= words.length <= 1000
    -> 1 <= words[i].length <= 1000
    -> words[i] consists of lowercase English letters.


Concepts: DP, Trie
"""


# My Solution
def sumPrefixScores(words: list[str]) -> list[int]:
    # root, dp = {}, {}                                         # Initialise DP and trie-root node
    dp = {}                                                     # Initialise DP
    for word in words:                                          # Iterate through all words
        pre = ""                                                # Initialise an empty string
        # node = root                                           # Assign reference to the trie-root
        for ch in word:                                         # Iterate through each character of the word
            pre += ch                                           # Append character to the prefix-string
            dp[pre] = dp.get(pre, 0) + 1                        # Increment the prefix-frequency in the DP

            # if ch not in node:                                # If the character is not a child reference of the node
            #     node[ch] = {}                                 # Assign the child key, an instance of another trie-node
            # node = node[ch]                                   # Traverse the current node to the nested trie-node

    res = []                                                    # Initialise the "result" array
    for word in words:                                          # Iterate through all words
        t = sum([dp[word[:i+1]] for i in range(len(word))])     # Sum frequencies of all the substring-prefixes
        res.append(t)                                           # Append the sum to the result array

    return res                                                  # Return the result


# Optimised Solution
def sumPrefixScores_op(words: list[str]) -> list[int]:
    root = {}                                                   # Initialise the trie-root node
    for word in words:                                          # Iterate through all the words
        node = root                                             # Assign reference to the trie-root
        for ch in word:                                         # Iterate through all character in the word
            if ch not in node:                                  # Check if character not a child of the current node
                node[ch] = [0, {}]                              # Assign a child reference to the current node

            node[ch][0] += 1                                    # Increment the frequency of the observed prefix
            node = node[ch][1]                                  # Traverse the current node to the nested trie

    res = []                                                    # Initialise the "result" array
    for word in words:                                          # Iterate through all words
        node, t = root, 0                                       # Initialise reference to the trie-root and a counter
        for ch in word:                                         # Iterate through all characters in the word
            t += node[ch][0]                                    # Increment the counter by the frequency of the prefix
            node = node[ch][1]                                  # Traverse the current node to the nested trie
        res.append(t)                                           # Append the counter value to the "result" array

    return res                                                  # Return the result
