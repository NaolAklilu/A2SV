class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjacents = defaultdict(list)
        indegree = defaultdict(int)
        visited = set()
        
        for left, right in adjacentPairs:
            adjacents[left].append(right)
            adjacents[right].append(left)
            
            indegree[left] += 1
            indegree[right] += 1
        
        queue = deque()
        for node in adjacents.keys():
            if indegree[node] == 1:
                visited.add(node)
                queue.append(node)
                break
        
        ans = [] 
        while queue:
            node = queue.popleft()
            ans.append(node)

            for neighbor in adjacents[node]:
                indegree[neighbor] -= 1
                
                if neighbor not in visited and indegree[neighbor] <= 1:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return ans
            