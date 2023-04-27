class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        queue = deque([0])
        visited = set()
        visited.add(0)
        
        while queue:
            room = queue.popleft()
            visited.add(room)
            
            for neighbor in rooms[room]:
                if neighbor not in visited:
                    queue.append(neighbor)
            
        
        for i in range(len(rooms)):
            if i not in visited:
                return False
            
        return True
            
        
        