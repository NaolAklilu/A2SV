class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = defaultdict(str)
        rank = defaultdict(int)
        
        def find(char):
            if char != parent[char]:
                parent[char] = find(parent[char])
                
            return parent[char]
            
            
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 != p2:
                if ord(p1) <= ord(p2):
                    parent[p2] = p1
                    rank[p1] += rank[p2]
                else:
                    parent[p1] = p2
                    rank[p2] += rank[p1]
                    
        for i in range(len(s1)):
            parent[s1[i]] = s1[i]
            parent[s2[i]] = s2[i]
            rank[s1[i]] = 1
            rank[s2[i]] = 1
            
        for i in range(len(baseStr)):
            parent[baseStr[i]] = baseStr[i]
            rank[baseStr[i]] = 1
            
        for i in range(len(s1)):
            union(s1[i], s2[i])
            
        ans = []
        for i in range(len(baseStr)):
            ans.append(find(baseStr[i]))
        
        return "".join(ans)
                
                
                
            