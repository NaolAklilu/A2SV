# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        parents = set()
        
        for parent, child, direction in descriptions:
            parents.add(parent)
          
        for parent, child, direction in descriptions:
            if child in parents:
                parents.remove(child)
                
        rootVal = list(parents)[0]
        valNodePair = {rootVal: TreeNode(rootVal)}
        
        for parent, child, direction in descriptions:
            if parent not in valNodePair:
                valNodePair[parent] = TreeNode(parent)
                
            if child not in valNodePair:
                valNodePair[child] = TreeNode(child)
            
            if direction == 1:
                valNodePair[parent].left = valNodePair[child]
            else:
                valNodePair[parent].right = valNodePair[child]
                
        return valNodePair[rootVal]
        