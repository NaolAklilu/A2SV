# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findRowElement(self, root, row):
        if not root:
            return
        
        self.result[row].append(root.val)
        
        self.findRowElement(root.left, row+1)
        self.findRowElement(root.right, row+1)

    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.result = defaultdict(list)
        self.findRowElement(root, 0)
        
        ans = []
        for key in self.result:
            ans.append(self.result[key])
        
        return ans