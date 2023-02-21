# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        oddhead = head
        dummyHead = ListNode()
        headNode = head.next
        evenHead = headNode
        
        while oddhead and oddhead.next:
            nextEven = oddhead.next
            oddhead.next = oddhead.next.next
            if oddhead.next:
                oddhead = oddhead.next
            
            evenHead.next = nextEven
            evenHead = evenHead.next
            
        evenHead.next = None
        oddhead.next = headNode
        
        return head
        
        
        