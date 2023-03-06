class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = [0]
        for item in range(1, len(prices)):
            while stack and prices[item] <= prices[stack[-1]]:
                prices[stack.pop()] -= prices[item]
                
            stack.append(item)
            
        return prices