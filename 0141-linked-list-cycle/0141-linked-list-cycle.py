# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        storeSet = set()
        curNode = head
        
        while curNode:
            if curNode in storeSet:
                return True
            storeSet.add(curNode)
            curNode = curNode.next
            
        return False
        