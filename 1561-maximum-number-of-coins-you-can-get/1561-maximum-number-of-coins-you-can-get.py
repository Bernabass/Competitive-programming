class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        updated = deque(piles)
        max_coin = 0
        
        
        
        while updated:
            alice = updated.popleft()
            mine = updated.popleft()
            bob = updated.pop()
            
            max_coin += mine
            
        return max_coin