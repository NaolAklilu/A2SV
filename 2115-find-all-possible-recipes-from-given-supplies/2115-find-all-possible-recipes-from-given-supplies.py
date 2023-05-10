class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        queue = deque()
        
        for ingredient in supplies:
            indegree[ingredient] = 0
            queue.append(ingredient)
        
        for i in range(len(ingredients)):
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipes[i])
                indegree[recipes[i]] += 1

        recipes = set(recipes)
        createdRecipe = []
        while queue:
            recipe = queue.popleft()
            if recipe in recipes:
                createdRecipe.append(recipe)
                
            for ingredient in graph[recipe]:
                indegree[ingredient] -= 1
                
                if indegree[ingredient] == 0:
                    queue.append(ingredient)
            
        return createdRecipe
            