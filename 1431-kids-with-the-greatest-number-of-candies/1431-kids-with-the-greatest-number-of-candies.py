class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        result = [False]*len(candies)
        
        for kid, candy in enumerate(candies):
            if candy + extraCandies >= greatest:
                result[kid] = True
                
        return result