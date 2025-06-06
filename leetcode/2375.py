"""
2375. Construct Smallest Number From DI String [MEDIUM]

You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning
decreasing.

A 0-indexed string num of length n + 1 is created using the following conditions:

    - num consists of the digits '1' to '9', where each digit is used at most once.
    - If pattern[i] == 'I', then num[i] < num[i + 1].
    - If pattern[i] == 'D', then num[i] > num[i + 1].

Return the lexicographically smallest possible string num that meets the conditions.


Example 1:
Input: pattern = "IIIDIDDD"
Output: "123549876"

Explanation:
At indices 0, 1, 2, and 4 we must have that num[i] < num[i+1].
At indices 3, 5, 6, and 7 we must have that num[i] > num[i+1].
Some possible values of num are "245639871", "135749862", and "123849765".
It can be proven that "123549876" is the smallest possible num that meets the conditions.
Note that "123414321" is not possible because the digit '1' is used more than once.


Example 2:
Input: pattern = "DDD"
Output: "4321"

Explanation:
Some possible values of num are "9876", "7321", and "8742".
It can be proven that "4321" is the smallest possible num that meets the conditions.


Constraints:

    -> 1 <= pattern.length <= 8
    -> pattern consists of only the letters 'I' and 'D'.


Concepts: Stacks
"""

# My Solution
def smallestNumber(pattern: str) -> str:
    stack = []                                                      # List to track decreasing nums
    res = ''                                                        # String to store the result

    x = 1                                                           # Counter to track curr-num
    for ch in pattern:                                              # Iterate through the pattern
        if ch == 'I':                                               # If the curr-char is 'I'
            res += str(x)                                           # Append the counter value to the res-str
            while stack:                                            # While the stack is non-empty
                res += stack.pop()                                  # Pop the last element and append to the res-str
        else:
            stack.append(str(x))                                    # Append the counter value to the list

        x += 1                                                      # Increment the counter

    stack.append(str(x))                                            # Append the counter value to the list
    while stack:                                                    # While the stack is non-empty
        res += stack.pop()                                          # Pop and append the last element to the res-str

    return res                                                      # Return the result


# Alternate Solution (Concise)
def smallestNumber_alt(pattern: str) -> str:
    n = len(pattern)                                                # Compute the string size
    result = ""                                                     # String to store the result
    stack = []                                                      # List to track the decreasing nums

    for i in range(n + 1):                                          # Iterate through the string range
        stack.append(i + 1)                                         # Append the element to the stack

        if i == n or pattern[i] == 'I':                             # Check if curr-char is 'I' or reached string end
            while stack:                                            # While the stack is non-empty
                result += str(stack.pop())                          # Pop and append the last element to the res-str

    return result                                                   # Return the result
