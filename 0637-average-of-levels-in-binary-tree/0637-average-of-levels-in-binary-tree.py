# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        averages = []
        visited = set()
        queue = deque([root])
        
        while queue:
            cur_length = len(queue)
            total = 0
            for i in range(cur_length):
                node = queue.popleft()
                total+= node.val
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                    
            averages.append(total/cur_length)
            
        return averages