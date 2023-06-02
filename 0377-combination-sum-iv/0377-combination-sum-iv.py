class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memo = { i: float(inf) for i in range(target+1)}
        
        def combination(curNum):
            if curNum == 0:
                return 1
            
            if curNum < -1:
                return 0
            
            score = 0
            for num in nums:
                if (curNum-num) >= 0 and memo[(curNum-num)] != float(inf):
                    score += memo[(curNum-num)]
                
                else:
                    curValue = combination(curNum-num)
                    if curValue != float(inf):
                        score += curValue
                        
            memo[curNum] = score
            
            return memo[curNum]
        
        return combination(target)