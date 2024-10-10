"""
Given an array, in every window of size 3 choose __at most__ 2 elements so that the final sum is maximised.
"""

from MinWindowSubSeq import MinWindowSubSeq_


def MaxWindowSum(arr: list, window: int) -> int:
    return sum(arr) - MinWindowSubSeq_(arr, window)


# x = [3, 2, 3, 2, 3, 5, 1, 3]
# print(MaxWindowSum(x, 3))
