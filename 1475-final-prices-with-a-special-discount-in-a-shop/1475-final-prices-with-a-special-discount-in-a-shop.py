class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = [0]
        discount = defaultdict(int)
        for item in range(1, len(prices)):
            while stack and prices[item] <= prices[stack[-1]]:
                discount[stack.pop()] = prices[item]
                
            stack.append(item)
            

        for item, price in enumerate(prices):
            prices[item] -= discount[item]
            
        return prices