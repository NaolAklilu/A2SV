# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.nodeCount = 0
        def traverseSubTree(node):
            if node:
                traverseSubTree(node.left)
                traverseSubTree(node.right)
                self.curSum += node.val
                self.count  += 1
                
        def traverse(node):
            self.curSum = 0
            self.count = 0
            
            if node:
                traverseSubTree(node)
                if self.curSum // self.count == node.val:
                    self.nodeCount += 1
                
                traverse(node.left)
                traverse(node.right)
                
            
        traverse(root)
        
        return self.nodeCount
                