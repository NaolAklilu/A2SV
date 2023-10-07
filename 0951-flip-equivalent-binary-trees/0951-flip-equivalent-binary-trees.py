# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(node1, node2):
            if node1 != None and node2 != None and node1.val != node2.val:
                return False
            
            if node1 != None and node2 == None or node1 == None and node2 != None:
                return False
            
            if node1 == None and node2 == None:
                return True
            
            if node2.left == None and node2.right == None and node1.left == None and node1.right == None:
                return True
            
            if node2.left != None and node2.right != None and node1.left != None and node1.right != None:
                if node2.left.val == node1.left.val and node2.right.val == node1.right.val:
                    return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
                    
                elif node1.left.val == node2.right.val and node1.right.val == node2.left.val:             
                    return dfs(node1.left, node2.right) and dfs(node1.right, node2.left)
                    
                else:
                    return False
                
            elif node1.left != None and node2.left != None and node1.right == None and node2.right == None:
                if node1.left.val == node2.left.val:
                    return dfs(node1.left, node2.left)
                else:
                    return False
                
            elif node1.right != None and node2.right != None and node1.left == None and node2.left == None:
                if node1.right.val == node2.right.val:
                    return dfs(node1.right, node2.right)
                else:
                    return False
                
            elif node1.right != None and node2.left != None and node1.left == None and node2.right == None:
                if node1.right.val == node2.left.val:                    
                    return dfs(node1.right, node2.left)
                else:
                    return False
                
            elif node1.left != None and node2.right != None and node1.right == None and node2.left == None:
                if node1.left.val == node2.right.val:                    
                    return dfs(node1.left, node2.right)
                else:
                    return False
                
            else:
                return False
            
        return dfs(root1, root2)
                