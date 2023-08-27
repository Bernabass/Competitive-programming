class Solution:
    def canCross(self, stones: List[int]) -> bool:
        indices = defaultdict(int)
        
        for idx, val in enumerate(stones):
            indices[val] = idx
        
        @cache
        def dp(stone, last_jump):
            if stone not in indices:
                return False
            
            if indices[stone] == len(stones) - 1:
                return True
            
            if last_jump - 1:
                if dp(stone + last_jump - 1, last_jump - 1):
                    return True
                
            return dp(stone + last_jump, last_jump) or dp(stone + last_jump + 1, last_jump + 1)
        
        return dp(1, 1)
            