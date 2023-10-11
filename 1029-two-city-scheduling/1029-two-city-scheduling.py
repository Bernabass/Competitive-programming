class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs)
        
        @cache
        def dp(idx, city_A, city_B):
            if city_A > (N // 2) or city_B > (N //2):
                return inf
            
            if idx == N:
                return 0
            
            cost_A, cost_B = costs[idx]            
            to_A = cost_A + dp(idx + 1, city_A + 1, city_B)
            to_B = cost_B + dp(idx + 1, city_A, city_B + 1)
            
            return min(to_A, to_B)
        
        return dp(0, 0, 0)
        