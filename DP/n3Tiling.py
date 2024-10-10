"""
HARD-PROBLEM (https://www.youtube.com/watch?v=8IQgU95iZ58&list=PLEL7R4Pm6EmD8pYyhvTcdF7qf-EFl3IWz&index=16)
Given a grid of either shape: 1xN, 2xN or 3xN
And a pair of tiles shaped: 1x3 and 2x2

Find the total # unique arrangements of the tiles, given one of the above grids.
"""


def n3Tiling(m: int, n: int) -> int:
    if m == 1:                                      # For grid shape: 1 x N
        return n % 3 == 0                           # If rows (N) are a multiple of 3, return 1 else 0

    elif m == 2:                                    # For grid shape: 2 x N
        if n < 4:                                   # Check for base-cases
            return not n == 1

        a, b, c = 0, 1, 1                           # Initialise base-cases
        i = 3                                       # Initialise iterator
        while (i := i + 1) <= n:                    # Iterate to N
            a, b, c = b, c, a + b                   # Update variables

        return b                                    # Return the result

    else:
        # BASE-CASES
        a1 = [1, 1, 2]                              # Variety of cells in a single column
        a2 = [0, 0, 0]                              # Variety of cells in a pair of columns
        a3 = [0, 0, 1]                              # Variety of cells in 3 columns

        for i in range(4, n + 1):                   # Iterate to N

            # Iteratively solve variety sub-problems
            a1.append(a1[i - 1] + a1[i - 3] + 2 * a2[i - 2])
            a2.append(a3[i - 1] + a2[i - 3])
            a3.append(a1[i - 3] + a3[i - 3])

        return a1[n]                                # Return the result
