class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        ans = []
        
        def dfs(node, path):
            if node == target:
                ans.append(path.copy())
                return
 
            for adj in graph[node]:
                path.append(adj)
                dfs(adj, path)
                path.pop()
                
            return
        
        dfs(0, [0])
        
        return ans