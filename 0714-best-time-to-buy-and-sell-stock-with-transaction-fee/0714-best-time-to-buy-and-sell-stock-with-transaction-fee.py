class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)
        
        @cache
        def dp(idx, flag):
            if idx == N:
                return 0 
            
            not_take = dp(idx + 1, flag)
            if flag:
                take =  prices[idx] - fee + dp(idx + 1, 1 - flag)
                
            else:
                take = -prices[idx] + dp(idx + 1, 1 - flag)
                
            return max(not_take, take)
        
        return dp(0, 0)
            
