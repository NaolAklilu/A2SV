class TrieNode:
    def __init__(self, val):
        self.val = val
        self.is_end = False
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode('.')

    def insert(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            char = word[i]
            if char not in cur.children:
                newNode = TrieNode(char)
                if i == len(word)-1:
                    newNode.is_end = True
                cur.children[char] = newNode
            else:
                if i == len(word)-1:
                    curNode = cur.children[char]
                    curNode.is_end = True
        
            cur = cur.children[char]

    def search(self, word: str) -> bool:
        cur = self.root
        
        for i in range(len(word)):
            char = word[i]
            
            if char not in cur.children:
                return False
            
            cur = cur.children[char]
            
        if cur.is_end == False:
            return False
        
        return True
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in range(len(prefix)):
            char = prefix[i]
            
            if char not in cur.children:
                return False
            
            cur = cur.children[char]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)