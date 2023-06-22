class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n < 2:
             return 0
        ans, min_ = 0, prices[0]
    
        for i in range(1, n):
            if prices[i] < min_:
                min_ = prices[i]
            elif prices[i] > min_ + fee:
                ans += prices[i] - fee - min_
                min_ = prices[i] - fee
                
        return ans
