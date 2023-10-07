class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        N = len(word)
        adj = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        
        def inbound(i, j):
            return 0 <= i < m and 0 <= j < n
        
        def dfs(row, col, idx):
            if idx == N:
                return True
            
            for r, c in adj:
                i, j = row + r, col + c
                
                if inbound(i, j) and (i, j) not in seen and board[i][j] == word[idx]:
                    seen.add((i, j))
                    if dfs(i, j, idx + 1):
                        return True
                    
                    seen.remove((i, j))
                    
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    seen = {(i, j)}
                    if dfs(i, j, 1):
                        return True 