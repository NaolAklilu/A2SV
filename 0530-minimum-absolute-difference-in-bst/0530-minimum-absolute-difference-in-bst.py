# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        nums = []
        queue = deque()
        queue.append(root)
        
        while queue:
            length = len(queue)
            
            for _ in range(length):
                popped = queue.popleft()
                nums.append(popped.val)
                
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
                    
        nums.sort()
        
        minValue = float(inf)
        for i in range(len(nums)-1):
            minValue = min(minValue, abs(nums[i] - nums[i+1]))
            
        return minValue
                
            
                
            