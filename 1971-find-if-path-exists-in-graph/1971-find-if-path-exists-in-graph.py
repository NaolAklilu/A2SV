class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dic = { i:i for i in range(n)}
        
        def find(x):
            node = x
            parent = dic[x]
            length = 0
            
            while x != dic[x]:
                parent = dic[x]
                length += 1
                x = dic[x]

            while node != dic[node]:
                dic[node] = parent
                node = dic[node]

            return parent, length

        def union(x, y):
            xrep, xlen = find(x)
            yrep, ylen = find(y)
            
            if xlen > ylen:
                dic[yrep] = xrep
            else:
                dic[xrep] = yrep

        for left, right in edges:
            union(left,right)
        
        
        return find(source)[0] == find(destination)[0]
    
    