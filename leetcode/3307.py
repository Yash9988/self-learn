"""
3307. Find the K-th Character in String Game II [HARD]

Alice and Bob are playing a game. Initially, Alice has a string word = "a".

You are given a positive integer k. You are also given an integer array operations, where operations[i] represents the
type of the ith operation.

Now Bob will ask Alice to perform all operations in sequence:

- If operations[i] == 0, append a copy of word to itself.
- If operations[i] == 1, generate a new string by changing each character in word to its next character in the
  English alphabet, and append it to the original word. For example, performing the operation on "c" generates "cd"
  and performing the operation on "zb" generates "zbac".

Return the value of the kth character in word after performing all the operations.

Note that the character 'z' can be changed to 'a' in the second type of operation.


Example 1:

Input: k = 5, operations = [0,0,0]
Output: "a"

Explanation:

Initially, word == "a". Alice performs the three operations as follows:

    - Appends "a" to "a", word becomes "aa".
    - Appends "aa" to "aa", word becomes "aaaa".
    - Appends "aaaa" to "aaaa", word becomes "aaaaaaaa".


Example 2:

Input: k = 10, operations = [0,1,0,1]
Output: "b"

Explanation:

Initially, word == "a". Alice performs the four operations as follows:

    Appends "a" to "a", word becomes "aa".
    Appends "bb" to "aa", word becomes "aabb".
    Appends "aabb" to "aabb", word becomes "aabbaabb".
    Appends "bbccbbcc" to "aabbaabb", word becomes "aabbaabbbbccbbcc".


Constraints:

    -> 1 <= k <= 10^14
    -> 1 <= operations.length <= 100
    -> operations[i] is either 0 or 1.
    -> The input is generated such that word has at least k characters after all operations.


Concepts: Bit-Manipulation
"""


def kthCharacter(k: int, operations: list[int]) -> str:
    res = 0                                         # Initialise result counter
    k -= 1                                          # Compute the k-th index

    for i, v in enumerate(operations):              # Iterate through all operations
        if k & (1 << i):                            # Check if i-th bit in k is 1
            res += v                                # Apply operation

    return chr(ord('a') + res % 26)                 # Return the result


"""
-> Intuition

Each operation will double the length of string.
The length of string will be 1,2,4,8,16...

Update k -= 1, we want to find s[k].
Consider k in binary format:

s[1xxx] is generated from s[xxx],

    - If the operation is 0, s[1xxx] = s[xxx]
    - If the operation is 1, s[1xxx] = s[xxx] + 1

-> Explanation

k -= 1 is the index of char.
If ith bit in k is 1,
it will apply operation[i].
Count the sum of applied operations.

-> Complexity

Time: O(min(logk, 60))
Space: O(1)
"""