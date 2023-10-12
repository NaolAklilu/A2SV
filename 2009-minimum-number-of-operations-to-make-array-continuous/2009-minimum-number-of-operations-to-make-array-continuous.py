class Solution:
    def minOperations(self, nums: List[int]) -> int:
        duplicateCount = 0
        nums.sort()
        numsCopy = []
        for num in nums:
            if numsCopy:
                if num == numsCopy[-1]:
                    continue
                else:
                    numsCopy.append(num)
                    
            else:
                numsCopy.append(num)
                
        left = 0
        right = 0
        m = len(nums)-1
        
        minCount = float('inf')
        count = 0
        while right < len(numsCopy):
            curLeft = numsCopy[left]
            curMax   = numsCopy[left] + m
            
            while right < len(numsCopy) and numsCopy[right] <= curMax:
                count += 1
                right += 1
                
            minCount = min(minCount, (m+1-count))
            count -= 1
            left += 1
            if right == len(numsCopy):
                break
                  
        return minCount
            
                
            
        
            