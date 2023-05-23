class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = {i:i for i in range(len(s))}
        rank = {i:1 for i in range(len(s))}
        
        def find(char):
            if char==parent[char]:
                return char
            
            parent[char] = find(parent[char])
            return parent[char]
        
        
        def union(char1, char2):
            char1Par = find(char1)
            char2Par = find(char2)
            
            if char1Par != char2Par:
                if rank[char1Par] > rank[char2Par]:
                    parent[char2Par] = char1Par
                    rank[char1Par] += rank[char2Par]
                else:
                    parent[char1Par] = char2Par
                    rank[char2Par] += rank[char1Par]
                
        for left, right in pairs:
            union(left, right)
        
        for left, right in pairs:
            find(left)
            find(right)
            
        group = defaultdict(list)
        for rep in parent:
            group[parent[rep]].append(s[rep])
        
        for rep in group:
            group[rep].sort(reverse=True)
        
        ans = []
        for i in range(len(s)):  
            rep = find(i)
            ans.append(group[rep].pop())
        
        return "".join(ans)