"""
3163. String Compression III [MEDIUM]

Given a string word, compress it using the following algorithm:

    - Begin with an empty string comp. While word is not empty, use the following operation:
        -- Remove a maximum length prefix of word made of a single character c repeating at most 9 times.
        -- Append the length of the prefix followed by c to comp.

Return the string comp.


Example 1:
Input: word = "abcde"
Output: "1a1b1c1d1e"

Explanation:
Initially, comp = "". Apply the operation 5 times, choosing "a", "b", "c", "d", and "e" as the prefix in each operation.
For each prefix, append "1" followed by the character to comp.


Example 2:
Input: word = "aaaaaaaaaaaaaabb"
Output: "9a5a2b"

Explanation:
Initially, comp = "". Apply the operation 3 times, choosing "aaaaaaaaa", "aaaaa", and "bb" as the prefix in each operation.

    - For prefix "aaaaaaaaa", append "9" followed by "a" to comp.
    - For prefix "aaaaa", append "5" followed by "a" to comp.
    - For prefix "bb", append "2" followed by "b" to comp.


Constraints:

    -> 1 <= word.length <= 2 * 10^5
    -> word consists only of lowercase English letters.


Concepts: Strings
"""


# My Solution
def compressedString(word: str) -> str:
    i, res = 1, ""                              # Initialise idx-var and result string
    curr, cnt = word[0], 1                      # Initialise curr-var and counter

    while i < len(word):                        # While the index is less than string length
        if word[i] != curr or cnt == 9:         # Check if curr-var and curr-char are not same or counter-val equals 9
            res += str(cnt) + curr              # Update the result string with counter-val and curr-var
            curr, cnt = word[i], 0              # Set the curr-var to curr-char and counter to 1
        cnt += 1                                # Increment the counter
        i += 1                                  # Increment the index

    return res + str(cnt) + curr                # Return the result
