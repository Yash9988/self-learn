"""
1025. Divisor Game [EASY]

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:

    - Choosing any x with 0 < x < n and n % x == 0.
    - Replacing the number n on the chalkboard with n - x.

Also, if a player cannot make a move, they lose the game.

Return true if and only if Alice wins the game, assuming both players play optimally.


Example 1:

Input: n = 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.

Example 2:

Input: n = 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.


Constraints: 1 <= n <= 1000
"""


# My Solution (Bottom-Up Approach)
def divisorGame(n: int) -> bool:
    dp = {1: 0}                                 # Initialise DP with base-case

    for i in range(2, n + 1):                   # Iterate till n (inclusive)
        dp[i] = 0                               # Default index value to zero (lose)
        for j in range(1, i):                   # Iterate to i
            if i % j == 0 and not dp[i - j]:    # Check if % and difference leads to a losing position
                dp[i] = 1                       # Mark the current position as winning
                break
    return bool(dp[n])                          # Return the final result


"""
-> Conclusion
If N is even, can win.
If N is odd, will lose.

-> Recursive Prove （Top-down)

If N is even.
We can choose x = 1.
The opponent will get N - 1, which is a odd.
Reduce to the case odd and he will lose.

If N is odd,
2.1 If N = 1, lose directly.
2.2 We have to choose an odd x.
The opponent will get N - x, which is a even.
Reduce to the case even and he will win.

So the N will change odd and even alternatively until N = 1.
"""


def optimalSol(n: int) -> bool:
    return n % 2 == 0
