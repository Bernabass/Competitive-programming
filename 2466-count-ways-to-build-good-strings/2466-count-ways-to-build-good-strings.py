class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [1] + [0]*(high)
        mod = 10**9 + 7

        greater = max(zero, one)
        lesser = min(zero, one)

        for i in range(lesser, greater):
            dp[i] += dp[i-lesser] % mod
        
        for i in range(greater, high+1):
            dp[i] += (dp[i-zero]+dp[i-one]) % mod
        
        return sum(dp[low:high+1]) % mod