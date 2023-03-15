class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        
        pos = n > 0
        n = abs(n)
        seen = defaultdict(int)
        def find_pow(x, n):
            if (x, n) in seen:
                return seen[(x, n)]
            
            if n == 1:
                return x
            
            n1 = n // 2
            n2 = n - n1
            left = find_pow(x, n1)
            right = find_pow(x, n2)
            seen[(x, n)] += left*right
            return left*right
        
        ans = find_pow(x, n)
        if pos:
            return ans
        
        return 1 / ans