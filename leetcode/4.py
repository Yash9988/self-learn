"""
4. Median of Two Sorted Arrays [HARD]

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).


Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.


Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


Constraints:

    -> nums1.length == m
    -> nums2.length == n
    -> 0 <= m <= 1000
    -> 0 <= n <= 1000
    -> 1 <= m + n <= 2000
    -> -106 <= nums1[i], nums2[i] <= 106


Concepts: Two Pointers
"""


# My Solution [Time: O(n + m); Space: O((n + m) / 2)]   TODO: Optimise for O(1) space by using only pointers!
def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    m, n = len(nums1), len(nums2)                   # Obtain and store the length of each array
    t = m + n                                       # Calculate the sum of the array sizes
    x = (t // 2) + 1                                # Calculate the median index

    count = l = r = 0                               # Initialise the pointers and counter
    s = []                                          # Initialise an array to store sorted numbers
    while l < m and r < n:                          # Iterate while pointers are within array range
        if nums1[l] < nums2[r]:                     # Check if value from first array is smaller than value from second
            s.append(nums1[l])                      # Add the value from the first array into the new array
            l += 1                                  # Increment the left pointer
        else:
            s.append(nums2[r])                      # Add the value from the second array into the new array
            r += 1                                  # Increment the right pointer
        count += 1                                  # Increment the counter

        if count >= x:                              # Check if counter has reached the median index
            break                                   # Break out of the while loop

    while count < x:                                # Check if counter is smaller than the median index
        if l < m:                                   # Check if the left pointer is smaller than the first array size
            s.append(nums1[l])                      # Add value to the array
            l += 1                                  # Increment the pointer
        if r < n:                                   # Check if the right pointer is smaller than the second array size
            s.append(nums2[r])                      # Add the value to the array
            r += 1                                  # Increment the pointer
        count += 1                                  # Increment the counter

    return sum(s[-2:]) / 2 if t % 2 == 0 else s[-1]  # Return the result


# Optimal Solution
def findMedianSortedArrays_p(nums1: list[int], nums2: list[int]) -> float:
    m = len(nums1)
    n = len(nums2)

    # when total length is odd, the median is the middle
    if (m + n) % 2 != 0:
        return get_kth(nums1, nums2, 0, m - 1, 0, n - 1, (m + n) // 2)
    else:
        # when total length is even, the median is the average of the middle 2
        x = get_kth(nums1, nums2, 0, m - 1, 0, n - 1, (m + n) // 2)
        y = get_kth(nums1, nums2, 0, m - 1, 0, n - 1, (m + n) // 2 - 1)
        return (x + y) / 2


def get_kth(nums1: list[int], nums2: list[int], start1: int, end1: int, start2: int, end2: int, k: int) -> int:
    if start1 > end1:
        return nums2[k - start1]
    if start2 > end2:
        return nums1[k - start2]

    middle1 = (start1 + end1) // 2
    middle2 = (start2 + end2) // 2
    middle1_value = nums1[middle1]
    middle2_value = nums2[middle2]

    # if sum of two medians' indices is smaller than k
    if (middle1 + middle2) < k:
        # if nums1 median value bigger than nums2, then nums2's first half will always be positioned before nums1's
        # median, so k would never be in num2's first half
        if middle1_value > middle2_value:
            return get_kth(nums1, nums2, start1, end1, middle2 + 1, end2, k)
        else:
            return get_kth(nums1, nums2, middle1 + 1, end1, start2, end2, k)
    # if sum of two medians' indices is bigger than k
    else:
        # if nums1 median value bigger than nums2, then nums2's first half would be merged before nums1's first half,
        # thus k always come before nums1's median, then nums1's second half would never include k
        if middle1_value > middle2_value:
            return get_kth(nums1, nums2, start1, middle1 - 1, start2, end2, k)
        else:
            return get_kth(nums1, nums2, start1, end1, start2, middle2 - 1, k)
