class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        level = defaultdict(int)
        level[(0, 0)] = poured
        
        while level:
            next_level = defaultdict(int)
            
            for position, amount in level.items():
                i, j = position
                if position == (query_row, query_glass):
                    return amount if amount < 1 else 1
                
                remaining = amount - 1
                
                if remaining > 0 and i + 1 < 100:
                    
                    next_level[(i + 1, j)] += remaining / 2
                    next_level[(i + 1, j + 1)] += remaining / 2
                    
            level = next_level
            
        return 0