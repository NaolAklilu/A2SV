# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.isSame = True
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(root1, root2):
            if not root1 and root2:
                self.isSame = False
            
            if not root2 and root1:
                self.isSame = False
                
            if root1 and root2:
                if root1.val != root2.val:
                    self.isSame = False
                    
                traverse(root1.left, root2.left)
                traverse(root1.right, root2.right)
                    
                
        traverse(p, q)
        
        return self.isSame
            
        
                    
            