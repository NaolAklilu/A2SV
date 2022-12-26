class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winnerCount = {}
        loserCount = {}
        answer = [[], []]
        
        for match in matches:
            if match[0] in winnerCount.keys():
                winnerCount[match[0]] += 1
            else:
                winnerCount[match[0]] = 1
                
            if match[1] in loserCount.keys():
                loserCount[match[1]] += 1
            else:
                loserCount[match[1]] = 1
                
        for winner in winnerCount:
            if winner not in loserCount:
                answer[0].append(winner)
        
        for loser in loserCount:
            if loserCount[loser] == 1:
                answer[1].append(loser) 
         
        for lst in answer:
            lst.sort()
            
        return answer
