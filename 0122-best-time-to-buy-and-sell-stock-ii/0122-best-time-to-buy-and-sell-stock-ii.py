class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        @cache
        def back_track(idx, do):
            if idx == n:
                return 0
            
            return max(do*prices[idx] + back_track(idx+1, -do), back_track(idx+1, do))
        
        return back_track(0, -1)