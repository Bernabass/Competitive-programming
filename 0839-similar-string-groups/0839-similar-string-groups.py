class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def dfs(i):
            if i in visited:
                return
            
            visited.add(i)
            for nei in adj[i]:
                dfs(nei)
        
        n, m = len(strs), len(strs[0])
        adj = defaultdict(list)

        for i in range(n):
            for j in range(i+1, n):
                change = 0
  
                for k in range(m):
                    if strs[i][k] != strs[j][k]:
                        change += 1
                    if change > 2:
                        break

                if not change or change == 2:
                    adj[i].append(j)
                    adj[j].append(i)
        
        visited, res = set(), 0

        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        
        return res