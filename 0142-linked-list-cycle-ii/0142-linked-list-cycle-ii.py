# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fastNode = head
        slowNode = head
        
        headNode = head
        
        while fastNode and fastNode.next:
            fastNode = fastNode.next.next
            slowNode = slowNode.next
            
            if fastNode == slowNode:
                while fastNode != headNode:
                    fastNode = fastNode.next
                    headNode = headNode.next
                    
                return headNode
            
        return None