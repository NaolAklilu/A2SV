# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        
        count = 0
        while temp:
            count += 1
            temp = temp.next
           
        if n == count:
            head = head.next
            return head
        
        i = 1
        nextNode = head
        while i < count - n:
            nextNode = nextNode.next
            i += 1

        nextNode.next = nextNode.next.next       
            
        return head
            