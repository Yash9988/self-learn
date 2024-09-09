"""
Choose _at least_ one element from every window of size 3 such that the sum of elements for the sub-sequence is
minimized.
"""


def MinWindowSubSeq(arr: list, window: int) -> int:
    if (N := len(arr)) <= window:                       # Check if array is equal (or less) than the window size
        return min(arr)                                 # Minimum sum is the min-element

    selected = [0 for _ in range(N)]                    # Set flag for each element to track selection
    min_sum = 0                                         # Initialise variable to hold the min-sum

    for i in range(window - 1, N):                      # Start from the end element of the first window
        min_, idx, new = arr[i], i, 1                   # Initialise variables to track the min-element

        for j in range(1, window):                      # Iterate through the window in reverse
            if selected[i - j]:                         # Check if any element from the window is already selected
                new = 0                                 # Flag no new element being selected in the current window
                break                                   # Break out of the loop
            elif arr[i - j] < min_:                     # Check if any element in window is smaller than current min
                min_, idx = arr[i - j], i - j           # Update the respective tracking variable

        if new:                                         # Check if any new element was selected from the window
            selected[idx] = 1                           # Update the element's flag as 1 (True)
            min_sum += min_                             # Add element's value to the min-sum variable

    return min_sum                                      # Return the result


x = [3, 2, 1, 1, 2, 3, 1, 3, 2, 1]
print(MinWindowSubSeq(x, 3))
