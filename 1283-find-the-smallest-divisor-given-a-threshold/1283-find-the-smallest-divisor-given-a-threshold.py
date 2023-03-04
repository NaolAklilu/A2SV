class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def isGood(val):
            divSum = 0
            for num in nums:
                divSum += ceil(num/val)
                
            if divSum <= threshold:
                return True
            else:
                return False
            
        
        left = 0
        right = max(nums)
        
        while right > left+1:
            mid = left + (right-left)//2
            
            if isGood(mid):
                right = mid
            else:
                left = mid
                
        return right