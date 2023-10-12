class Solution:
    def numTeams(self, rating: List[int]) -> int:
        dic = {}
        teamCount = 0
        
        for i in range(len(rating)-1, -1, -1):
            minCount = 0
            maxCount = 0
            
            for person in dic.keys():
                if person < rating[i]:
                    minCount += 1
                    teamCount += dic[person][0]
                else:
                    maxCount += 1
                    teamCount += dic[person][1]
                
            dic[rating[i]] = [minCount, maxCount]

        return teamCount
            
                