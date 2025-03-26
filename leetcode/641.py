"""
641. Design Circular Deque [MEDIUM]

Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:

- MyCircularDeque(int k) Initializes the deque with a maximum size of k.
- boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
- boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
- boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
- boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
- int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
- int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
- boolean isEmpty() Returns true if the deque is empty, or false otherwise.
- boolean isFull() Returns true if the deque is full, or false otherwise.


Example 1:

Input:
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast",
"insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output:
[null, true, true, true, false, 2, true, true, true, 4]

Explanation:

MyCircularDeque myCircularDeque = new MyCircularDeque(3);
myCircularDeque.insertLast(1);  // return True
myCircularDeque.insertLast(2);  // return True
myCircularDeque.insertFront(3); // return True
myCircularDeque.insertFront(4); // return False, the queue is full.
myCircularDeque.getRear();      // return 2
myCircularDeque.isFull();       // return True
myCircularDeque.deleteLast();   // return True
myCircularDeque.insertFront(4); // return True
myCircularDeque.getFront();     // return 4


Constraints:

    -> 1 <= k <= 1000
    -> 0 <= value <= 1000
    -> At most 2000 calls will be made to insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty,
       isFull.


Concepts: Deque Implementation
"""
# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()


class MyCircularDeque:

    def __init__(self, k: int):
        self._size = 0                                          # Counter to track elements in deque
        self._front, self._rear = 0, 0                          # Front and Rear pointers
        self._capacity = k                                      # Size of the deque
        self._data = [-1] * k                                   # Array to hold deque values

    def insertFront(self, value: int) -> bool:
        if self.isFull():                                       # Check if the deque is full
            return False                                        # Return False

        if self.isEmpty():                                      # Check if the deque is empty
            self._data[self._front] = value                     # Insert value at the front pointer index
        else:
            self._front = (self._front - 1) % self._capacity    # Update the location of the front pointer
            self._data[self._front] = value                     # Insert value at the front pointer index
        self._size += 1                                         # Increment the size counter

        return True                                             # Return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():                                       # Check if the deque is full
            return False                                        # Return False

        if self.isEmpty():                                      # Check if the deque is empty
            self._data[self._rear] = value                      # Insert value at the rear pointer index
        else:
            self._rear = (self._rear + 1) % self._capacity      # Update the location of the rear pointer
            self._data[self._rear] = value                      # Insert value at the rear pointer index
        self._size += 1                                         # Increment the size counter

        return True                                             # Return True

    def deleteFront(self) -> bool:
        if self.isEmpty():                                      # Check if the deque is empty
            return False                                        # Return False

        self._data[self._front] = -1                            # Remove the value at the front pointer index
        self._front = (self._front + 1) % self._capacity        # Update the location of the front pointer
        self._size -= 1                                         # Decrement the size counter

        if self.isEmpty():                                      # Check if the deque is empty
            self._rear = self._front                            # Set the pointer equal

        return True                                             # Return True

    def deleteLast(self) -> bool:
        if self.isEmpty():                                      # Check if the deque is empty
            return False                                        # Return False

        self._data[self._rear] = -1                             # Remove the value at the rear pointer index
        self._rear = (self._rear - 1) % self._capacity          # Update the location of the rear pointer
        self._size -= 1                                         # Decrement the size counter

        if self.isEmpty():                                      # Check if the deque is empty
            self._front = self._rear                            # Set the pointer equal

        return True                                             # Return True

    def getFront(self) -> int:
        return self._data[self._front]                          # Return the value at the front pointer index

    def getRear(self) -> int:
        return self._data[self._rear]                           # Return the value at the rear pointer index

    def isEmpty(self) -> bool:
        return self._size == 0                                  # Return whether the size counter equals zero

    def isFull(self) -> bool:
        return self._size == self._capacity                     # Return whether the size counter equals capacity
