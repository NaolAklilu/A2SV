class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode('.')

    def addWord(self, word: str) -> None:
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
                
        def findWord(curNode, index):
            if index == len(word):
                if curNode.is_end == True:
                    return True
                else:
                    return False
            
            char = word[index]
            if char == '.':
                for child in curNode.children:
                    result = findWord(curNode.children[child], index+1)

                    if result == True:
                        return True
                return False
            
            else:
                if char not in curNode.children:
                    return False
            
            curNode = curNode.children[char]
            return findWord(curNode, index+1)
        
        cur = self.root
        return findWord(cur, 0)
                
                    
            
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)