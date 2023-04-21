# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        def dfs(node):           
            if node:
                if node.left:
                    if node.left.left == None and node.left.right == None:
                        self.total += node.left.val
                        
                dfs(node.left)
                dfs(node.right) 
                
            return
        
        dfs(root)
        
        return self.total