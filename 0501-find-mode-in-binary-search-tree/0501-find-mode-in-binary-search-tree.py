# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        node_Count = defaultdict(int)
        self.maxMode = 0
        
        def traverse(root):
            if root:
                traverse(root.left)
                traverse(root.right)
                node_Count[root.val] += 1
                if node_Count[root.val] > self.maxMode:
                    self.maxMode = node_Count[root.val] 
        
        traverse(root)
        modeNodes = []
        for node in node_Count:
            if node_Count[node] == self.maxMode:
                modeNodes.append(node)
                
        return modeNodes