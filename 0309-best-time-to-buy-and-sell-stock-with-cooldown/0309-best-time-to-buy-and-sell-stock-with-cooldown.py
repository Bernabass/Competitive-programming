class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def back_track(idx, hold):
            if idx >= n:
                return 0
            
            if hold:
                sell_profit = prices[idx] + back_track(idx + 2, 0)
                hold_profit = back_track(idx + 1, 1)
                
                return max(sell_profit, hold_profit)
            
            else:
                buy_profit = -prices[idx] + back_track(idx + 1, 1)
                hold_profit = back_track(idx + 1, 0)
                
                return max(buy_profit, hold_profit)
        
        return back_track(0, 0)