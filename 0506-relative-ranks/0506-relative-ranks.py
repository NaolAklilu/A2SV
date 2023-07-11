class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        temp = []
        ans = []
        for i in range(len(score)):
            ans.append("0")
            
        dic = {}
        for i in range(len(score)):
            dic[score[i]] = i
            score[i] = -1*score[i]
            
    
        while score:
            heapify(score)
            num = -1*heappop(score)
            if len(temp) == 0:
                ans[dic[num]] = "Gold Medal"
            elif len(temp) == 1:
                ans[dic[num]] = "Silver Medal"
            elif len(temp) == 2:
                ans[dic[num]] = "Bronze Medal"
            else:
                ans[dic[num]] = str(len(temp)+1)
                
            temp.append(num)
        
        return ans