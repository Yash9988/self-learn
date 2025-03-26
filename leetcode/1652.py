"""
1652. Defuse the Bomb [EASY]

You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of
length of n and a key k.

To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

    - If k > 0, replace the ith number with the sum of the next k numbers.
    - If k < 0, replace the ith number with the sum of the previous k numbers.
    - If k == 0, replace the ith number with 0.

As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!


Example 1:
Input: code = [5,7,1,4], k = 3
Output: [12,10,16,13]

Explanation: Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1].
Notice that the numbers wrap around.


Example 2:
Input: code = [1,2,3,4], k = 0
Output: [0,0,0,0]

Explanation: When k is zero, the numbers are replaced by 0.


Example 3:
Input: code = [2,4,9,3], k = -2
Output: [12,5,6,13]

Explanation: The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice that the numbers wrap around again. If k is negative,
the sum is of the previous numbers.


Constraints:

    -> n == code.length
    -> 1 <= n <= 100
    -> 1 <= code[i] <= 100
    -> -(n - 1) <= k <= n - 1


Concepts: Prefix-Sum
"""


# My Solution
def decrypt(code: list[int], k: int) -> list[int]:
    n = len(code)                                                   # Compute the length of the list
    res = []                                                        # Initialise the result list

    for i in range(n):                                              # Iterate through the list
        temp = 0                                                    # Initialise a counter
        for j in range(abs(k)):                                     # Iterate through the window
            temp += code[(i + j + 1) % n] if k > 0 \
                else code[(i - j - 1) % n]                          # Increment the counter based upon condition
        res.append(temp)                                            # Append the counter value to the list

    return res                                                      # Return the list


# Optimised Solution
def decrypt_op(code: list[int], k: int) -> list[int]:
    n = len(code)                                                   # Compute the length of the list

    if k == 0:                                                      # Check if k is zero
        return [0] * n                                              # Return a list of zeros

    result = [0] * n                                                # Initialize the result list.

    start, end, step = (1, k + 1, 1) if k > 0 else (k, 0, 1)        # Determine the direction of the sliding window
    window_sum = sum(code[i % n] for i in range(start, end))        # Initialize the first window sum

    for i in range(n):                                              # Iterate through the list elements
        result[i] = window_sum                                      # Store the current window sum in the result

        window_sum -= code[(i + start) % n]                         # Remove outgoing element
        window_sum += code[(i + end) % n]                           # Add incoming element

    return result                                                   # Return the result list
