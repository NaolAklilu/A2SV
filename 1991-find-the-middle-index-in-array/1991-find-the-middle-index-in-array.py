class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        leftPrefix = [0]*len(nums)
        rightPrefix = [0]*len(nums)
        
        for i in range(1, len(nums)):
            leftPrefix[i] = leftPrefix[i-1] + nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            rightPrefix[i] = rightPrefix[i+1] + nums[i+1]
        
        for i in range(len(nums)):
            if leftPrefix[i] == rightPrefix[i]:
                return i
        return -1