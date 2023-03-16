class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        stack = []
        minPtr = -1
        for index in range(len(nums)-1, -1, -1):
            if minPtr != -1 and nums[minPtr] > nums[index]:
                return True
            
            while stack and nums[stack[-1]] < nums[index]:
                minPtr = stack.pop()
                
            stack.append(index)
            
            
        return False