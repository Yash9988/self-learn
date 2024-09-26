"""
729. My Calendar I [MEDIUM]

You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a
double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval
[start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

    - MyCalendar() Initializes the calendar object.

    - boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without
      causing a double booking. Otherwise, return false and do not add the event to the calendar.


Example 1:

Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but
                         // not including 20.


Constraints:

    -> 0 <= start < end <= 109
    -> At most 1000 calls will be made to book.


Concepts: Min-Max range, Binary Search, SortedList(?)
"""
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
from bisect import *


# Brute-Force Approach
class MyCalendar:
    def __init__(self):
        self.bookings = []                                      # Initialise an array to store the booking-date ranges

    def book(self, start: int, end: int) -> bool:
        for date in self.bookings:                              # Iterate through all the dates in booking
            if max(date[0], start) < min(date[1], end):         # Check if the current booking range doesn't qualify
                return False                                    # Return False

        self.bookings.append((start, end))                      # Add the current range to the booking ledger
        return True                                             # Return True


# Optimised Solution
class MyCalendarOP:

    def __init__(self):
        self.bookings = []                                      # Initialise an array to store the booking-date ranges

    def book(self, start, end):
        q1 = bisect_right(self.bookings, start)                 # Acquire the right-index for the start date, using BS
        q2 = bisect_left(self.bookings, end)                    # Acquire the left-index for the end date, using BS

        if q1 == q2 and q1 % 2 == 0:                            # Check if the indexes are same and right-index is even
            self.bookings[q1:q1] = [start, end]                 # Append the dates into the array, maintaining order
            return True                                         # Return True

        return False                                            # Return False
