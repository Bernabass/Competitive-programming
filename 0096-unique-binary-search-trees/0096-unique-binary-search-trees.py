class Solution:
    def numTrees(self, n: int) -> int:
        
        memo = defaultdict(int)
        def divide(n):
            if n in memo:
                return memo[n]
            
            if n <= 1:
                return 1
            
            total = 0
            for i in range(n):
                total += divide(i) * divide(n-i-1)
               
            memo[n] += total
            return total
        
        return divide(n)