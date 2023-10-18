class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        parent = defaultdict(str)
        rank = defaultdict(int)
        
        
        def find(string):
            if string != parent[string]:
                parent[string] = find(parent[string])
            return parent[string]
        
        def union(s1, s2):
            p1, p2 = find(s1), find(s2)
            
            if p1 != p2:
                if rank[p1] >= rank[p2]:
                    parent[p2] = p1
                    rank[p1] += rank[p2]
                else:
                    parent[p1] = p2
                    rank[p2] += rank[p1]
        
        
        for string in strs:
            parent[string] = string
            rank[string] = 1
            
        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                diffCount = 0
                string1 = strs[i]
                string2 = strs[j]
                
                for index in range(len(string1)):
                    if string1[index] != string2[index]:
                        diffCount += 1
                
                if diffCount <= 2:
                    union(string1, string2)
                    
        parents = set()
        for string in parent:
            parents.add(find(string))
            
        return len(parents)
                    