# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        dummyNode = dummyHead
        
        ptr1 = l1
        ptr2 = l2
        rem = 0
        while ptr1 and ptr2:
            curSum = ptr1.val + ptr2.val + rem
            if curSum > 9:
                quo = int(str(curSum)[1])
                rem = int(str(curSum)[0])
                
                dummyNode.next = ListNode(quo)                
            else:
                dummyNode.next = ListNode(curSum)
                rem = 0
                
            dummyNode = dummyNode.next
                
            ptr1 = ptr1.next
            ptr2 = ptr2.next
                
        while ptr1:
            curSum = ptr1.val + rem
            if curSum > 9:
                quo = int(str(curSum)[1])
                rem = int(str(curSum)[0])
                
                dummyNode.next = ListNode(quo)                
            else:
                dummyNode.next = ListNode(curSum)
                rem = 0
                
            dummyNode = dummyNode.next
            ptr1 = ptr1.next
                
        while ptr2:
            curSum = ptr2.val + rem
            if curSum > 9:
                quo = int(str(curSum)[1])
                rem = int(str(curSum)[0])
                
                dummyNode.next = ListNode(quo)                
            else:
                dummyNode.next = ListNode(curSum)
                rem = 0
             
            dummyNode = dummyNode.next
            ptr2 = ptr2.next
                
        if rem > 0:
            dummyNode.next = ListNode(rem)
            
        return dummyHead.next