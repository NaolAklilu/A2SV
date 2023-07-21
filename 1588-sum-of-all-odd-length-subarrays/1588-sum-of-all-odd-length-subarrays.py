class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        left, right = 0, 0
        total = 0
        
        while left < len(arr):
            if right < len(arr):
                if (right-left+1)%2 != 0:
                    total += sum(arr[left:right+1])
                right += 1
                
            else:
                left += 1
                right = left
        
        return total
                