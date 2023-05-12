from typing import List
from collections import defaultdict, deque
from typing import List


class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        time = [0 for _ in range(n)]
        
        for source, des in edges:
            graph[source-1].append(des-1)
            indegree[des-1] += 1
        
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        levelCount = 0
        while queue:
            levelCount += 1
            length = len(queue)
            
            for _ in range(length):
                node = queue.popleft()
                time[node] = str(levelCount)
                
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
                        
        return " ".join(time)
            
        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        print(res)
        

# } Driver Code Ends