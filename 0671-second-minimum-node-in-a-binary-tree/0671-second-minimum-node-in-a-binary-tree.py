# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        nums = set()
        
        def findValues(node):
            nums.add(node.val)
            if node.left:
                findValues(node.left)
            if node.right:
                findValues(node.right)   
            
            return
        
        findValues(root)
        
        nums = list(nums)
        nums.sort()
        
        if len(nums) > 1:
            return nums[1]
        else:
            return -1
        
        