class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        n, GRAPH = len(recipes), defaultdict(list)
        indices = dict(zip(recipes, range(n)))
        supplies = set(supplies)
        INDEGREE, level = defaultdict(int), []
        created = []
        
        for node, children in enumerate(ingredients):
            for adj in children:
                if adj in indices:
                    GRAPH[indices[adj]].append(node)
                    INDEGREE[node] += 1
         
        for node in range(n):
            if not INDEGREE[node]:
                for ingred in ingredients[node]:
                    if ingred not in supplies:
                        break
                        
                else:
                    level.append(node)
                    created.append(recipes[node])
                    supplies.add(recipes[node])
        
        while level:
            next_level = []
            
            for node in level:
                for adj in GRAPH[node]:
                    if INDEGREE[adj]:
                        for ingred in ingredients[adj]:
                            if ingred not in supplies:
                                break

                        else:
                            INDEGREE[adj] -= 1
                            if not INDEGREE[adj]:
                                next_level.append(adj)
                                created.append(recipes[adj])
                                supplies.add(recipes[adj])
                            
            level = next_level
    
        return created