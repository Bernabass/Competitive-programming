class Solution:
    def numTilings(self, n: int) -> int:
        
        @cache
        def even(n):
            if n <= 0:
                return 0
            
            if n == 1:
                return 1
            
            if n == 2:
                return 2
            
            
            return (even(n - 1) + even(n - 2) + 2 * odd(n - 2)) % (10**9 + 7)
       
        @cache
        def odd(n):
            if n <= 0:
                return 0
            
            if n == 1:
                return 1
            
            
            return (odd(n - 1) + even(n - 1)) % (10**9 + 7)
        
        return even(n)