"""
2349. Design a Number Container System [MEDIUM]

Design a number container system that can do the following:

    - Insert or Replace a number at the given index in the system.
    - Return the smallest index for the given number in the system.

Implement the NumberContainers class:

    - NumberContainers() Initializes the number container system.
    - void change(int index, int number) Fills the container at index with the number. If there is already a number at
      that index, replace it.
    - int find(int number) Returns the smallest index for the given number, or -1 if there is no index that is filled by
      number in the system.


Example 1:
Input:
["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"]
[[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]
Output:
[null, -1, null, null, null, null, 1, null, 2]

Explanation:
NumberContainers nc = new NumberContainers();
nc.find(10); // There is no index that is filled with number 10. Therefore, we return -1.
nc.change(2, 10); // Your container at index 2 will be filled with number 10.
nc.change(1, 10); // Your container at index 1 will be filled with number 10.
nc.change(3, 10); // Your container at index 3 will be filled with number 10.
nc.change(5, 10); // Your container at index 5 will be filled with number 10.
nc.find(10); // Number 10 is at the indices 1, 2, 3, and 5. Since the smallest index that is filled with 10 is 1, we return 1.
nc.change(1, 20); // Your container at index 1 will be filled with number 20. Note that index 1 was filled with 10 and then replaced with 20.
nc.find(10); // Number 10 is at the indices 2, 3, and 5. The smallest index that is filled with 10 is 2. Therefore, we return 2.


Constraints:

    -> 1 <= index, number <= 10^9
    -> At most 10^5 calls will be made in total to change and find.


Concepts: Custom-DS, Heap, Hashmap
"""
from collections import defaultdict
from heapq import heappush, heappop


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)

# My Solution (Optimised)
class NumberContainers:

    def __init__(self):
        self.idx = defaultdict(list)                                # Dict to map all associated indices to resp-num
        self.nums = defaultdict(lambda: -1)                         # Dict to map container idx to asso-num

    def change(self, index: int, number: int) -> None:
        self.nums[index] = number                                   # Update the number at the index
        heappush(self.idx[number], index)                           # Append the index to the num-idx-heap

    def find(self, number: int) -> int:
        if not self.idx[number]:                                    # Check if the num-idx-heap is empty
            return -1                                               # Return -1

        heap = self.idx[number]                                     # Create a copy of the num-idx-heap
        while heap:                                                 # While the heap is non-empty
            if self.nums[heap[0]] == number:                        # Check if the smallest-idx is assigned the same num
                return heap[0]                                      # Return the idx

            heappop(heap)                                           # Pop the smallest-idx (assigned to other num)

        return -1                                                   # Return -1
