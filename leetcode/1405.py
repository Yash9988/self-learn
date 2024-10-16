"""
1405. Longest Happy String [MEDIUM]

A string s is called happy if it satisfies the following conditions:

    - s only contains the letters 'a', 'b', and 'c'.
    - s does not contain any of "aaa", "bbb", or "ccc" as a substring.
    - s contains at most a occurrences of the letter 'a'.
    - s contains at most b occurrences of the letter 'b'.
    - s contains at most c occurrences of the letter 'c'.

Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings,
return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.


Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"

Explanation: "ccbccacc" would also be a correct answer.


Example 2:

Input: a = 7, b = 1, c = 0
Output: "aabaa"

Explanation: It is the only correct answer in this case.


Constraints:

    -> 0 <= a, b, c <= 100
    -> a + b + c > 0


Concepts: Heap
"""
from heapq import *
from collections import Counter


# Optimal Solution
def longestDiverseString_op(a: int, b: int, c: int) -> str:
    max_heap = []                                               # Initialise a heap
    if a: heappush(max_heap, (-a, 'a'))                         # Push the value of 'a' in the heap, if non-zero
    if b: heappush(max_heap, (-b, 'b'))                         # Push the value of 'b' in the heap, if non-zero
    if c: heappush(max_heap, (-c, 'c'))                         # Push the value of 'c' in the heap, if non-zero

    res = []                                                    # Initialise the result list
    while max_heap:                                             # While the heap is not empty
        first, char1 = heappop(max_heap)                        # Pop the char with maximum value from the heap
        if len(res) >= 2 and res[-1] == res[-2] == char1:       # Check if curr-char is same as the previous two
            if not max_heap:                                    # If there is no other choice
                return ''.join(res)                             # Return the current state of result list

            second, char2 = heappop(max_heap)                   # Pop the char with (second) max-val from the heap
            res.append(char2)                                   # Append the character to the list
            second += 1                                         # Decrement the character count
            if second != 0:                                     # Check if char-count is non-zero
                heappush(max_heap, (second, char2))             # Push the (second) character (back) into the heap
            heappush(max_heap, (first, char1))                  # Push the (first) character into the heap, as well

            continue                                            # Skip to the next iteration

                                                                # Situation that first-char can directly be added
        res.append(char1)                                       # Append the (first) character to the result
        first += 1                                              # Decrement the character count
        if first != 0:                                          # Check if character count is non-zero
            heappush(max_heap, (first, char1))                  # Push the character back into the heap

    return ''.join(res)                                         # Join and return the characters in result list


# Alternate Solution
def longestDiverseString_alt(a: int, b: int, c: int) -> str:
    result = []                                                 # Initialise the result list
    remaining = Counter({'a': a,'b': b,'c': c})                 # Initialise a dictionary of characters & their counts
    (fence, _), (wedge, _) = remaining.most_common(2)           # Obtain the character with the highest counts

    while remaining[fence] > 0 and remaining[wedge] > 0:        # While no new groups could be formed
        result.append(fence)                                    # Append the character with the highest count
        remaining[fence] -= 1                                   # Decrement the character count

        if len(result) >= 2 and result[-2] == fence:            # Check if we can't add the character again
            pass
        elif remaining[fence] > 0:                              # Check if the character count is non-zero
            result.append(fence)                                # Add another instance of the character
            remaining[fence] -= 1                               # Decrement the character count

        result.append(wedge)                                    # Append the second character w/ the next highest count
        remaining[wedge] -= 1                                   # Decrement the count of the respective character

        (fence, _), (wedge, _) = remaining.most_common(2)       # Recompute the character with the highest counts

    if remaining[fence] > 0:                                    # Check if the count of secondary character is non-zero
        result.append(fence)                                    # Append the character to the list
        remaining[fence] -= 1                                   # Decrement the character count
        if remaining[fence] > 0:                                # Check if count is still non-zero
            result.append(fence)                                # Append the character into the list, again

    return ''.join(result)                                      # Join and return the characters in result list
