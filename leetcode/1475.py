"""
1475. Final Prices With a Special Discount in a Shop [EASY]

You are given an integer array prices where prices[i] is the price of the ith item in a shop.

There is a special discount for items in the shop. If you buy the ith item, then you will receive a discount equivalent
to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you will not receive
any discount at all.

Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, considering
the special discount.


Example 1:
Input: prices = [8,4,6,2,3]
Output: [4,2,4,2,3]

Explanation:
- For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will
pay is 8 - 4 = 4.

- For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will
pay is 4 - 2 = 2.

- For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will
pay is 6 - 2 = 4.

- For items 3 and 4 you will not receive any discount at all.


Example 2:
Input: prices = [1,2,3,4,5]
Output: [1,2,3,4,5]

Explanation: In this case, for all items, you will not receive any discount at all.


Example 3:
Input: prices = [10,1,1,6]
Output: [9,0,1,6]


Constraints:

    -> 1 <= prices.length <= 500
    -> 1 <= prices[i] <= 1000


Concepts: Stack/Deque
"""


# My Solution
def finalPrices(prices: list[int]) -> list[int]:
    n = len(prices)                                                 # Obtain the size of the list
    res = [0] * n                                                   # List to store the results

    for i in range(n):                                              # Iterate through the range of list
        f = False                                                   # Flag to track the state of price change
        for j in range(i + 1, n):                                   # Iterate through the range of remaining list
            if prices[j] <= prices[i]:                              # Check if later prices are smaller than current
                res[i] = prices[i] - prices[j]                      # Update the result list with the discounted price
                f = True                                            # Set the change flag
                break                                               # Break out of the loop

        if not f:                                                   # Check if price hasn't changed
            res[i] = prices[i]                                      # Update the original price in the result

    return res                                                      # Return the result


# Optimised Solution
def finalPrices_op(prices: list[int]) -> list[int]:
    stack = []                                                      # List to track original price indices
    res = prices[:]                                                 # List to store the results

    for i in range(len(prices)):                                    # Iterate through the list range
        while stack and prices[stack[-1]] >= prices[i]:             # Check if the stack price is higher than current
            res[stack.pop()] -= prices[i]                           # Update the result with the discounted prices

        stack.append(i)                                             # Append the current price index to the stack

    return res                                                      # Return the result
