class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max_product = 0
        
        for idx, word in enumerate(words):
            mask = 0
            for letter in word:
                bit = ord(letter) - 96
                mask |= 1 << bit
                
            words[idx] = (mask, word)
        
        for mask1, first in words:
            for mask2, second in words:
                if not (mask1 & mask2):
                    max_product = max(max_product, len(first)*len(second))
                    
        return max_product