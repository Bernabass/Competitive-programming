class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        candidates = []
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    candidates.append((i, j))
                    
        n = len(candidates)
        
        def is_valid(i, j, curr):
            row = i - (i % 3)
            col = j - (j % 3)
            
            for x in range(row, row + 3):
                for y in range(col, col + 3):
                    if curr == board[x][y]:
                        return False
                    
            if curr in board[i]:
                return False
            
            for k in range(9):
                if board[k][j] == curr:
                    return False
                    
            return True
        
        def back_track(idx):
            
            if idx == n:
                return True
            
            row, col = candidates[idx]
            
            for num in range(1, 10):
                curr = str(num)
                if is_valid(row, col, curr):
                    
                    board[row][col] = curr
                    
                    if back_track(idx + 1):
                        return True
                    
                    board[row][col] = "."
            
            return False
        
        back_track(0)