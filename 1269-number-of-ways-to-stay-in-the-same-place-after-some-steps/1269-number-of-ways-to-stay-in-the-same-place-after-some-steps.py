class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        @cache
        def dp(idx, steps):
            if steps < 0 or idx < 0 or idx == arrLen:
                return 0
            
            if idx == steps == 0:
                return 1
                
            return (dp(idx - 1, steps - 1) + dp(idx + 1, steps - 1) + dp(idx, steps - 1)) % MOD
                
        return dp(0, steps)