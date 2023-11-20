class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        graph = {}
        
        for winner, loser in matches:
            if winner in graph:
                graph[winner][0] += 1
            else:
                graph[winner] = [1, 0]
            
            if loser in graph:
                graph[loser][1] += 1
            else:
                graph[loser] = [0, 1]
        
        winners = set()
        losers = set()
        
        for player in graph:
            if graph[player][1] == 0:
                winners.add(player)
            
            if graph[player][1] == 1:
                losers.add(player)
            
        return [sorted(list(winners)), sorted(list(losers))]