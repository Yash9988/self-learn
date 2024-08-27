"""
848. Shifting Letters [MEDIUM]

You are given a string s of lowercase English letters and an integer array shifts of the same length.

Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

    For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.

Return the final string after all such shifts to s are applied.

Example 1:

Input: s = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation: We start with "abc".
After shifting the first 1 letters of s by 3, we have "dbc".
After shifting the first 2 letters of s by 5, we have "igc".
After shifting the first 3 letters of s by 9, we have "rpl", the answer.

Example 2:

Input: s = "aaa", shifts = [1,2,3]
Output: "gfd"


Constraints:

    - 1 <= s.length <= 105
    - s consists of lowercase English letters.
    - shifts.length == s.length
    - 0 <= shifts[i] <= 109
"""


def shiftingLetters(s: str, shifts: list[int]) -> str:
    i, t, ans, = len(s) - 1, 0, ""                      # Initialise answer string, accumulator and iterator
    while i >= 0:                                       # Iterate in reverse
        t += shifts[i]                                  # Accumulate shifts
        t %= 26                                         # Mod with 26 (letters in alphabet)
        ans += chr(wrapAround(ord(s[i]) + t))           # Add accumulated shift to character
        i -= 1                                          # Reduce the iterator
    return ans[::-1]                                    # Reverse the order


'''
Helper function to implement wrap-around from 'z', back to 'a'.
'''
def wrapAround(n: int) -> int:
    while n > 122:
        diff = n - 122
        n = 96 + diff
    return n


def OptimalSol(s: str, shifts: list[int]) -> str:
    ans, shift = '', 0
    for i in range(len(shifts) - 1, -1, -1):
        ans += chr((ord(s[i]) - ord('a') + shift + shifts[i]) % 26 + ord('a'))
        shift += shifts[i]

    return ans[::-1]


def MinimalSol(s: str, shifts: list[int]) -> str:
    for i in range(len(shifts) - 1)[::-1]:
        shifts[i] += shifts[i + 1]

    return "".join(chr((ord(c) - 97 + s) % 26 + 97) for c, s in zip(s, shifts))


"""
-> Explanation:
One pass to count suffix sum of shifts.
One pass to shift letters in string S

-> Time Complexity: O(N)
"""