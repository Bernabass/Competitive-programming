class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        self.ans = -1
        
        arr = [0] * len(edges)
        prev_visited = set()
        
        def dfs(node, val):
            if node in prev_visited:
                return
            
            
            arr[node] = val
            visited.add(node)
            prev_visited.add(node)
            child = edges[node]
            
            if child in visited:
                self.ans = max(self.ans, val - arr[child] + 1)
                return 
                
            if child != -1:
                dfs(child, val + 1)
                
                
        for num in range(len(edges)):
            if num not in prev_visited:
                visited = set()
                dfs(num, 1)
                
        return self.ans