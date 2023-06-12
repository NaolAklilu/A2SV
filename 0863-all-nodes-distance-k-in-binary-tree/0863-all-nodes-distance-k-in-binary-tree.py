# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        if k == 0:
            return [target.val]
        
        graph = defaultdict(list)
        queue = deque([root])
        
        while queue:
            
            node = queue.popleft()
            
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                
                queue.append(node.left)
                
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                
                queue.append(node.right)
                
        result = []
        visited = set()
        visited.add(target)
        queue = deque([(target, 0)])
        
        while queue:
            
            node, distance = queue.popleft()
            if distance == k:
                result.append(node.val)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance+1))
                
        
        return result