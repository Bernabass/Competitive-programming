class Solution:
    def integerBreak(self, n: int) -> int:
        
        @cache
        def dp(Sum):
            if Sum == n:                    
                return 1
                    
            if Sum > n:
                return 0
            
            max_product = 1
            for num in range(n - 1, 0, -1):
                max_product = max(max_product, num *dp(Sum + num))
                
            return max_product
        
        return dp(0)