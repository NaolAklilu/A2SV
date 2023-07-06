# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        queue = deque()
        if root is not None:
            queue.append(root)
        count = 0
        
        while queue:
            curLength = len(queue)
            count += 1
            
            for _ in range(curLength):
                popped = queue.popleft()
                if popped.left:
                    queue.append(popped.left)
                
                if popped.right:
                    queue.append(popped.right)
                   
        return count
        
                
            
        