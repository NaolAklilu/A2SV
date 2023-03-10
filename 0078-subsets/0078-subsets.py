class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()
        def helper(cur, index):
            if index == len(nums):
                return
            
            for i in range(index , len(nums)):
                temp = cur[:]
                if temp and nums[i] > temp[-1]:
                    temp.append(nums[i])
                    res.append(temp)
                    helper(temp, index+1)
                    
                elif not temp:
                    temp.append(nums[i])
                    res.append(temp)
                    helper(temp, index+1)
                
        
        helper([], 0)
        
        return res
                
        