class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []
        
        def dp(index, curAmount, curNums):
            curNums = curNums[:]
            if index == len(candidates):
                if curAmount == 0:
                    if curNums not in results:
                        results.append(curNums)
                        
                return
            
            notTake = dp(index+1, curAmount, curNums)
            if candidates[index] <= curAmount:
                curNums.append(candidates[index])
                dp(index, curAmount-candidates[index], curNums)
                curNums.pop()
            
            return 
        
        dp(0, target, [])
        
        return results
                
            