class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        @cache
        def back_track(idx, do, count):
            if idx == n or count == 2:
                return 0
            
            return max(do*prices[idx] + back_track(idx+1, -do, count+1), back_track(idx+1, do, count))
        
        return back_track(0, -1, 0)