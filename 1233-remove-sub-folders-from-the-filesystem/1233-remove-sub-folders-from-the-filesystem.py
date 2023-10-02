class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.is_end = False
        self.folder = ""

class Solution:
    
    def __init__(self):
        self.root = TrieNode(".")
        
    def insert(self, folder):
        cur = self.root
        curFolder = list(folder[1:].split("/"))
        
        for i in range(len(curFolder)):
            char = curFolder[i]
            if char not in cur.children:
                newNode = TrieNode(char)
                if i == len(curFolder)-1:
                    newNode.is_end = True
                    newNode.folder = folder
                cur.children[char] = newNode
            else:
                curNode = cur.children[char]                    
                if i == len(curFolder)-1:
                    curNode.is_end = True
                    curNode.folder = folder
                    
            cur = cur.children[char]
    
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        for fold in folder:
            self.insert(fold)
        
        folders = set()
        for fold in folder:
            curFolder = list(fold[1:].split("/"))
            cur = self.root
            for char in curFolder:
                cur = cur.children[char]
                if cur.is_end == True:
                    folders.add(cur.folder)
                    break
                
        return list(folders)
        
        
        
        
        