class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        @cache
        def back_track(idx, prev, needed):
            if m - idx < needed:
                return inf
            
            if idx == m:
                return 0
            
            ans, curr = inf, houses[idx]
            if curr:
                if not needed and curr != prev:
                    return ans
                
                return min(ans, back_track(idx + 1, curr, needed - (curr != prev)))
                
            for i in range(1, n + 1):
                if not needed and i != prev:
                    continue
                                     
                ans = min(ans, cost[idx][i-1] + back_track(idx + 1, i, needed - (i != prev)))
                    
            return ans
        
        res = back_track(0, n + 1, target)
        
        return -1 if res == inf else res