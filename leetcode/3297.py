"""
3297. Count Substrings That Can Be Rearranged to Contain a String I [MEDIUM]

You are given two strings word1 and word2.

A string x is called valid if x can be rearranged to have word2 as a _prefix_.

Return the total number of valid _substrings_ of word1.


Example 1:

Input: word1 = "bcca", word2 = "abc"
Output: 1

Explanation:

The only valid substring is "bcca" which can be rearranged to "abcc" having "abc" as a prefix.


Example 2:

Input: word1 = "abcabc", word2 = "abc"
Output: 10

Explanation:

All the substrings except substrings of size 1 and size 2 are valid.


Example 3:

Input: word1 = "abcabc", word2 = "aaabc"
Output: 0


Constraints:

    -> 1 <= word1.length <= 105
    -> 1 <= word2.length <= 104
    -> word1 and word2 consist only of lowercase English letters.


Concepts: Double Pointers, Substrings
"""
from collections import defaultdict


# Optimised Solution
def validSubstringCount(word1: str, word2: str) -> int:
    # c = Counter(word2)                # Obtain frequency of all character in prefix (Manual counting is ~2x faster)
    if len(word1) < len(word2):         # Check if the length of prefix is greater
        return 0                        # Return 0

    c = defaultdict(int)                # Initialise a default-dict to store character frequencies for prefix word
    for ch in word2:                    # Iterate through all characters in the prefix
        c[ch] += 1                      # Increment the respective character count

    l, m, res = 0, len(c), 0            # Initialise counters for left-pointer, matches, and result
    for ch in word1:                    # Iterate through all characters in word1 string
        c[ch] -= 1                      # Decrement the frequency of the current character
        if c[ch] == 0:                  # Check if the frequency is zero
            m -= 1                      # Reduce the match counter, denoting the satisfaction of requirement in prefix

        while m == 0:                   # While the match counter is zero
            lch = word1[l]              # Acquire the character at left-pointer
            if c[lch] == 0:             # Check if the frequency of the said character is zero
                m += 1                  # Increment the match counter, denoting reversion of prefix requirement
            c[lch] += 1                 # Increment the frequency of the current character
            l += 1                      # Increment the left pointer

        res += l                        # Add the index of left-pointer to the result, after each iteration
    return res                          # Return the result


# Alternate Solution
def validSubstringCount_alt(word1: str, word2: str) -> int:
    v = [0] * 26                        # Initialise array to store the frequency of each character in the prefix
    for c in word2:                     # Iterate through all characters in the prefix
        v[ord(c) - ord('a')] += 1       # Increment the frequency at the respective index for character, in array

    cnt = [0] * 26                      # Initialise another frequency array
    start = 0                           # Initialise a start-pointer
    k = len(word2)                      # Store the length of the word2 string
    count = 0                           # Initialise a counter

    for i in range(len(word1)):         # Iterate through all characters in word1
        curr = word1[i]                 # Obtain the character at the current index
        idx = ord(curr) - ord('a')      # Calculate the index for the character
        if v[idx] > 0:                  # Check if the character frequency is > 0 for prefix
            if cnt[idx] < v[idx]:       # Check if the ch-freq for word1 < ch-freq for prefix
                k -= 1                  # Decrement the value of length-counter

        cnt[idx] += 1                   # Increment the word1 frequency for current character

        while k == 0:                   # While the length-counter is zero
            count += len(word1) - i     # Increment counter by the difference between word1-length and iterator-index
            pre = word1[start]          # Obtain the character at the start pointer
            idx = ord(pre) - ord('a')   # Calculate the index for the prefix character
            cnt[idx] -= 1               # Decrement the ch-freq for word1
            if v[idx] > 0:              # Check if ch-freq for prefix is > 0
                if cnt[idx] < v[idx]:   # Check if ch-freq for word1 is < ch-freq for prefix
                    k += 1              # Increment the value of length-counter
            start += 1                  # Increment the start pointer

    return count                        # Return the final counter value
