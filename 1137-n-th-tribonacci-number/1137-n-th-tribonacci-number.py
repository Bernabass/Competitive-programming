class Solution:
    def tribonacci(self, n: int) -> int:
        def tribonacci(n, memo={}):
            if n in memo:  #1.1 added
                return memo[n]  #1.2 added
            if n == 0:  #2
                return 0  #3
            if n == 1 or n == 2:  #4
                return 1 #5

            memo[n] = tribonacci(n - 1, memo) + tribonacci(n - 2, memo) + tribonacci(n - 3, memo)  #6 changed
            return memo[n]  #6.1 added
        
        return tribonacci(n, memo={})