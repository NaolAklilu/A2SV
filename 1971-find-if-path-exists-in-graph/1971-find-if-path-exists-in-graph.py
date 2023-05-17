class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        rep = { i:i for i in range(n)}
        size = { i:1 for i in range(n)}
        
        def find(x):
            node = x
            parent = rep[x]
            length = 0
            
            while x != rep[x]:
                parent = rep[x]
                size[node] += 1
                x = rep[x]

            while node != rep[node]:
                rep[node] = parent
                node = rep[node]

            return parent

        def union(x, y):
            xrep = find(x)
            yrep = find(y)
            
            if xrep != yrep:
                if size[x] > size[y]:
                    rep[yrep] = xrep
                    size[x] += size[y]
                    size[y] = 0
                else:
                    rep[xrep] = yrep
                    size[y] += size[x]
                    size[x] = 0

        for left, right in edges:
            union(left,right)
        
        return find(source) == find(destination)
    
    