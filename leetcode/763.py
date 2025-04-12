"""
763. Partition Labels [MEDIUM]

You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in
at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as
["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.


Example 1:
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]

Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.


Example 2:
Input: s = "eccbbbbdec"
Output: [10]


Constraints:

    -> 1 <= s.length <= 500
    -> s consists of lowercase English letters.


Concepts: Hashmap, Substrings,
"""


# Optimised Solution
def partitionLabels(s: str) -> list[int]:
    last_occurrence = {}                                            # Dict to track the last idx of the char

    for i, char in enumerate(s):                                    # Iterate through the string
        last_occurrence[char] = i                                   # Update the idx for the curr-char

    result = []                                                     # List to store the result
    start = end = 0                                                 # Pointers to track the ends of a partition

    for i, char in enumerate(s):                                    # Iterate through the string
        end = max(end, last_occurrence[char])                       # Update the pointer with max-val (idx)

        if i == end:                                                # Check if the curr-idx equals part-end
            result.append(end - start + 1)                          # Compute and append the substring size
            start = i + 1                                           # Reset the start-pointer to the next-idx

    return result                                                   # Return the result
