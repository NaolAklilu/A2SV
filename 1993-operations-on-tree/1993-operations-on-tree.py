class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.visited = {}
        self.graph = defaultdict(list)
        for i in range(1, len(parent)):
            self.graph[parent[i]].append(i)

    def lock(self, num: int, user: int) -> bool:
        if num not in self.visited:
            self.visited[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if num in self.visited and self.visited[num] == user:
            self.visited.pop(num)
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        curNum = num
        while curNum != -1:
            if self.parent[curNum] not in self.visited:
                curNum = self.parent[curNum]
            else:
                return False
        
        if num in self.visited:
            return False
        
        decendants = set()
        visited = set()
        self.lockedCount = 0
        def dfs(node):
            visited.add(node)
                            
            for decendant in self.graph[node]:
                if decendant not in visited:
                    decendants.add(decendant)
                    if decendant != num and decendant in self.visited:
                        self.lockedCount += 1
                    
                    dfs(decendant)
                    
            return
        
        dfs(num)
        
        if self.lockedCount == 0:
            return False
        self.visited[num] = user
        for n in decendants:
            if n in self.visited:
                self.visited.pop(n)
        
        return True
        
        
            


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)