class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        adj = [(0, 1), (0, -1), (1, 0), (-1, 0)]      
        
        def bfs(time):
            visited = set()
            queue = deque([(0, 0)])

            while queue:
                x, y = queue.popleft()
                if (x, y) == (n - 1, n - 1):
                    return True
                
                for r, c in adj:
                    i, j = x + r, y + c
                    if 0 <= i < n and 0 <= j < n and (i, j) not in visited and grid[i][j] <= time:
                        visited.add((i, j))
                        queue.append((i, j))
        
        left, right = grid[0][0], n**2
        
        while left < right:
            mid = (left + right) // 2
            
            if bfs(mid):
                right = mid
                
            else:
                left = mid + 1
                
        return left