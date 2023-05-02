class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        def subsets(s):  
            if len(s) == 0:  
                return [[]]  
            x = subsets(s[:-1])  
            return x + [[s[-1]] + y for y in x] 

        maxBitValue = nums[0]
        
        for i in range(1, len(nums)):
            maxBitValue = maxBitValue|nums[i]
            
        count = 0
        result = subsets(nums)
        for subset in result:
            bitValue = 0
            for num in subset:
                bitValue = bitValue | num
            
            if bitValue == maxBitValue:
                count += 1
            
        return count
            
        