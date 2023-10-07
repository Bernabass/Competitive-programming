class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        
        @cache
        def dp(curr_max, cost, length):
            if length == n:
                if cost == k:
                    return 1
                
                return 0
            
            if length > n:
                return 0
            
            count = 0
            for num in range(1, m + 1):
                count += dp(max(curr_max, num), cost + (num > curr_max), length + 1) % MOD
                
            return count % MOD
        
        
        return dp(-1, 0, 0)