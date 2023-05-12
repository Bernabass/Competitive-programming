class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        self.ans, n = -1, len(edges)
        arr = [0]*n

        def dfs(node, val):
            if arr[node] == -1:
                return
            
            arr[node] = val
            child = edges[node]
            
            if child != -1 and arr[child] not in {0, -1}:
                self.ans = max(self.ans, val - arr[child] + 1)
                arr[node] = -1
                
                return 
                
            if child != -1:
                dfs(child, val + 1)
            
            arr[node] = -1
                 
        for num in range(len(edges)):
            if not arr[num]:
                dfs(num, 1)
           
        return self.ans