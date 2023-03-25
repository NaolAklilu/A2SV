# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nextGreater = defaultdict(int)
        
        temp = head
        stack = []
        values= []
        index = 0
        while temp:
            while stack and values[stack[-1]] < temp.val:
                nextGreater[stack[-1]] = temp.val
                stack.pop()
                
            stack.append(index)
            values.append(temp.val)
            temp = temp.next
            index += 1
            
        while stack:
            nextGreater[stack.pop()] = 0 
        
        ans = [0]*len(nextGreater)
        for num in nextGreater:
            ans[num] = nextGreater[num] 
        
        return ans
                
        