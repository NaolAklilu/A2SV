class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = defaultdict(str)
        rank = defaultdict(int)
        owner = defaultdict(int)
        
        def find(email):
            if email != parent[email]:
                parent[email] = find(parent[email])
            return parent[email]
        
        def union(e1, e2):
            p1, p2 = find(e1), find(e2)
            
            if p1 != p2:
                if rank[p1] >= rank[p2]:
                    parent[p2] = p1
                    rank[p1] += rank[p2]
                else:
                    parent[p1] = p2
                    rank[p2] += rank[p1]
             
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                parent[accounts[i][j]] = accounts[i][j]
                owner[accounts[i][j]] = i
                rank[accounts[i][j]] = 1
        
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])-1):
                union(accounts[i][j], accounts[i][j+1])
        
        parentChildren = defaultdict(list)
        for email in parent:
            parentChildren[find(email)].append(email)
            
        results = []
        for email in parentChildren:
            curPerson = [accounts[owner[email]][0]]
            curPerson.extend(sorted(parentChildren[email]))
            results.append(curPerson)
            
        return results
        