class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left = 0
        if len(arr) == 1:
            return 1
        
        maxLength1 = 1
        for right in range(1,len(arr)):
            if right%2 == 0:
                if arr[right] < arr[right-1]:
                    maxLength1 = max(maxLength1, right-left+1)
                else:
                    left = right
            
            else:
                if arr[right] > arr[right-1]:
                    maxLength1 = max(maxLength1, right-left+1)
                else:
                    left = right
                    
        maxLength2 = 1
        left = 0
        for right in range(1,len(arr)):
            if right%2 == 0:
                if arr[right] > arr[right-1]:
                    maxLength2 = max(maxLength2, right-left+1)
                else:
                    left = right
            
            else:
                if arr[right] < arr[right-1]:
                    maxLength2 = max(maxLength2, right-left+1)
                else:
                    left = right
                    
        return max(maxLength1, maxLength2)
        
        
                