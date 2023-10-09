# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        dic = defaultdict(set)
        
        def dfs(node):
            if node.val == p.val or node.val == q.val:
                dic[node.val].add(node.val)
            
            if node.left == None and node.right == None:
                return dic[node.val]
            
            if node.left != None:
                res = dfs(node.left)
                if len(res) > 0:
                    for val in res:
                        dic[node.val].add(val)
                    
            if node.right != None:
                res2 = dfs(node.right)
                if len(res2) > 0:
                    for val in res2:
                        dic[node.val].add(val)
                        
            return dic[node.val]
        
        dfs(root)
        
        queue = deque()
        queue.append(root)
        firstParent = None
        while queue:
            node = queue.popleft()
            if q.val in dic[node.val] and p.val in dic[node.val]:
                firstParent = node
                
            if node.left != None:
                queue.append(node.left)
            
            if node.right != None:
                queue.append(node.right)
        
        return firstParent
                    
                    
            
                    
            
            