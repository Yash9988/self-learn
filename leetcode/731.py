"""
731. My Calendar II [MEDIUM]

You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a
triple booking.

A triple booking happens when three events have some non-empty intersection (i.e., some moment is common to all the
three events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval
[start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendarTwo class:

    - MyCalendarTwo() Initializes the calendar object.

    - boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without
      causing a triple booking. Otherwise, return false and do not add the event to the calendar.


Example 1:

Input:
["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output:
[null, true, true, true, false, true, true]

Explanation:

MyCalendarTwo myCalendarTwo = new MyCalendarTwo();

myCalendarTwo.book(10, 20);  // return True, The event can be booked.
myCalendarTwo.book(50, 60);  // return True, The event can be booked.
myCalendarTwo.book(10, 40);  // return True, The event can be double booked.
myCalendarTwo.book(5, 15);   // return False, The event cannot be booked, because it would result in a triple booking.
myCalendarTwo.book(5, 10);   // return True, The event can be booked, as it does not use time 10 which is already double
                                booked.
myCalendarTwo.book(25, 55);  // return True, The event can be booked, as the time in [25, 40) will be double booked with
                                the third event, the time [40, 50) will be single booked, and the time [50, 55) will be
                                double booked with the second event.


Constraints:

    -> 0 <= start < end <= 109
    -> At most 1000 calls will be made to book.


Concepts: Double lists, Binary Search
"""
# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
from bisect import *


class MyCalendarTwo:
    def __init__(self):
        self.calendar = []                                          # Initialise list to hold booking-date ranges
        self.overlaps = []                                          # Initialise list to hold overlap-dates ranges

    def book(self, start, end):
        for i, j in self.overlaps:                                  # Iterate through the overlapping-date ranges
            if start < j and end > i:                               # Check if current booking lies between any range
                return False                                        # Return False

        for i, j in self.calendar:                                  # Iterate through all booking-date ranges
            if start < j and end > i:                               # Check if current booking lies between any range
                self.overlaps.append((max(start, i), min(end, j)))  # Append the date range to the overlap list
        self.calendar.append((start, end))                          # Append the dates to the booking list
        return True                                                 # Return True


# Optimised Solution
class MyCalendarTwoOP:
    def __init__(self):
        self.single_booked = []                                     # Initialise an array to store single booking ranges
        self.double_booked = []                                     # Initialise an array to store double booking ranges

    def intersection(self, intervals, s, e):

        l = bisect_left(intervals, s)                               # Obtain the BS left index for start date
        r = bisect_right(intervals, e)                              # Obtain the BS right index for end date
        intersection = []                                           # Initialise an array to store intersections

        if l % 2:                                                   # If left-index is odd
                                                                    # We may create empty interval where s==intervals[l]
            if intervals[l] != s:                                   # Check if date at left-index is different
                intersection.append(s)                              # Append start date to the array
            else:
                l = l + 1                                           # Increment the lef-index

        intersection += intervals[l:r]                              # Append the interval slice to intersection array

        if r % 2:                                                   # If right-index is odd
                                                                    # We may create empty interval where e==intervals[r-1]
            if intervals[r - 1] != e:                               # Check if date at right-index - 1 is different
                intersection.append(e)                              # Append end date to the array
            else:
                intersection.pop()                                  # Remove the last date from the intersection array

        return intersection                                         # Return the intersection array

    def add(self, intervals, s, e):

        l = bisect_left(intervals, s)                               # Obtain the BS left-index for start date
        r = bisect_right(intervals, e)                              # Obtain the BS right-index for end date
        new = []                                                    # Initialise an array to store new date range

        if not l % 2:                                               # If left-index is even
            new.append(s)                                           # Append start date to the array

        if not r % 2:                                               # If right-index is even
            new.append(e)                                           # Append end date to the array

        intervals[l:r] = new                                        # Update the interval slice with array values

    def book(self, start: int, end: int) -> bool:

        if self.intersection(self.double_booked, start, end):       # Check if date range is present in intersect-array
            return False                                            # Return False

        intersection = self.intersection(self.single_booked,
                                         start, end)                # Obtain the intersection array for single bookings

        if intersection:                                            # If intersection array is not empty
            for i in range(len(intersection) // 2):                 # Iterate through half the intersection array
                i1 = intersection[2 * i]                            # Store to value at 2*index in the array
                i2 = intersection[2 * i + 1]                        # Store the valur at 2*index+1 in the array
                self.add(self.double_booked, i1, i2)                # Add the index-range to the double booked array

        self.add(self.single_booked, start, end)                    # Add the date-range to the single booked array

        return True                                                 # Return False
