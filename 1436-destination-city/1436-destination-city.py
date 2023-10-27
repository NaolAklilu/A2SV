class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        citySet = set()
        graph = defaultdict(list)
        
        for source, dest in paths:
            citySet.add(source)
            citySet.add(dest)
            
            graph[source].append(dest)
        
        for city in citySet:
            if graph[city] == []:
                return city
            