"""
3295. Report Spam Message [MEDIUM]

You are given an array of strings message and an array of strings bannedWords.

An array of words is considered spam if there are at least two words in it that exactly match any word in bannedWords.

Return true if the array message is spam, and false otherwise.


Example 1:

Input: message = ["hello","world","leetcode"], bannedWords = ["world","hello"]

Output: true

Explanation:

The words "hello" and "world" from the message array both appear in the bannedWords array.


Example 2:

Input: message = ["hello","programming","fun"], bannedWords = ["world","programming","leetcode"]

Output: false

Explanation:

Only one word from the message array ("programming") appears in the bannedWords array.


Constraints:

    -> 1 <= message.length, bannedWords.length <= 105
    -> 1 <= message[i].length, bannedWords[i].length <= 15
    -> message[i] and bannedWords[i] consist only of lowercase English letters.


Concepts: Hashset
"""
from collections import Counter


# My Solution
def reportSpam(message: list[str], bannedWords: list[str]) -> bool:
    text, ban = Counter(message), set(bannedWords)                  # Convert lists to Set and Counter
    x = 0                                                           # Initialise counter
    for word in ban:                                                # Iterate though all banned words
        x += text[word] if word in text else 0                      # Increment counter by frequency of word in message
        if x > 1:                                                   # If counter is greater than 1
            return True                                             # Return True
    return False                                                    # Return False


# Optimised Solution
def reportSpam_op(message: list[str], bannedWords: list[str]) -> bool:
    s = set(bannedWords)                                            # Convert list of banned words into a set
    return sum(m in s for m in message) > 1                         # Return the sum of occurrences of words in message
