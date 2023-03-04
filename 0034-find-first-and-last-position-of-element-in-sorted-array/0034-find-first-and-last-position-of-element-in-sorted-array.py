class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        
        isFound = False
        for i in range(len(nums)):
            if nums[i] == target:
                if isFound:
                    res[1] = i
                else:
                    res[0] = i
                    res[1] = i
                    isFound = True
             
        return res