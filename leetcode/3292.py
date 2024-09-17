"""
3292. Minimum Number of Valid Strings to Form Target II [HARD]

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
    -> 1 <= words[i].length <= 5 * 104
    -> The input is generated such that sum(words[i].length) <= 105.
    -> words[i] consists only of lowercase English letters.
    -> 1 <= target.length <= 5 * 104
    -> target consists only of lowercase English letters.

"""


def minValidStrings(words: list[str], target: str) -> int:
    dp = [0] * len(target)                                              # Initialise the DP (Cost to form the prefix)

    def search(prefix):                                                 # Helper method to search for prefix in words
        for word in words:                                              # Iterate through all words
            if word.startswith(prefix):                                 # Check if prefix in current word
                return True
        return False

    left, right = 0, 0                                                  # Initialise 2 pointers at the start of target

    for i in range(len(target)):                                        # Iterate through the target string
        while not search(target[left:right + 1]) and left <= right:     # Check if prefix is in any of the words
            left += 1                                                   # Increment the left pointer, while true

        if left > right:                                                # If left pointer precedes the right one
            return -1                                                   # Return -1

        strLen = right - left + 1                                       # Calculate the current substring length
        dp[i] = 1 if i < strLen else dp[i - strLen] + 1                 # Update the DP

        right += 1                                                      # Increment the right pointer

    return dp[-1]                                                       # Return the result
