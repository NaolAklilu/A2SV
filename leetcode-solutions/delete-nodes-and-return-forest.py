# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        nodes = set()
        to_delete = set(to_delete)
            
        def recursion(node):
            if node is None:
                return None
            
            leftNode, rightNode = None, None
            if node.left:
                leftNode = recursion(node.left)
                if leftNode == None:
                    node.left = None
                
            if node.right:
                rightNode = recursion(node.right)
                if rightNode == None:
                    node.right = None
                    
            
            if node.val in to_delete:
                if leftNode:
                    nodes.add(leftNode)
                
                if rightNode:
                    nodes.add(rightNode)
                    
                return None
            
            return node
        
        rootNode = recursion(root)
        if rootNode:
            nodes.add(rootNode)
        
        return list(nodes)
        
                    
                    