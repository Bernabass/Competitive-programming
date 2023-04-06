class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        max_len = 0
        graph = defaultdict(set)
        
        for src, dest in roads:
            graph[src].add(dest)
            graph[dest].add(src)
            
        for node, start in graph.items():
            key1 = {node}
            graph[node] = []
            for next_node, target in graph.items():
                
                union = len(start) + len(target)
                intersection = len(key1.intersection(target))
                max_len = max(max_len, union - intersection)
            
            graph[node] = start

        return max_len
                              
                              