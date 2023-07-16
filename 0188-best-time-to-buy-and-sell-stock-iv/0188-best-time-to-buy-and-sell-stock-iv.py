class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        
        @cache
        def back_track(idx, do, k):
            if idx == n or not k:
                return 0
            
            return max(do*prices[idx] + back_track(idx+1, -do, k-1), back_track(idx+1, do, k))
        
        return back_track(0, -1, 2*k)