class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.products = []

class Solution:
    
    def __init__(self):
        self.root = TrieNode(".")
        
    def insert(self, word):
        cur = self.root
        
        for char in word:
            if char not in cur.children:
                newNode = TrieNode(char)
                newNode.products.append(word)
                cur.children[char] = newNode
            else:
                curNode = cur.children[char]
                curNode.products.append(word)
          
            cur = cur.children[char]
    
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans = []
        
        for product in products:
            self.insert(product)
            
        cur = self.root
        for char in searchWord:
            if char not in cur.children:
                ans.append([])
                newNode = TrieNode(char)
                cur.children[char] = newNode
            else:
                charNode = cur.children[char]
                if len(charNode.products) >= 3:
                    ans.append(charNode.products[:3])
                else:
                    ans.append(charNode.products)
                    
            cur = cur.children[char]
            
        return ans
        
        
        
        