# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(node):
            if node:
                isValid(node.left)
                res.append(node.val)
                isValid(node.right)
         
        res = []
        isValid(root)
        
        for i in range(1, len(res)):
            if res[i] <= res[i-1]:
                return False
        
        return True
                