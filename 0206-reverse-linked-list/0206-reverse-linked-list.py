# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        current_node = head
        previous_node = None
        nextNode = current_node.next
        
        while current_node != None:
            current_node.next = previous_node
            previous_node = current_node
            current_node = nextNode
            
            if nextNode != None:
                nextNode = nextNode.next
                
        return previous_node