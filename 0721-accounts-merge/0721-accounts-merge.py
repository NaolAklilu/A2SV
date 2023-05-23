class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = defaultdict(str)
        owner = defaultdict(int)
        rank = defaultdict(int)
        
        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        
        def union(email1, email2):
            email1Par = find(email1)
            email2Par = find(email2)
            
            if rank[email1Par] > rank[email2Par]:
                parent[email2Par] = email1Par
                rank[email1Par] += rank[email2Par]
            else:
                parent[email1Par] = email2Par
                rank[email2Par] += rank[email1Par]
                
        
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                parent[accounts[i][j]] = accounts[i][j]
                owner[accounts[i][j]] = i
                rank[accounts[i][j]] = 1
                
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])-1):
                union(accounts[i][j], accounts[i][j+1])
             
        parentChild = defaultdict(list)
        for email in parent:
            parentChild[find(email)].append(email)
            
        ans = []
        for parent in parentChild:
            curAccount = []
            curAccount.append(accounts[owner[parent]][0])
            curAccount.extend(sorted(parentChild[parent]))
            ans.append(curAccount)
                
        return ans
        
                
                