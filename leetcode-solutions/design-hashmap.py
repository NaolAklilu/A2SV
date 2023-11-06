class Node:
    def __init__(self, key=-1,val = -1):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class MyHashMap:

    def __init__(self):
        self.head = Node()

    def put(self, key: int, value: int) -> None:
        curHead = self.head
        
        while curHead.next:
            if curHead.key == key:
                break
                
            curHead = curHead.next
        
        if curHead.key == key:
            curHead.val = value
        else:
            newNode = Node(key, value)
            curHead.next = newNode
            newNode.prev = curHead

    def get(self, key: int) -> int:
        curHead = self.head
        
        while curHead:
            if curHead.key == key:
                return curHead.val
            curHead = curHead.next
            
        return -1
        

    def remove(self, key: int) -> None:
        curHead = self.head
        
        while curHead:
            if curHead.key == key:
                leftNode = curHead.prev
                if leftNode == None:
                    if curHead.next != None:
                        self.head = curHead.next
                    else:
                        self.head = Node()
                else:
                    nextNode = curHead.next
                    leftNode.next = nextNode
                    if nextNode != None:
                        nextNode.prev = leftNode
            
            curHead = curHead.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


