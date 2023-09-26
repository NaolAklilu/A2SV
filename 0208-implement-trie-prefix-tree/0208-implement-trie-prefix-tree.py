class TrieNode:
    def __init__(self, val):
        self.val = val
        self.is_end = False
        self.children = [None for _ in range(26)]

class Trie:

    def __init__(self):
        self.root = TrieNode('.')

    def insert(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            index = ord(word[i])-ord('a')
            if cur.children[index] == None:
                if i == len(word)-1:
                    newNode = TrieNode(word[i])
                    newNode.is_end = True
                    cur.children[index] = newNode
                else:
                    cur.children[index] = TrieNode(word[i])
            else:
                if i == len(word) - 1:
                    curNode = cur.children[index]
                    curNode.is_end = True
            
            cur = cur.children[index] 
            

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            index = ord(char) - ord('a')
                        
            if cur.children[index] == None:
                return False
            
            cur = cur.children[index]
            
        if cur.is_end == False:
            return False
        
        return True
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            index = ord(char)-ord('a')
            
            if cur.children[index] == None:
                return False
            
            cur = cur.children[index]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)