class Solution:
    def racecar(self, target: int) -> int:
        
        visited = set((0, 1))
        queue = deque([(0, 1)])
        
        count = 0
        while queue:
            count += 1
            length = len(queue)
            
            for i in range(length):
                pos, speed = queue.popleft()
                
                option = (pos+speed, speed*2)
                if option[0] == target:
                    return count
                if option not in visited:
                    if abs(option[0] - target) < target:
                        queue.append(option)
                        visited.add(option)
                        
               
                if speed > 0:
                    option = (pos, -1)
                    if option[0] == target:
                        return count
                    if option not in visited:
                        if abs(option[0] - target) < target:
                            queue.append(option)
                            visited.add(option)
                    
                else:
                    option = (pos, 1) 
                    if option[0] == target:
                        return count
                    if option not in visited:
                        if abs(option[0] - target) < target:
                            queue.append(option)
                            visited.add(option)
                        
        return count

                
                
            