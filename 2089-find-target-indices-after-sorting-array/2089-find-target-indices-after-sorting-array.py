class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        indices = []
        
        maxNum = max(nums)
        temp = [0] * (maxNum+1)
        
        for num in nums:
            temp[num] += 1
        
        numsList = []
        for i in range(len(temp)):
            if temp[i] > 0:
                while temp[i] != 0:
                    numsList.append(i)
                    temp[i] -= 1
        
        
        for i in range(len(numsList)):
            if numsList[i] == target:
                indices.append(i)
        
        return indices
        
        