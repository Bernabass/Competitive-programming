class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        factors = self.factors(n)
        ans = len(factors) - 1
        
        for i in range(len(factors) - 1):
            ans += (factors[i] // factors[i+1]) - 1
            
        return ans + factors[-1]
            
    def factors(self, n):
        factors = []
        d = 2

        while d * d <= n:
            while n % d == 0:
                factors.append(n)
                n //= d
            d += 1
        if n > 1:
            factors.append(n)

        return factors