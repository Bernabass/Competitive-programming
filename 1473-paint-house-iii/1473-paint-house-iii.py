class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        @cache
        def back_track(idx, prev, needed):
            if m - idx < needed:
                return -1
            
            if idx == m:
                return 0
            
            ans = inf
            for i in range(1, n + 1):
                curr = houses[idx]
                if not needed and i != prev:
                    continue
                 
                if curr:
                    if not needed and (curr != prev):
                        break
                    rest = back_track(idx + 1, curr, needed - (curr != prev))
                    if rest != -1:
                        ans = min(ans, rest)
                        
                    break
                    
                rest = back_track(idx + 1, i, needed - (i != prev))
                if rest != -1:
                    ans = min(ans, cost[idx][i-1] + rest)
                    
            return -1 if ans == inf else ans
        
        return back_track(0, n + 1, target)