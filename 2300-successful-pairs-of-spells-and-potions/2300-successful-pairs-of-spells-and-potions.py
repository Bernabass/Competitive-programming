class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        pairs = []
                
        def min_valid_potion(spell):
            left = 0
            right = len(potions) - 1
            
            while left <= right:
                mid = (left+right) // 2
                
                if spell*potions[mid] >= success:
                    if mid and spell*potions[mid-1] >= success:
                        right = mid - 1
                        
                    else:
                        return mid
                    
                else:
                    left = mid + 1
                    
            return left
        
        for spell in spells:
            pairs.append(len(potions)-min_valid_potion(spell))
            
        return pairs