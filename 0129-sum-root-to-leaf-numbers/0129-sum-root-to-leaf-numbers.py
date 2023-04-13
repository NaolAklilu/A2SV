# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def path(node, arr):
            nums = arr[:]
                
            if node:
                nums.append(str(node.val))
                if node.left == None and node.right == None:
                    numSum = "".join(nums)
                    return int(numSum)
                
                if node.left and node.right == None:
                    return path(node.left, nums)
                
                if node.left == None and node.right:
                    return path(node.right, nums)
                
                if node.left and node.right:
                    leftSum = path(node.left, nums)
                    rightSum = path(node.right, nums)
                
                    return leftSum + rightSum
            
        return path(root,[])