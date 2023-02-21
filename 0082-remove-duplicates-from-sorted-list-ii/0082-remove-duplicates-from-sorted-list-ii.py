# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curNode = head
        dummyHead = ListNode()
        dummyHead.next = curNode
        
        dummyNode = dummyHead
        while curNode:
            if curNode.next and curNode.val == curNode.next.val:
                while curNode.next and curNode.val == curNode.next.val:
                    curNode = curNode.next
                
                dummyNode.next = curNode.next
                curNode = curNode.next
                
            else:
                dummyNode = dummyNode.next
                curNode = curNode.next
            
        return dummyHead.next
                