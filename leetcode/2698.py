"""
2698. Find the Punishment Number of an Integer [MEDIUM]

Given a positive integer n, return the punishment number of n.

The punishment number of n is defined as the sum of the squares of all integers i such that:

    - 1 <= i <= n
    - The decimal representation of i * i can be partitioned into contiguous substrings such that the sum of the integer
      values of these substrings equals i.


Example 1:
Input: n = 10
Output: 182

Explanation: There are exactly 3 integers i in the range [1, 10] that satisfy the conditions in the statement:
- 1 since 1 * 1 = 1
- 9 since 9 * 9 = 81 and 81 can be partitioned into 8 and 1 with a sum equal to 8 + 1 == 9.
- 10 since 10 * 10 = 100 and 100 can be partitioned into 10 and 0 with a sum equal to 10 + 0 == 10.
Hence, the punishment number of 10 is 1 + 81 + 100 = 182


Example 2:
Input: n = 37
Output: 1478

Explanation: There are exactly 4 integers i in the range [1, 37] that satisfy the conditions in the statement:
- 1 since 1 * 1 = 1.
- 9 since 9 * 9 = 81 and 81 can be partitioned into 8 + 1.
- 10 since 10 * 10 = 100 and 100 can be partitioned into 10 + 0.
- 36 since 36 * 36 = 1296 and 1296 can be partitioned into 1 + 29 + 6.
Hence, the punishment number of 37 is 1 + 81 + 100 + 1296 = 1478



Constraints:

    -> 1 <= n <= 1000


Concepts: Substrings, DFS
"""


# Optimised Solution
def punishmentNumber(n: int) -> int:
    # Helper method to recursively check all partitions for a valid punishment split
    def checkPunish(s: int, t: int) -> bool:
        if t < 0 or s < t:                                          # Check if the partition is invalid
            return False                                            # Return False

        if s == t:                                                  # Check if the partition is valid
            return True                                             # Return True

        # Recursively check all partitions for a valid partition
        return (
                checkPunish(s // 10, t - s % 10)
                or checkPunish(s // 100, t - s % 100)
                or checkPunish(s // 1000, t - s % 1000)
        )

    res = 0                                                         # Counter to track the result

    for num in range(1, n + 1):                                     # Iterate through the desired range
        sqr = num * num                                             # Compute the square of the num
        if checkPunish(sqr, num):                                   # Check if num is a valid punish-num
            res += sqr                                              # Increment the counter by the square value

    return res                                                      # Return the result


# Alternate Solution
def punishmentNumber_alt(n: int) -> int:
    # Helper method to recursively check all partitions for a valid punishment split
    def checkPunish(s: str, t: int) -> bool:
        if s == "" and t == 0:                                      # Check if the partition is valid
            return True                                             # Return True

        if t < 0:                                                   # Check if the partition is invalid
            return False                                            # Return False

        ans = False                                                 # Bool-counter to track validity state
        for i in range(len(s)):                                     # Iterate through all pivot points
            l, r = s[:i + 1], s[i + 1:]                             # Partition the string at the pivot
            rem = t - int(l)                                        # Compute the remaining sum left to achieve

            if checkPunish(r, rem):                                 # Check if the partition is valid
                ans = True                                          # Set the bool-counter
                break                                               # Break out of the loop

        return ans                                                  # Return the result

    res = 0                                                         # Counter to track the result

    for num in range(1, n + 1):                                     # Iterate through the desired range
        sqr = num * num                                             # Compute the square of the num
        if checkPunish(sqr, num):                                   # Check if num is a valid punish-num
            res += sqr                                              # Increment the counter by the square value

    return res                                                      # Return the result
