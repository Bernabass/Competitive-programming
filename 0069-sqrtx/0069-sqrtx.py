class Solution:
    def mySqrt(self, x: int) -> int:
        
        left = 0
        j = (x + 1) // 2
        while j > 0:
            while (left + j) * (left + j) <= x:
                left += j
            j //= 2
                
                
        return left