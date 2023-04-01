# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.result = []
        
        def traversal(node, arr):
            
#             if not node:
#                 if sum(arr) == targetSum:
#                     # print(arr)
#                     self.result.append(arr[:])
                
#                 return
                    
            if node:
                arr.append(node.val)                
                if not node.right and not node.left:
                    if sum(arr) == targetSum:
                        self.result.append(arr[:])
                traversal(node.left, arr)
                traversal(node.right, arr)
                arr.pop()
        
        traversal(root, [])
        
        return self.result