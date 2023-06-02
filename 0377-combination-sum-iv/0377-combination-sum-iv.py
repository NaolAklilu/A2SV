class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memo = { i: 0 for i in range(1, target+1)}
        
        for curTarget in range(1, target+1):
            for num in nums:
                if curTarget-num == 0:
                    memo[curTarget] += 1
                elif curTarget-num > 0:
                    memo[curTarget] += memo[curTarget-num]
                    
        return memo[target]
        
        