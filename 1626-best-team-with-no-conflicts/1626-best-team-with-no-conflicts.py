class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pair = [[scores[i], ages[i]] for i in range(len(scores))]
        pair.sort()
        memo = [pair[i][0] for i in range(len(pair))]
        
        for i in range(len(pair)):
            curScore, curAge = pair[i]
            for j in range(i):
                score, age = pair[j]
                if curAge >= age:
                    memo[i] = max(memo[i], curScore+memo[j])
                
        return max(memo)
        
        
                    
                
        
                
            
        
        