class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.word = ""
        self.count = 1
        self.is_end = False

class Solution:
    
    def __init__(self):
        self.root = TrieNode(".")
        
    def insert(self, word):
        cur = self.root
        
        for i in range(len(word)):
            char = word[i]
            if char not in cur.children:
                newNode = TrieNode(char)
                if i == len(word)-1:
                    newNode.word = word
                    newNode.is_end = True
                
                cur.children[char] = newNode
                
            else:
                curNode = cur.children[char]
                if i == len(word)-1:
                    curNode.word = word
                    curNode.is_end = True
                curNode.count += 1
            
            cur = cur.children[char]
                
    
    def longestWord(self, words: List[str]) -> str:
        
        def dfs(curNode):
            curCount = curNode.count
            curWord = [curNode.word]
            
            if curNode.is_end == False:
                return [1, curWord]
            
            if curNode.count == 1:
                return [1, curWord]
            
            count = 0
            for neighbor in curNode.children:
                count, words = dfs(curNode.children[neighbor])
                if len(curWord[0]) < len(words[0]):
                    curWord = words
                elif len(curWord[0]) == len(words[0]):
                    curWord.extend(words)
            
            if count+1 <= curCount:
                return [count+1,curWord]
            else:
                return [1, [curNode.word]]
        
        for word in words:
            self.insert(word)
            
        cur = self.root
  
        curWords = [""]
        for child in cur.children:
            reCount, resWords = dfs(cur.children[child])
            
            if len(curWords[0]) < len(resWords[0]):
                curWords = resWords
            elif len(curWords[0]) == len(resWords[0]):
                curWords.extend(resWords)
  
        curWords.sort()
        return curWords[0]
        
        
        
        