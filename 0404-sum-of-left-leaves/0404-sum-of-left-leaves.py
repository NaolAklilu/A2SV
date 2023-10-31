# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def findLeft(node):
            leftSum = 0
            if node:
                if node.left:
                    if node.left.left == None and node.left.right == None:
                        leftSum = node.left.val
                    else:
                        leftSum += findLeft(node.left)
                    
                if node.right:
                    leftSum += findLeft(node.right)
                    
                    
            return leftSum
        
        totalSum = 0
        totalSum += findLeft(root)
        
        return totalSum