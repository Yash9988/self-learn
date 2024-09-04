"""
Find the length for the longest (increasing) sub-sequence
"""


# N^2 approach
def longestSeq(arr: list) -> int:
    n = len(arr)
    l = [1 for _ in range(n)]                   # Set longest subsequence for each element as 1

    for i in range(1, n):                       # Iterate through all elements
        for j in range(i):                      # Iterate through earlier elements
            if arr[j] < arr[i]:                 # Check for condition of sub-sequence
                l[i] = max(l[i], l[j] + 1)      # Store the longest sub-sequence length

    return max(l)                               # Return the maximum length


# N log N approach
def longestSeqOp(arr: list) -> int:
    def bSearch(l: int, r: int) -> int:     # Binary search to replace the next largest element (log N)
        if l == r:
            return l

        mid = l + ((r - l) // 2)

        if arr[mid] == a:
            return mid
        elif arr[mid] > a:
            return bSearch(l, mid)
        else:
            return bSearch(mid + 1, r)

    res = arr[:1]                           # Start with first element since the 1 is the smallest possible length

    for a in arr[1:]:                       # Iterate through array (N)
        if a > res[-1]:                     # Append if last element is smaller (or larger, depending upon condition)
            res.append(a)
        else:
            idx = bSearch(0, len(res) - 1)  # Find the closest larger element in array
            res[idx] = a                    # Replace with the smaller value (still preserving the length)

    return len(res)                         # Return length of the resultant sub-sequence


# x = [10, 22, 9, 33, 21, 50, 41, 60, 80]
# print(longestSeq(x))
# print(longestSeqOp(x))
