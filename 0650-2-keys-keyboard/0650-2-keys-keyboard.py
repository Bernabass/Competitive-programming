class Solution:
    def minSteps(self, n: int) -> int:
        
        @cache
        def dp(written, copied):
            paste = copy = inf
            if written == n:
                return 0
            
            if written > n:
                return paste
            
            if copied:
                paste = dp(written + copied, copied)
                
            if written > copied:
                copy = dp(written, written)
                
            return min(copy, paste) + 1
        
        return dp(1, 0)