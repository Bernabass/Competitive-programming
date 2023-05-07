class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        n = right + 1
        is_prime = [1] * n
        is_prime[0] = is_prime[1] = 0
        ans = [-1, -1]
        
        for i in range(2, int(n**0.5)+1):
            if is_prime[i]:
                for j in range(i**2, n, i):
                    is_prime[j] = 0
         
        prev, min_diff = None, float("inf")
        for k in range(left, n):
            if is_prime[k]:
                if prev:
                    curr_diff = k - prev
                    if curr_diff < min_diff:
                        ans = [prev, k]
                        min_diff = curr_diff
                        
                prev = k
                                 
        return ans