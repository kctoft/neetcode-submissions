# Create Node class (single pointer)
class ListNode:
    def __init__(self, value, next_node=None):
        self.val = value
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        # singly linked list
        self.head = ListNode(-1) # dummy node
        self.tail = self.head

    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        # traverse through the list
        while curr:
            # found a match
            if i == index:
                return curr.val
            # increment and update pointer
            i += 1
            curr = curr.next
        # no match
        return -1


    def insertHead(self, val: int) -> None:
        # create new node to insert at head
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node

        # if list is empty, add the first node
        if not new_node.next:
            self.tail = new_node
        

    def insertTail(self, val: int) -> None:
        # create a new node at the tail of the list
        self.tail.next = ListNode(val)
        self.tail = self.tail.next


    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        # continue incrementing
        while i < index and curr:
            i += 1
            curr = curr.next
        
        # skip the node (i.e., remove it)
        if curr and curr.next:
            # edge case: remove tail
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

        

    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []
        # contnue to increment while there are still nodes
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
        
