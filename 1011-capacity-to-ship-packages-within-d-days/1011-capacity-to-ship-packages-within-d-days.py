class Solution:          
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def isGood(capacity):
            curSum = 0
            dayCount = 0
            for right in range(len(weights)):
                curSum += weights[right]
                if curSum < capacity and right == len(weights)-1:
                    dayCount += 1

                elif curSum > capacity:
                    if right == len(weights)-1:
                        dayCount += 1
                    dayCount += 1
                    curSum = weights[right]

                elif curSum == capacity:
                    dayCount += 1
                    curSum = 0
                    
            if dayCount <= days:
                return True
            else:
                return False
            
        left = max(weights)-1
        right = sum(weights)
        
        while left+1 < right:
            mid = left + (right-left)//2
            
            if isGood(mid):
                right = mid
            else:
                left = mid
        
        return right
        
   



















        