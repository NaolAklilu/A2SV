# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        verticals =defaultdict(list)
        
        def dfs(node, row, col):
            if not node:
                return
            
            verticals[col].append((row,node.val))
            
            dfs(node.left, row+1, col-1)
            dfs(node.right, row+1, col+1)
            
            return
        
        dfs(root, 0, 0)
        
        
        resultColumns = []
        for i in sorted(verticals):
            column = verticals[i]
            column.sort()
            curColumn = []
            for col in column:
                curColumn.append(col[1])
            resultColumns.append(curColumn)
            
        return resultColumns
            