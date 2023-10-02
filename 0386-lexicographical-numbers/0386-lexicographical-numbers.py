class TrieNode:
    
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.is_end = False
        self.number = -1

class Solution:
    
    def __init__(self):
        self.root = TrieNode(".")
        
    def insert(self, num):
        cur = self.root
        digits = list(num)
        
        for digit in digits:
            if digit not in cur.children:
                cur.children[digit] = TrieNode(digit)
            
            cur = cur.children[digit]
            
        cur.is_end = True
        cur.number = num
        
    def dfs(self, curNode, result):
        if curNode.is_end == True:
            result.append(curNode.number)
        
        for n in range(10):
            if str(n) in curNode.children:
                self.dfs(curNode.children[str(n)], result)
    
    def lexicalOrder(self, n: int) -> List[int]:
        for num in range(1, n+1):
            self.insert(str(num))
            
        cur = self.root
        result = []
        self.dfs(cur, result)
        
        return [int(num) for num in result]
        
        
            