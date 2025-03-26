"""
3304. Find the K-th Character in String Game I [EASY]

Alice and Bob are playing a game. Initially, Alice has a string word = "a".

You are given a positive integer k.

Now Bob will ask Alice to perform the following operation forever:

Generate a new string by changing each character in word to its next character in the English alphabet, and append
it to the original word.

For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".

Return the value of the kth character in word, after enough operations have been done for word to have at least k characters.

Note that the character 'z' can be changed to 'a' in the operation.


Example 1:

Input: k = 5
Output: "b"

Explanation:

Initially, word = "a". We need to do the operation three times:

    - Generated string is "b", word becomes "ab".
    - Generated string is "bc", word becomes "abbc".
    - Generated string is "bccd", word becomes "abbcbccd".


Example 2:

Input: k = 10
Output: "c"


Constraints:

    -> 1 <= k <= 500


Concepts: Bit-Manipulation
"""


# My Solution
def kthCharacter(k: int) -> str:
    if k == 1:                                      # Check for base-case
        return "a"                                  # Return 'a'

    word = "a"                                      # Initialise the word-string
    while len(word) < k:                            # While the word-len is smaller than desired index value
        for ch in word:                             # Iterate through the characters of word
            if ch == 'z':                           # Check if the curr-char is 'z'
                word += 'a'                         # Wrap around to 'a' and append in the word-string
            else:
                word += chr(ord(ch) + 1)            # Increment the character by one and append, otherwise

    return word[k - 1]                              # Return the character at k-th position


# Optimal Solution
def kthCharacter_op(k: int) -> str:
    return chr(ord('a') + (k - 1).bit_count())


"""
-> INTUITION

Update k -= 1, we want to find s[k].

Consider k in binary format:
s[1xxx] is generated from s[xxx],
s[1xxx] = s[xxx] + 1

-> EXPLANATION

Each bit means it's incremented once.

s[k] = s[0] + bits_count(k)

Just return bit count of k.

-> COMPLEXITY

- Time: O(logk)
- Space: O(1)
"""