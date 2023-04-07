class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for source, destination in roads:
            graph[source].append(destination)
            graph[destination].append(source)
            
        maxLength = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                elif i not in graph[j]:
                    maxLength = max(maxLength, (len(graph[i]) + len(graph[j])))
                else:
                    maxLength = max(maxLength, (len(graph[i]) + len(graph[j]) - 1))
                
        return maxLength