# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        queue = deque()
        if root is not None:
            queue.append(root)
        
        while queue:
            length = len(queue)
            count += 1
            
            for _ in range(length):
                popped = queue.popleft()
                if not popped.left and not popped.right:
                    return count
                
                if popped.left:
                    queue.append(popped.left)
                    
                if popped.right:
                    queue.append(popped.right)
                
        return count