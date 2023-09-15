class Solution:
    def tribonacci(self, n: int) -> int:
        def tribonacci(n, memo={0: 0, 1: 1, 2: 1}):  #1 # change
            if n in memo:  #2.1
                return memo[n]  #2.2

            memo[n] = tribonacci(n - 1, memo) + tribonacci(n - 2, memo) + tribonacci(n - 3, memo)  #6 # change
            return memo[n]  #7
        
        return tribonacci(n)