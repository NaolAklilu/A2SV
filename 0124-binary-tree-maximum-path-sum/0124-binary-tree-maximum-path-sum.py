# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.maxSum = -1001
        
        def maxPath(node):
            curSum = 0
            if node:
                if node.left and node.right == None:
                    leftMax = maxPath(node.left)
                    curSum = leftMax
                    self.maxSum = max(curSum, self.maxSum)
                    curSum = max(leftMax + node.val, node.val)
                    self.maxSum = max(curSum, self.maxSum)
                    
                elif node.left == None and node.right:
                    rightMax = maxPath(node.right)
                    curSum = rightMax
                    self.maxSum = max(curSum, self.maxSum)
                    curSum = max(rightMax + node.val, node.val)
                    self.maxSum = max(curSum, self.maxSum)
                    
                elif node.left and node.right:
                    leftMax = maxPath(node.left)
                    rightMax = maxPath(node.right)

                    curSum = max(leftMax, rightMax)
                    self.maxSum = max(curSum, self.maxSum)
                    curSum = max(curSum+node.val, node.val)
                    self.maxSum = max(curSum, self.maxSum)
                    self.maxSum = max(leftMax + rightMax + node.val, self.maxSum)
                    
                else:
                    curSum = node.val
                    self.maxSum = max(curSum, self.maxSum)
                
                return curSum
            
        maxPath(root)
        
        return self.maxSum
                
            