class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        memo = {}
        
        def dfs(index, time):
            if index == len(satisfaction):
                return 0
            
            if (index, time) not in memo:
                memo[(index, time)] = max(dfs(index+1, time), (time+1)*satisfaction[index] + dfs(index+1, time+1))
                
            return memo[(index, time)]
        
        return dfs(0, 0)