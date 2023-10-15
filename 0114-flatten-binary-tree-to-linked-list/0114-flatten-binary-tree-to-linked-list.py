# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:        
        stack = []
        
        def dfs(node):
            if node:
                stack.append(node)
                dfs(node.left)
                dfs(node.right)
                
        dfs(root)
        stack.reverse()
        if not stack:
            return root
        
        curNode = stack.pop()
        while stack:
            curNode.right = stack.pop()
            curNode.left = None
            
            curNode = curNode.right
        
        return root
            