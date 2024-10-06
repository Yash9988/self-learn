"""
2491. Divide Players Into Teams of Equal Skill [MEDIUM]

You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. Divide
the players into n / 2 teams of size 2 such that the total skill of each team is equal.

The chemistry of a team is equal to the product of the skills of the players on that team.

Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams such
that the total skill of each team is equal.


Example 1:

Input: skill = [3,2,5,1,3,4]
Output: 22
Explanation:
Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each team has a total skill of 6.
The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.


Example 2:

Input: skill = [3,4]
Output: 12
Explanation:
The two players form a team with a total skill of 7.
The chemistry of the team is 3 * 4 = 12.


Example 3:

Input: skill = [1,1,2,3]
Output: -1
Explanation:
There is no way to divide the players into teams such that the total skill of each team is equal.


Constraints:

    -> 2 <= skill.length <= 105
    -> skill.length is even.
    -> 1 <= skill[i] <= 1000


Concepts: Counting & Pairing
"""
from collections import Counter


def dividePlayers(skill: list[int]) -> int:
    s = 2 * sum(skill) // len(skill)                    # Compute each team's expected skill
    chemistry = 0
    cnt = Counter(skill)                                # Count skills

    for v, c in cnt.items():                            # For all players with a given skill, \
        if c != cnt[s-v]:                               # check that there is the same number \
            return -1                                   # of players with paired skill.
        chemistry += c * v * (s-v)                      # Compute chemistry for these pairs

    return chemistry // 2                               # We double-counted, correct for this


# Optimised Solution
def dividePlayers_op(skill: list[int]) -> int:
    skill.sort()                                        # Sort the skill-array
    n = len(skill)
    rem = skill[0] + skill[-1]                          # Compute each team's expected skill
    tsum = skill[0] * skill[-1]                         # Compute and store the product of extremes

    for j in range(1, n // 2):                          # Iterate through half the sorted list
        if skill[j] + skill[n - j - 1] != rem:          # Check if the border values don't sum to the expected skill
            return -1                                   # Return -1
        tsum += skill[j] * skill[n - j - 1]             # Increment the total sum by the product of border values

    return tsum                                         # Return the resulting sum
