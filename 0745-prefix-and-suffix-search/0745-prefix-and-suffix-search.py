class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.words = []

class WordFilter:

    def __init__(self, words: List[str]):
        self.frontRoot = TrieNode('.')
        self.backRoot = TrieNode('.')
        
        for i in range(len(words)-1, -1, -1):
            self.insertFront(words[i], i)
        
        for j in range(len(words)-1, -1, -1):
            self.insertBack(words[j], j)
        
    
    def insertFront(self, word, index):
        cur = self.frontRoot
        
        for char in word:
            if char not in cur.children:
                newNode = TrieNode(char)
                newNode.words.append(index)
                cur.children[char] = newNode
            else:
                curNode = cur.children[char]
                curNode.words.append(index)

            cur = cur.children[char]
            
    def insertBack(self, word, index):
        cur = self.backRoot
        
        for i in range(len(word)-1, -1, -1):
            char = word[i]
            if char not in cur.children:
                newNode = TrieNode(char)
                newNode.words.append(index)
                cur.children[char] = newNode
            else:
                curNode = cur.children[char]
                curNode.words.append(index)
            
            cur = cur.children[char]
    

    def f(self, pref: str, suff: str) -> int:
        fronts = []
        backs = set()
        curFront = self.frontRoot
        for char in pref:
            if char in curFront.children:
                curFront = curFront.children[char]
            else:
                return -1
            
        fronts = curFront.words
        
        curBack = self.backRoot
        for char in reversed(suff):
            if char in curBack.children:
                curBack = curBack.children[char]
            else:
                return -1
        
        backs = set(curBack.words)

        for index in fronts:
            if index in backs:
                return index
            
        return -1
        
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)