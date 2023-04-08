"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.maxCount = 0
        self.count = 0
        
        def dfs(node, curCount):
            if node == None:
                return
            
            curCount += 1
            self.maxCount = max(self.maxCount, curCount)
            
            for child in node.children:
                dfs(child, curCount)
                
        
        dfs(root, 0)
        
        return self.maxCount
                
                
                