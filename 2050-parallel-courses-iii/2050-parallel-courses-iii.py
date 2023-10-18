class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        GRAPH = defaultdict(list)
        max_time = 0

        for parent, child in relations:
            GRAPH[parent].append(child)
          
        @cache
        def dp(node):
            max_path = 0
            
            for adj in GRAPH[node]:
                max_path = max(max_path, dp(adj))
                
            return time[node - 1] + max_path
            
        for node in range(1, n + 1):
            max_time = max(max_time, dp(node))
            
        return max_time