# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inOrder(root):
            if root:
                inOrder(root.left)
                res.append(root.val)
                inOrder(root.right)
                
        res = []
        inOrder(root)
        
        return res