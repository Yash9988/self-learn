# Time: O(#Bits), Space: O(1)
def countSetBits(n: int) -> int:
    res = 0
    while n:
        res += n & 1
        n >>= 1
    return res


# Time: O(#Set-Bits), Space: O(1)
def countSetBits_op(n: int) -> int:
    res = 0
    while n:
        res += 1
        n &= n - 1
    return res


def getIthBit(n: int, i: int) -> int:
    return n & (1 << i) != 0


def flipIthBit(n: int, i: int) -> int:
    return n ^ (1 << i)


def unsetIthBit(n: int, i: int) -> int:
    return n & ~(1 << i)