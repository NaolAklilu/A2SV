class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dic = {}
        nums += nums
        
        for i in range(len(nums)):
            dic[i] = -1
            
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                dic[stack[-1]] = nums[i]
                stack.pop()
                
            stack.append(i)
            
            
        res = []
        for i in range(n):
            res.append(dic[i])
                
        return res
            
            