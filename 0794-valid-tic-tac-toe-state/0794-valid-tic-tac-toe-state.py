class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        temp = Counter("".join(board))
        R_diag, L_diag = set(), set()
        winner = set()
        if (temp["X"] - temp["O"]) not in {0,1}:
            return False
        
        for row in range(3):
            nth_row,nth_col = set(), set()
            for col in range(3):
                if row + col == 2:
                    L_diag.add(board[row][col])
                if row - col == 0:
                    R_diag.add(board[row][col])
                nth_row.add(board[row][col])
                nth_col.add(board[col][row])
           
            if len(nth_row) == 1:
                winner |= nth_row
            if len(nth_col) == 1:
                winner |= nth_col
            
        if len(R_diag) == 1:
            winner |= R_diag 
        if len(L_diag) == 1:
             winner |= L_diag
        
        if len(winner) > 1:
            return False
        else:
            if winner == {"X"}:
                return temp["X"] - temp["O"] == 1
            elif winner == {"O"}:
                return temp["X"] - temp["O"] == 0
            else:
                return (temp["X"] - temp["O"]) in {0,1}