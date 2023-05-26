class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        left, right = 0, 0
        swapRight = right
        
        while right < len(arr)-1:
            if arr[right] <= arr[right+1]:
                right += 1
                if arr[right] != arr[right-1] and arr[left] > arr[right]:
                    swapRight = right
            
            else:
                left = right
                right += 1
                swapRight = right
                
        if arr[left] > arr[swapRight]:
            arr[left], arr[swapRight] = arr[swapRight], arr[left]
            
        return arr
        
        
            
        