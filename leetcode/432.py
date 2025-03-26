"""
432. All O`one Data Structure [HARD]

Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:

- AllOne() Initializes the object of the data structure.
- inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it
  with count 1.
- dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it
  from the data structure. It is guaranteed that key exists in the data structure before the decrement.
- getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
- getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".

Note that each function must run in O(1) average time complexity.


Example 1:

Input:
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
Output:
[null, null, null, "hello", "hello", null, "hello", "leet"]

Explanation:
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "hello"
allOne.inc("leet");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "leet"


Constraints:

    -> 1 <= key.length <= 10
    -> key consists of lowercase English letters.
    -> It is guaranteed that for each call to dec, key is existing in the data structure.
    -> At most 5 * 104 calls will be made to inc, dec, getMaxKey, and getMinKey.


Concepts: Custom Data-Structure, Hashmap, Doubly-LL
"""
from collections import defaultdict


class Node(object):
    def __init__(self):
        self.key_set = set([])                              # Initialise a hashmap, w/ count as index for BoW
        self.prev, self.nxt = None, None                    # Initialise 2 pointers for doubly linked-list

    def add_key(self, key):
        self.key_set.add(key)                               # Append the string-length key into the hashmap

    def remove_key(self, key):
        self.key_set.remove(key)                            # Remove the string-length key from the hashmap

    def get_any_key(self):
        if self.key_set:                                    # Check if hashmap is non-empty
            result = self.key_set.pop()                     # Pop a random element from the hashmap
            self.add_key(result)                            # Add the element back into the hashmap
            return result                                   # Return the element
        else:
            return None                                     # Return None

    def count(self):
        return len(self.key_set)                            # Return the size of the hashmap

    def is_empty(self):
        return len(self.key_set) == 0                       # Return whether the hashmap is empty


class DoubleLinkedList(object):
    def __init__(self):
        self.head_node, self.tail_node = Node(), Node()     # Initialise the head and tail node
        self.head_node.nxt = self.tail_node                 # Set the next pointer for head to the tail node
        self.tail_node.prev = self.head_node                # Set the prev pointer for tail to the head node
        return

    def insert_after(self, x):
        node, temp = Node(), x.nxt                          # Initialise new node and obtain node from the next pointer
        x.nxt, node.prev = node, x                          # Link the new node ahead of the input-node
        node.nxt, temp.prev = temp, node                    # Link the stored node ahead of the new node
        return node                                         # Return the new (center) node

    def insert_before(self, x):
        return self.insert_after(x.prev)                    # Insert the element before the current node

    def remove(self, x):
        prev_node = x.prev                                  # Store the linked previous node
        prev_node.nxt, x.nxt.prev = x.nxt, prev_node        # Link the previous node with the next of current node
        return

    def get_head(self):
        return self.head_node.nxt                           # Return the head node

    def get_tail(self):
        return self.tail_node.prev                          # Return the tail node

    def get_sentinel_head(self):
        return self.head_node                               # Return the "main" head

    def get_sentinel_tail(self):
        return self.tail_node                               # Return the "main" tail


class AllOne(object):
    def __init__(self):
        self.dll = DoubleLinkedList()                       # Initialise the Doubly-LL
        self.key_counter = defaultdict(int)                 # Initialise the string-hashmap
        self.node_freq = {0: self.dll.get_sentinel_head()}  # Initialise the frequency-hashmap

    def _rmv_key_pf_node(self, pf, key):
        node = self.node_freq[pf]                           # Obtain node for (prev-)freq of key
        node.remove_key(key)                                # Remove the key from within the hashmap of node
        if node.is_empty():                                 # Check if the node's hashmap is empty
            self.dll.remove(node)                           # Remove the node from the DLL
            self.node_freq.pop(pf)                          # Remove the freq-key from the node hashmap
        return

    def inc(self, key):
        self.key_counter[key] += 1                          # Increment key count
        cf = self.key_counter[key]                          # Obtain current key-frequency
        pf = self.key_counter[key] - 1                      # Obtain previous key-frequency
        if cf not in self.node_freq:                        # Check if curr-freq not in node-freq hashmap
            self.node_freq[cf] = (
                self.dll.insert_after(self.node_freq[pf]))  # Insert new node in DLL for curr-freq
        self.node_freq[cf].add_key(key)                     # Add the key to the hashset of curr-freq node
        if pf > 0:                                          # Check if the prev-freq was non-zero
            self._rmv_key_pf_node(pf, key)                  # Remove the key from hashset of prev-freq hashset

    def dec(self, key):
        if key in self.key_counter:                         # Check if key is present in the frequency hashset
            self.key_counter[key] -= 1                      # Decrement the frequency of key
            cf = self.key_counter[key]                      # Get the current key-frequency
            pf = self.key_counter[key] + 1                  # Get the previous key-frequency
            if self.key_counter[key] == 0:                  # If the curr-freq is zero
                self.key_counter.pop(key)                   # Remove the key from the frequency hashset
            if cf != 0:                                     # If the curr-freq is non-zero
                if cf not in self.node_freq:                # Check if curr-freq key is in node-hashset
                    self.node_freq[cf] = self.dll.insert_before(self.node_freq[pf])     # Inset new node before
                self.node_freq[cf].add_key(key)             # Add the key to the corresponding node's hashset
            self._rmv_key_pf_node(pf, key)                  # Remove the key from the hashset of the prev-node

    def getMaxKey(self):
        return self.dll.get_tail().get_any_key() \
            if self.dll.get_tail().count() > 0 else ""      # Return any key from the end node is elements in the node

    def getMinKey(self):
        return self.dll.get_head().get_any_key() \
            if self.dll.get_tail().count() > 0 else ""      # Return any key from the start node is elements in the node
