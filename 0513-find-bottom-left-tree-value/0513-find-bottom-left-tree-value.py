# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        nodes = []
        queue = deque()
        queue.append(root)
        
        while queue:
            length = len(queue)
            lst = []
            
            for _ in range(length):
                poppedNode = queue.popleft()
                lst.append(poppedNode.val)
                if poppedNode.left:
                    queue.append(poppedNode.left)
                    
                if poppedNode.right:
                    queue.append(poppedNode.right)
                    
            nodes.append(lst)
        
        return nodes[-1][0]