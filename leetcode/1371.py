"""
1371. Find the Longest Substring Containing Vowels in Even Counts [MEDIUM]

Given the string s, return the size of the longest substring containing each vowel an even number of times. That is,
'a', 'e', 'i', 'o', and 'u' must appear an even number of times.


Example 1:

Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.


Example 2:

Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains two e's.


Example 3:

Input: s = "bcbcbc"
Output: 6
Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.


Constraints:

    -> 1 <= s.length <= 5 x 10^5
    -> s contains only lowercase English letters.

"""


# Optimal Solution (Time: O(N), Space: O(1))
def findTheLongestSubstring(s: str) -> int:
    seen = {0: -1}                                          # Initialise with the default/starting index as -1
    res = cur = 0                                           # Set the "result" and "current" counters
    for i, c in enumerate(s):                               # Iterate through each character
        cur ^= 1 << ('aeiou'.find(c) + 1) >> 1              # Update the counter wrt corresponding character
        seen.setdefault(cur, i)                             # Update the dictionary if the key doesn't exist
        res = max(res, i - seen[cur])                       # Update the result with the largest length so far
    return res                                              # Return the result


"""
-> Explanation

cur records the count of "aeiou"
cur & 1 = the records of a % 2
cur & 2 = the records of e % 2
cur & 4 = the records of i % 2
cur & 8 = the records of o % 2
cur & 16 = the records of u % 2
seen note the index of first occurrence of cur

Note that we don't really need the exact count number,
we only need to know if it's odd or even.

If it's one of aeiou,
'aeiou'.find(c) can find the index of vowel,
cur ^= 1 << 'aeiou'.find(c) will toggle the count of vowel.

But for no vowel characters,
'aeiou'.find(c) will return -1,
that's reason that we do 1 << ('aeiou'.find(c) + 1) >> 1.


                                       a       e       i       o       u       other
"aeiou".indexOf(s.charAt(i)) + 1       1       2       3       4       5       0
1 << tmp                               2       4       8      16      32       1
(1 << tmp) >> 1                        1       2       4       8      16       0

"""