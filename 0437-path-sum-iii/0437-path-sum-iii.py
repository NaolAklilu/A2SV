# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def dfs(node):
            count = 0
            sums = []
            if node.val == targetSum:
                count += 1
                
            sums.append(node.val)
            if node.left == None and node.right == None:
                return [sums, count]
            
            if node.left != None:
                prevSums, cnt = dfs(node.left)
                count += cnt
                for prevSum in prevSums:
                    if prevSum + node.val == targetSum:
                        count += 1
                    sums.append(prevSum+node.val)
            
            if node.right != None:
                prevSums, cnt = dfs(node.right)
                count += cnt
                for prevSum in prevSums:
                    if prevSum + node.val == targetSum:
                        count += 1
                    sums.append(prevSum+node.val)
                
            return [sums, count]
        
        totalCount = 0
        if root != None:
            sums, totalCount = dfs(root)
        return totalCount