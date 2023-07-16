class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def back_track(idx, do, cooldown):
            if idx == n:
                return 0
            
            if not cooldown:
                curr1 = do*prices[idx] + back_track(idx+1, -do, not(do < 0))
                    
                curr2 = back_track(idx+1, do, cooldown)
                
                return max(curr1, curr2)
            
            return back_track(idx+1, do, 1-cooldown)
        
        return back_track(0, -1, 0)