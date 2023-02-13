class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        visitedNum = {}
        
        if len(nums) == 1:
            return nums[0]
        
        for num in set(nums):
            visitedNum[num] = 0
                
        left, right = 0, 1
        visitedNum[nums[left]] += 1
        
        ans = 0        
        while right < len(nums):
            if visitedNum[nums[right]] == 0:
                visitedNum[nums[right]] += 1
                right += 1
                
                if right == len(nums):
                    if ans < sum(nums[left:right]):
                        ans = sum(nums[left:right])
            
            else:
                if ans < sum(nums[left:right]):
                    ans = sum(nums[left:right])
                
                while visitedNum[nums[right]] != 0:
                    visitedNum[nums[left]] -= 1
                    left += 1
        
        return ans