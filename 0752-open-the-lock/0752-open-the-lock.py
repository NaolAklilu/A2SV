class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        directions = [-1, 1]
        if '0000' in deadends:
            return -1
        
        if '0000' == target:
            return 0
        
        queue = deque([[0,0,0,0]])
        count = 0
        visited = set()
        
        while queue:
            count += 1
            length = len(queue)
            
            for _ in range(length):
                state = queue.popleft()
                for i in range(4):
                    for dir in directions:
                        curState = state[:]
                        curState[i] = (curState[i]+dir)%10
                        string = []
                        for j in range(4):
                            string.append(str(curState[j]))
                            
                        if "".join(string) == target:
                            return count
                                          
                        if "".join(string) not in deadends and  "".join(string)  not in visited:
                            queue.append(curState)
                            visited.add( "".join(string) )
                            
        return -1 
        
        
        
        