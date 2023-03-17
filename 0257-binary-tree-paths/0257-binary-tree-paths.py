# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        self.result = []
        def dfs(cur, curNode):
            if curNode and curNode.left == None and curNode.right == None:
                temp = cur[:]
                temp.append(str(curNode.val))
                self.result.append("->".join(temp))
                return
            
            if curNode == None:
                return 
            
            temp = cur[:]
            temp.append(str(curNode.val))
            
            dfs(temp, curNode.left)
            dfs(temp, curNode.right)
            
    
        dfs([], root)
        
        return self.result