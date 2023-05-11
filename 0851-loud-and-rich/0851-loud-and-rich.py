class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        GRAPH, seen = defaultdict(list), set()
        answer = list(range(len(quiet)))
        
        for adj, node in richer:
            GRAPH[node].append(adj)
            
        def dfs(node):
            if node in seen:
                return answer[node]
            
            seen.add(node)
            for adj in GRAPH[node]:
                person = dfs(adj)
                if quiet[person] < quiet[answer[node]]:
                    answer[node] = person
                    
            return answer[node]
        
        for node in range(len(quiet)):
            answer[node] = dfs(node)
            
        return answer