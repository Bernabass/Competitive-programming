class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = defaultdict(lambda:inf)
        dp[0] = 0
        
        for idx in range(n + 1):
            left = max(0, idx - ranges[idx])
            right = min(n, idx + ranges[idx])
            
            for i in range(left, right + 1):
                dp[right] = min(dp[right], dp[i] + 1)
                
        return -1 if dp[n] == inf else dp[n]