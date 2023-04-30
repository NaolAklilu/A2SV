class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        
        visited = set()
        def findApples(branch):
            visited.add(branch)
            time = 0
            
            for neighbor in graph[branch]:
                if neighbor not in visited:
                    time += findApples(neighbor)
             
            if branch != 0:
                if time != 0:
                    time += 2

                else:
                    if hasApple[branch] == True:
                        time += 2
                
            return time
        
        result = findApples(0)
        
        return result