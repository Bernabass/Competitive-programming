class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        distance = defaultdict(lambda : float("inf"))
        distance[(0, 0)] = 0
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        seen = set()
        heap = [(0, (0, 0))]
        
        def inbound(i, j):
            return 0 <= i < m and 0 <= j < n
        
        while heap:
            curr_distance, curr_node = heappop(heap)
            row, col = curr_node
            
            if curr_node == (m - 1, n - 1):
                return distance[(m - 1, n - 1)]
                
            seen.add(curr_node)
            
            for dx, dy in directions:
                i, j = dx + row, dy + col
                potential_distance = curr_distance + grid[row][col]
                
                if inbound(i, j) and potential_distance < distance[(i, j)]:
                    distance[(i, j)] = potential_distance
                    heappush(heap, (potential_distance, (i, j)))               