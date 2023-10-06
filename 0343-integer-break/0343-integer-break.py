class Solution:
    def integerBreak(self, n: int) -> int:
        
        if n <= 3:
            return n - 1
        
        quo, rem = divmod(n, 3)
        
        if not rem:
            return 3**quo
        
        if rem == 1:
            return 3**(quo - 1) * 4
        
        return 3**(quo) * 2