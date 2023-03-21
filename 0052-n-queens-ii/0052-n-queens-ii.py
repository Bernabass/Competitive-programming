class Solution:
    def totalNQueens(self, n: int) -> int:
        # Use bit manipulation to represent the board
        board = 0
        
        # Count of queens attacking each column, diagonal, and anti-diagonal
        col_attacks = [0] * n
        diag_attacks = [0] * (2 * n - 1)
        anti_diag_attacks = [0] * (2 * n - 1)
        
        # Backtracking function
        def backtrack(row=0, count=0):
            nonlocal board
            nonlocal col_attacks
            nonlocal diag_attacks
            nonlocal anti_diag_attacks
            
            if row == n:
                # Valid solution found
                count += 1
            else:
                # Try placing a queen in each column of the current row
                for col in range(n):
                    col_attack_idx = col
                    diag_attack_idx = row + col
                    anti_diag_attack_idx = n - 1 - row + col
                    
                    # Check if the column, diagonal, and anti-diagonal are attacked
                    if col_attacks[col_attack_idx] or diag_attacks[diag_attack_idx] or anti_diag_attacks[anti_diag_attack_idx]:
                        continue
                    
                    # Place the queen and update the attack counts
                    board ^= (1 << col)
                    col_attacks[col_attack_idx] = 1
                    diag_attacks[diag_attack_idx] = 1
                    anti_diag_attacks[anti_diag_attack_idx] = 1
                    
                    # Move to the next row
                    count = backtrack(row+1, count)
                    
                    # Remove the queen and update the attack counts
                    board ^= (1 << col)
                    col_attacks[col_attack_idx] = 0
                    diag_attacks[diag_attack_idx] = 0
                    anti_diag_attacks[anti_diag_attack_idx] = 0
                    
            return count
        
        # Start the backtracking search
        return backtrack()
