"""
2594. Minimum Time to Repair Cars [MEDIUM]

You are given an integer array ranks representing the ranks of some mechanics. ranks_i is the rank of the i-th mechanic.
A mechanic with a rank r can repair n cars in r * n^2 minutes.

You are also given an integer cars representing the total number of cars waiting in the garage to be repaired.

Return the minimum time taken to repair all the cars.

Note: All the mechanics can repair the cars simultaneously.


Example 1:
Input: ranks = [4,2,3,1], cars = 10
Output: 16

Explanation:
- The first mechanic will repair two cars. The time required is 4 * 2 * 2 = 16 minutes.
- The second mechanic will repair two cars. The time required is 2 * 2 * 2 = 8 minutes.
- The third mechanic will repair two cars. The time required is 3 * 2 * 2 = 12 minutes.
- The fourth mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
It can be proved that the cars cannot be repaired in less than 16 minutes.


Example 2:
Input: ranks = [5,1,8], cars = 6
Output: 16

Explanation:
- The first mechanic will repair one car. The time required is 5 * 1 * 1 = 5 minutes.
- The second mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
- The third mechanic will repair one car. The time required is 8 * 1 * 1 = 8 minutes.
It can be proved that the cars cannot be repaired in less than 16 minutes.


Constraints:

    -> 1 <= ranks.length <= 1^05
    -> 1 <= ranks[i] <= 100
    -> 1 <= cars <= 10^6


Concepts: Binary Search
"""


# Optimised Solution
def repairCars(ranks: list[int], cars: int) -> int:
    # Helper method to check the feasibility of the current "guess"
    def can_repair_all(time):
        total_cars_repaired = 0                                     # Counter to track total repaired cars

        for rank in ranks:                                          # Iterate through the list
            cars_repaired = int((time / rank) ** 0.5)               # Compute the cars repaired by the curr-mechanic
            total_cars_repaired += cars_repaired                    # Increment the counter by the cars repaired
            if total_cars_repaired >= cars:                         # Check if the total cars repaired exceeds required
                return True                                         # Return True

        return False                                                # Return False

    left, right = 1, min(ranks) * cars * cars                       # Pointers to track the search boundaries

    while left < right:                                             # While the left pointer is smaller than the right
        mid = (left + right) // 2                                   # Compute the center of the boundary

        if can_repair_all(mid):                                     # Check the feasibility for the mid-val
            right = mid                                             # Decrease the upper bound for the search window
        else:
            left = mid + 1                                          # Increase the lower bound, otherwise

    return left                                                     # Return the result
