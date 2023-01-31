# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:      
        if head == None or head.next == None:
            return head
        nextNode = head.next
        head.next = self.swapPairs(nextNode.next)
        nextNode.next = head

        return nextNode
        