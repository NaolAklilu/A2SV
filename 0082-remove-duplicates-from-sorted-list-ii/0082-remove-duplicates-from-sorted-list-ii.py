# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fakeNode = ListNode()
        fakeNode.next = head
        
        cur = fakeNode
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                cur.next = head.next
            else:
                cur = cur.next
                
            head = head.next
                
        return fakeNode.next