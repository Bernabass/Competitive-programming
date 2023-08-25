class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10**9 + 7
        @cache
        def dp(idx, steps):
            if steps < 0:
                return 0
            
            if idx == endPos and steps == 0:
                return 1
                
            return (dp(idx - 1, steps - 1) + dp(idx + 1, steps - 1)) % MOD
                
        return dp(startPos, k) % MOD