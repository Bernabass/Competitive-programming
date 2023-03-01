class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        uniques = defaultdict(int)
        left = 0
        min_card = float("inf")
        
        for right in range(len(cards)):
            uniques[cards[right]] += 1
            
            while right - left + 1 > len(uniques):
                min_card = min(min_card, right - left + 1)
                uniques[cards[left]] -= 1
                
                if not uniques[cards[left]]:
                    del uniques[cards[left]]
                    
                left += 1
                
            
            
        if min_card == float("inf"):
            min_card = - 1
            
        return min_card