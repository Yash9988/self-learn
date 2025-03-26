"""
773. Sliding Puzzle [HARD]

On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. A move consists of
choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given the puzzle board `board`, return the least number of moves required so that the state of the board is solved. If
it is impossible for the state of the board to be solved, return -1.


Example 1:
Input: board = [[1,2,3],[4,0,5]]
Output: 1

Explanation: Swap the 0 and the 5 in one move.


Example 2:
Input: board = [[1,2,3],[5,4,0]]
Output: -1

Explanation: No number of moves will make the board solved.


Example 3:
Input: board = [[4,1,2],[5,0,3]]
Output: 5

Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]


Constraints:

    -> board.length == 2
    -> board[i].length == 3
    -> 0 <= board[i][j] <= 5
    -> Each value board[i][j] is unique.


Concepts: Heap, Deque, BFS, Action Set
"""
from collections import deque
from heapq import heappush, heappop


# Optimised Solution
def slidingPuzzle_op(board: list[list[int]]) -> int:
    # Helper method to check if the sequence order is valid
    def check(seq):
        n = len(seq)                                                # Obtain the sequence length
        cnt = sum(seq[i] > seq[j] for i in range(n)
                  for j in range(i, n))                             # Compute the count for the sequence order
        return cnt % 2 == 0                                         # Return if the count is even

    # Helper method to compute the "distance" for a given state
    def f(s):
        ans = 0
        for i in range(m * n):
            if s[i] != '0':
                num = ord(s[i]) - ord('1')
                ans += abs(i // n - num // n) + abs(i % n - num % n)
        return ans

    m, n = 2, 3                                                     # Initialise the dimensions of the board
    seq = []                                                        # Initialise an empty list to store sequences
    start, end = '', '123450'                                       # Initialise the start and end state

    for i in range(m):                                              # Iterate through the rows
        for j in range(n):                                          # Iterate through the cols
            if board[i][j] != 0:                                    # Check if the curr-val is not 0
                seq.append(board[i][j])                             # Append the board value to the seq-list
            start += str(board[i][j])                               # Append the value to the start state

    if not check(seq):                                              # Check if sequence order is not valid
        return -1                                                   # Return -1

    q = [(f(start), start)]                                         # Initialise a queue with start state tuple
    dist = {start: 0}                                               # Initialise a dict to track the distance/moves

    while q:                                                        # While the queue is non-empty
        _, state = heappop(q)                                       # Pop out the state with the smallest diff-metric
        if state == end:                                            # Check if the curr-state is same as the target
            return dist[state]                                      # Return the distance/moves

        p1 = state.index('0')                                       # Obtain the 1D position of `0` in the curr-state
        i, j = p1 // n, p1 % n                                      # Compute its 2D position counterpart
        s = list(state)                                             # Convert the state into a list of strings

        for a, b in [[0, -1], [0, 1], [1, 0], [-1, 0]]:             # Iterate through the possible move-set
            x, y = i + a, j + b                                     # Compute the offset indices
            if 0 <= x < m and 0 <= y < n:                           # Check if the indices are within the grid
                p2 = x * n + y                                      # Compute the 1D position
                s[p1], s[p2] = s[p2], s[p1]                         # Swap the values at original and offset positions
                next = ''.join(s)                                   # Store the new state
                s[p1], s[p2] = s[p2], s[p1]                         # Swap the values back to their original state

                # Check if unobserved state and its "distance" is larger than that of curr-state
                if next not in dist or dist[next] > dist[state] + 1:
                    dist[next] = dist[state] + 1                    # Update the distance of new state
                    heappush(q, (dist[next] + f(next), next))       # Push the new state and its distance into the heap

    return -1                                                       # If we exhaust the queue without finding the target


# Alternate Solution
def slidingPuzzle_alt(board: list[list[int]]) -> int:
    target = "123450"                                               # Initialise target state
    start = ''.join(str(num) for row in board for num in row)       # Initialise start state

    # Initialise a neighbors map for each index in the 1D representation of the board
    neighbors = {
        0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
        3: [0, 4], 4: [1, 3, 5], 5: [2, 4]
    }

    # BFS setup
    queue = deque([(start, 0)])                                     # Initialise deque in the form: (state, moves)
    visited = set()                                                 # Initialise a set to track all visited states
    visited.add(start)                                              # Append the start state to the set

    while queue:                                                    # While the queue is non-empty
        state, moves = queue.popleft()                              # Pop the leftmost tuple from the queue

        if state == target:                                         # Check if we've reached the target
            return moves                                            # Return the result

        zero_index = state.index('0')                               # Find the index of zero

        # Iterate new states obtained by swapping '0' with its neighbors
        for neighbor in neighbors[zero_index]:
            new_state = list(state)                                 # Convert state to a list for mutation

            # Swap '0' with the neighbor
            new_state[zero_index], new_state[neighbor] = new_state[neighbor], new_state[zero_index]

            new_state_str = ''.join(new_state)                      # Convert back to string

            if new_state_str not in visited:                        # Check if this new state hasn't been visited
                visited.add(new_state_str)                          # Append the state into the visited set
                queue.append((new_state_str, moves + 1))            # Append the state to the queue

    return -1                                                       # If we exhaust the queue without finding the target
