# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init(self):
        self.resNode = TreeNode()
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def commonAncestor(node):
            if node:
                if node.val < p.val and node.val < q.val:
                    commonAncestor(node.right)
                elif node.val > p.val and node.val > q.val:
                    commonAncestor(node.left)
                else:
                    self.resNode = node
             
        commonAncestor(root)
        
        return self.resNode