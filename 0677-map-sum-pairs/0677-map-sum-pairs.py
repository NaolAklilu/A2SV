class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.score = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode('.')
        self.visited = {}

    def insert(self, key: str, val: int) -> None:
        cur = self.root
        isExist = False
        if key in self.visited:
            isExist = True
        
        for char in key:
            if char not in cur.children:
                newNode = TrieNode(char)
                newNode.score += val
                cur.children[char] = newNode
            else:
                curNode = cur.children[char]
                if isExist:
                    curNode.score -= self.visited[key]
                    curNode.score += val
                else:
                    curNode.score += val
                
            cur = cur.children[char]
        
        self.visited[key] = val

    def sum(self, prefix: str) -> int:
        cur = self.root
        
        for char in prefix:
            if char not in cur.children:
                return 0
            cur = cur.children[char]
            
        return cur.score


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)