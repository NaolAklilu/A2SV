class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        binary_sum = defaultdict(int)
        
        prefixSum = 0
        goalCount = 0
        for i in range(len(nums)):
            prefixSum += nums[i]
            
            if prefixSum == goal:
                goalCount += 1
                
            if prefixSum - goal in binary_sum:
                goalCount += binary_sum[prefixSum - goal]
                
            binary_sum[prefixSum] += 1
            
        return goalCount
         