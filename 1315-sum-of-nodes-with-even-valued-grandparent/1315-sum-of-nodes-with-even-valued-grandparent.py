# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.sum = 0
        
        def dfs(node, parentNode):
            if node == None:
                return
            else:
                if parentNode%2 == 0:
                    if node.left:
                        self.sum += node.left.val

                    if node.right:
                        self.sum += node.right.val

                dfs(node.left, node.val)
                dfs(node.right, node.val)
            
            return
        
        if root.left:
            dfs(root.left, root.val)
        
        if root.right:
            dfs(root.right, root.val)
            
        return self.sum