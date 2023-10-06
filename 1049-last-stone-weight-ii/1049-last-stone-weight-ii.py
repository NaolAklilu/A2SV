class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        totalSum = sum(stones)
        halfSum = ceil(totalSum/2)
        self.curHalf = float(inf)
        
        @cache
        def dfs(i, curSum):
            if curSum >= halfSum:
                if abs(halfSum - curSum) < abs(halfSum - self.curHalf):
                    self.curHalf = curSum
            
            if i == len(stones):
                return
                       
            dfs(i+1, curSum+stones[i])
            dfs(i+1, curSum)
            
        dfs(0, 0)
        
        half1 = self.curHalf
        half2 = totalSum - self.curHalf
        return abs(half2 - half1)
            
            
            
            
        