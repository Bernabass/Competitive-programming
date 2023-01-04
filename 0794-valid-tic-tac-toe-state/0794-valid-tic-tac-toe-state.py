class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        freq = Counter("".join(board))
        winner = set()
        if (freq["X"] - freq["O"]) not in {0,1}:
            return False
        
        for row in range(3):
            if (board[row][0] == board[row][1] == board[row][2]):
                winner.add(board[row][0])
            if (board[0][row] == board[1][row] == board[2][row]):
                winner.add(board[0][row])     
   
        if (board[0][0] == board[1][1] == board[2][2]) or (board[2][0] == board[1][1] == board[0][2]):
            winner.add(board[1][1])
        
        if len(winner) > 1:
            return False
        elif winner == {"X"}:
            return freq["X"] - freq["O"] == 1
        elif winner == {"O"}:
            return freq["X"] - freq["O"] == 0
        return True