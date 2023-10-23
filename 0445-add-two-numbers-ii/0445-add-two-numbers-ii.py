# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []
        
        curHead = l1
        while curHead:
            stack1.append(curHead.val)
            curHead = curHead.next
            
        curHead = l2
        while curHead:
            stack2.append(curHead.val)
            curHead = curHead.next
           
        
        result = []
        rem = 0
        while stack1 and stack2:
            curDigit = rem
            curDigit += stack1.pop()
            curDigit += stack2.pop()
            
            result.append(curDigit%10)
            rem = curDigit//10
            
        if stack1:
            while stack1:
                curDigit = rem
                curDigit += stack1.pop()
                result.append(curDigit%10)
                rem = curDigit//10
        
        if stack2:
            while stack2:
                curDigit = rem
                curDigit += stack2.pop()
                result.append(curDigit%10)
                rem = curDigit//10
                
        if rem != 0:
            result.append(rem)
        
        head = ListNode()
        curHead = head
        while result:
            newNode = ListNode(result.pop())
            curHead.next = newNode
            curHead = curHead.next
        
        return head.next