# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque()
        if root:
            queue.append(root)
        
        while queue:
            length = len(queue)
            
            for _ in range(length):
                popped = queue.popleft()                   
                if popped.left:
                    queue.append(popped.left)
                    
                if popped.right:
                    queue.append(popped.right)
                    
                popped.left, popped.right = popped.right, popped.left
                    
        return root
                
            