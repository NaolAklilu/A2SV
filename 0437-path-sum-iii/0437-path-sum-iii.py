# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
            
        def traversal(node, arr):
            count = 0       
            if node:
                arr.append(node.val) 
                curSum = 0
                for i in range(len(arr)-1, -1, -1):
                    curSum += arr[i]
                    if curSum == targetSum:
                        count += 1
                
                count += traversal(node.left, arr)
                count += traversal(node.right, arr)
                arr.pop()
                
            return count
        
        result = traversal(root, [])
        
        return result