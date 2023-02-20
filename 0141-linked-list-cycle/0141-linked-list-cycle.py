# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fastNode = head
        slowNode = head
        
        while fastNode and fastNode.next:
            fastNode= fastNode.next.next
            slowNode= slowNode.next
            
            if fastNode == slowNode:
                return True
            
        return False
        