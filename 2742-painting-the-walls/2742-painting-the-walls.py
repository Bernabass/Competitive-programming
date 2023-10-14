class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(time)
        info = [sum(time[i:]) for i in range(n)]

        @cache
        def dp(idx, rem):
            if idx == n:
                return 0 if rem >= 0 else inf
            
            if rem >= n - idx:
                return 0
            
            if rem + info[idx] < 0:
                return inf

            return min(dp(idx + 1, rem - 1), cost[idx] + dp(idx + 1, rem + time[idx]))

        return dp(0, 0)