class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        GRAPH, n = defaultdict(list), len(quiet)
        answer = [501] * n
        
        for adj, node in richer:
            GRAPH[node].append(adj)
            
        def dfs(node):
            if answer[node] != 501:
                return answer[node]
            
            answer[node] = min(node, answer[node])
            for adj in GRAPH[node]:
                person = dfs(adj)
                
                if quiet[person] < quiet[answer[node]]:
                    answer[node] = person
                         
            return answer[node]
        
        for node in range(n):
            answer[node] = dfs(node)
            
        return answer