class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        bars = total_cost = 0
        for price in costs:
            if total_cost + price > coins:
                return bars
            total_cost += price
            bars += 1
        return bars