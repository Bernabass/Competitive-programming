class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        self.ans, n = -1, len(edges)
        arr, colors = [0]*n, [0]*n

        
        def dfs(node, val):
            if colors[node] == 2:
                return
            
            arr[node] = val
            colors[node] = 1
            child = edges[node]
            
            if child != -1 and colors[child] == 1:
                self.ans = max(self.ans, val - arr[child] + 1)
                colors[node] = 2
                return 
                
            if child != -1:
                dfs(child, val + 1)
            
            colors[node] = 2
                 
        for num in range(len(edges)):
            if not colors[num]:
                dfs(num, 1)
           
        return self.ans