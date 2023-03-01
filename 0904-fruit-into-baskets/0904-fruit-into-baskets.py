class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        baskets = defaultdict(int)
        left = max_pick = 0
        
        for right in range(len(fruits)):
            baskets[fruits[right]] += 1
            
            while len(baskets) > 2:
                baskets[fruits[left]] -= 1
                
                if not baskets[fruits[left]]:
                    del baskets[fruits[left]]
                    
                left += 1
                
            max_pick = max(max_pick, right - left + 1)
            
        
        return max_pick
            