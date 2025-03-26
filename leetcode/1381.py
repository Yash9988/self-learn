"""
1381. Design a Stack With Increment Operation [MEDIUM]

Design a stack that supports increment operations on its elements.

Implement the CustomStack class:

    - CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack.
    - void push(int x) Adds x to the top of the stack if the stack has not reached the maxSize.
    - int pop() Pops and returns the top of the stack or -1 if the stack is empty.
    - void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements
      in the stack, increment all the elements in the stack.


Example 1:

Input:
["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
Output:
[null,null,null,2,null,null,null,null,null,103,202,201,-1]

Explanation:
CustomStack stk = new CustomStack(3); // Stack is Empty []
stk.push(1);                          // stack becomes [1]
stk.push(2);                          // stack becomes [1, 2]
stk.pop();                            // return 2 --> Return top of the stack 2, stack becomes [1]
stk.push(2);                          // stack becomes [1, 2]
stk.push(3);                          // stack becomes [1, 2, 3]
stk.push(4);                          // stack still [1, 2, 3], Do not add another elements as size is 4
stk.increment(5, 100);                // stack becomes [101, 102, 103]
stk.increment(2, 100);                // stack becomes [201, 202, 103]
stk.pop();                            // return 103 --> Return top of the stack 103, stack becomes [201, 202]
stk.pop();                            // return 202 --> Return top of the stack 202, stack becomes [201]
stk.pop();                            // return 201 --> Return top of the stack 201, stack becomes []
stk.pop();                            // return -1 --> Stack is empty return -1.


Constraints:

    -> 1 <= maxSize, x, k <= 1000
    -> 0 <= val <= 100
    -> At most 1000 calls will be made to each method of increment, push and pop each separately.


Concepts: Stack Implementation, Lazy Increment
"""
# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)


# My Solution
class CustomStack:

    def __init__(self, maxSize: int):
        self._stack = []                                # Initialise an empty list (stack)
        self._size = 0                                  # Initialise a size-counter
        self._capacity = maxSize                        # Store the maxSize value as stack capacity

    def push(self, x: int) -> None:
        if self._size == self._capacity:                # Check if the stack is full
            return                                      # Return None
        self._stack.append(x)                           # Insert the element in the stack
        self._size += 1                                 # Increment the size-counter

    def pop(self) -> int:
        if not self._size:                              # Check if the stack is empty
            return -1                                   # Return -1
        self._size -= 1                                 # Decrement the size-counter
        return self._stack.pop()                        # Remove and return the top-element

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self._size)):             # Iterate through the provided range
            self._stack[i] += val                       # Increment the stack elements by the provided value


# Optimised Solution (Lazy Increment)
class CustomStackOP:

    def __init__(self, maxSize: int):
        self.stack = []                                 # Initialise an empty list (stack)
        self.maxSize = maxSize                          # Store stack's maxSize
        self.inc = []                                   # Initialise an empty list (increments)

    def push(self, x: int) -> None:
        if len(self.stack) == self.maxSize:             # Check if stack is full
            return
        self.stack.append(x)                            # Insert the element is the stack
        self.inc.append(0)                              # Append zero in the increment list

    def pop(self) -> int:
        if len(self.stack) == 0:                        # Check if the stack is empty
            return -1                                   # Return -1
        if len(self.inc) > 1:                           # Check if there are more than 1 element in the stack
            self.inc[-2] += self.inc[-1]                # Increment the 2nd-last element of the stack by the given value
        return self.stack.pop() + self.inc.pop()        # Pop and sum the elements from stack and increment lists

    def increment(self, k: int, val: int) -> None:
        k = min(k, len(self.stack))                     # Obtain the minimum value between stack-size and given range
        if k == 0:                                      # Check if range is zero
            return                                      # Return None
        self.inc[k - 1] += val                          # Increment the last element of increment-list by given value
