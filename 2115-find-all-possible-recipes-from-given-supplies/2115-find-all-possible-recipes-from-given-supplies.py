class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:        
        graph = defaultdict(list)
        indegree = {}
        
        for item in supplies:
            indegree[item] = 0
        
        supplies = set(supplies)
        for i in range(len(recipes)):
            indegree[recipes[i]] = len(ingredients[i])
        
        for i in range(len(recipes)):
            for ingre in ingredients[i]:
                graph[ingre].append(recipes[i])
                
                if ingre in supplies:
                    indegree[ingre] = 0
                else:
                    if ingre in indegree:
                        continue
                    else:
                        indegree[ingre] = float(inf)
            
        queue = deque([])
        created_recipes = set()
        
        for ingredient in indegree:
            if indegree[ingredient] == 0:
                queue.append(ingredient)
            
        while queue:
            cur_ingredient = queue.popleft()
            created_recipes.add(cur_ingredient)
            
            for neighbor in graph[cur_ingredient]:
                indegree[neighbor] -= 1
                
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        results = []
        for recipe in recipes:
            if recipe in created_recipes:
                results.append(recipe)
                
        return results
                
            
                
                
        
            