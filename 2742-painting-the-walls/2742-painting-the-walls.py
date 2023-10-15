class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        N = len(time)
        suffix_sum = defaultdict(int)
        for i in range(N - 2, -1, -1): 
            suffix_sum[i] = suffix_sum[i + 1] + time[i + 1]

        @cache
        def dp(idx, worked):
            if idx == N:
                return 0
            
            if worked >= N - idx:
                return 0
            
            paid = cost[idx] + dp(idx + 1, worked + time[idx])
            free = inf
            if worked + suffix_sum[idx] > 0:
                free = dp(idx + 1, worked - 1)
        
            return min(paid, free)
            
        return dp(0, 0)