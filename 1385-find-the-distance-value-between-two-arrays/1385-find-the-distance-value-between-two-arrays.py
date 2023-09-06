class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        
        for num1 in arr1:
            innerCount = 0
            for num2 in arr2:
                if abs(num1-num2) <= d:
                    innerCount += 1
            
            if innerCount == 0:
                count += 1
                
        return count