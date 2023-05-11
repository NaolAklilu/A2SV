from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    def dfs(node, colors, parent):
	        if colors[node] == 1:
	            return True
	            
	        colors[node] = 1
	        for neighbor in adj[node]:
                if neighbor != parent:
    	            if dfs(neighbor, colors, node):
    	                return True
	        
	        colors[node] = 2
	        return False
	       
	    
		colors = [0 for _ in range(V)]
		
		for i in range(V):
		    if colors[i] != 0:
		        continue
		    if dfs(i, colors, -1):
		        return True
		        
		return False
		



#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends