class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
 
        is_prime = [1] * n
        is_prime[0] = is_prime[1] = 0
        count = 2
 
        for i in range(2, int(n**0.5)+1):
            if is_prime[i]:
                for j in range(i**2, n, i):
                    count += is_prime[j]
                    is_prime[j] = 0
                    
        return n - count