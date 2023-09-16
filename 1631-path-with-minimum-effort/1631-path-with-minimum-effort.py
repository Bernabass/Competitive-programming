class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        adj = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        
        def inbound(i, j):
            return 0 <= i < m and 0 <= j < n

        seen, queue = set(), [(0, (0, 0))]
        min_effort = 0
        
        while queue:
            curr_effort, (x, y) = heapq.heappop(queue)
            if (x, y) in seen:
                continue
            min_effort = max(min_effort, curr_effort)
            seen.add((x, y))
            if x == m - 1 and y == n - 1:
                return min_effort

            for r, c in adj:
                i, j = x + r, y + c
                if inbound(i, j) and (i, j) not in seen:
                    heapq.heappush(queue, (abs(heights[i][j] - heights[x][y]), (i, j)))
                    
        return 0