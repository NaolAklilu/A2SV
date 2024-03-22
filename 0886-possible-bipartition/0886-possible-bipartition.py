class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        
        
        groups = [-1 for i in range(n)]
        groups[0] = 1
        
        graph = defaultdict(list)
        for node1, node2 in dislikes:
            graph[node1].append(node2)
            graph[node2].append(node1)
            
        visited = [False for i in range(n)]
        
        def bipartite(node):
            visited[node-1] = True
            for neighbor in graph[node]:
                if not visited[neighbor-1]:
                    groups[neighbor-1] = 1 - groups[node-1]
                    if not bipartite(neighbor):
                        return False
                else:
                    if groups[neighbor-1] == groups[node-1]:
                        return False
            return True
        
        for i in range(1,n+1):
            if not visited[i-1]:
                if not bipartite(i):
                    return False
            
        return True
        