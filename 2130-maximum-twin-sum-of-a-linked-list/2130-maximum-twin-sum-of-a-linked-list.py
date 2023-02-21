# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dic = {}
        temp = head
        
        count = 0
        while temp:
            dic[count] = temp.val
            count += 1
            
            temp =temp.next
         
        maxSum = 0
        for i in range(count//2):
            curSum = dic[i] + dic[count-1-i]    
            
            if curSum > maxSum:
                maxSum = curSum
                
        return maxSum
            
            