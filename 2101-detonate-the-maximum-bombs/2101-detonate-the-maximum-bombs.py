class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        def detonate(bomb, graph,visited):
            visited.add(bomb)
            count = 1
            
            for neighbor in graph[bomb]:
                if neighbor not in visited:
                    count += detonate(neighbor, graph, visited)
                
            return count
        
        bombDic = {}
        for i in range(len(bombs)):
            bombDic[i+1] = bombs[i]
    
        graph = defaultdict(list)
        for i in range(1, len(bombs)+1):
            for j in range(1, len(bombs)+1):
                if i != j:
                    diff = sqrt( (bombDic[i][0] - bombDic[j][0])**2 + (bombDic[i][1] - bombDic[j][1])**2)
                    if diff <= bombDic[i][2]:
                        graph[i].append(j)

        
        maxCount = 0
        for i in range(1, len(bombs)+1):
            visited = set()
            curCount = detonate(i, graph, visited)
            maxCount = max(curCount, maxCount)
        
        return maxCount
            
        
        
        