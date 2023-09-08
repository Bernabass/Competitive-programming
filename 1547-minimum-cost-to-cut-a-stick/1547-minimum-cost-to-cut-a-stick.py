class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.extend([0, n])
        cuts.sort()
        N = len(cuts)
        
        @cache
        def dp(left, right):
            if left == right - 1:
                return 0

            min_cost = inf
            for idx in range(left + 1, right):
                curr_cost = cuts[right] - cuts[left]
                min_cost = min(min_cost, dp(left, idx) + dp(idx, right) + curr_cost)

            return min_cost
        
        return dp(0, N - 1)