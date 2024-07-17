# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        result = []
        
        def dfs(node, hasParent):
            if node:
                dfs(node.left, True)
                dfs(node.right, True)
                
                if node.val in to_delete:
                    if node.left:
                        if node.left.val in to_delete:
                            node.left = None
                        else:
                            result.append(node.left)
                    
                    if node.right:
                        if node.right.val in to_delete:
                            node.right = None
                        else:
                            result.append(node.right)
                else:
                    if node.left:
                        if node.left.val in to_delete:
                            node.left = None
                    
                    if node.right:
                        if node.right.val in to_delete:
                            node.right = None
                    
                            
                if hasParent == False and node.val not in to_delete:
                    result.append(node)
                    
        dfs(root, False)
            
        return result