# Create a Node class
class Node:
    # Node init method
    def __init__(self, value: int):
        self.value = value # value of the node
        self.prev = None # left pointer
        self.next = None # right pointer



class Deque:
    # Initialize the empty queue with dummpy pointers
    def __init__(self):
        # initialize the stack
        self.head = None # head - left end
        self.tail = None # tail - right end
        self.size = 0


    def isEmpty(self) -> bool:
        # empty if the head is null/None
        return self.head is None
        
    # void append(int value) will insert value at
    # the end of the queue
    def append(self, value: int) -> None:
        # Create a new node
        new_node = Node(value)

        # case 1: adding to an empty queue
        if self.isEmpty():
            self.head = self.tail = new_node
        # case 2: add to the new node to the rear
        else:
            # update the pointers
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        # increment size of queue by 1
        self.size +=1

    # void appendleft(int val) will insert value at 
    # the beginning of the queue.
    def appendleft(self, value: int) -> None:
        # Create a new node
        new_node = Node(value)

        # case 1: adding to the empty queue (from the left)
        if self.isEmpty():
            self.head = self.tail = new_node
        
        # Adding at the head of the queue
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        # increment size of queue by 1
        self.size +=1

    # int pop() will remove and return the value at the end of
    # the queue. If the queue is empty, return -1
    def pop(self) -> int:
        # edge case: return -1 if the queue is empty
        if self.isEmpty():
            return -1
        
        # remove the value at the end of the queue, return that value
        value = self.tail.value
        # case: single node in queue
        if self.head is self.tail:
            self.head = self.tail = None
        # case: >1+ nodes in queue
        else:
            # remove the end
            self.tail = self.tail.prev
            self.tail.next = None
        # decrement by 1 & return the value
        self.size -= 1
        return value

    # int popleft() will remove and return the value at the beginning of
    # the queue. If the queue is empty, return -1
    def popleft(self) -> int:
        # edge case: return -1 if the queue is empty
        if self.isEmpty():
            return -1

        value = self.head.value
        # case: sinle node queue
        if self.head is self.tail:
            self.head = self.tail = None
        # case: queue >1+
        else:
            self.head = self.head.next
            self.head.prev = None
        # decrement by 1 & return the value
        self.size -= 1
        return value
