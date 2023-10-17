class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        memo = defaultdict(int)
        max_count = 0
          
        def dfs(node, seen):
            if node in memo:
                return memo[node]
            
            if node == -1:
                return 0
            seen.add(node)
            count = 1
            for adj in [leftChild[node], rightChild[node]]:
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