# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head
        
        tempNode = head
        count = 0
        while tempNode:
            count += 1
            tempNode = tempNode.next
        
        fastNode = head
        slowNode = head
        
        k = k%count
        
        if k == 0:
            return head
        
        i = k
        while i > 1:
            fastNode = fastNode.next
            i -= 1
            
        while fastNode.next:
            if fastNode.next.next == None:
                lastNode=slowNode
                
            fastNode = fastNode.next
            slowNode = slowNode.next
        
        lastNode.next = None
        fastNode.next = head
        head = slowNode
    
        return head