"""
1014. Best Sightseeing Pair [MEDIUM]

You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing
spots i and j have a distance j - i between them.

The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the
sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.


Example 1:
Input: values = [8,1,5,2,6]
Output: 11

Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11


Example 2:
Input: values = [1,2]
Output: 2


Constraints:

    -> 2 <= values.length <= 5 * 10^4
    -> 1 <= values[i] <= 1000


Concepts: Best-so-far
"""


# Optimised Solution
def maxScoreSightseeingPair(values: list[int]) -> int:
    res = curr = 0                                                  # Counters to track curr-max & best max-final-sum

    for i, n in enumerate(values):                                  # Iterate through the values
        res = max(res, curr + n - i)                                # Update the counter with max-sum so far
        curr = max(curr, n + i)                                     # Update the counter with curr-max so far

    return res                                                      # Return the result


# Alternate Solution (More explanatory)
def maxScoreSightseeingPair_alt(values: list[int]) -> int:

    best_score = best_half_score = 0                                # Counters to track best-half and best scores

    for value in values:                                            # Iterate through the values
        best_half_score -= 1                                        # Decrement the half-score counter
        if best_half_score + value > best_score:                    # Check if curr-sum is higher than best-sum
            best_score = best_half_score + value                    # Update the counter with max-sum

        if value > best_half_score:                                 # Check if curr-val is higher than best-half val
            best_half_score = value                                 # Update the counter with the max-val

    return best_score                                               # Return the result
