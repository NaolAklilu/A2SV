class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:   
        if index < 0 or index >= self.size or self.size == 0:
            return -1
        
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.val
                
    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode
        self.size += 1

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        if self.size != 0:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = newNode
        else:
            self.head = newNode
        
        self.size += 1
                
    def addAtIndex(self, index: int, val: int) -> None:
        newNode = ListNode(val)
        
        if index < 0 or index > self.size:
            return
        
        if index <= self.size and index > 0:
            cur = self.head
            for i in range(index-1):
                cur = cur.next
            newNode.next = cur.next
            cur.next = newNode
            self.size += 1
        elif index == 0:
            self.addAtHead(val)
        

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head
        if index < self.size and index > 0:
            for i in range(index-1):
                cur = cur.next
            deleted_node = cur.next
            cur.next = deleted_node.next
            self.size -= 1
            
        elif index == 0:
            self.head = self.head.next
            self.size -= 1