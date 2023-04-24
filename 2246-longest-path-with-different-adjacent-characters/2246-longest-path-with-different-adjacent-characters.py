class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        self.maxCount = 0
        visited = [0 for i in range(len(parent))]
        
        graph = defaultdict(list)
        for i in range(1, len(parent)):
            graph[i].append(parent[i])
            graph[parent[i]].append(i)
        
        def findPath(node):
            visited[node] = 1
            
            count = 1
            
            neighborChildCount = []
            for neighbor in graph[node]:
                if visited[neighbor] == 0:
                    if s[neighbor] != s[node]:
                        curCount = findPath(neighbor)
                        neighborChildCount.append(curCount)
                    
                    else:
                        curCount = findPath(neighbor)
                        self.maxCount = max(curCount, self.maxCount)           
            
            if len(neighborChildCount) > 1:
                neighborChildCount.sort()
                curMax = neighborChildCount[-1] + neighborChildCount[-2] + 1
                self.maxCount = max(curMax, self.maxCount)
                return neighborChildCount[-1]+1
            elif len(neighborChildCount) == 1:
                self.maxCount = max(neighborChildCount[-1]+1, self.maxCount)
                return neighborChildCount[-1]+1
            else:
                self.maxCount = max(count, self.maxCount)
                return count
        
        findPath(0)
                
        return self.maxCount
        
        
        
            