"""
539. Minimum Time Difference [MEDIUM]

Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two
time-points in the list.


Example 1:

Input: timePoints = ["23:59","00:00"]
Output: 1


Example 2:

Input: timePoints = ["00:00","23:59","00:00"]
Output: 0


Constraints:

    -> 2 <= timePoints.length <= 2 * 104
    -> timePoints[i] is in the format "HH:MM".

"""


def findMinDifference(timePoints: list[str]) -> int:
    def convert(time):                                          # Helper method to convert time string to integer
        return int(time[:2]) * 60 + int(time[3:])

    minutes = list(map(convert, timePoints))                    # Convert the input string list to list of minutes
    minutes.sort()                                              # Sort the list of minutes

    diff = [(y - x) % (24 * 60) for x, y in                     # Find the difference between consecutive time-stamps
            zip(minutes, minutes[1:] + minutes[:1])]

    return min(diff)                                            # Return the (minimum) result

