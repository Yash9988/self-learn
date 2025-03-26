"""
1408. String Matching in an Array [EASY]

Given an array of string words, return all strings in words that is a substring of another word. You can return the
answer in any order.

A substring is a contiguous sequence of characters within a string


Example 1:
Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]

Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.


Example 2:
Input: words = ["leetcode","et","code"]
Output: ["et","code"]

Explanation: "et", "code" are substring of "leetcode".


Example 3:
Input: words = ["blue","green","bu"]
Output: []

Explanation: No string of words is substring of another string.


Constraints:

    -> 1 <= words.length <= 100
    -> 1 <= words[i].length <= 30
    -> words[i] contains only lowercase English letters.
    -> All the strings of words are unique.


Concepts: Substring count
"""


# My Solution
def stringMatching(words: list[str]) -> list[str]:
    n = len(words)                                                  # Obtain the size of the input list
    res = []                                                        # List to store the result

    for i in range(n):                                              # Iterate through the range of the list
        for j in range(n):                                          # Iterate through the range of the list
            if i != j and words[i] in words[j]:                     # Check if curr-word is a substring of another
                res.append(words[i])                                # Append the word to the list
                break                                               # Break out of the curr-loop

    return res                                                      # Return the result


# Optimised Solution
def stringMatching_op(words: list[str]) -> list[str]:
    s = ' '.join(words)                                             # Concatenate all words into a string
    return [word for word in words if s.count(word) > 1]            # Check for substrings and return the result
