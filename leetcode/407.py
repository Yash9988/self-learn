"""
407. Trapping Rain Water II [HARD]

Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the
volume of water it can trap after raining.


Example 1:
Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4

Explanation: After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.


Example 2:
Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
Output: 10


Constraints:

    -> m == heightMap.length
    -> n == heightMap[i].length
    -> 1 <= m, n <= 200
    -> 0 <= heightMap[i][j] <= 2 * 10^4


Concepts: Heap, BFS
"""
import heapq


# Optimised Solution
def trapRainWater(heightMap: list[list[int]]) -> int:
    M, N = len(heightMap), len(heightMap[0])                        # Obtain the grid dimensions

    h = []                                                          # List to store map states

    # Tracking the boundaries of the elevation map
    for i in [0, M - 1]:                                            # Iterate through the first & last row
        for j in range(N):                                          # Iterate through the columns
            h.append((heightMap[i][j], i, j))                       # Append the state to the list
            heightMap[i][j] = -1                                    # Update the cell value

    for i in range(1, M - 1):                                       # Iterate through the rows
        for j in [0, N - 1]:                                        # Iterate through the first & last col
            h.append((heightMap[i][j], i, j))                       # Append the state the list
            heightMap[i][j] = -1                                    # Update the cell value

    heapq.heapify(h)                                                # Heapify the list

    tot = 0                                                         # Counter to track the water volume
    while h:                                                        # While the heap is non-empty
        height, x, y = heapq.heappop(h)                             # Pop out the smallest tuple
        stack = [(x, y)]                                            # Stack to track indices

        while h and h[0][0] == height:                              # While the heap contains similar height tuples
            _, x, y = heapq.heappop(h)                              # Pop the tuple from the heap
            stack.append((x, y))                                    # Append the indices to the stack

        while stack:                                                # While the stack is non-empty
            x, y = stack.pop()                                      # Pop the indices from the stack
            for d in [-1, 1]:                                       # Iterate through the neighbouring cells
                nX, nY = x + d, y + d                               # Compute the neighbouring indices

                if nX < 0 or nX >= M or heightMap[nX][y] == -1:     # Check for invalid row index
                    pass
                elif height > heightMap[nX][y]:                     # Check if neighbour elevation is smaller
                    tot += height - heightMap[nX][y]                # Increment the counter by the height diff
                    stack.append((nX, y))                           # Append the indices to the stack
                    heightMap[nX][y] = -1                           # Update the cell value
                else:
                    heapq.heappush(h, (heightMap[nX][y], nX, y))    # Append the state to the heap, otherwise
                    heightMap[nX][y] = -1                           # Update the cell value

                if 0 > nY or N <= nY or heightMap[x][nY] == -1:     # Check for invalid col-index
                    pass
                elif height > heightMap[x][nY]:                     # Check if the neighbour elevation is smaller
                    tot += height - heightMap[x][nY]                # Increment the counter by the height diff
                    stack.append((x, nY))                           # Append the indices to the stack
                    heightMap[x][nY] = -1                           # Update the cell value
                else:
                    heapq.heappush(h, (heightMap[x][nY], x, nY))    # Append the state to the heap, otherwise
                    heightMap[x][nY] = -1                                 # Update the cell value

    return tot                                                      # Return the result


# Alternate Solution
def trapRainWater_alt(heightMap: list[list[int]]) -> int:
    if not heightMap or not heightMap[0]:                           # Check for edge cases
        return 0                                                    # Return 0

    m, n = len(heightMap), len(heightMap[0])                        # Obtain the grid dimensions
    visited = [[False] * n for _ in range(m)]                       # 2D list to track visited cells
    minHeap = []                                                    # Heap to store grid states

    # Add boundary cells
    for i in range(m):                                              # Iterate through the rows
        for j in [0, n - 1]:                                        # Iterate through boundary columns
            heapq.heappush(minHeap, (heightMap[i][j], i, j))        # Append the state to the heap
            visited[i][j] = True                                    # Mark the cell visited

    for j in range(n):                                              # Iterate through the columns
        for i in [0, m - 1]:                                        # Iterate through boundary rows
            if not visited[i][j]:                                   # Check if the cell is unvisited
                heapq.heappush(minHeap, (heightMap[i][j], i, j))    # Append the state to the heap
                visited[i][j] = True                                # Mark the cell visited

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]                 # Directions to explore the neighbours cells
    waterTrapped = 0                                                # Counter to track the water volume

    while minHeap:                                                  # While the heap is non-empty
        height, x, y = heapq.heappop(minHeap)                       # Pop the smallest tuple from the heap

        for dx, dy in directions:                                   # Iterate through the directions
            nx, ny = x + dx, y + dy                                 # Compute the neighbour index

            # Check if the indices are valid and the cell is unvisited
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                waterTrapped += max(0, height - heightMap[nx][ny])  # Increment the counter by the height-diff

                # Append the state to the heap
                heapq.heappush(minHeap, (max(height, heightMap[nx][ny]), nx, ny))

                visited[nx][ny] = True                              # Mark the cell visited

    return waterTrapped                                             # Return the result
