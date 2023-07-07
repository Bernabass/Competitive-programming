class Solution:
    def tribonacci(self, n: int) -> int:
        a , b , c = 0, 1, 1
        
        for i in range(3, n+1):
            a, b, c = b, c, a+b+c
            
        return a if not n else c