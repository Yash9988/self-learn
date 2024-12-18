"""
2182. Construct String With Repeat Limit [MEDIUM]

You are given a string s and an integer repeatLimit. Construct a new string repeatLimitedString using the characters of
s such that no letter appears more than repeatLimit times in a row. You do not have to use all characters from s.

Return the lexicographically largest repeatLimitedString possible.

A string 'a' is lexicographically larger than a string 'b' if in the first position where a and b differ, string a has a
letter that appears later in the alphabet than the corresponding letter in b. If the first min(a.length, b.length)
characters do not differ, then the longer string is the lexicographically larger one.


Example 1:
Input: s = "cczazcc", repeatLimit = 3
Output: "zzcccac"

Explanation: We use all of the characters from s to construct the repeatLimitedString "zzcccac".
The letter 'a' appears at most 1 time in a row.
The letter 'c' appears at most 3 times in a row.
The letter 'z' appears at most 2 times in a row.
Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
The string is the lexicographically largest repeatLimitedString possible so we return "zzcccac".
Note that the string "zzcccca" is lexicographically larger but the letter 'c' appears more than 3 times in a row, so it
is not a valid repeatLimitedString.


Example 2:
Input: s = "aababab", repeatLimit = 2
Output: "bbabaa"

Explanation: We use only some of the characters from s to construct the repeatLimitedString "bbabaa".
The letter 'a' appears at most 2 times in a row.
The letter 'b' appears at most 2 times in a row.
Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
The string is the lexicographically largest repeatLimitedString possible so we return "bbabaa".
Note that the string "bbabaaa" is lexicographically larger but the letter 'a' appears more than 2 times in a row, so it
is not a valid repeatLimitedString.



Constraints:

    -> 1 <= repeatLimit <= s.length <= 10^5
    -> s consists of lowercase English letters.


Concepts: Heap
"""
from heapq import heapify, heappush, heappop
from collections import Counter


# Optimised Solution
def repeatLimitedString(s: str, repeatLimit: int) -> str:
    chars = Counter(s)                                              # Compute the char-freq for the string
    sorted_chars = sorted(chars.items(), reverse=True)              # Sort the item-tuples in descending order

    ans = []                                                        # List to store the result string

    while sorted_chars:                                             # While the list of tuples is non-empty
        char, freq = sorted_chars[0]                                # Obtain the largest freq-tuple
        if freq <= repeatLimit:                                     # Check if the freq is smaller than limit
            ans.append(char * freq)                                 # Append all the instances of the char to the result
            sorted_chars.pop(0)                                     # Pop the first tuple from the PQ
        else:
            ans.append(char * repeatLimit)                          # Append limited instances of char to the result
            sorted_chars[0] = (char, freq - repeatLimit)            # Update the tuple with the remaining instances

            if len(sorted_chars) > 1:                               # Check if the tuple-list has more than one element
                next_char, next_freq = sorted_chars[1]              # Obtain the second largest freq-tuple
                ans.append(next_char)                               # Append a single instance of the char to the result
                if next_freq == 1:                                  # Check if the char has a single instance remaining
                    sorted_chars.pop(1)                             # Pop the freq-tuple from the PQ
                else:
                    sorted_chars[1] = (next_char, next_freq - 1)    # Update the tuple with the remaining instances
            else:
                break                                               # Break from the loop, otherwise

    return ''.join(ans)                                             # Return the result


# Alternate Solution
def repeatLimitedString_alt(s: str, repeatLimit: int) -> str:
    heap = [(-ord(k), v) for k, v in Counter(s).items()]            # List to store char-freq-tuples
    heapify(heap)                                                   # Convert the list into a heap

    res = []                                                        # List to store the result
    while heap:                                                     # While the heap is non-empty
        k, v = heappop(heap)                                        # Pop the largest tuple from the heap
        if res and res[-1] == k:                                    # Check if the last result-char is same as current
            if not heap:                                            # Check if the heap is empty
                break                                               # Break out from the loop

            k_, v_ = heappop(heap)                                  # Pop the second largest tuple from the heap
            res.append(k_)                                          # Append a single instance of the char to the result
            if v_ - 1:                                              # Check if remaining instances are non-zero
                heappush(heap, (k_, v_ - 1))                        # Push the updated tuple back into the heap
            heappush(heap, (k, v))                                  # Push the original tuple back into the heap
        else:
            cnt = min(v, repeatLimit)                               # Compute the max-char-instances than can be added
            res.extend([k] * cnt)                                   # Append the instances to the result
            if v - cnt:                                             # Check if remaining instances are non-zero
                heappush(heap, (k, v - cnt))                        # Push the updated tuple back into the heap

    return "".join(chr(-x) for x in res)                            # Return the result
