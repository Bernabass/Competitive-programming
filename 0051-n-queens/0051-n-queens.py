class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [["."] * n for _ in range(n)]
        attacked = {"R":defaultdict(int), "C":defaultdict(int), "RD":defaultdict(int), "LD":defaultdict(int)}
        ans = []
        
        def back_track(row, grid, attacked):
            
            if row == n:
                res = ["".join(_) for _ in grid]
                ans.append(res)
                
                return
            
            for col in range(n):
                if attacked["R"][row] or attacked["C"][col]:
                    continue

                if attacked["RD"][(row - col)] or attacked["LD"][(row + col)]:
                    continue              

                grid[row][col] = "Q"
                attacked["R"][row] += 1
                attacked["C"][col] += 1
                attacked["RD"][row - col] += 1
                attacked["LD"][row + col] += 1
                
                if back_track(row + 1, grid, attacked):
                    return False
                
                grid[row][col] = "."
                attacked["R"][row] -= 1
                attacked["C"][col] -= 1
                attacked["RD"][row - col] -= 1
                attacked["LD"][row + col] -= 1
        
        back_track(0, grid, attacked)
        
        return ans