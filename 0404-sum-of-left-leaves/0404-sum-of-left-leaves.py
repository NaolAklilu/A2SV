# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            total = 0
            if node:
                if node.left:
                    if node.left.left == None and node.left.right == None:
                        total += node.left.val
                        
                total += dfs(node.left)
                total += dfs(node.right) 
                
            return total
        
        totalSum = dfs(root)
        
        return totalSum