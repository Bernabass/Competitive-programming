class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        GRAPH = defaultdict(list)
        ans = [1]*n
        
        for parent, child in edges:
            GRAPH[parent].append(child)
            GRAPH[child].append(parent)
            
        def dfs(parent, seen):
            memo = Counter()
            
            for child in GRAPH[parent]:
                if child != seen:
                    memo += dfs(child, parent)
                
            ans[parent] += memo[labels[parent]]
            memo[labels[parent]] += 1
            
            return memo
            
        dfs(0, n)
        
        return ans