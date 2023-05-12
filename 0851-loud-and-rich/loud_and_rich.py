class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        indegree = defaultdict(int)
        graph = defaultdict(list)
        answer = [ i for i in range(len(quiet))]
        
        for rich, poor in richer:
            graph[rich].append(poor)
            indegree[poor] += 1
           
        queue = deque()
        for i in range(len(quiet)):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            rich = queue.popleft()
            
            for neighbor in graph[rich]:
                indegree[neighbor] -= 1
               
                if quiet[rich] < quiet[answer[neighbor]]:
                    answer[neighbor] = rich

                if quiet[answer[rich]] < quiet[answer[neighbor]]:
                    answer[neighbor] = answer[rich]

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        for i in range(len(quiet)):
            if answer[i] == -1:
                answer[i] = quiet[i]
                
        return answer
