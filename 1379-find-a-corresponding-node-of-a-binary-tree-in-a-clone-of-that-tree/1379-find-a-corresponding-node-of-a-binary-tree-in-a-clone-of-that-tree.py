# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:        
        queue = deque()
        queue.append(cloned)
        
        while queue:
            length = len(queue)
            
            for _ in range(length):
                poppedNode = queue.popleft()
                if poppedNode.val == target.val:
                    return poppedNode
                
                if poppedNode.left:
                    queue.append(poppedNode.left)
                if poppedNode.right:
                    queue.append(poppedNode.right)
                    
        
            
            