class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        
        GRAPH = defaultdict(list)
        count = [0]
        for node, adj in edges:
            GRAPH[node].append(adj)
            GRAPH[adj].append(node)
            
        def dfs(node, prev):
            curr_sum = values[node]
            for adj in GRAPH[node]:
                if adj != prev:
                    curr_sum += dfs(adj, node)

            if (curr_sum) % k:
                return curr_sum
            
            count[0] += 1
            return 0
        
        dfs(0, "ahhh")
        
        return count[0]