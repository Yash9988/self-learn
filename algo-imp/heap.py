"""
Implementation for (Min) Heap data structure

IMPORTANT: The indexing begins with ONE(1) to implement the algorithm seamlessly!!!
"""


class Heap:
    def __init__(self, arr=None):

        self.heap = {}                      # Initialise heap as a dict
        self.curr = 1                       # curr points to the next available index

        if arr is not None:                 # Heapify input array
            [self.push(a) for a in arr]

    # Method to swap nodes if child is smaller than parent (bottom to top)
    def swap_up(self, idx):
        if idx - 1:                                                 # Proceed if not the root index
            curr, parent = self.heap[idx], self.heap[idx // 2]
            if curr < parent:                                       # Swap child and parent node
                self.heap[idx], self.heap[idx // 2] = parent, curr
                self.swap_up(idx // 2)                              # Recursively swap until order is restored

    # Method to swap nodes if parent is larger than child (top to bottom)
    def swap_down(self, idx=1):
        if idx < self.curr and 2 * idx < self.curr:
            child1, child2 = self.heap.get(2 * idx, float('inf')), self.heap.get(2 * idx + 1, float('inf'))
            children = enumerate([child1, child2])                                # Get child nodes
            min_idx = min(children, key=lambda x: x[1])[0]                        # Obtain child-node with min. value
            parent, min_child = self.heap[idx], self.heap[2 * idx + min_idx]
            if min_child < parent:                                                # Swap parent and child node
                self.heap[idx], self.heap[2 * idx + min_idx] = min_child, parent
                self.swap_down(2 * idx + min_idx)                   # Recursively swap until order is restored

    # Insert new element into the heap
    def push(self, n):
        self.heap[self.curr] = n        # Insert element at the bottom of the heap ("array")
        self.swap_up(self.curr)         # Check with the parent-node to restore the heap logic order
        self.curr += 1                  # Increment the curr-pointer

    # Remove (and return) the root node from the heap
    def pop(self):
        if self.curr - 1:
            self.curr -= 1                  # Decrement to point at the last node of heap
            self.heap[1], self.heap[self.curr] = self.heap[self.curr], self.heap[1]  # Swap the root node with last node
            temp = self.heap[self.curr]
            del self.heap[self.curr]
            self.swap_down()                # Check with children node to restore heap logic order
            return temp
        else:
            return "The heap is empty"

    def heapify(self, arr):
        [self.push(a) for a in arr]

    def size(self):
        return len(self.heap)

    def __str__(self):      # TODO: Add proper string representation (using a tree structure, preferably)
        return f"{[self.heap[i] for i in range(1, self.curr)]}"


h = Heap()

# for a in [50, 30, 20]:
#     h.push(a)
#
# print(h)
# print(h.pop())
# print(h)
