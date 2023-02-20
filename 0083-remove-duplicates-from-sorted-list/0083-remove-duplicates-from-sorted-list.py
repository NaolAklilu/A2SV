# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slowNode = head
        fastNode = head
        while fastNode:
            if slowNode != fastNode and slowNode.val != fastNode.val:
                slowNode = fastNode
            
            else:
                slowNode.next = fastNode.next 
            
            fastNode = fastNode.next
            
        return head
                
            
            
            