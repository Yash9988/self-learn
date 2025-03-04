"""
2570. Merge Two 2D Arrays by Summing Values [EASY]

You are given two 2D integer arrays nums1 and nums2.

    - nums1[i] = [id_i, val_i] indicate that the number with the id id_i has a value equal to val_i.
    - nums2[i] = [id_i, val_i] indicate that the number with the id id_i has a value equal to val_i.

Each array contains unique ids and is sorted in ascending order by id.

Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:

    - Only ids that appear in at least one of the two arrays should be included in the resulting array.
    - Each id should be included only once and its value should be the sum of the values of this id in the two arrays.
      If the id does not exist in one of the two arrays, then assume its value in that array to be 0.

Return the resulting array. The returned array must be sorted in ascending order by id.


Example 1:
Input: nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]
Output: [[1,6],[2,3],[3,2],[4,6]]

Explanation: The resulting array contains the following:
- id = 1, the value of this id is 2 + 4 = 6.
- id = 2, the value of this id is 3.
- id = 3, the value of this id is 2.
- id = 4, the value of this id is 5 + 1 = 6.


Example 2:
Input: nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]
Output: [[1,3],[2,4],[3,6],[4,3],[5,5]]

Explanation: There are no common ids, so we just include each id with its value in the resulting list.


Constraints:

    -> 1 <= nums1.length, nums2.length <= 200
    -> nums1[i].length == nums2[j].length == 2
    -> 1 <= id_i, val_i <= 1000
    -> Both arrays contain unique ids.
    -> Both arrays are in strictly ascending order by id.


Concepts:
"""
from collections import defaultdict


# My Solution
def mergeArrays(nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
    sums = defaultdict(int)                                         # Dict to track the sums at ids
    ids = set([])                                                   # Set to track the seen ids

    for idx, num in nums1:                                          # Iterate through the first list
        sums[idx] += num                                            # Append the num-val at corr-id
        ids.add(idx)                                                # Add the id to the set

    for idx, num in nums2:                                          # Iterate through the second list
        sums[idx] += num                                            # Append the num-val at corr-id
        ids.add(idx)                                                # Add the id to the set

    res = []                                                        # List to track the result
    for idx in range(max(ids) + 1):                                 # Iterate through the range of ids
        if idx in ids:                                              # Check if id present in the set
            res.append([idx, sums[idx]])                            # Append the tuple to the list: (id, sum)

    return res                                                      # Return the result


# Optimised Solution
def mergeArrays_op(nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
    n1, n2 = len(nums1), len(nums2)                                 # Obtain the list sizes
    l = r = 0                                                       # Set 2 pointers
    res = []                                                        # List to store the result

    while l < n1 and r < n2:                                        # While both pointers are smaller than list sizes
        if nums1[l][0] == nums2[r][0]:                              # Check if the tuple ids are equal
            res.append([nums1[l][0], nums1[l][1] + nums2[r][1]])    # Append the sum of the elements to the list
            l += 1                                                  # Increment the left pointer
            r += 1                                                  # Increment the right pointer

        elif nums1[l][0] < nums2[r][0]:                             # Check if left-id is smaller than right-id
            res.append(nums1[l])                                    # Append the left tuple to the list
            l += 1                                                  # Increment the left pointer

        else:
            res.append(nums2[r])                                    # Append the right tuple to the list, otherwise
            r += 1                                                  # Increment the right pointer

    while l < n1:                                                   # While the left pointer is smaller than list size
        res.append(nums1[l])                                        # Append the tuple to the list
        l += 1                                                      # Increment the pointer

    while r < n2:                                                   # While the right pointer is smaller than list size
        res.append(nums2[r])                                        # Append the tuple to the list
        r += 1                                                      # Increment the right pointer

    return res                                                      # Return the result
