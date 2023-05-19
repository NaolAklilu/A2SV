class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}
        size = {}
        notEqual = set()
        equals = set()
        
        for equation in equations:
            parent[equation[0]] = equation[0]
            parent[equation[3]] = equation[3]
            
            size[equation[0]] = 1
            size[equation[3]] = 1
        
        def find(node):
            if node == parent[node]:
                return node
            
            parent[node] = find(parent[node])
            return parent[node]
        
        def union(node1, node2):
            node1Parent = find(node1)
            node2Parent = find(node2)
            
            if node1Parent != node2Parent:
                if size[node1Parent] > size[node2Parent]:
                    parent[node2Parent] = node1Parent
                    size[node1Parent] += size[node2Parent]

                else:
                    parent[node1Parent] = node2Parent
                    size[node2Parent] += size[node1Parent]
                    
        for equation in equations:
            if equation[1] == "!":
                notEqual.add((equation[0], equation[3]))
            else:
                equals.add((equation[0], equation[3]))
                union(equation[0], equation[3])
        
        for node1, node2 in notEqual:
            if find(node1) == find(node2):
                return False
            
        for node1, node2 in equals:
            if find(node1) != find(node2):
                return False
            
        return True
            
        
        