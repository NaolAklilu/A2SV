class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        nodes = set()
        for i in range(len(equations)):
            dividend, divisor = equations[i]
            nodes.add(dividend)
            nodes.add(divisor)
            graph[(dividend, divisor)] = values[i]
            graph[(divisor, dividend)] = 1/values[i]
            # graph[(dividend)].append((dividend, divisor, values[i]))
            # graph[(divisor)].append((divisor, dividend, 1/values[i]))
            
        result = []
        for dividend, divisor in queries:
            if dividend not in nodes or divisor not in nodes:
                result.append(-1)
                continue
            
            quotient = {}
            for node1, node2 in graph:
                quotient[node1] = float('inf')
                quotient[node2] = float('inf')
            quotient[dividend] = 1
            
            for _ in range(len(graph)-1):
                for u, v in graph:
                    quo = graph[(u, v)]
                    if quotient[u]*quo < quotient[v]:
                        quotient[v] = quotient[u]*quo
            
            result.append(quotient[divisor])
            
        for i in range(len(result)):
            if result[i] == float('inf'):
                result[i] = -1
        return result
            