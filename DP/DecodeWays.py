"""
A message containing letters A-Z is being encoded to numbers (1 to 26).

Given a non-empty string containing only digits, determine the total #ways to decode it.
"""


# Top-Down Approach
def DecodeWays(code: str) -> int:
    if len(code) == 1:                                              # Initialise base-cases
        return 1 if int(code) else 0                                # Check for invalid value (0)
    elif len(code) == 2:
        return (1 if int(code) < 27 else 0) + DecodeWays(code[:-1])

    return DecodeWays(code[:-1]) + DecodeWays(code[:-2])            # Recursively obtain solutions for sub-problems


# Bottom-Up Approach
def DecodeWays_(code: str) -> int:
    dp = [1, 1 if int(code[0]) else 0]                              # Initialise base-cases for DP

    for i in range(2, len(code) + 1):                               # Iterate from the second element of code
        ans = dp[i - 1] if int(code[i - 1]) else 0                  # Iteratively obtain solution for sub-problems
        ans += dp[i - 2] if int(code[i-2: i]) < 27 else 0

        dp.append(ans)                                              # Append the solution to the DP

    return dp[-1]                                               # Return the result


# print(DecodeWays("0"))
# print(DecodeWays_("226"))
# print(DecodeWays("1226"))
