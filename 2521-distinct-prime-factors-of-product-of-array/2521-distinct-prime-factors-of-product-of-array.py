class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        count = set()
        
        for num in nums:
            count |= self.unique_prime_factors(num)
            
        return len(count)
        
        
    def unique_prime_factors(self, n):
        factors = set()
        for d in range(2, int(n**0.5)+1):
            while not(n % d):
                factors.add(d)
                n //= d

        if n > 1:
            factors.add(n)

        return factors
        
        