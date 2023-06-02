# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = defaultdict(int)
        head = root
        
        def find(node):
            if node.left == None and node.right == None:
                memo[node] = node.val
                return memo[node]
            
            memo[node] = node.val
            childValue = 0
            
            if node.left and node.left not in memo:
                find(node.left)
                childValue += memo[node.left]
                if node.left.left:
                    memo[node] += memo[node.left.left]
                
                if node.left.right:
                    memo[node] += memo[node.left.right]
                
            if node.right and node.right not in memo:
                find(node.right)
                childValue += memo[node.right]
                
                if node.right.left:
                    memo[node] += memo[node.right.left]
                
                if node.right.right:
                    memo[node] += memo[node.right.right]
                
            memo[node] = max(memo[node], childValue)
            
            return memo[node]
        
        return find(head)
            
            
                
                