class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        N = len(rides)
        rides.sort()
        
        @cache
        def dp(idx):
            if idx == N or idx == -1:
                return 0
                
            start, end, tip = rides[idx]
            no_pick = dp(idx + 1)
            next_idx = bisect_left(rides, [end, -1, -1])
            pick = (end - start + tip) + dp(next_idx)
                
            return max(pick, no_pick)
        
        return dp(0)