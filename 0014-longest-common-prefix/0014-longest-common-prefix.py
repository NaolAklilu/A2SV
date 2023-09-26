class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode(".")
    
    def insert(self, word):
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

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        rootTrie = Trie()
        emptyExist = False
        for word in strs:
            if len(word) == 0:
                emptyExist = True
            rootTrie.insert(word)
    
        if emptyExist == True:
            rootTrie.root = TrieNode('.')
            
        cur = rootTrie.root
        ans = []
        while len(cur.children) == 1 and cur.is_end == False:
            keys = list(cur.children.keys())
            cur = cur.children[keys[0]]
            ans.append(cur.val)
        
        return "".join(ans)
        
        
        