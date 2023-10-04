from sys import stdin, stdout
 
def inp():
        return int(stdin.readline())
 
def inlt():
    return list(map(int, stdin.readline().strip().split()))
 
def insr():
    s = stdin.readline().strip()
    return list(s[:len(s)])
 
def invr():
    return map(int, stdin.readline().strip().split())
 
 
class Graph:
    def __init__(self, numberOfVertices):
        self.V = numberOfVertices
        self.graph = []
        self.visited = set()
 
    def add_edge(self, u, v, w):
        self.graph.append([u-1, v-1, w])
 
    def bellman_ford(self, src):
        dist = [0] * self.V
        previous = [-1] * self.V
        node = -1
        for _ in range(self.V):
            node = -1
            for u, v, w in self.graph:
                if dist[u] + w < dist[v]:
                    previous[v] = u
                    dist[v] = dist[u] + w
                    node = v
        
        if node == -1:
            print("NO")
        else:
            cycle = []
            for _ in range(n):
                node = previous[node]
            curNode = node
            while True:
                cycle.append(str(curNode + 1))
                if curNode == node and len(cycle) > 1:
                    break
                curNode = previous[curNode]
            cycle.reverse()
            print("YES")
            print(" ".join(cycle))
 
if __name__ == "__main__":
    n, m = invr()
    edges = []
    g = Graph(n)
 
    for _ in range(m):
        u, v, w = invr()
        g.add_edge(u, v, w)
 
    g.bellman_ford(0)
