# Implementation for (Min) Heap data structure
class Heap:
    def __init__(self):
        self.heap = []
        self.last = 0
    def swap_up(self, idx):
        if idx - 1:
            curr, parent = self.heap[idx - 1], self.heap[(idx // 2) - 1]
            if curr < parent:
                self.heap[idx - 1], self.heap[(idx // 2) - 1] = parent, curr
                self.swap_up(idx // 2)
    def swap_down(self, idx=1):
        min_idx = min(enumerate([self.heap[(2 * idx) - 1], self.heap[2 * idx]]), key=lambda x: x[1])[0]
        parent, min_child = self.heap[idx - 1], self.heap[(2 * idx) - 1 + min_idx]
        if min_child < parent:
            self.heap[idx - 1], self.heap[(2 * idx) - 1 + min_idx] = min_child, parent
            self.swap_down((2 * idx) - 1 + min_idx)
    def push(self, n):
        self.heap.append(n)
        self.last += 1
        self.swap_up(self.last)
    def pop(self):
        self.heap[0], self.heap[self.last] = self.heap[self.last], self.heap[0]
        self.last -= 1
        self.swap_up()