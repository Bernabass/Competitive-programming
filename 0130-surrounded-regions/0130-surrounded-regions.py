class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        adj = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        seen = set()
        
        def is_valid(row, col, letter):
            return 0 <= row < m and 0 <= col < n and (row, col) not in seen and board[row][col] == letter
        
        def bfs(row, col, edge):
            seen.add((row, col))
            queue = deque([(row, col)])
                
            while queue:
                row, col = queue.popleft()
            
                for r, c in adj:
                    i, j = row+r, col+c

                    if is_valid(i, j, "O"):
                        if not edge: board[i][j] = "X"
                        seen.add((i, j))
                        queue.append((i, j))
                
        for row in range(m):
            for col in range(n):
                if is_valid(row, col, "O") and (0 in (row, col) or row == m-1 or col == n-1):
                    bfs(row, col, 1)
                    
        for row in range(m):
            for col in range(n):
                if is_valid(row, col, "X"):
                    bfs(row, col, 0)