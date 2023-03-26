# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        prevNode = None
        isLeftVisited = False
        curNode = head
        
        for i in range(right):
            if i == left - 1:
                leftNode = prevNode
                startNode= curNode
                isLeftVisited = True
                
            
            if isLeftVisited:
                forwardNode = curNode.next
                curNode.next = prevNode
                prevNode = curNode
                if i != right-1:
                    curNode = forwardNode
                
            else:
                prevNode = curNode
                curNode = curNode.next
                forwardNode = curNode.next
                
        startNode.next = forwardNode
        if not leftNode:
            return curNode
        
        leftNode.next = curNode
        return head