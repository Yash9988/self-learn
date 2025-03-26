"""
3321. Find X-Sum of All K-Long Subarrays II [HARD]

You are given an array nums of n integers and two integers k and x.

The x-sum of an array is calculated by the following procedure:

- Count the occurrences of all elements in the array.
- Keep only the occurrences of the top x most frequent elements. If two elements have the same number of occurrences,
  the element with the bigger value is considered more frequent.
- Calculate the sum of the resulting array.

Note that if an array has less than x distinct elements, its x-sum is the sum of the array.

Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the _subarray_ nums[i..i + k - 1].


Example 1:

Input: nums = [1,1,2,2,3,4,2,3], k = 6, x = 2
Output: [6,10,12]

Explanation:

- For subarray [1, 1, 2, 2, 3, 4], only elements 1 and 2 will be kept in the resulting array. Hence,
  answer[0] = 1 + 1 + 2 + 2.

- For subarray [1, 2, 2, 3, 4, 2], only elements 2 and 4 will be kept in the resulting array. Hence,
  answer[1] = 2 + 2 + 2 + 4. Note that 4 is kept in the array since it is bigger than 3 and 1 which occur the same
  number of times.

- For subarray [2, 2, 3, 4, 2, 3], only elements 2 and 3 are kept in the resulting array. Hence,
  answer[2] = 2 + 2 + 2 + 3 + 3.


Example 2:

Input: nums = [3,8,7,8,7,5], k = 2, x = 2
Output: [11,15,15,15,12]

Explanation:
Since k == x, answer[i] is equal to the sum of the subarray nums[i..i + k - 1].


Constraints:

    -> nums.length == n
    -> 1 <= n <= 10^5
    -> 1 <= nums[i] <= 10^9
    -> 1 <= x <= k <= nums.length


Concepts: Sorted-Containers, SortedList
"""
from sortedcontainers import SortedList
from collections import Counter


def findXSum(nums: list[int], k: int, x: int) -> list[int]:
    # Method to update the count of element and add to the bottom container
    def update(n: int, v: int) -> None:
        nonlocal curr_sum                               # Obtain the reference to curr-sum variable from outer scope

        if count[n]:                                    # Check if count of element is non-zero
            try:                                        # Attempt removing the data-tuple from bottom container
                bot.remove([count[n], n])
            except:
                top.remove([count[n], n])               # Remove the data-tuple from the top container
                curr_sum -= count[n] * n                # Update and overwrite the value of curr_sum counter

        count[n] += v                                   # Update the count of the element by the provided value
        if count[n]:                                    # Check if the element count is non-zero
            bot.add([count[n], n])                      # Add the data-tuple to the bottom container

    top, bot = SortedList(), SortedList()               # Initialise 2 sorted containers
    count, curr_sum = Counter(), 0                      # Initialise a freq-dict and a curr-sum counter
    res = []                                            # Initialise the result list

    for i, n in enumerate(nums):                        # Iterate through all the elements of the input-list
        update(n, 1)                                    # Increment the count of the curr-ele
        if i >= k:                                      # Check if curr-idx is greater than the window width
            update(nums[i - k], -1)                     # Decrement the count of the element at the start of the window

        while bot and len(top) < x:                     # While the top container length is smaller than `x`
            c, n = bot.pop()                            # Pop out the largest data-tuple from the bottom container
            curr_sum += c * n                           # Update the value of the curr-sum counter respectively
            top.add([c, n])                             # Add the data-tuple to the top container

        while bot and bot[-1] > top[0]:                 # While the largest-element in bottom > smallest-element in top
            cb, nb = bot.pop()                          # Pop the largest data-tuple from bottom container
            ct, nt = top.pop(0)                         # Pop the smallest data-tuple from top container

            curr_sum -= ct * nt                         # Decrement the counter value wrt data-tuple from top
            curr_sum += cb * nb                         # Increment the counter value wrt data-tuple from bottom

            bot.add([ct, nt])                           # Add the smaller data-tuple to bottom
            top.add([cb, nb])                           # Add the larger data-tuple to top

        if i >= k - 1:                                  # Check if index is equal to window width
            res.append(curr_sum)                        # Append the counter value to the result list

    return res                                          # Return the result
