class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.count = 1

class Solution:
    
    def __init__(self):
        self.root = TrieNode('.')
        
        
    def insert(self, word):
        cur = self.root
        
        for char in word:
            if char not in cur.children:
                newNode = TrieNode(char)
                cur.children[char] = newNode
            else:
                curNode = cur.children[char]
                curNode.count += 1
            
            cur = cur.children[char]
            
        
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        for word in words:
            self.insert(word)
        
        ans = []
        
        for word in words:
            cur = self.root
            count = 0
            for char in word:
                cur = cur.children[char]
                count += cur.count
            
            ans.append(count)
            
        return ans
            
            
        
            
            