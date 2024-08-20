"""
Given an array of n elements, find the maximum sub-array sum (Kadane's Algorithm)
"""


def max_sum(arr):
    ans, total = float('-inf'), 0

    for n in arr:
        total += n              # Add 'n' to total
        ans = max(ans, total)   # Set 'ans' as max total
        total = max(total, 0)   # Discard negative sum

    return ans


a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sum(a))