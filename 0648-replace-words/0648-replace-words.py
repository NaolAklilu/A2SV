class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.is_end = False

class Solution:
    def __init__(self):
        self.root = TrieNode('.')
    
    def insert(self, word) -> None:
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
        
    
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for word in dictionary:
            self.insert(word)
        
        ans = []
        for word in list(sentence.split(" ")):
            cur = self.root
            curWord = []
            
            for char in word:
                if char not in cur.children:
                    ans.append(word)
                    break
                
                else:
                    curWord.append(char)
                
                cur = cur.children[char]
                
                if cur.is_end == True:
                    ans.append("".join(curWord))
                    break
            else:
                ans.append("".join(curWord))
        
        return " ".join(ans)
        
        
        