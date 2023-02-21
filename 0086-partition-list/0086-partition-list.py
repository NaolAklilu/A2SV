# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1Head = ListNode()
        dummy2Head = ListNode()
        
        dummy1Node = dummy1Head
        dummy2Node = dummy2Head
        
        while head:
            if head.val < x:
                dummy1Node.next = head
                dummy1Node = dummy1Node.next
            else:
                dummy2Node.next = head
                dummy2Node = dummy2Node.next
                
            head = head.next
        
        dummy2Node.next = None
        dummy1Node.next = dummy2Head.next

        return dummy1Head.next