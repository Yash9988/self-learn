"""
3305. Count of Substrings Containing Every Vowel and K Consonants I [MEDIUM]

You are given a string word and a non-negative integer k.

Return the total number of _substrings_ of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and
exactly k consonants.


Example 1:

Input: word = "aeioqq", k = 1
Output: 0

Explanation:
There is no substring with every vowel.


Example 2:

Input: word = "aeiou", k = 0
Output: 1

Explanation:
The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".


Example 3:

Input: word = "ieaouqqieaouqq", k = 1
Output: 3

Explanation:
The substrings with every vowel and one consonant are:

    - word[0..5], which is "ieaouq".
    - word[6..11], which is "qieaou".
    - word[7..12], which is "ieaouq".


Constraints:

    -> 5 <= word.length <= 250
    -> word consists only of lowercase English letters.
    -> 0 <= k <= word.length - 5


Concepts: Substrings, Double Pointers
"""


def countOfSubstrings(word: str, k: int) -> int:
    def ch_map(x):                                  # Helper method to map character of input-string to desired index
        return vow.index(x) \
            if x in vow else 5

    vow = 'aeiou'                                   # Initialise a string of all vowels
    n = len(word)                                   # Compute and store the length of the input-string
    s = l = 0                                       # Initialise 2 pointers at the start of the word
    ans = 0                                         # Initialise result counter
    imap = list(map(ch_map, word))                  # Compute and obtain the index-map for word

    cnt = [0 for _ in range(6)]                     # Initialise a list to store the character frequency

    for r in range(n):                              # Iterate through the word
        cnt[imap[r]] += 1                           # Increment the frequency of the current character

        while l < r and cnt[5] > k:                 # While the count of consonants is higher than desired
            cnt[imap[l]] -= 1                       # Decrement the frequency of character at left pointer-index
            l += 1                                  # Increment the left pointer
            s = l                                   # Set the start pointer at the new position of left pointer

        while cnt[5] == k and l < r:                # While the count of consonants is exactly as desired
            idx = imap[l]                           # Obtain the index of character at left pointer index
            if idx < 5:                             # Check if the character is a vowel
                if cnt[idx] > 1:                    # Check if the vowel-count is greater than one
                    cnt[idx] -= 1                   # Decrement the count of respective vowel character
                    l += 1                          # Increment the left pointer
                else:
                    break                           # Break out of the loop, otherwise
            else:
                break                               # Break out of the loop, otherwise

        if cnt[5] == k and min(cnt[:5]) > 0:        # Check if the count of consonant is exactly as desired
            ans += (l - s + 1)                      # Increment the result-counter by the possible number of substrings
                                                    # b/w start and left pointers.

    return ans                                      # Return the result
