# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        def helper(node, row):
            if not node:
                return
            
            row_nodes[row].append(node.val)
            
            helper(node.left, row+1)
            helper(node.right, row+1)
            
        row_nodes = defaultdict(list)
        
        helper(root, 0)
        rightNodes = []
        for row in row_nodes:
            rightNodes.append(row_nodes[row][-1])
        
        return rightNodes
        