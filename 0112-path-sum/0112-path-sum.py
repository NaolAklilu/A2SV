# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
            
        def traversal(node, arr):
            count = 0       
            if node:
                arr.append(node.val)                
                if not node.right and not node.left:
                    if sum(arr) == targetSum:
                        count += 1
                count += traversal(node.left, arr)
                count += traversal(node.right, arr)
                arr.pop()
                
            return count
        
        result = traversal(root, [])
        
        return result