"""
3320. Count The Number of Winning Sequences [HARD]

Alice and Bob are playing a fantasy battle game consisting of n rounds where they summon one of three magical creatures
each round: a Fire Dragon, a Water Serpent, or an Earth Golem. In each round, players simultaneously summon their
creature and are awarded points as follows:

    - If one player summons a Fire Dragon and the other summons an Earth Golem, the player who summoned the Fire Dragon
      is awarded a point.

    - If one player summons a Water Serpent and the other summons a Fire Dragon, the player who summoned the Water
      Serpent is awarded a point.

    - If one player summons an Earth Golem and the other summons a Water Serpent, the player who summoned the Earth
      Golem is awarded a point.

    - If both players summon the same creature, no player is awarded a point.

You are given a string s consisting of n characters 'F', 'W', and 'E', representing the sequence of creatures Alice will
summon in each round:

    - If s[i] == 'F', Alice summons a Fire Dragon.
    - If s[i] == 'W', Alice summons a Water Serpent.
    - If s[i] == 'E', Alice summons an Earth Golem.

Bob’s sequence of moves is unknown, but it is guaranteed that Bob will never summon the same creature in two consecutive
rounds. Bob beats Alice if the total number of points awarded to Bob after n rounds is strictly greater than the points
awarded to Alice.

Return the number of distinct sequences Bob can use to beat Alice.

Since the answer may be very large, return it modulo 10^9 + 7.


Example 1:

Input: s = "FFF"
Output: 3

Explanation:
Bob can beat Alice by making one of the following sequences of moves: "WFW", "FWF", or "WEW". Note that other winning
sequences like "WWE" or "EWW" are invalid since Bob cannot make the same move twice in a row.


Example 2:

Input: s = "FWEFW"
Output: 18

Explanation:
Bob can beat Alice by making one of the following sequences of moves: "FWFWF", "FWFWE", "FWEFE", "FWEWE", "FEFWF",
"FEFWE", "FEFEW", "FEWFE", "WFEFE", "WFEWE", "WEFWF", "WEFWE", "WEFEF", "WEFEW", "WEWFW", "WEWFE", "EWFWE", or "EWEWE".


Constraints:

    -> 1 <= s.length <= 1000
    -> s[i] is one of 'F', 'W', or 'E'.


Concepts: DP
"""
from collections import Counter


def countWinningSequences(s: str) -> int:
    mod = 10 ** 9 + 7                                               # Initialise mod value
    n = len(s)                                                      # Compute input-string length
    s = ['FWE'.find(c) for c in s]                                  # Convert the string to a list of indexes
    dp = [[Counter() for j in range(3)] for i in range(n)]          # Initialise DP

    for i in range(n):                                              # Iterate through the range of list length
        for j in range(3):                                          # Iterate through all creature types
            d = (j - s[i] + 1) % 3 - 1                              # Calculate the score for respective type
            if i == 0:                                              # Check for base case
                dp[i][j][d] = 1                                     # Update the counter at index with score value
            else:
                for j2 in range(3):                                 # Iterate through creature types
                    if j != j2:                                     # Check to ensure same creature isn't used twice
                        for v in dp[i - 1][j2]:                     # Iterate through all score values
                            dp[i][j][v + d] += dp[i - 1][j2][v]     # Update the DP at curr-idx using prev-idx values
                            dp[i][j][v + d] %= mod                  # Apply the mod to contain the answer within limit

    res = 0                                                         # Initialise result counter
    for j in range(3):                                              # Iterate through creature types
        for v in range(1, n + 1):                                   # Iterate through the range of all possible scores
            res += dp[n - 1][j][v]                                  # Accumulate the value at index in the counter

    return res % mod                                                # Apply the mode and return the result
