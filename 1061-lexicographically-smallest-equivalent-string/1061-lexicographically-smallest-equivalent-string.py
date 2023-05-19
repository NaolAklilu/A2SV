class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {}
        size = {}
        for char in s1:
            parent[char] = char
            size[char] = 1
            
        for char in s2:
            parent[char] = char
            size[char] = 1
            
        def find(char):
            if parent[char] == char:
                return char
            
            parent[char] = find(parent[char])
            return parent[char]
            
        def union(char1, char2):
            parent1 = find(char1)
            parent2 = find(char2)

            if ord(parent1) < ord(parent2):
                parent[parent2] = parent1
                for char in parent:
                    if parent[char] == parent2:
                        parent[char] = parent1
            else:
                parent[parent1] = parent2
                for char in parent:
                    if parent[char] == parent1:
                        parent[char] = parent2
            
        for i in range(len(s1)):
            union(s1[i], s2[i])
        
        result = []
        for char in baseStr:
            if char in parent:
                result.append(parent[char])
            else:
                result.append(char)
                
        return "".join(result)
            
            
            