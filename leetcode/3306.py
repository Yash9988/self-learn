"""
3306. Count of Substrings Containing Every Vowel and K Consonants II [MEDIUM]

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

    -> 5 <= word.length <= 2 * 105
    -> word consists only of lowercase English letters.
    -> 0 <= k <= word.length - 5


Concepts: Substrings, Double Pointers,
"""
from collections import defaultdict


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


# Alternate Solution
def countOfSubstrings_alt(word: str, k: int) -> int:
    def countAtLeastMConsonants(m):                 # Method to find all substrings with _at least_ k characters
        n = len(word)                               # Compute the length of the input word string
        vowels = ('a', 'e', 'i', 'o', 'u')          # Initialise a tuple of vowels
        vmap = defaultdict(int)                     # Initialise a dictionary for vowel frequency
        num_con = 0                                 # Initialise consonant counter
        res = 0                                     # Initialise result counter
        l = r = 0                                   # Initialise 2 pointers
        while r < n or l < n:                       # While the left and right pointers are smaller than word length
            if len(vmap) == 5 and num_con >= m:     # Check if the count of consonants is equal or higher than desired
                res += n - r + 1                    # Compute and add the possible substrings at right pointer
                if word[l] not in vowels:           # Check if character at left pointer index is a consonant
                    num_con -= 1                    # Decrement the consonant counter
                else:
                    vmap[word[l]] -= 1              # Decrement the count of the respective vowel
                    if vmap[word[l]] == 0:          # Check if the frequency for that vowel is zero
                        del vmap[word[l]]           # Remove the corresponding vowel from the dictionary
                l += 1                              # Increment the left pointer
            else:
                if r == n:                          # Check if right pointer has reached the end of the word
                    break                           # Break out of the while-loop
                if word[r] not in vowels:           # Check if character at right pointer index is a consonant
                    num_con += 1                    # Increment the consonant counter
                else:
                    vmap[word[r]] += 1              # Increment the count of the respective vowel-char
                r += 1                              # Increment the right pointer

        return res                                  # Return the result

    return countAtLeastMConsonants(k) - countAtLeastMConsonants(k + 1)


"""
Two Passes (Trick)

We use a simpler sliding window to find all substrings with at least k characters.
Then, we subtract the number of substrings with at least k + 1 characters.
"""