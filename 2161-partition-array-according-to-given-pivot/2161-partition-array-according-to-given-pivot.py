class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        greaterNums = []
        newNums = []
        
        pivotCount = 0
        for num in nums:
            if num < pivot:
                newNums.append(num)
            elif num == pivot:
                pivotCount += 1
            else:
                greaterNums.append(num)
                
        newNums.extend([pivot] * pivotCount)
        newNums.extend(greaterNums)
        
        return newNums