# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        
        def dfs(curArr, curSum, curNode):
            if curNode.left == None and curNode.right == None:
                if curSum == targetSum:
                    result.append(curArr[:])
                    
                    
            if curNode.left != None:
                curArr.append(curNode.left.val)
                curSum += curNode.left.val
                dfs(curArr, curSum, curNode.left)
                curArr.pop()
                
            if curNode.right != None:
                if curNode.left != None:
                    curSum -= curNode.left.val
                curArr.append(curNode.right.val)
                curSum += curNode.right.val
                
                dfs(curArr, curSum, curNode.right)
                curArr.pop()
         
        if root != None:
            dfs([root.val], root.val, root)
        
        return result
                