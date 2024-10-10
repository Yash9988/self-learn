"""
Given 'n' non-negative integers representing an elevation map where the width of each bar is 1.
Compute how much water is trapped in the crevices, after raining.
"""


# Bottom-Up Approach (Time: O(n); Space: O(n))
def RWTrapping(arr: list[int]) -> int:
    n = len(arr)                                            # Store the length of the array
    left, right = [arr[0]], [arr[-1]]                       # Initialise DP for left and right direction

    for i in range(1, n):                                   # Iterate from the second element to last
        left.append(max(left[-1], arr[i]))                  # Compare and append the highest elevation so far

    for i in range(n - 2, -1, -1):                          # Iterate from the second last element to the first one
        right.append(max(right[-1], arr[i]))                # Compare and append the highest elevation so far

    right = right[::-1]                                     # Reverse the 'right' array to align with general indexing

    ans = 0                                                 # Initialise counter
    for i in range(n):                                      # Iterate through the array
        ans += min(left[i], right[i]) - arr[i]              # Calculate & add the water accumulated at the current index

    return ans                                              # Return the answer


# Double-pointer Approach (Time: O(n); Space: O(1))
def RWTrapping_(arr: list[int]) -> int:
    left = right = ans = 0                                  # Initialise trackers and counter
    i, j = 0, len(arr) - 1                                  # Set another pointers at the start and end of the array

    while i <= j:                                           # While the left pointer is smaller than the right
        left = max(left, arr[i])                            # Update the left tracker with the max-elevation so far
        right = max(right, arr[j])                          # Update the right tracker with the max-elevation so far

        if left < right:                                    # If the left tracker is smaller
            ans += left - arr[i]                            # Update the counter with collected water at current index
            i += 1                                          # Increment the left pointer
        else:                                               # If the right tracker is smaller (or equal)
            ans += right - arr[j]                           # Update the counter
            j -= 1                                          # Decrement the right pointer

    return ans                                              # Return the result


# print(RWTrapping([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# print(RWTrapping_([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
