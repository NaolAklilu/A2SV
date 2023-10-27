class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        prefSet, sufSet = set(), set()
        
        for i in range(len(nums)):
            prefSet.add(nums[i])
            prefix[i] = len(prefSet)
            
        
        for i in range(len(nums)-1, -1, -1):
            suffix[i] = len(sufSet)
            sufSet.add(nums[i])
        
        result = []
        for i in range(len(nums)):
            result.append(prefix[i] - suffix[i])
        
        return result