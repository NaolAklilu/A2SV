class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None] * 26

class Trie:

    def __init__(self):
        self.base = ord('a')
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        
        for i in range(len(word)):
            char = word[i]
            index = ord(char) - self.base
            
            if not cur.children[index]:
                newNode = TrieNode()
                cur.children[index] = newNode
                
            cur = cur.children[index]
        
        cur.is_end = True
                
    def search(self, word: str) -> bool:
        cur = self.root
        
        for char in word:
            index = ord(char) - self.base
            
            if not cur.children[index]:
                return False
            
            cur = cur.children[index]
        
        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        
        for char in prefix:
            index = ord(char) - self.base
            
            if cur.children[index] == None:
                return False
            
            cur = cur.children[index]
            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)