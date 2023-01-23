class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        max_coin = 0
        left = 1
        right = len(piles) - 1
        
        while left <= right:
            max_coin += piles[left]
            
            left += 2
            right -= 1
           
        return max_coin