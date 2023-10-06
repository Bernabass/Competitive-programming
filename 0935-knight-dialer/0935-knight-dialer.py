class Solution:
    def knightDialer(self, n: int) -> int:
        adj = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]
        prohibited = {(3, 0), (3, 2)}
        MOD = 10 ** 9 + 7
        
        def valid(i, j):
            return (i, j) not in prohibited and (0 <= i < 4 and 0 <= j < 3)
        
        @cache
        def dp(i, j, n):
            if not n:
                return 1
            
            count = 0
            for r, c in adj:
                x, y = i + r, j + c
                
                if valid(x, y):
                    count += dp(x, y, n - 1) % MOD
                    
            return count
        
        total = 0
        
        for i in range(4):
            for j in range(3):
                if valid(i, j):
                    total += dp(i, j, n - 1) % MOD
                    
        return total % MOD