class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}

        def back_track(idx, state):
            if idx == n or state == 4:
                return 0

            if (idx, state) in memo:
                return memo[(idx, state)]

            do = -1 if state % 2 == 0 else 1
            max_profit = max(
                do * prices[idx] + back_track(idx + 1, state + 1),
                back_track(idx + 1, state)
            )
            memo[(idx, state)] = max_profit
            return max_profit

        return back_track(0, 0)
