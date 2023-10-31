class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(int)
        nodes = set()
        
        for index, (dividend, divisor) in enumerate(equations):
            nodes.add(dividend)
            nodes.add(divisor)
            graph[(dividend, divisor)] = values[index]
            graph[(divisor, dividend)] = 1 / values[index]
        
        results = []
        for dividend, divisor in queries:
            if dividend not in nodes or divisor not in nodes:
                results.append(-1)
                continue
                
            quotient = {}
            for node1, node2 in graph:
                quotient[node1] = float('inf')
                quotient[node2] = float('inf')
            quotient[dividend] = 1
            
            for _ in range(len(graph)-1):
                for u, v in graph:
                    quo = graph[(u, v)]
                    if quo*quotient[u] < quotient[v]:
                        quotient[v] = quo*quotient[u]
                    
            results.append(quotient[divisor])
            
        
        for i in range(len(results)):
            if results[i] == float('inf'):
                results[i] = -1
        
        return results
            
            