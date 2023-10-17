class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        GRAPH = defaultdict(list)
        memo = defaultdict(int)
        max_count = 0
        for node in range(n):
            if leftChild[node] != -1:
                GRAPH[node].append(leftChild[node])
            if rightChild[node] != -1:
                GRAPH[node].append(rightChild[node])
          
        
        def dfs(node, seen):
            if node in memo:
                return memo[node]
            seen.add(node)
            count = 1
            for adj in GRAPH[node]:
                if adj in seen:
                    return -1
                
                ans = dfs(adj, seen)
                if ans == -1:
                    return -1
                
                count += ans
                
            memo[node] = count
                
            return count
        
        for node in range(n):
            if node not in memo:
                ans = dfs(node, set())
                if ans == -1:
                    return False
                max_count = max(ans, max_count)
            
        return max_count == n