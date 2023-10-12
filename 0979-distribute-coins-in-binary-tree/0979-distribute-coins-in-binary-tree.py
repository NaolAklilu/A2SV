# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        moves = 0
        def traverse(node):
            nonlocal moves
            
            if not node:
                return 0
            
            leftValue = traverse(node.left)
            rightValue = traverse(node.right)
            
            moves += abs(leftValue)
            moves += abs(rightValue)
            
            return node.val-1 + leftValue + rightValue
        
        traverse(root)
        return moves